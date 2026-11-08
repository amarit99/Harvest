# Harvest — คู่มือภาพ AI

ใช้ไฟล์นี้ทุกตอนเพื่อให้ภาพออกมาหน้าตาเดียวกัน
คัดลอก **คำบรรยายตัวละคร** + **สไตล์** ไปต่อท้าย prompt ของทุกช็อต
(prompt ใช้ภาษาอังกฤษ เพราะเครื่องมือสร้างภาพส่วนใหญ่เข้าใจภาษาอังกฤษได้แม่นกว่า)

> เคล็ดลับ: สร้างภาพหน้าตรงของตัวละครแต่ละตัวให้ได้ภาพที่ชอบก่อน 1 ภาพ
> แล้วใช้ภาพนั้นเป็น reference image / character reference ในทุกช็อตต่อจากนั้น

## สไตล์ (ใส่ท้ายทุก prompt)

```
cinematic film still, vertical 9:16, photorealistic, muted desaturated earthy palette,
soft 35mm film grain, natural moody lighting, rural Thailand after the apocalypse,
shallow depth of field
```

## ป้าแวว

```
Thai woman aged 55, sun-weathered tan skin, deep smile lines, short graying hair tied back
with a faded cloth, thin scar through her left eyebrow, faded indigo farmer's shirt,
dark loose trousers, black rubber boots, red-and-white checkered pha khao ma cloth around
her neck, holding a curved rice sickle
```
**จุดจำ:** แผลเป็นที่คิ้วซ้าย ผ้าขาวม้าลายแดงขาว เคียว

## ภูมิ

```
Thai teenage boy aged 17, very thin, messy black hair with grown-out shaved sides,
dirty faded black hoodie with cut-off sleeves, khaki cargo shorts, worn sneakers wrapped
in silver duct tape, bandage on his right hand, canvas backpack, carrying a large steel
adjustable wrench
```
**จุดจำ:** ประแจเหล็กอันใหญ่ รองเท้าพันเทปกาวสีเงิน ผ้าพันมือขวา

## ผีรวง

```
gaunt walking corpse of a Thai villager, grey-green cracked skin, black fungal veins
spreading across the body, clusters of tiny black mold growing from the eyes and mouth,
faint black spores drifting in the air, tattered farmer clothes, unsettling but not gory
```
**จุดจำ:** ราดำงอกจากตาและปาก ฝุ่นสปอร์สีดำลอยรอบตัว

## กล้า (ลูกชายป้าแวว) — ใช้ในรูปถ่ายและภาพย้อนอดีต

```
Thai man aged 25, short black hair, warm broad smile, slightly sunburned face, faded blue
work shirt, red-and-white checkered pha khao ma cloth around his neck
```
**จุดจำ:** ผ้าขาวม้าลายแดงขาวผืนเดียวกับของป้าแวว
**ฉากย้อนอดีตในค่าย (ตอน 9):** เพิ่ม `gaunt and sick, coughing black dust`

## จ่าเดช (หัวหน้าค่ายหลักสี่)

```
large Thai man aged 45, shaved head, a burn scar across the left side of his face and neck,
faded olive military jacket with the sleeves rolled up, cloth armband on his left arm
reading "หลักสี่", rifle slung over his shoulder, cold calm eyes
```
**จุดจำ:** แผลไฟไหม้ที่หน้าซีกซ้าย เสื้อทหารสีเขียวซีด

## คนของค่ายหลักสี่

```
gaunt armed Thai survivors in mismatched worn clothes, each wearing a white cloth armband
hand-painted with the Thai text "หลักสี่" in red
```
**จุดจำ:** ปลอกแขนผ้าขาว เขียนคำว่า "หลักสี่" สีแดง (ใช้ตั้งแต่ศพในแม่น้ำตอน 3)

## พร็อพสำคัญ

| พร็อพ | ใช้ในตอน | prompt |
|---|---|---|
| วิทยุสื่อสาร | 1, 2, 6, 7 | `small black walkie-talkie with a blinking red light` |
| เคียวของกล้า | 6, 11, 12 | `old rice sickle with the Thai name "กล้า" carved into its wooden handle` |
| บัตรประชาชนกล้า | 8, 9, 12 | `Thai national ID card with the photo of a smiling young man` (ห้ามใส่เลขบัตรที่อ่านได้) |
| ถังน้ำมัน | 8, 10, 12 | `red plastic jerrycan of diesel` |
| กระสอบเมล็ดพันธุ์ | 10, 12 | `burlap sack of seed rice tied with rope` |

## สีของข้าวในแต่ละช่วง

| ตอน | ข้าว |
|---|---|
| 1–2 | ตอซังข้าวตายสีดำ / เมล็ดพันธุ์ |
| 3–5 | ต้นกล้าเขียวสด |
| 6 | ต้นข้าวเขียวเข้ม สูง |
| 7–9 | รวงเหลืองอมเขียว |
| 10–11 | รวงสีทองเต็มทุ่ง |
| 12 | ทุ่งไหม้ดำ |

## สถานที่

| สถานที่ | prompt |
|---|---|
| นาของป้าแวว | `vast fallow rice paddies, a lone wooden Thai stilt house, a small rice granary beside it` |
| หอไซโลโรงสีร้าง | `a tall rusted rice mill silo towering on the horizon` |
| เมืองร้าง | `an abandoned small Thai town street, shuttered shophouses, overgrown weeds` |
| ค่ายหลักสี่ (ปั๊มร้าง) | `an abandoned gas station turned into a survivor camp, pickup trucks, burning oil drums` |
| วัดบนเนิน | `a small weathered Thai temple on a hill with a bell tower` |
