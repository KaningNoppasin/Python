# ธิติวุฒิ โพธิ์สัมพันธ์สิงห์ เลขที่ 9 E22
# นภสินธุ์ เรนเรื่อง เลขที่ 28 E22

def hint():
    try:
        f = open("hint.txt", "r",encoding='utf-8' )
        data = f.readlines()
        f.close()
        return data
    except :
        print("/t***Error Don't have File-->hint.txt***")

def word_result():
    try:
        f = open("word_result.txt", "r",encoding='utf-8' )
        data = f.readlines()
        f.close()
        return data
    except :
        print("/t***Error Don't have File-->word_result.txt***")

# loopซ้อนกันเนื่องจาก
# loopแรกจะเป็นตัวดำเนินเกมและจบเกมโดยเช็คค่าหัวใจว่าผู้เล่นแพ้รึยังถ้าผู้เล่นแพ้จะทำการจัดจบทันที 
# loopที่สองคือloopแต่ละข้อผู้เล่นต้องตอบคำถามให้ถูกจนกว่าจะถูกจึงสามารถเล่นด่านจ่อไปได้

def question_D(n,h,heart,word_result,word_number,word_switch):
    n += 1
    while True:
        if word_switch == 1:
            print(word_result[word_number])
            word_number += 2
            print(word_result[word_number])
            word_number += 1
            print(word_result[word_number])
            word_number += 1
            print(word_result[word_number])
            print("If you want a hint, press h.")
            word_switch = 0 #ใช้งานเสร็จแล้ว--->ปิด
        answer = input(f"Your ANS Question {n}: ")
        word_number_ANS = word_number
        if answer.upper() == "A":
            word_number_ANS += 2
            print(f"\n{word_result[word_number_ANS]}")
            heart -= 1
            if heart <= 0 :
                break
            continue
        elif answer.upper() == "B":
            word_number_ANS += 4
            print(f"\n{word_result[word_number_ANS]}")
            heart -= 1
            if heart <= 0 :
                break
            continue
        elif answer.upper() == "C":
            word_number_ANS += 6
            print(f"\n{word_result[word_number_ANS]}")
            heart -= 1
            if heart <= 0 :
                break
            continue
        elif answer.upper() == "D":
            word_number_ANS += 8
            print(f"\n{word_result[word_number_ANS]}")
            word_number += 9
            heart += 1
            # if heart <= 0 :
            #     break
            
            word_switch = 1 #ตอบถูกแล้ว-->เปิด
            break
        # if answer.upper() == "A":
        #     word_number += 2
        #     print(f"\n{word_result[word_number]}")
        #     print(word_number)
        #     word_number += 8
        #     heart -= 1
        #     if heart <= 0 :
        #         break
        #     continue
        # elif answer.upper() == "B":
        #     word_number += 4
        #     print(f"\n{word_result[word_number]}")
        #     print(word_number)
        #     word_number += 6
        #     heart -= 1
        #     if heart <= 0 :
        #         break
        #     continue
        # elif answer.upper() == "C":
        #     word_number += 6
        #     print(f"\n{word_result[word_number]}")
        #     print(word_number)
        #     word_number += 4
        #     heart -= 1
        #     if heart <= 0 :
        #         break
        #     continue
        # elif answer.upper() == "D":
        #     word_number += 8
        #     print(f"\n{word_result[word_number]}")
        #     print(word_number)
        #     word_number += 2
        #     heart += 1
        #     # if heart <= 0 :
        #     #     break
            
        #     word_switch = 1 #ตอบถูกแล้ว-->เปิด
        #     break
        elif answer.upper() == "H":
            if h == 0:
                print(f"The Hint -->{hint[n-1]}")
                h += 1
            elif h != 0:
                print("\n\t*** You use too many hints ***")
            continue
        else:
            print(f"\n\t *** Not have {answer} in ans ***")
            continue
    return n,h,heart,word_result,word_number,word_switch

name = "kaning"
n = 0   #จำนวนข้อ
h = 0   #จำนวนคำใบ้ที่ใช้
heart = 3   #พลังชีวิต
word_number = 0 #ลำดับข้อความต่างๆ ให้เริ่มที่index=0
word_result = word_result()
word_switch = 1 #1=เปิด 0=ปิด เอาไว้ปิดเปิดข้อความคำถามแต่ละข้อ
word_number_ANS = 0 #indexที่กำหนด ข้อความอสดงผลเวลาที่ผู้เล่น ตอบabcd indexแต่ละอันมีค่าไม่เท่ากัน
hint = hint()

# name = input("Please enter a player name: ")

print(f"""
\tHello {name.capitalize()}.
Welcome to the adventure game.
""")

while True:
    # First question
    # D คือคำตอบที่ถูก
    #สร้างเงื่อนไขข้อด้วยเพื่อให้มันไม่loopต่อ
    n,h,heart,word_result,word_number,word_switch = question_D(n,h,heart,word_result,word_number,word_switch)
    print(f"ข้อ :{n} จำนวนคำใบ้ที่ใช้ :{h} พลังชีวิต :{heart} ลำดับindexของคำในเนื้อเรื่อง :{word_number}")
    n,h,heart,word_result,word_number,word_switch = question_D(n,h,heart,word_result,word_number,word_switch)
    print(f"ข้อ :{n} จำนวนคำใบ้ที่ใช้ :{h} พลังชีวิต :{heart} ลำดับindexของคำในเนื้อเรื่อง :{word_number}")
    if heart > 0 :
        print("ํYou Win")
    elif heart <= 0 :
        print("ํYou Loss")
    print("end program")
    break
