def dis(price,rate):
    discount = price*(rate/100)
    total = price-discount
    return total,discount

price = float(input("ป้อนค่า price"))

if price <= 0 :
    print("price ต้องมีค่ามากกว่าศูนย์")
elif 0<price<1000 :
    x,y = dis(price,5)
    print("Discount = ",y)
    print("Total = ",x)
elif price>=1000 :
    x,y = dis(price,8)
    print("Discount = ",y)
    print("Total = ",x)