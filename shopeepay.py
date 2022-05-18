#ตั้งราคา%ที่ลดได้
#ตั้งค่าสูงสุดของราคาลดได้
# คำนวนว่าซื้อราคาเท่าไรลดคุ้มสุด
# นภสินธุ์ เรนเรือง
import math as m

def leninput (word):
    leninput = input(word)
    while len(leninput)==0 :
        print("\n\tError len = 0\n")
        leninput = input(word)
    return leninput

percen = int(leninput("ส่วนลด(%) :\t"))
maxdisscount = int(leninput("\nลดสูงสุด (บาท):\t"))
if maxdisscount == 0:
    maxdisscount = m.inf
pricenodisscount = int(leninput("\nราคาขณะยังไม่ลด (บาท):\t"))

disscount = pricenodisscount*(percen/100)
maxprice = (100*maxdisscount)/percen
realdisscount = disscount
if disscount > maxdisscount:
    disscount = maxdisscount
price = pricenodisscount-disscount

print(f"\nลดราคา \t=\t{disscount:.2f} บาท")
print(f"\nราคาที่ควรจะได้ลด \t=\t{realdisscount:.2f} บาท")
print(f"\n\n*****************\n\nเหลือราคา \t{price:.2f} บาท\n\n*****************")
print(f"\nราคาที่คุ้มสุด(ได้ใช้ลดสูงสุด) \t=\t{maxprice:.2f} บาท\n")