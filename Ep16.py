#ifซ้อนif
age = int(input("ป้อนอายุของคุณ:"))

if age <= 15 :
    if age == 15 :
        print("ม.3")
    elif age == 14:
        print("ม.2")
    elif age == 13:
        print("ม.1")
    elif 7 >= age >= 12 :
        print("ประถม")
    else :
        print("อนุบาล")
else :
    print("ม.ปลาย")