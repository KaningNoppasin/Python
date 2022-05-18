# def dis(price,rate):
#     discount = price*(rate/100)
#     total = price-discount
#     print("Discount = ",discount)
#     print("Total = ",total)
# price = float(input("ป้อนค่า price"))
# if price <= 0 :
#     print("price ต้องมีค่ามากกว่าศูนย์")
# elif 0<price<1000 :
#     rate = 5
#     dis(price,rate)
# elif price>=1000 :
#     rate = 8
#     dis(price,rate)

def dis(price,rate):
    discount = price*(rate/100)
    total = price-discount
    print("Discount = ",discount)
    print("Total = ",total)
price = float(input("ป้อนค่า price"))
if price <= 0 :
    print("price ต้องมีค่ามากกว่าศูนย์")
elif 0<price<1000 :
    dis(price,5)
elif price>=1000 :
    dis(price,8)