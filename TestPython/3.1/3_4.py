
hr_1 = 60
t = 13
areat = 17
def show_ms():
    print("Don't panic, tack a deep breath ... good luck!")
def Lawn_cal(area):
    atn = (hr_1/t)*areat    #1เครื่อง 1ชม ได้จำนวนที่ตัดได้
    number = int((area//atn)+1)
    return number
def show_Lawn(number):
    print(f"Lawn mowers = {number}")
show_ms()

show_Lawn(Lawn_cal(float(input("Enter your area: "))))