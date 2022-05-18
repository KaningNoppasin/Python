import math
n = int(input("จำนวนด้าน>>\t"))
s = int(input("ความยาวด้านแต่ละด้าน>>\t"))
polygon_area = (n*(s**2)) / (4*(math.tan(math.pi/n)))


print("รูปหลายเหลี่ยมที่มี",n,"ด้าน ความยาวด้านละ",s,"จะมีพื้นที่เท่ากับ {:.3f}".format(polygon_area))

print(f"รูปหลายเหลี่ยมที่มี {n} ด้าน ความยาวด้านละ {s} จะมีพื้นที่เท่ากับ {round(polygon_area,3)}")