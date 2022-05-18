#เที่ยบค่ามากกว่าน้อยกว่า
x = int(input("ป้อมเลขที่1:"))
y = int(input("ป้อมเลขที่2:"))

if x > y :
    print(f"{x}มากกว่า{y} อยู่ {x-y}")
elif x < y :
    print(f"{y}มากกว่า{x} อยู่ {y-x}")
else :
    print("xกับyมี่ค่าเท่ากัน")
print("จบโปรแกรม")
