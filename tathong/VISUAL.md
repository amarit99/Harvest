# ตาทอง — คู่มือภาพ AI และหน้าจอระบบ

คัดลอก **คำบรรยายตัวละคร** กับ **สไตล์** ไปต่อท้าย prompt ของทุกช็อต (prompt เป็นภาษาอังกฤษ)
**ห้ามใส่ตัวหนังสือหรือป้ายราคาใน prompt** หน้าจอระบบทั้งหมดใส่ตอนตัดต่อ

## สไตล์ (ใส่ท้ายทุก prompt)

```
stylized 2.5D, 3D animated movie render, soft volumetric lighting, warm saturated colors,
expressive faces, cinematic depth of field
```

## ตัวละคร

### บุญ
```
Thai man aged 28, lean, tan skin, short messy black hair, faded olive work shirt with
rolled sleeves, white towel around his neck, kind tired eyes
```
เมื่อใช้ระบบ เพิ่ม `wearing old round gold-rimmed glasses`
**จุดจำ:** ผ้าขนหนูขาวคล้องคอ เสื้อเขียวขี้ม้าซีด แว่นกลมกรอบทอง

### ฝน
```
Thai woman aged 27, shoulder-length black hair with bangs, simple cream blouse,
gentle worried face
```

### แม่ยาย
```
Thai woman aged 58, short permed hair, red silk blouse, many thick gold necklaces and
bracelets, holding a folding fan, sneering expression
```
**จุดจำ:** สร้อยทองหลายเส้น พัด เสื้อไหมแดง

### เคน
```
Thai man aged 35, slicked-back hair, navy suit, flashy gold watch, smug smile
```

### แพรว
```
Thai woman aged 32, long wavy hair, glamorous dress, designer handbag
```

## สถานที่

| สถานที่ | prompt |
|---|---|
| บ้านแม่ยาย | `a Thai suburban family house dining room with a birthday banquet table` |
| บ้านคนตาย | `an old dim wooden Thai house at night full of dusty old belongings` |
| รถรับซื้อของเก่า | `an old pickup truck loaded with scrap metal and junk` |
| แผงลอตเตอรี่ | `a small roadside Thai lottery ticket stall under a street lamp at night` |

## หน้าจอระบบ (ใส่ตอนตัดต่อ)

| สี | ความหายาก | โค้ดสี |
|---|---|---|
| เทา | ของทั่วไป | `#9AA0A6` |
| เขียว | ดี | `#3FBF6F` |
| ฟ้า | หายาก | `#3EA6FF` |
| ม่วง | หายากมาก | `#B06BFF` |
| ทอง | ล้ำค่า | `#FFC83D` |

- **ป้ายราคา:** กล่องโปร่งแสงสีเข้ม มุมโค้ง ขอบเรืองแสงตามสีความหายาก ตัวเลขใหญ่
- **ข้อความแจ้งเตือน:** แถบกลางจอ ขึ้นต้นด้วย "ติ๊ง!" พร้อมเสียงติ๊ง
- **คำโกหก (ขั้น 3 ขึ้นไป):** ข้อความสีแดง "โกหก" ลอยเหนือหัวคนพูด
