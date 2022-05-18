w = int(input("น้ำหนัก(kg)     :"))
h = int(input("ส่วนสูง(cm)    :"))/100 #/100 ต้องคิดเป็น m
BMI = w/h**2

if BMI < 18.5 :
    print(f"ค่าBMI={BMI} ต่ำกว่าเกณฑ์")
elif 18.5 <= BMI <= 22.9 :
    print(f"ค่าBMI={BMI} สมส่วน")
elif 22.9 < BMI <= 24.9 :
    print(f"ค่าBMI={BMI} น้ำหนักเกิน")
elif 24.9 < BMI <= 29.9 :
    print(f"ค่าBMI={BMI} โรคอ้วนระดับ1")
else :
    print(f"ค่าBMI={BMI} โรคอ้วนระดับอันนตราย")