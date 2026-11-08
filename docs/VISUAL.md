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

## สถานที่

| สถานที่ | prompt |
|---|---|
| นาของป้าแวว | `vast fallow rice paddies, a lone wooden Thai stilt house, a small rice granary beside it` |
| หอไซโลโรงสีร้าง | `a tall rusted rice mill silo towering on the horizon` |
| วัดบนเนิน | `a small weathered Thai temple on a hill with a bell tower` |
