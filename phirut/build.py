#!/usr/bin/env python3
"""ประกอบคลิป พิรุธ จากไฟล์บท JSON (ใช้ได้ทุกตอนตั้งแต่ EP02)

ใช้: python3 build.py script_ep02.json
ต้องมีก่อน: ภาพใน images/ (node render.js ...), เสียงบรรยายใน audio/vo_epXX/<id>.mp3, fonts/Kanit-*.ttf

ฟิลด์ในแต่ละบรรทัดของบท:
  img      ภาพ (path ใต้ images/)
  kind     kb = ซูมช้า (ค่าเริ่มต้น) | static = นิ่ง (ใช้กับภาพเฉลยทีละขั้น) | shake = สั่น
  lead/tail  เวลาเงียบก่อน/หลังเสียงพูด (วินาที)
  sfx      [[ชื่อเสียง, เวลา]] เวลาเป็นวินาทีจากต้นช็อต หรือ "vo:0.5" = ครึ่งทางของเสียงพูด
           ชื่อเสียง: boom, boom_soft, whoosh, marker, tinnitus, heartbeat
  music    pizz | fast | clock | drone | none (บรรทัดติดกันที่ใช้ค่าเดียวกันจะต่อเป็นเพลงเดียว)
  countdown  รายการภาพนับถอยหลัง ภาพละ 1 วินาที เล่นต่อจากบรรทัดนี้
"""
import json, os, subprocess, sys, wave
import numpy as np

ROOT = os.path.dirname(os.path.abspath(__file__))
SR, FPS, W, H = 44100, 30, 1080, 1920
rng = np.random.default_rng(7)

# ---------- เสียงสังเคราะห์ ----------
def env(n, a=0.005, r=0.1):
    e = np.ones(n); na, nr = int(a*SR), int(r*SR)
    if na: e[:na] = np.linspace(0, 1, na)
    if nr: e[-nr:] *= np.linspace(1, 0, nr)
    return e

def onepole(x, a):
    """ฟิลเตอร์ low-pass แบบ one-pole; a เป็นค่าคงที่หรืออาร์เรย์ต่อแซมเปิล"""
    a = np.broadcast_to(np.asarray(a, dtype=float), x.shape)
    y = np.empty_like(x); s = 0.0
    for i in range(len(x)):
        s = (1-a[i])*x[i] + a[i]*s; y[i] = s
    return y

def lowpass(x, cut): return onepole(x, np.exp(-2*np.pi*cut/SR))

def tick(strong=False):
    n = int(.03*SR); x = rng.standard_normal(n) * np.exp(-np.linspace(0, 12, n))
    return (x - lowpass(x, 1500)) * (0.5 if strong else 0.3)

def boom(dur=2.2):
    n = int(dur*SR); t = np.arange(n)/SR
    f = 55*np.exp(-t*1.2) + 30
    x = np.sin(2*np.pi*np.cumsum(f)/SR) * np.exp(-t*2.2)
    m = int(.25*SR); x[:m] += lowpass(rng.standard_normal(m), 400) * np.exp(-np.linspace(0, 8, m)) * 1.5
    return x * 0.9

def whoosh(dur=.6):
    n = int(dur*SR)
    return onepole(rng.standard_normal(n), np.linspace(0.97, 0.6, n)) * np.sin(np.linspace(0, np.pi, n))**2 * 1.2

def marker():
    n = int(.45*SR); t = np.arange(n)/SR; x = rng.standard_normal(n)
    x = lowpass(x - lowpass(x, 1800), 5000)
    return x * (0.55 + 0.45*np.sin(2*np.pi*14*t)) * env(n, .02, .08) * 0.55

def tinnitus(dur=1.8):
    n = int(dur*SR); t = np.arange(n)/SR
    return np.sin(2*np.pi*6800*t) * np.sin(np.linspace(0, np.pi, n)) * 0.07

def heartbeat():
    out = np.zeros(int(.8*SR))
    for off, amp in ((0, 1), (.22, .7)):
        n = int(.18*SR); t = np.arange(n)/SR; i = int(off*SR)
        out[i:i+n] += np.sin(2*np.pi*48*t) * np.exp(-t*22) * amp
    return out * 0.9

SFX = {"boom": boom, "boom_soft": lambda: boom(1.6)*.5, "whoosh": whoosh, "marker": marker,
       "tinnitus": tinnitus, "heartbeat": heartbeat}

def pluck(freq, dur, bright=0.5):
    n = int(dur*SR); N = max(2, int(SR/freq))
    y = np.zeros(n + N); y[:N] = rng.uniform(-1, 1, N)*bright + rng.uniform(-1, 1, N)*(1-bright)*.3
    for s in range(N, n+N, N):
        e = min(s+N, n+N); prev = y[s-N:e-N]
        prev2 = y[s-N-1:e-N-1] if s-N-1 >= 0 else np.concatenate([[0], y[s-N:e-N-1]])
        y[s:e] = 0.497*(prev + prev2[:len(prev)])
    return y[N:] * env(n, .002, .05)

def note(m): return 440*2**((m-69)/12)

def pizz_bed(dur, bpm=96, pattern=None, level=.22):
    pattern = pattern or [38, None, 45, None, 41, None, 45, 44, 38, None, 45, None, 46, 45, 44, 41]
    step = 60/bpm/2; out = np.zeros(int(dur*SR)+SR); i = 0; t = 0.0
    while t < dur:
        m = pattern[i % len(pattern)]; s = int(t*SR)
        if m:
            p = pluck(note(m), .55, .6) * (1 if i % 4 == 0 else .7); out[s:s+len(p)] += p[:len(out)-s]
        if i % 8 == 6:
            p = pluck(note(m+24 if m else 74), .3, .9)*.25; out[s:s+len(p)] += p[:len(out)-s]
        t += step; i += 1
    n = int(dur*SR)
    return out[:n] * level * env(n, min(1.5, dur/4), min(1.5, dur/4))

def drone(dur, level=.12):
    n = int(dur*SR); t = np.arange(n)/SR
    x = np.sin(2*np.pi*36.7*t) + .6*np.sin(2*np.pi*55*t) + .3*np.sin(2*np.pi*73.4*t*(1+.002*np.sin(t)))
    return x * (0.6 + 0.4*np.sin(2*np.pi*.15*t)) * env(n, min(1.0, dur/4), min(1.0, dur/4)) * level

def clock_bed(dur):
    out = np.zeros(int(dur*SR)+SR)
    for k in np.arange(0, dur, .5):
        c = tick(k % 1 == 0); s = int(k*SR); out[s:s+len(c)] += c
    return out[:int(dur*SR)]

def music_for(name, dur):
    if name == "pizz": return pizz_bed(dur)
    if name == "fast": return pizz_bed(dur, bpm=120, pattern=[38, 38, 45, 38, 46, 38, 45, 44], level=.17) + drone(dur, .06)
    if name == "clock": return clock_bed(dur)
    if name == "drone": return drone(dur)
    return np.zeros(int(dur*SR))

# ---------- main ----------
def main(cfg_path):
    cfg = json.load(open(cfg_path))
    ep = os.path.splitext(os.path.basename(cfg_path))[0].replace("script_", "")
    vo_dir, work = f"{ROOT}/audio/vo_{ep}", f"{ROOT}/out/{ep}"
    os.makedirs(f"{work}/seg", exist_ok=True)
    tempo = cfg.get("tempo", 1.15)

    def load_vo(path):
        raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-af", f"atempo={tempo}", "-f", "f32le",
                              "-ac", "1", "-ar", str(SR), "-"], check=True, capture_output=True).stdout
        return np.frombuffer(raw, dtype=np.float32).copy()

    segs, subs, vos, sfx, mus = [], [], [], [], []   # mus: (start, end, name)
    t = 0.0
    for l in cfg["lines"]:
        vo = load_vo(f"{vo_dir}/{l['id']}.mp3"); vlen = len(vo)/SR
        lead, tail = l.get("lead", .35), l.get("tail", .45)
        dur = lead + vlen + tail
        segs.append((l["img"], dur, l.get("kind", "kb")))
        vos.append((t+lead, vo))
        parts = [p for p in l["sub"].split("|") if p]; tot = sum(map(len, parts)); s0 = t+lead
        for p in parts:
            pd = vlen*len(p)/tot; subs.append((s0, s0+pd, p)); s0 += pd
        for name, at in l.get("sfx", []):
            off = lead + vlen*float(at[3:]) if isinstance(at, str) else at
            sfx.append((t+off, SFX[name]()))
        seg_music = l.get("music", "none")
        t += dur
        for img in l.get("countdown", []):
            segs.append((img, 1.0, "static")); sfx += [(t, tick(True)), (t+.5, tick())]; t += 1.0
        if mus and mus[-1][2] == seg_music: mus[-1] = (mus[-1][0], t, seg_music)
        else: mus.append((t - dur - len(l.get("countdown", [])), t, seg_music))
    if "end" in cfg:
        segs.append((cfg["end"]["img"], cfg["end"]["dur"], "kb"))
        if mus and mus[-1][2] != "none": mus[-1] = (mus[-1][0], t + cfg["end"]["dur"], mus[-1][2])
        t += cfg["end"]["dur"]
    total = t

    mix = np.zeros(int((total+1)*SR)); music = np.zeros_like(mix); mask = np.zeros_like(mix)
    def put(buf, start, x, g=1.0):
        s = int(start*SR); e = min(len(buf), s+len(x)); buf[s:e] += x[:e-s]*g
    for a, b, name in mus: put(music, a, music_for(name, b-a))
    for st, x in vos:
        put(mix, st, x); s = int(st*SR); mask[s:s+len(x)] = 1
    k = int(.25*SR); duck = np.convolve(mask, np.ones(k)/k, mode="same")
    mix += music * (1 - .45*duck)
    for st, x in sfx: put(mix, st, x, .8)
    mix = np.tanh(mix[:int(total*SR)]*1.1) / np.tanh(1.1) * .92
    with wave.open(f"{work}/mix.wav", "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((np.clip(mix, -1, 1)*32767).astype(np.int16).tobytes())

    def ts(x): return f"{int(x//3600)}:{int(x % 3600//60):02d}:{x % 60:05.2f}"
    ass = ["[Script Info]", "ScriptType: v4.00+", f"PlayResX: {W}", f"PlayResY: {H}", "WrapStyle: 0", "",
           "[V4+ Styles]",
           "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
           "Style: Sub,Kanit Medium,50,&H00FFFFFF,&H00FFFFFF,&H28000000,&H00000000,0,0,0,0,100,100,0,0,3,12,0,2,60,60,165,1",
           "", "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
    for s, e, p in subs:
        ass.append(f"Dialogue: 0,{ts(s)},{ts(e)},Sub,,0,0,0,,{p.replace('“', '\"').replace('”', '\"')}")
    open(f"{work}/subs.ass", "w").write("\n".join(ass))

    lst = []
    for i, (img, dur, kind) in enumerate(segs):
        n = max(1, round(dur*FPS)); out = f"{work}/seg/{i:02d}.mp4"
        if kind == "kb":
            z = f"1+0.07*on/{n}" if i % 2 == 0 else f"1.07-0.07*on/{n}"
            vf = f"scale={W*2}:{H*2},zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s={W}x{H}:fps={FPS}"
        elif kind == "shake":
            vf = f"scale={W+80}:{H+140},crop={W}:{H}:'40+30*sin(n*1.7)':'70+30*cos(n*2.3)',eq=contrast=1.15,fps={FPS}"
        else:
            vf = f"scale={W}:{H},fps={FPS}"
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-loop", "1", "-i", f"{ROOT}/images/{img}", "-frames:v", str(n),
                        "-vf", vf + ",format=yuv420p", "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-r", str(FPS), out], check=True)
        lst.append(f"file '{out}'")
    open(f"{work}/seg/list.txt", "w").write("\n".join(lst))
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", f"{work}/seg/list.txt",
                    "-c", "copy", f"{work}/video_raw.mp4"], check=True)
    out = f"{ROOT}/{cfg.get('out', f'out/phirut_{ep}.mp4')}"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", f"{work}/video_raw.mp4", "-i", f"{work}/mix.wav",
                    "-vf", f"subtitles={work}/subs.ass:fontsdir={ROOT}/fonts,fade=t=in:st=0:d=0.4",
                    "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-c:a", "aac", "-b:a", "192k",
                    "-shortest", "-movflags", "+faststart", out], check=True)
    print(f"done: {os.path.relpath(out, ROOT)} ({total:.1f}s)")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "script_ep02.json")
