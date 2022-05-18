#การเข้าถึงตัวอักษร
name = "NongNingnakap1234" #index => 0
print(name[0:3])
print(name[5:9])
print(name[2])
print(name[-2])

#การหาความยาวstr
print(len(name))

#ลบช่องว่างซ้ายขวา่
n = "   abcd   "
print(len(n))
n = n.strip()#ลบช่องว่างซ้ายขวา
# n = n.lstrip()    l=>ลบช่องซ้าย
# n = n.rstrip()    r=>ลบช่องขวา
print(len(n))

print(name.upper()) #เปลี่ยนเป็นตัวพิมพืใหญ่
print(name.lower()) #เปลี่ยนเป็นตัวพิมเล้ก

print(name.capitalize())    #เปลี่ยนเป็นตัวใหญ่**เฉพาะตัวหน้า**

print(name.replace("Nong","P ")) 
#print(name.replace(old, new))  การแทนที่ข้อความ ข้อความที่ต้องการแก้,แก้เป็น...,ลำดับ(ใส่จำนวนข้อความที่ต้องการแก้)
print(name.replace("N","P ",1))