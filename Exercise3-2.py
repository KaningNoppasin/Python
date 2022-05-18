amount = int(input("จำนวนทุนแรกเริ่ม>>"))
period = int(input("จำนวนปีที่ลงทุน>>"))
rate = float(input("อัตราดอกเบี้ยต่อปี(%)>>"))/100       #%ต้องหาร100
fv = amount*(1+(rate))**period
print("มูลค่าในอนาคตของเงินลงทุนคือ :",format(fv,",.2f"))