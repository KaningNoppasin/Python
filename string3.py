fruit = "ไปซื้อผลไม้ มีทุเรียน มังคุด ข้าวเหนียวทุเรียน ที่ตลาด แวะไปสวนทุเรียนด้วย"
print(fruit.count("ทุเรียน")) #นับจำนวนคำ

name = "นายกอไก่ ใจดี"
print(name.startswith("นาย"))   #เช็คคำขึ้นต้น

if name.startswith("นาย"):
    print("ผู้ชาย")
else :
    print("เป็นบุคคลอื่น")

name1 = "11504566"

if name1.endswith("0"): #เช็คคำลงท้าย
    print("ถูกหวย")
else :
    print("ไม่ถูกหวย")