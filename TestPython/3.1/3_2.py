import math as m
def area_circle(radius):
    area = (m.pi)*(radius**2)
    return area
radius = float(input("ป้อนค่ารัสมี:"))
if radius > 0:
    area = area_circle(radius)
    print(f"พท.วงกลม = {area:.2f}ตร.หน่วย")
elif radius <= 0:
    print("โปรดป้อนค่ามากกว่าศูนย์")