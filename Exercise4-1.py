year = int(input("ปีพศ.ที่ต้องการตรวจสอบ:"))
leapyear = (year-543)
if (leapyear%400 == 0) or (leapyear%100 !=0) and (leapyear%4==0):
    print(f"ปี{year}เป็นleapyear")
else :
    print(f"ปี{year}ไม่เป็นเป็นleapyear")