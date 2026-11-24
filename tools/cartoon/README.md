# tools/cartoon — ระบบทำการ์ตูนหัวกลมด้วยโค้ด

ทำคลิปแนวตั้ง 1080×1920 ได้ครบในเครื่องเดียว: ภาพ เสียงพูด เพลง เสียงประกอบ ซับ และตัดต่อ

## ไฟล์
- `engine.html`: วาดฉาก ตัวละคร เอฟเฟกต์ ป้ายชื่อ ตัวหนังสือเด้ง และซับ บน canvas
- `render.js`: ใช้ Playwright เปิด engine แล้วส่งภาพทีละเฟรมเข้า ffmpeg
- `build.py`: สร้างเสียงพูดด้วย ElevenLabs, คำนวณเวลาแต่ละฉากจากความยาวเสียง, เรนเดอร์ภาพ, ผสมเพลงกับเสียงประกอบ (ลดเสียงเพลงเองตอนมีคนพูด)
- `fonts/`: ฟอนต์ Kanit (SIL Open Font License)

## ใช้งาน
```
python3 tools/cartoon/build.py <episode.json> <cast.json> <assets_dir> <work_dir> <out.mp4>
```
- `TIMELINE_ONLY=1` สร้างแค่เสียงกับไทม์ไลน์ ไม่เรนเดอร์ภาพ
- `REVIDEO=1` บังคับเรนเดอร์ภาพใหม่
- ดูภาพนิ่งก่อนเรนเดอร์จริง: `node tools/cartoon/render.js <work>/timeline.json <cast.json> <prefix> 3,10,20`

## ไฟล์ตอน (episode.json)
แต่ละฉากกำหนด: `bg` (restaurant, street, hub, room, rain, boardroom) หรือ `card`, `actors` (id, x, s, expr, pose, item, enter),
`lines` (who, text, expr/pose ระหว่างพูด), `pops` (ตัวหนังสือเด้ง), `fx` (coins, sparkle, flash, shake), `sfx`, `mood` (light, tense, sad, triumph), `tag`, `cam`
- **expr:** n ปกติ · h ยิ้ม · s เศร้า · a โกรธ · x ตกใจ · m ยิ้มเยาะ · c ร้องไห้
- **pose:** down · wave · point · hold · hips · phone · throw · kneel · shrug · facepalm
