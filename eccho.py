while True:

    def e():
        HbA1c = float(input("เปอเซนต์ค่าน้ำตาลในเลือดที่คุณตรวจมา :" ))##รับอินพุตของค่าน้ำตาล
        A = int((HbA1c*28.7)-46.7)##กำหนดตัวแปล
        B = int((HbA1c*1.59)-2.59)##กำหนดตัวแปล
        return HbA1c,A,B
    def p():
        if HbA1c != 0:##ถ้าอินพุตไม่เท่ากับศูนย์ให้ทำงานต่อ
                choose = input("ค่าที่คุณต้องการที่จะได้ [1]mg/dL or [2]mmol/L : ")##รับอินพุตของค่าน้ำตาล
                print("-------------------------------")
                if choose !=0:##ถ้าอินพุตไม่ใส่ศูนย์ให้ทำงาน
                    for i in choose:##
                        if i == "1":##
                            print("ค่าน้ำตาลในเลือดของคุณประมาณ",A,"mg/dL")
                            print("-------------------------------")
                        if i == "2":##
                            print("ค่าน้ำตาลในเลือดของคุณประมาณ",B,"mmol/L")
                            print("-------------------------------")
                if A >= 68 and A<=85:##
                    print("คุณมี HbA1c ที่ต่ำกว่าปกติ ")
                    print("-------------------------------")
                elif A >=88 and A<= 114:
                    print("คุณมีค่าเฉลี่ยที่ปกติ")
                    print("-------------------------------")
                elif A >=117 and A<= 137:
                    print("คุณมีความเสี่ยงเป็นโรคเบาหวาน")
                    print("-------------------------------")
                elif A >=140 and A<= 154:
                    print("คุณเป็นเบาหวาน")
                    print("-------------------------------")
                elif A >=157 and A<= 169:
                    print("คุณมีความเสี่ยงที่เป็นเบาหวานขั้นอันตราย")
                    print("-------------------------------")
                else:
                    print("คุณเป็นเบาหวานขั้นอันตราย")
                    print("-------------------------------")

    HbA1c,A,B = e()
    p()

