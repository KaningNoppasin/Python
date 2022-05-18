a = 0
while (a == 0):
    temp = input("อุณหภูมิ (C,F,K) :")
    degree= int(temp[:-1])           #ลบหน่วยข้างหลังที่เป็นstrออก แล้วแปลงเป็นint
    unit=temp[-1].upper()            #เอาตัวท้ายสุดแล้วปรับเป็นตัวพิมใหญ่
    if unit == "C" or unit == "K" or unit == "F":
        a=1
        break
    else:
        print("หน่วยผิด!!!!!!!!!!")
        continue
print("ทำงานได้")
