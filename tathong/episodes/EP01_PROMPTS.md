# ตาทอง ตอนที่ 1 — ชุด prompt สำหรับสร้างภาพเอง

ใช้กับ ChatGPT, Gemini, Midjourney หรือ Leonardo ก็ได้ ทุก prompt เป็นภาษาอังกฤษและสมบูรณ์ในตัว คัดลอกไปวางได้ทั้งก้อน

## วิธีใช้ (สำคัญ: ทำขั้นที่ 1 ก่อน)

1. **สร้างภาพอ้างอิงตัวละครก่อน** (หัวข้อ A) เลือกภาพที่ชอบที่สุดของแต่ละคนเก็บไว้
2. **ทุกช็อตที่มีตัวละคร** ให้แนบภาพอ้างอิงของตัวละครนั้นไปด้วย แล้วพิมพ์นำหน้า prompt ว่า
   `Use the attached image as the character reference. Keep the same face, hair and outfit.`
   - Midjourney: ใช้ `--cref <ลิงก์ภาพ>` ต่อท้าย
   - Leonardo: ใช้ Character Reference
3. **ห้ามให้เครื่องมือใส่ตัวหนังสือในภาพ** ป้ายราคาและหน้าจอระบบผมใส่ตอนตัดต่อ
4. **ตั้งชื่อไฟล์** เป็น `EP01_01.png` ถึง `EP01_13.png` ตามเลขช็อต แล้วส่งกลับมาให้ผมในแชตนี้

**สไตล์** ต่อท้ายอยู่ในทุก prompt แล้ว:
`stylized 2.5D animated film look, high-quality 3D animation render, soft cinematic lighting, expressive faces, vertical 9:16, no text`

---

## A. ภาพอ้างอิงตัวละคร (ทำก่อน)

### A1 · บุญ
```
Character reference sheet, front view, waist-up portrait of Boon: a Thai man aged 28, lean build, warm tan skin, short messy black hair, kind but tired eyes, faded olive-green work shirt with rolled sleeves, a white towel draped around his neck. Plain neutral background. Stylized 2.5D animated film look, high-quality 3D animation render, soft cinematic lighting, expressive face, vertical 9:16, no text.
```

### A2 · บุญ สวมแว่น
```
Same character as reference: Boon, a Thai man aged 28, short messy black hair, faded olive-green work shirt, white towel around his neck, now wearing old round thin gold-rimmed glasses (thin gold metal frame, not black). Front view waist-up, plain neutral background. Stylized 2.5D animated film look, high-quality 3D animation render, soft cinematic lighting, vertical 9:16, no text.
```

### A3 · ฝน
```
Character reference sheet, front view, waist-up portrait of Fon: a Thai woman aged 27, shoulder-length straight black hair with bangs, gentle worried face, simple cream-colored blouse. Plain neutral background. Stylized 2.5D animated film look, high-quality 3D animation render, soft cinematic lighting, vertical 9:16, no text.
```

### A4 · แม่ยาย
```
Character reference sheet, front view, waist-up portrait of the mother-in-law: a Thai woman aged 58, slightly plump, short permed gray-black hair, heavy makeup, sneering arrogant expression, red silk blouse, many thick gold necklaces and gold bracelets, holding a folding fan. Plain neutral background. Stylized 2.5D animated film look, high-quality 3D animation render, soft cinematic lighting, vertical 9:16, no text.
```

### A5 · เคน
```
Character reference sheet, front view, waist-up portrait of Ken: a Thai man aged 35, slicked-back black hair, smug confident smile, tailored navy-blue suit, white shirt, flashy gold wristwatch. Plain neutral background. Stylized 2.5D animated film look, high-quality 3D animation render, soft cinematic lighting, vertical 9:16, no text.
```

---

## B. ช็อตตอนที่ 1

### ช็อต 1 · แม่ยายทิ้งของขวัญ (อ้างอิง: A4)
```
The mother-in-law (Thai woman aged 58, short permed hair, red silk blouse, thick gold necklaces) sneering with contempt as she drops a small cheap gift box into a trash bin, at a family birthday party in a Thai suburban house, birthday decorations and banquet table blurred behind her, relatives laughing in the background. Low angle, dramatic. Stylized 2.5D animated film look, high-quality 3D animation render, soft cinematic lighting, expressive faces, vertical 9:16, no text.
```

### ช็อต 2 · เคนใส่สร้อยทองให้แม่ยาย (อ้างอิง: A5, A4)
```
Ken (Thai man aged 35, slicked-back hair, navy suit, gold watch) smugly fastening a thick gold necklace around the neck of the delighted mother-in-law (Thai woman aged 58, permed hair, red silk blouse) at a birthday banquet table, relatives clapping. Warm festive lighting. Stylized 2.5D animated film look, high-quality 3D animation render, soft cinematic lighting, expressive faces, vertical 9:16, no text.
```

### ช็อต 3 · บุญยืนคนเดียวข้างประตู (อ้างอิง: A1)
```
Boon (Thai man aged 28, messy black hair, faded olive work shirt, white towel around neck, no glasses) standing alone by the doorway of a lively family birthday party, holding his cap with both hands, looking down, ignored by everyone. The party is warm and bright, he is in shadow. Stylized 2.5D animated film look, high-quality 3D animation render, soft cinematic lighting, expressive faces, vertical 9:16, no text.
```

### ช็อต 4 · ฝนแอบจับมือบุญใต้โต๊ะ (อ้างอิง: A3, A1)
```
Close-up under a banquet table covered with a white tablecloth: a young woman's hand in a cream sleeve gently holding a man's rough working hand in a faded olive sleeve, secretly, comforting. Soft warm light. Stylized 2.5D animated film look, high-quality 3D animation render, soft cinematic lighting, vertical 9:16, no text.
```

### ช็อต 5 · รถกระบะหน้าบ้านคนตาย
```
An old rusty pickup truck loaded with scrap metal and junk, parked in front of a dark, old wooden Thai house on stilts at night, moonlight, a single dim light inside, eerie but quiet. Wide shot. Stylized 2.5D animated film look, high-quality 3D animation render, cinematic moonlight, vertical 9:16, no text.
```

### ช็อต 6 · บุญหยิบแว่นจากกล่อง (อ้างอิง: A1)
```
Boon (Thai man aged 28, messy black hair, faded olive work shirt, white towel around neck, NOT wearing glasses) in a dark dusty room of an old wooden house, lit by a flashlight, holding up a pair of old round thin gold-rimmed glasses he just found in a dusty cardboard box, looking at them curiously. Stylized 2.5D animated film look, high-quality 3D animation render, flashlight lighting, expressive face, vertical 9:16, no text.
```

### ช็อต 7 · บุญสวมแว่น (อ้างอิง: A2)
```
Boon (Thai man aged 28, messy black hair, faded olive work shirt, white towel around neck) putting on old round thin gold-rimmed glasses with both hands, a mysterious golden glow shining on the lenses, dark dusty room, magical moment. Close-up. Stylized 2.5D animated film look, high-quality 3D animation render, golden rim light, expressive face, vertical 9:16, no text.
```

### ช็อต 8 · ห้องเต็มของเก่า
```
Interior of a dusty dark room in an old wooden Thai house, full of old belongings: an old radio, wall clocks, a sewing machine, stacks of boxes, piles of junk, flashlight beam with floating dust, slight golden magical haze. Leave some empty space in the upper and middle areas. Stylized 2.5D animated film look, high-quality 3D animation render, cinematic lighting, vertical 9:16, no text.
```

### ช็อต 9 · ชามลายครามในกล่อง
```
An old antique blue-and-white porcelain bowl sitting among junk in a dusty cardboard box, a beam of light falling on it, faint purple magical glow around the bowl, dark background. Close-up. Leave empty space above the bowl. Stylized 2.5D animated film look, high-quality 3D animation render, dramatic lighting, vertical 9:16, no text.
```

### ช็อต 10 · บุญตกใจ (อ้างอิง: A2)
```
Boon (Thai man aged 28, messy black hair, faded olive work shirt, white towel around neck) wearing round thin gold-rimmed glasses, holding the frame with one hand, wide-eyed and shocked, mouth slightly open, dark dusty room with faint golden light on his face. Close-up. Stylized 2.5D animated film look, high-quality 3D animation render, expressive face, vertical 9:16, no text.
```

### ช็อต 11 · แผงลอตเตอรี่ข้างทาง
```
A small roadside Thai lottery ticket stall at night under a single street lamp, a wooden display board with rows of lottery tickets, empty quiet street, a little rain on the road reflecting the light. Wide shot. Stylized 2.5D animated film look, high-quality 3D animation render, cinematic night lighting, vertical 9:16, no readable text or numbers.
```

### ช็อต 12 · ลอตเตอรี่ใบหนึ่งเรืองแสงทอง
```
Close-up of rows of paper lottery tickets on a wooden board at night, ONE single ticket in the center glowing with bright golden magical light and sparkles, the others dark. Leave empty space above the glowing ticket. Stylized 2.5D animated film look, high-quality 3D animation render, cinematic lighting, vertical 9:16, no readable text or numbers.
```

### ช็อต 13 · หน้าบุญกับแสงทองในแว่น (อ้างอิง: A2)
```
Extreme close-up of Boon's face (Thai man aged 28, messy black hair) wearing round thin gold-rimmed glasses, golden light reflected in both lenses, a slight determined smile, night street lights blurred behind him. Stylized 2.5D animated film look, high-quality 3D animation render, cinematic lighting, expressive face, vertical 9:16, no text.
```
