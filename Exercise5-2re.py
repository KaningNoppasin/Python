
max_weight = 450
total_weight = 0
w = 0
person = 1

print('ถ้าไม่มีใครเข้าไปในลิฟต์อีก ให้ใส่น้ำหนักเป็น 0')
while (total_weight < max_weight) or (person <= 6):
    w = float(input(f'น้ำหนักของคนที่: {person} >>'))
    if w == 0:
        break

    if (total_weight + w) > max_weight:
        print('น้ำหนักเกินกำหนด!!!')
        continue

    total_weight += w
    person += 1

if total_weight % 1 == 0:
    print('น้ำหนักรวม:', total_weight // 1)
else:
    print('น้ำหนักรวม:', total_weight)
