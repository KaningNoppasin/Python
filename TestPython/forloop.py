vocabulary = input("ใส่คำศัพท์ : ")
n = 0
m = 0
for text in vocabulary :
    m=m+1
    print(f"{text} เป็นตัวอักษรตัวที่ {m}")
    if text == "a" or text == "A" or text == "e" or text == "E" or text == "i" or text == "I" or text == "o" or text == "O" or text == "u" or text == "U" :
        n = n+1
        print(f"มีสระ {text} เป็นตัวอักษรตัวที่ {m}")
        print("-"*25)
    else:
        print("-"*25)
else :
    print(f"คำว่า {vocabulary} มีสระ {n} ตัว")
    print("-"*25)
print(f"มีตัวอักษรทั้งหมด {m} ตัว")