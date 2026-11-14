#!/usr/bin/env python3
"""ประกอบคลิป พิรุธ EP01: ภาพ + เสียงบรรยาย + เสียงประกอบ/ดนตรีที่สังเคราะห์เอง + ซับไตเติล

ต้องมีก่อน: images/*.png (node render.js), audio/vo/*.mp3 (เสียงจาก ElevenLabs), fonts/Kanit-*.ttf
ใช้: python3 build_ep01.py  ->  out/phirut_ep01.mp4
"""
import json, os, subprocess, wave
import numpy as np

ROOT = os.path.dirname(os.path.abspath(__file__))
SR = 44100
FPS = 30
TEMPO = 1.15           # เร่งเสียงบรรยายเล็กน้อยให้จังหวะกระชับ
W, H = 1080, 1920
os.makedirs(f"{ROOT}/out/seg", exist_ok=True)
rng = np.random.default_rng(7)

def sh(*a):
    subprocess.run(a, check=True, capture_output=True)

def load_vo(path):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-af", f"atempo={TEMPO}",
                          "-f", "f32le", "-ac", "1", "-ar", str(SR), "-"], check=True, capture_output=True).stdout
    return np.frombuffer(raw, dtype=np.float32).copy()

# ---------- เสียงสังเคราะห์ ----------
def env(n, a=0.005, r=0.1):
    e = np.ones(n); na, nr = int(a*SR), int(r*SR)
    if na: e[:na] = np.linspace(0, 1, na)
    if nr: e[-nr:] *= np.linspace(1, 0, nr)
    return e

def lowpass(x, cut):
    a = np.exp(-2*np.pi*cut/SR); y = np.zeros_like(x); s = 0.0
    for i in range(len(x)):          # สั้น ๆ เท่านั้น
        s = (1-a)*x[i] + a*s; y[i] = s
    return y

def tick(strong=False):
    n = int(.03*SR); x = rng.standard_normal(n) * np.exp(-np.linspace(0, 12, n))
    x = x - lowpass(x, 1500)                  # เหลือย่านสูง เป็นเสียง "ติ๊ก"
    return x * (0.5 if strong else 0.3)

def boom(dur=2.2):
    n = int(dur*SR); t = np.arange(n)/SR
    f = 55*np.exp(-t*1.2) + 30
    x = np.sin(2*np.pi*np.cumsum(f)/SR) * np.exp(-t*2.2)
    nz = lowpass(rng.standard_normal(int(.25*SR)), 400) * np.exp(-np.linspace(0, 8, int(.25*SR)))
    x[:len(nz)] += nz*1.5
    return x * 0.9

def whoosh(dur=.6):
    n = int(dur*SR); x = rng.standard_normal(n)
    a = np.linspace(0.97, 0.6, n); y = np.zeros(n); s = 0.0   # ฟิลเตอร์เปิดขึ้นเรื่อย ๆ
    for i in range(n):
        s = (1-a[i])*x[i] + a[i]*s; y[i] = s
    return y * np.sin(np.linspace(0, np.pi, n))**2 * 1.2

def marker():
    """เสียงปากกาเมจิกวง: นอยส์ย่านกลางสูง สั่นเป็นจังหวะ"""
    n = int(.45*SR); t = np.arange(n)/SR; x = rng.standard_normal(n)
    x = x - lowpass(x, 1800); x = lowpass(x, 5000)
    mod = 0.55 + 0.45*np.sin(2*np.pi*14*t)
    return x * mod * env(n, .02, .08) * 0.55

def tinnitus(dur=1.6):
    n = int(dur*SR); t = np.arange(n)/SR
    return np.sin(2*np.pi*6800*t) * np.sin(np.linspace(0, np.pi, n)) * 0.07

def heartbeat():
    out = np.zeros(int(.8*SR))
    for off, amp in ((0, 1), (.22, .7)):
        n = int(.18*SR); t = np.arange(n)/SR
        b = np.sin(2*np.pi*48*t) * np.exp(-t*22) * amp
        i = int(off*SR); out[i:i+n] += b
    return out * 0.9

def pluck(freq, dur, bright=0.5):
    """สายดีด (Karplus-Strong) ใช้ทำพิซซิกาโต"""
    n = int(dur*SR); N = max(2, int(SR/freq))
    y = np.zeros(n + N); y[:N] = rng.uniform(-1, 1, N) * bright + rng.uniform(-1, 1, N)*(1-bright)*.3
    for s in range(N, n+N, N):                # ทำทีละบล็อกความยาว N
        e = min(s+N, n+N)
        prev = y[s-N:e-N]; prev2 = y[s-N-1:e-N-1] if s-N-1 >= 0 else np.concatenate([[0], y[s-N:e-N-1]])
        y[s:e] = 0.497*(prev + prev2[:len(prev)])
    return y[N:] * env(n, .002, .05)

def note(m): return 440*2**((m-69)/12)

def pizz_bed(dur, bpm=96, pattern=None, level=.22):
    """ไลน์พิซซิกาโตแนวนักสืบ (ดีไมเนอร์ เดินเบส + โน้ตตอบ)"""
    pattern = pattern or [38, None, 45, None, 41, None, 45, 44, 38, None, 45, None, 46, 45, 44, 41]
    step = 60/bpm/2; out = np.zeros(int(dur*SR)+SR); i = 0; t = 0.0
    while t < dur:
        m = pattern[i % len(pattern)]
        if m:
            p = pluck(note(m), .55, .6) * (1 if i % 4 == 0 else .7)
            s = int(t*SR); out[s:s+len(p)] += p[:len(out)-s]
        if i % 8 == 6:                       # โน้ตสูงแทรกให้ขี้เล่น
            p = pluck(note(m+24 if m else 74), .3, .9)*.25
            s = int(t*SR); out[s:s+len(p)] += p[:len(out)-s]
        t += step; i += 1
    return out[:int(dur*SR)] * level

def drone(dur, level=.10):
    n = int(dur*SR); t = np.arange(n)/SR
    x = (np.sin(2*np.pi*36.7*t) + .6*np.sin(2*np.pi*55*t) + .3*np.sin(2*np.pi*73.4*t*(1+.002*np.sin(t))))
    return x * (0.6 + 0.4*np.sin(2*np.pi*.15*t)) * env(n, 1.0, 1.0) * level

# ---------- ไทม์ไลน์ ----------
d = json.load(open(f"{ROOT}/script_ep01.json"))
segs, subs = [], []          # segs: (image, start, dur, kind)
vo_track = []                # (start, samples)
sfx = []                     # (start, samples)
t = 0.0
section = {}                 # ช่วงเวลาไว้วางดนตรี
for l in d["lines"]:
    lid = l["id"]
    if lid == "16":          # การ์ดปิดท้าย
        segs.append(("10_end.png", t, 4.5, "kb")); t += 4.5; break
    vo = load_vo(f"{ROOT}/audio/vo/{lid}.mp3")
    lead = {"01": .6, "08": 1.4, "15": .8}.get(lid, .35)
    tail = {"01": .5, "03": .4, "07": .2, "13": .9, "14": .8, "15": 1.6}.get(lid, .45)
    dur = lead + len(vo)/SR + tail
    kind = "static" if lid in ("09", "10", "11", "12", "13") else ("shake" if lid == "08" else "kb")
    segs.append((l["img"], t, dur, kind))
    vo_track.append((t+lead, vo))
    # ซับ: แบ่งเวลาตามความยาวข้อความ
    parts = [p for p in l["sub"].split("|") if p]
    tot = sum(len(p) for p in parts); s0 = t+lead; vlen = len(vo)/SR
    for p in parts:
        pd = vlen*len(p)/tot; subs.append((s0, s0+pd, p)); s0 += pd
    # เสียงประกอบตามฉาก
    if lid == "01": sfx += [(t, boom())]
    if lid in ("02", "04", "05", "06"): sfx += [(t, whoosh())]
    if lid == "03": sfx += [(t, whoosh()), (t+lead+len(vo)/SR*.28, heartbeat())]
    if lid == "08": sfx += [(t, tinnitus(1.8)), (t+1.0, boom(1.6)*.5)]
    if lid in ("09", "10", "11", "12", "13"): sfx += [(t+.05, marker())]
    if lid == "15": sfx += [(t+lead+len(vo)/SR*.55, boom(2.6))]
    section[lid] = (t, t+dur)
    t += dur
    if lid == "07":          # นับถอยหลัง 3-2-1 เงียบ มีแต่เสียงนาฬิกา
        for k in (3, 2, 1):
            segs.append((f"08_challenge_{k}.png", t, 1.0, "static"))
            sfx += [(t, tick(True)), (t+.5, tick())]
            t += 1.0
        section["count"] = (t-3, t)
total = t

# ---------- มิกซ์เสียง ----------
mix = np.zeros(int((total+1)*SR))
def put(start, x, gain=1.0):
    s = int(start*SR); e = min(len(mix), s+len(x)); mix[s:e] += x[:e-s]*gain

music = np.zeros_like(mix)
def mput(start, x):
    s = int(start*SR); e = min(len(music), s+len(x)); music[s:e] += x[:e-s]
a, b = section["01"][0], section["06"][1]
mput(a+.8, pizz_bed(b-a-.8) * env(int((b-a-.8)*SR)+0, 1.5, 1.5)[:int((b-a-.8)*SR)])
a, b = section["07"][0], section["count"][1]
clock = np.zeros(int((b-a)*SR))
for k in np.arange(0, b-a-3, .5):
    c = tick(k % 1 == 0); s = int(k*SR); clock[s:s+len(c)] += c
mput(a, clock)
a, b = section["09"][0], section["14"][1]
fast = [38, 38, 45, 38, 46, 38, 45, 44]
mput(a, pizz_bed(b-a, bpm=120, pattern=fast, level=.17) * env(int((b-a)*SR), .3, 2.0)[:int((b-a)*SR)])
mput(a, drone(b-a, .06))
a, b = section["15"][0], total
mput(a, drone(b-a, .12))

vo_mask = np.zeros_like(mix)
for st, x in vo_track:
    put(st, x, 1.0)
    s = int(st*SR); vo_mask[s:s+len(x)] = 1
# ducking: ดนตรีเบาลงเมื่อมีเสียงพูด
k = int(.25*SR); duck = np.convolve(vo_mask, np.ones(k)/k, mode="same")
mix += music * (1 - .45*duck)
for st, x in sfx: put(st, x, .8)
mix = mix[:int(total*SR)]
mix = np.tanh(mix*1.1) / np.tanh(1.1) * .92
with wave.open(f"{ROOT}/out/mix.wav", "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((np.clip(mix, -1, 1)*32767).astype(np.int16).tobytes())

# ---------- ซับไตเติล (ASS) ----------
def ts(x):
    h = int(x//3600); m = int(x % 3600//60); s = x % 60
    return f"{h}:{m:02d}:{s:05.2f}"
ass = ["[Script Info]", "ScriptType: v4.00+", f"PlayResX: {W}", f"PlayResY: {H}", "WrapStyle: 0", "",
       "[V4+ Styles]",
       "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
       "Style: Sub,Kanit Medium,50,&H00FFFFFF,&H00FFFFFF,&H28000000,&H00000000,0,0,0,0,100,100,0,0,3,12,0,2,60,60,165,1",
       "", "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
for s, e, p in subs:
    p = p.replace("“", "\"").replace("”", "\"")
    ass.append(f"Dialogue: 0,{ts(s)},{ts(e)},Sub,,0,0,0,,{p}")
open(f"{ROOT}/out/subs.ass", "w").write("\n".join(ass))

# ---------- วิดีโอ ----------
lst = []
for i, (img, st, dur, kind) in enumerate(segs):
    n = max(1, round(dur*FPS)); out = f"{ROOT}/out/seg/{i:02d}.mp4"
    src = f"{ROOT}/images/{img}"
    if kind == "kb":
        zin = i % 2 == 0
        z = f"1+0.07*on/{n}" if zin else f"1.07-0.07*on/{n}"
        vf = (f"scale={W*2}:{H*2},zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s={W}x{H}:fps={FPS}")
    elif kind == "shake":
        vf = (f"scale={W+80}:{H+140},crop={W}:{H}:'40+30*sin(n*1.7)':'70+30*cos(n*2.3)',"
              f"eq=contrast=1.15,fps={FPS}")
    else:
        vf = f"scale={W}:{H},fps={FPS}"
    vf += f",format=yuv420p"
    sh("ffmpeg", "-y", "-v", "error", "-loop", "1", "-i", src, "-frames:v", str(n), "-vf", vf,
       "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-r", str(FPS), out)
    lst.append(f"file '{out}'")
open(f"{ROOT}/out/seg/list.txt", "w").write("\n".join(lst))
sh("ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", f"{ROOT}/out/seg/list.txt",
   "-c", "copy", f"{ROOT}/out/video_raw.mp4")
sh("ffmpeg", "-y", "-v", "error", "-i", f"{ROOT}/out/video_raw.mp4", "-i", f"{ROOT}/out/mix.wav",
   "-vf", f"subtitles={ROOT}/out/subs.ass:fontsdir={ROOT}/fonts,fade=t=in:st=0:d=0.4",
   "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-c:a", "aac", "-b:a", "192k",
   "-shortest", "-movflags", "+faststart", f"{ROOT}/out/phirut_ep01.mp4")
print(f"done: out/phirut_ep01.mp4  ({total:.1f}s)")
