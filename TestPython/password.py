password = "pornhub"
change = 5
while change>0:
    user_input = input("ใส่รหัส : ")
    if(user_input == password):
        print("ผ่าน")
        break
    else:
        change -= 1
        print("ไม่ผ่าน")

print("จบ")