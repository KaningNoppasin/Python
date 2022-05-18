a = input("ข้อความ:")
n = 0   #n=จำนวนสระ
z = 0   #z=เป็นอักษรตัวที่
for x in a :
    z += 1
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u" or \
        x == "A" or x == "E" or x == "I" or x == "O" or x == "U":
        n += 1
        print(f"มีสระ\t{x}\tเป็นตัวอักษรที่\t{z}")
else :
    print(f"ข้อความ\t{a}\tมี่สระทั้งหมด\t{n} ตัว")