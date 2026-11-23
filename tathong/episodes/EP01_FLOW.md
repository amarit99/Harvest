# ตาทอง ตอนที่ 1 — "แว่นของคนตาย" · ชุดคำสั่งสำหรับ Google Flow

ใช้คู่กับบท [`EP01.md`](EP01.md) ไฟล์นี้แปลงบทเป็น **11 คลิป** สำหรับสร้างวิดีโอใน Flow (Veo)
รวมความยาวหลังตัดต่อประมาณ **74 วินาที**

**สไตล์ภาพ:** การ์ตูน 2D เวกเตอร์ตัวจิ๋ว (chibi) ตามภาพตัวอย่าง [`../ref/boon_style.jpg`](../ref/boon_style.jpg) เล่าเรื่องแบบละครสั้น (ถ่ายใกล้ ตัดเร็ว ตาเรืองแสงทองกับเส้นแสงสแกน)

---

## ขั้นที่ 0 · ตั้งค่าใน Flow

- **อัตราส่วน:** 9:16 (แนวตั้ง)
- **โมเดล:** Veo รุ่นคุณภาพสูงสุดที่บัญชีใช้ได้ ใช้ตัวที่มีเสียงในตัว
- **โหมด:** ใช้ **Ingredients to Video** สำหรับคลิปที่มีตัวละคร โดยใส่ภาพอ้างอิงตัวละครจากขั้นที่ 1 เป็น ingredient หน้าตัวละครจะได้เหมือนกันทุกคลิป
- **ทุกคลิปยาว 8 วินาที:** ผมจะตัดให้เหลือตามความยาวในตาราง
- **ถ้า Flow เตือนเรื่องความปลอดภัยของผู้เยาว์:** สไตล์ตัวจิ๋วทำให้ตัวละครดูเหมือนเด็ก ทุก prompt จึงระบุอายุ และขึ้นต้นด้วย `All characters are adults.` อย่าลบส่วนนี้ออก
- **ห้ามมีตัวหนังสือและซับในวิดีโอ:** ป้ายราคา ชื่อเรื่อง และซับไตเติล ผมใส่ตอนตัดต่อ

## ขั้นที่ 1 · สร้างภาพอ้างอิงตัวละคร (สร้างภาพใน Flow ก่อน)

สร้างคนละ 2–4 ภาพ แล้วเลือกภาพที่ชอบที่สุดเก็บไว้เป็น ingredient
**บุญ:** ใช้ภาพ [`../ref/boon_style.jpg`](../ref/boon_style.jpg) เป็น ingredient ได้เลย หรือสร้างใหม่จาก R1
ทุกภาพอ้างอิงต่อท้ายด้วย Style Preset เดียวกัน เพื่อให้ลายเส้นเหมือนกันทุกตัว

**R1 · บุญ**
```
Boon, a Thai junk-buyer man aged 28, spiky messy black hair, faded olive-green work shirt with rolled sleeves, olive work pants, brown boots, a white towel draped around his neck, kind face, full body, standing pose, 2D vector game art style, chibi proportions, bold clean dark-brown outlines, cel-shaded coloring, warm muted earthy color palette, minimalist cute facial features with dot eyes and small smile, plain warm cream background (#F7EEDD), dynamic action pose, simple sketchy ground lines, flat vector illustration, vertical 9:16.
```

**R2 · แว่น (พร็อพ)**
```
old vintage round glasses with a thin gold metal frame, slightly scratched lenses, a small golden sparkle, centered object, no character, 2D vector game art style, chibi proportions, bold clean dark-brown outlines, cel-shaded coloring, warm muted earthy color palette, minimalist cute facial features with dot eyes and small smile, plain warm cream background (#F7EEDD), dynamic action pose, simple sketchy ground lines, flat vector illustration, vertical 9:16.
```

**R3 · ฝน**
```
Fon, a Thai woman aged 27, shoulder-length straight black hair with bangs, simple cream blouse, long brown skirt, gentle slightly worried face, full body, standing shyly with hands clasped, 2D vector game art style, chibi proportions, bold clean dark-brown outlines, cel-shaded coloring, warm muted earthy color palette, minimalist cute facial features with dot eyes and small smile, plain warm cream background (#F7EEDD), dynamic action pose, simple sketchy ground lines, flat vector illustration, vertical 9:16.
```

**R4 · แม่ยาย**
```
the mother-in-law, a plump Thai woman aged 58, short curly permed hair, red silk blouse, many thick gold necklaces and gold bracelets, holding a folding fan, arrogant sneering face with raised eyebrows, full body, hands on hips, 2D vector game art style, chibi proportions, bold clean dark-brown outlines, cel-shaded coloring, warm muted earthy color palette, minimalist cute facial features with dot eyes and small smile, plain warm cream background (#F7EEDD), dynamic action pose, simple sketchy ground lines, flat vector illustration, vertical 9:16.
```

**R5 · เคน**
```
Ken, a Thai man aged 35, slicked-back hair, navy-blue suit with white shirt, flashy gold wristwatch, smug smirk, full body, showing off with one hand raised, 2D vector game art style, chibi proportions, bold clean dark-brown outlines, cel-shaded coloring, warm muted earthy color palette, minimalist cute facial features with dot eyes and small smile, plain warm cream background (#F7EEDD), dynamic action pose, simple sketchy ground lines, flat vector illustration, vertical 9:16.
```

---

## ขั้นที่ 2 · คลิปตอนที่ 1

คำต่อท้ายนี้ใส่ไว้ในทุก prompt แล้ว:
`All characters are adults. 2D vector game art style animation, chibi proportions, bold clean dark-brown outlines, cel-shaded coloring with two-tone hard shadows, warm muted earthy color palette, minimalist cute faces with dot eyes, simple flat vector background, smooth 2D animation, vertical 9:16. No on-screen text, no subtitles.`

**เรื่องเสียงพูด:** ทุกคลิปมี prompt สองแบบ
- **แบบ A** ให้ Veo พูดภาษาไทยเอง ลองแบบนี้ก่อน
- **แบบ B** ไม่มีเสียงพูด ใช้เมื่อสำเนียงไทยที่ Veo พูดออกมาฟังไม่ดี แล้วผมจะพากย์ทับทีหลัง

ประโยค `(VO)` คือเสียงบรรยายในใจของบุญ ไม่ต้องให้ Veo พูด ผมใส่ทีหลังทุกครั้ง

---

### คลิป 1 · 0:00–0:06 · ของขวัญลงถังขยะ (ปมเปิด)
**Ingredients:** R4 (แม่ยาย), R1 (บุญ)
```
At a lively Thai family birthday party in a suburban house, the arrogant mother-in-law (the woman in the red silk blouse with gold necklaces) holds up a small cheap gift box with two fingers, looks at it with disgust, then drops it into a trash bin next to her. Relatives around the banquet table burst out laughing. Behind her, the 28-year-old man in the olive work shirt with a towel around his neck stands frozen, humiliated. Fast push-in on her sneering face. Sound: party chatter, mocking laughter. She says in Thai: "ของขวัญเก้าสิบเก้าบาท… เก็บมาจากถังขยะรึไง ไอ้บุญ". All characters are adults. 2D vector game art style animation, chibi proportions, bold clean dark-brown outlines, cel-shaded coloring with two-tone hard shadows, warm muted earthy color palette, minimalist cute faces with dot eyes, simple flat vector background, smooth 2D animation, vertical 9:16. No on-screen text, no subtitles.
```
**แบบ B:** ลบประโยค `She says in Thai: ...` แล้วเพิ่ม `She speaks mockingly but no audible dialogue.`
**ตัดใช้:** 6 วินาที

### คลิป 2 · 0:06–0:12 · เคนใส่สร้อยทอง
**Ingredients:** R5 (เคน), R4 (แม่ยาย)
```
The smug man in the navy suit and gold watch stands behind the mother-in-law in the red silk blouse and fastens a thick shiny gold necklace around her neck at the birthday banquet table. She touches the necklace, delighted, beaming with pride; relatives clap and cheer. Medium close-up, warm festive lighting, slow orbit around them. Sound: applause, cheering. He says in Thai: "สร้อยทองห้าบาทครับแม่". All characters are adults. 2D vector game art style animation, chibi proportions, bold clean dark-brown outlines, cel-shaded coloring with two-tone hard shadows, warm muted earthy color palette, minimalist cute faces with dot eyes, simple flat vector background, smooth 2D animation, vertical 9:16. No on-screen text, no subtitles.
```
**ตัดใช้:** 6 วินาที

### คลิป 3 · 0:12–0:19 · บุญยืนคนเดียว
**Ingredients:** R1 (บุญ)
```
The 28-year-old man in the faded olive work shirt with a white towel around his neck stands alone by the doorway of a bright, noisy family party, holding his cap with both hands, looking down silently. Everyone ignores him; he is half in shadow while the party glows warmly behind him. Slow dolly-in to his face, his jaw tightens. Sound: muffled party noise, no dialogue. All characters are adults. 2D vector game art style animation, chibi proportions, bold clean dark-brown outlines, cel-shaded coloring with two-tone hard shadows, warm muted earthy color palette, minimalist cute faces with dot eyes, simple flat vector background, smooth 2D animation, vertical 9:16. No on-screen text, no subtitles.
```
**(VO) บุญ:** ผมชื่อบุญ อาชีพรับซื้อของเก่า… ในบ้านนี้ ผมมีค่าน้อยกว่าเศษเหล็ก
**ตัดใช้:** 7 วินาที

### คลิป 4 · 0:19–0:25 · ฝนจับมือบุญ
**Ingredients:** R3 (ฝน), R1 (บุญ), R4 (แม่ยาย)
```
All characters are adults. At a birthday banquet table, the plump 58-year-old mother-in-law in the red silk blouse and gold necklaces turns to her adult daughter Fon, a 27-year-old married woman with bangs in a cream blouse, and speaks to her scornfully while fanning herself. Fon lowers her eyes and stays silent. Next to Fon sits her husband Boon, a 28-year-old man in an olive work shirt with a white towel around his neck. On top of the table, Fon quietly places her hand over her husband's hand and gives it a small supportive squeeze; he looks at her gratefully. Medium shot, then close-up on the two hands resting on the tabletop. Sound: quiet room tone. The mother says in Thai: "ฝน… แกน่าจะแต่งกับคนแบบเคน". 2D vector game art style animation, chibi proportions, bold clean dark-brown outlines, cel-shaded coloring with two-tone hard shadows, warm muted earthy color palette, minimalist cute faces with dot eyes, simple flat vector background, smooth 2D animation, vertical 9:16. No on-screen text, no subtitles.
```
**(VO) บุญ:** มีแค่ฝนคนเดียว ที่ยังจับมือผมไว้
**ตัดใช้:** 6 วินาที

### คลิป 5 · 0:25–0:31 · บ้านคนตาย (ชื่อเรื่องขึ้น)
**Ingredients:** R1 (บุญ)
```
Night. An old rusty pickup truck loaded with scrap metal pulls up in front of a dark, old wooden Thai house on stilts, moonlight, insects chirping. The 28-year-old man in the olive work shirt gets out. An elderly Thai man in a white undershirt comes down the wooden stairs carrying a dusty cardboard box and hands it to him with a tired shrug. Wide shot, then medium. Sound: crickets, truck engine ticking. The old man says in Thai: "เอาไปเถอะ… ของพวกนี้ไม่มีค่าอะไรหรอก". All characters are adults. 2D vector game art style animation, chibi proportions, bold clean dark-brown outlines, cel-shaded coloring with two-tone hard shadows, warm muted earthy color palette, minimalist cute faces with dot eyes, simple flat vector background, smooth 2D animation, vertical 9:16. No on-screen text, no subtitles.
```
**ผมใส่เพิ่ม:** ชื่อเรื่อง **ตาทอง**
**ตัดใช้:** 6 วินาที

### คลิป 6 · 0:31–0:38 · สวมแว่น ตาเรืองแสงทอง ⭐
**Ingredients:** R1 (บุญ), R2 (แว่น)
```
Inside a dim, dusty room lit by a single flashlight, the 28-year-old man in the olive work shirt pulls a pair of old round thin gold-rimmed glasses out of the cardboard box, wipes the lens with the towel around his neck, and slowly puts them on. The instant the glasses touch his face, his dot eyes begin to glow bright gold behind the lenses, a soft golden light pulses outward, and dust particles shimmer in the air. Close-up on his face, slow push-in to his glowing eyes. Sound: a soft magical shimmer, rising hum, no dialogue. All characters are adults. 2D vector game art style animation, chibi proportions, bold clean dark-brown outlines, cel-shaded coloring with two-tone hard shadows, warm muted earthy color palette, minimalist cute faces with dot eyes, simple flat vector background, smooth 2D animation, vertical 9:16. No on-screen text, no subtitles.
```
**ผมใส่เพิ่ม:** เสียงติ๊ง กับแจ้งเตือน "ติ๊ง! ระบบเริ่มทำงาน"
**ตัดใช้:** 7 วินาที

### คลิป 7 · 0:38–0:45 · แสงสแกนกวาดผ่านของเก่า
```
Point-of-view shot slowly panning across a dusty dark room full of old belongings: an old radio, a wall clock, an old sewing machine, stacks of boxes. A thin glowing golden scanning line sweeps across each object one after another, leaving a brief golden shimmer on each. Floating dust in the flashlight beam. Leave empty space around the objects. Sound: soft electronic chime each time the golden line passes an object. All characters are adults. 2D vector game art style animation, chibi proportions, bold clean dark-brown outlines, cel-shaded coloring with two-tone hard shadows, warm muted earthy color palette, minimalist cute faces with dot eyes, simple flat vector background, smooth 2D animation, vertical 9:16. No on-screen text, no subtitles.
```
**ผมใส่เพิ่ม:** ป้ายราคาเด้งขึ้นทีละชิ้น (เทา ฿12 · เทา ฿40 · เขียว ฿350)
**(VO) บุญ:** ทุกอย่างในห้อง… มีราคาลอยอยู่ตรงหน้าผม
**ตัดใช้:** 7 วินาที

### คลิป 8 · 0:45–0:52 · ชามลายคราม (จุดสะใจ) ⭐
**Ingredients:** R1 (บุญ), R2 (แว่น)
```
The 28-year-old man wearing round thin gold-rimmed glasses lifts an old blue-and-white porcelain bowl out of the junk box and holds it close in front of his face. Extreme close-up: the bowl fills half the frame while one of his eyes glows bright gold behind the lens. A thin bright golden scanning line slowly sweeps across the surface of the bowl from edge to edge, leaving a purple shimmer. His eyes widen in disbelief. Sound: magical scanning sound, low bass hit, no dialogue. All characters are adults. 2D vector game art style animation, chibi proportions, bold clean dark-brown outlines, cel-shaded coloring with two-tone hard shadows, warm muted earthy color palette, minimalist cute faces with dot eyes, simple flat vector background, smooth 2D animation, vertical 9:16. No on-screen text, no subtitles.
```
**ผมใส่เพิ่ม:** ป้ายสีม่วง **฿180,000**
**(VO) บุญ:** ชามที่เขาจะเอาไปทิ้ง… แสนแปด
**ตัดใช้:** 7 วินาที

### คลิป 9 · 0:52–0:58 · ถอดแว่น สวมใหม่
**Ingredients:** R1 (บุญ), R2 (แว่น)
```
Close-up: the 28-year-old man takes off the round gold-rimmed glasses, the golden glow in his eyes instantly disappears and his dot eyes look normal; he blinks, confused. He slowly puts the glasses back on and his dot eyes glow gold again. He lets out a short stunned laugh. Dim dusty room, flashlight light. Sound: glow fading sound, then shimmer returning, his short breathy laugh, no dialogue. All characters are adults. 2D vector game art style animation, chibi proportions, bold clean dark-brown outlines, cel-shaded coloring with two-tone hard shadows, warm muted earthy color palette, minimalist cute faces with dot eyes, simple flat vector background, smooth 2D animation, vertical 9:16. No on-screen text, no subtitles.
```
**(VO) บุญ:** ผมถอดแว่น ป้ายก็หาย… ผมสวมใหม่ มันก็กลับมา
**ตัดใช้:** 6 วินาที

### คลิป 10 · 0:58–1:06 · ลอตเตอรี่เรืองแสงทอง (ปมค้าง)
**Ingredients:** R1 (บุญ), R2 (แว่น)
```
Night, a quiet wet street. The 28-year-old man wearing round gold-rimmed glasses walks past a small roadside Thai lottery ticket stall under a single street lamp. He stops. Close-up of the wooden board with rows of paper lottery tickets: one single ticket in the middle starts glowing bright gold with sparkles while all the others stay dark. His face lit by the golden glow. No readable numbers or text on the tickets. Sound: night street ambience, a deep magical chime, music cuts to silence. All characters are adults. 2D vector game art style animation, chibi proportions, bold clean dark-brown outlines, cel-shaded coloring with two-tone hard shadows, warm muted earthy color palette, minimalist cute faces with dot eyes, simple flat vector background, smooth 2D animation, vertical 9:16. No on-screen text, no subtitles.
```
**ผมใส่เพิ่ม:** แจ้งเตือน "ติ๊ง! ตรวจพบวัตถุระดับทอง" แล้วตามด้วยป้ายสีทอง **รางวัลที่ 1 · ฿6,000,000**
**ตัดใช้:** 8 วินาที

### คลิป 11 · 1:06–1:14 · ตาทองหลังแว่น (ปิดตอน)
**Ingredients:** R1 (บุญ), R2 (แว่น)
```
Extreme close-up of the 28-year-old man's eyes behind round thin gold-rimmed glasses at night, the golden glow of the lottery ticket reflected in both lenses, his dot eyes glowing gold. Slowly the corner of his mouth lifts into a quiet, confident smile. Very slow push-in. Sound: low heartbeat-like bass, silence, no dialogue. All characters are adults. 2D vector game art style animation, chibi proportions, bold clean dark-brown outlines, cel-shaded coloring with two-tone hard shadows, warm muted earthy color palette, minimalist cute faces with dot eyes, simple flat vector background, smooth 2D animation, vertical 9:16. No on-screen text, no subtitles.
```
**(VO) บุญ:** แม่ยายพูดถูกอย่างหนึ่ง… ผมเก็บของจากถังขยะจริง ๆ แต่ผมจะยังไม่บอกใคร
**ผมใส่เพิ่ม:** "ตอนต่อไป — รางวัลที่ 1"
**ตัดใช้:** 8 วินาที

---

## ขั้นที่ 3 · ส่งกลับมาให้ผม

- ตั้งชื่อไฟล์เป็น `C01.mp4` ถึง `C11.mp4` ตามเลขคลิป แล้วส่งในแชตนี้
- ถ้าคลิปไหนสร้างได้หลายแบบ ส่งมาได้ทุกแบบ ผมจะเลือกให้
- ผมจะตัดต่อ ใส่หน้าจอระบบ (ป้ายราคา แจ้งเตือน เสียงติ๊ง) ชื่อเรื่อง ซับไตเติลภาษาไทย และเสียงบรรยาย (VO)
