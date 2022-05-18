'''
temp = input("อุณหภูมิ(CหรือF):")
degree = int(temp[:-1])          #เอาข้อความทุกตัวยกเว้นต้วสุดท้าย
unit = temp[-1].upper()     #เอาข้อความตัวสุดท้ายแล้วแปลงเป็นตังพิมใหญ่
if unit == "C" :
    tempf = int((degree*9/5)+32)
    print(f"อุณหภูมิ(C): {degree} = อุณหภูมิ(F): {tempf}")
elif unit == "F" :
    tempc = int((degree-32)*5/9)
    print(f"อุณหภูมิ(F): {degree} = อุณหภูมิ(C): {tempc}")
'''
#แปลงอุณหภูมิ
temp = input("ป้อนอุณหภูมิ (องศา) :") #45C

degree= int(temp[:-1]) #45
unit=temp[-1].upper() #C


if unit=="C":
    result=(9*degree)/5+32
    unit_result="ฟาเรนไฮน์"
elif unit=="F":
    result=(degree-32)*5/9
    unit_result="เซลเซียส"
print("แปลงตัวเลข = ",temp," เป็น ",unit_result," = ",result)