score = float(input("ข้อมูลเลขจำนวนจริง:"))
x = 0
n = 0

for n in range(0,6):
    n += 1
    x += int(input(f"น้ำหนักของคนที่{n} (กิโลกรัม): >>>"))
    b = n
    if x >= 450:
        for a in range(6-n):
            n += 1
            print(f"น้ำหนักของคนที่ {n} (กิโลกรัม): >>> 0")
        print(f"จำนวนวนคน {b} คน น้ำหนักรวม {x} กิโลกรัม")
        break
else :
    print(f"จำนวนวนคน {n} คน น้ำหนักรวม {x} กิโลกรัม")