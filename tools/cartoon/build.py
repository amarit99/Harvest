#!/usr/bin/env python3
"""Build a cartoon episode end to end.

usage: python3 build.py <episode.json> <cast.json> <assets_dir> <work_dir> <out.mp4>

assets_dir holds reusable audio (music_<mood>.mp3, sfx_<name>.mp3); missing ones
are generated with the ElevenLabs API (the session proxy supplies the key).
"""
import hashlib, json, os, subprocess, sys, urllib.request

EP, CASTF, ASSETS, WORK, OUT = sys.argv[1:6]
HERE = os.path.dirname(os.path.abspath(__file__))
EL = "https://api.elevenlabs.io"
os.makedirs(ASSETS, exist_ok=True); os.makedirs(f"{WORK}/tts", exist_ok=True)

MUSIC = {
    "light": "cheerful light everyday background music for a cartoon, soft ukulele, claps and xylophone, gentle, loopable",
    "tense": "tense suspenseful background music, low pulsing strings and soft ticking, loopable",
    "sad": "sad emotional background music, slow solo piano with soft strings, rainy night mood, loopable",
    "triumph": "triumphant powerful background music, epic drums and brass, confident boss energy, loopable",
}
SFX = {
    "coin": "a handful of coins thrown and bouncing on a hard floor",
    "ring": "smartphone ringtone ringing twice",
    "rain": "heavy rain falling on a city street at night with distant thunder",
    "ding": "short bright app notification ding",
    "hit": "deep cinematic boom hit with short reverb",
}


def post(path, body, out):
    req = urllib.request.Request(EL + path, data=json.dumps(body).encode(), headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=180) as r, open(out, "wb") as f:
        f.write(r.read())


def dur(f):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]))


def run(a):
    subprocess.run(a, check=True)


for k, p in MUSIC.items():
    f = f"{ASSETS}/music_{k}.mp3"
    if not os.path.exists(f):
        print("music", k); post("/v1/sound-generation", {"text": p, "duration_seconds": 22, "prompt_influence": 0.5}, f)
for k, p in SFX.items():
    f = f"{ASSETS}/sfx_{k}.mp3"
    if not os.path.exists(f):
        print("sfx", k); post("/v1/sound-generation", {"text": p, "duration_seconds": 6 if k == "rain" else 2, "prompt_influence": 0.6}, f)

ep = json.load(open(EP)); cast = json.load(open(CASTF))

# ---- TTS + timing
t0 = 0.0; scenes = []; vo_events = []; sfx_events = []; moods = []
for sc in ep["scenes"]:
    t = 0.35; lines = []
    for ln in sc.get("lines", []):
        who = ln["who"]; voice = cast[who if who in cast else "vo"]["voice"]
        h = hashlib.sha1((voice + ln["text"]).encode()).hexdigest()[:12]
        f = f"{WORK}/tts/{h}.mp3"
        if not os.path.exists(f):
            print("tts", who, ln["text"])
            post(f"/v1/text-to-speech/{voice}?output_format=mp3_44100_128",
                 {"text": ln["text"], "model_id": "eleven_v3", "language_code": "th", "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}}, f)
        d = dur(f)
        l2 = dict(ln); l2.update(at=round(t, 3), dur=round(d, 3)); lines.append(l2)
        vo_events.append((f, t0 + t)); t += d + float(os.environ.get('GAP', '0.3'))
    D = max(t + float(os.environ.get('TAIL', '0.45')), sc.get("minDur", 2.0))
    s2 = dict(sc); s2.update(start=round(t0, 3), dur=round(D, 3), lines=lines)
    if "coinsLine" in sc and lines:
        s2["coinsAt"] = lines[sc["coinsLine"]]["at"] + 0.4
    for e in sc.get("sfx", []):
        at = e.get("at", 0) if "line" not in e else lines[e["line"]]["at"] + e.get("off", 0)
        sfx_events.append((f"{ASSETS}/sfx_{e['name']}.mp3", t0 + at, e["name"]))
    moods.append((sc.get("mood", "none"), t0, D))
    scenes.append(s2); t0 += D
TOTAL = round(t0, 3)
tl = {"total": TOTAL, "next": ep.get("next"), "scenes": scenes}
json.dump(tl, open(f"{WORK}/timeline.json", "w"), ensure_ascii=False)
print("total", TOTAL)
if os.environ.get("TIMELINE_ONLY"): sys.exit(0)

# ---- video
if not os.path.exists(f"{WORK}/video.mp4") or os.environ.get("REVIDEO"):
    run(["node", f"{HERE}/render.js", f"{WORK}/timeline.json", CASTF, f"{WORK}/video.mp4"])

# ---- music bed: merge consecutive scenes with same mood into segments
segs = []
for m, s, d in moods:
    if segs and segs[-1][0] == m: segs[-1][2] += d
    else: segs.append([m, s, d])
ins, parts, labels = [], [], []
for i, (m, s, d) in enumerate(segs):
    if m == "none": continue
    ins += ["-stream_loop", "-1", "-i", f"{ASSETS}/music_{m}.mp3"]; k = len(ins) // 4 - 1
    ms = int(s * 1000)
    parts.append(f"[{k}]atrim=0:{d + 0.6},aresample=48000,aformat=channel_layouts=stereo,afade=t=in:d=0.4,afade=t=out:st={max(d - 0.2, 0)}:d=0.8,volume=0.20,adelay={ms}|{ms}[m{k}]")
    labels.append(f"[m{k}]")
nm = len(labels)
base = nm
for j, (f, at) in enumerate(vo_events):
    ins += ["-i", f]; ms = int(at * 1000)
    parts.append(f"[{base + j}]aresample=48000,aformat=channel_layouts=stereo,volume=1.5,adelay={ms}|{ms}[v{j}]")
nv = len(vo_events); base2 = base + nv
for j, (f, at, name) in enumerate(sfx_events):
    ins += ["-i", f]; ms = int(at * 1000); vol = 0.35 if name == "rain" else 0.7
    parts.append(f"[{base2 + j}]aresample=48000,aformat=channel_layouts=stereo,volume={vol},adelay={ms}|{ms}[x{j}]")
ns = len(sfx_events)
fc = ";".join(parts) + ";"
fc += "".join(f"[v{j}]" for j in range(nv)) + f"amix={nv}:normalize=0,apad[vo];[vo]asplit[vo1][vo2];"
fc += "".join(labels) + "".join(f"[x{j}]" for j in range(ns)) + f"amix={nm + ns}:normalize=0,apad[bg];"
fc += "[bg][vo1]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=400[duck];[duck][vo2]amix=2:normalize=0,alimiter=limit=0.95[a]"
run(["ffmpeg", "-nostdin", "-y", "-loglevel", "error", *ins, "-filter_complex", fc, "-map", "[a]", "-t", str(TOTAL), f"{WORK}/mix.wav"])
run(["ffmpeg", "-nostdin", "-y", "-loglevel", "error", "-i", f"{WORK}/video.mp4", "-i", f"{WORK}/mix.wav", "-map", "0:v", "-map", "1:a",
     "-c:v", "libx264", "-preset", "fast", "-crf", "21", "-maxrate", "6M", "-bufsize", "12M", "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", OUT])
print("done", OUT)
