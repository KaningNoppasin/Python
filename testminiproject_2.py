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

def question_A(n,h,heart,word_result,word_number,word_switch):
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
            word_number += 10
            heart += 1
            word_switch = 1 #ตอบถูกแล้ว-->เปิด
            break
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
            heart -= 1
            if heart <= 0 :
                break
            continue
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

def question_B(n,h,heart,word_result,word_number,word_switch):
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
            word_number += 10
            heart += 1
            word_switch = 1 #ตอบถูกแล้ว-->เปิด
            break
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
            heart -= 1
            if heart <= 0 :
                break
            continue
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

def question_C(n,h,heart,word_result,word_number,word_switch):
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
            word_number += 10
            heart += 1
            word_switch = 1 #ตอบถูกแล้ว-->เปิด
            break
        elif answer.upper() == "D":
            word_number_ANS += 8
            print(f"\n{word_result[word_number_ANS]}")
            heart -= 1
            if heart <= 0 :
                break
            continue
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
            word_number += 10
            heart += 1
            word_switch = 1 #ตอบถูกแล้ว-->เปิด
            break
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

def question_4(n,h,heart,word_result,word_number,word_switch):
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
            heart -= 1
            if heart <= 0 :
                break
            continue
        elif answer.upper() == "Z":
            word_number_ANS += 10
            print(f"\n{word_result[word_number_ANS]}")
            word_number += 12
            heart += 1
            word_switch = 1 #ตอบถูกแล้ว-->เปิด
            break
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

def question_A_2_Q6(n,h,heart,word_result,word_number,word_switch,answer):
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
            word_number += 6
            heart += 1
            word_switch = 1 #ตอบถูกแล้ว-->เปิด
            break
        elif answer.upper() == "B":
            word_number_ANS += 4
            print(f"\n{word_result[word_number_ANS]}")
            heart -= 1
            if heart <= 0 :
                break
            #กำหนดค่าเพื่อเริ่มต้นใหม่
            word_number = 0 #ลำดับข้อความต่างๆ ให้เริ่มที่index=0
            word_switch = 1 #1=เปิด 0=ปิด เอาไว้ปิดเปิดข้อความคำถามแต่ละข้อ
            word_number_ANS = 0
            heart = 1
            n = 0
            break
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
    return n,h,heart,word_result,word_number,word_switch,answer

def question_A_2_Q8(n,h,heart,word_result,word_number,word_switch):
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
            word_number += 4
            heart += 1
            word_switch = 1 #ตอบถูกแล้ว-->เปิด
            break
        elif answer.upper() == "B":
            word_number_ANS += 4
            print(f"\n{word_result[word_number_ANS]}")
            heart -= 1
            if heart <= 0 :
                break
            continue
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

def question_A_3(n,h,heart,word_result,word_number,word_switch):
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
            word_number += 8
            heart += 1
            word_switch = 1 #ตอบถูกแล้ว-->เปิด
            break
        elif answer.upper() == "B":
            word_number_ANS += 4
            print(f"\n{word_result[word_number_ANS]}")
            word_number += 8
            word_switch = 1 #ตอบแล้ว-->เปิด เนื่องจากไปอีกข้อ
            print(f"ข้อ :{n} จำนวนคำใบ้ที่ใช้ :{h} พลังชีวิต :{heart} ลำดับindexของคำในเนื้อเรื่อง :{word_number}")
            heart -= 1
            if heart <= 0 :
                break
            n,h,heart,word_result,word_number,word_switch = question_SPC(n,h,heart,word_result,word_number,word_switch)
        elif answer.upper() == "C":
            word_number_ANS += 6
            print(f"\n{word_result[word_number_ANS]}")
            heart -= 1
            if heart <= 0 :
                break
            continue
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

def question_SPC(n,h,heart,word_result,word_number,word_switch):
    n += 1
    word_number += 10
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
            heart -= 99
            if heart <= 0 :
                break
            continue
        elif answer.upper() == "B":
            word_number_ANS += 4
            print(f"\n{word_result[word_number_ANS]}")
            heart -= 99
            if heart <= 0 :
                break
            continue
        elif answer.upper() == "H":
            if h == 0:
                print(f"The Hint -->{hint[8]}")
                h += 1
            elif h != 0:
                print("\n\t*** You use too many hints ***")
            continue
        else:
            print(f"\n\t *** Not have {answer} in ans ***")
            continue
    return n,h,heart,word_result,word_number,word_switch

# name = "kaning"
n = 0   #จำนวนข้อ
h = 0   #จำนวนคำใบ้ที่ใช้
heart = 3   #พลังชีวิต
word_number = 0 #ลำดับข้อความต่างๆ ให้เริ่มที่index=0
word_switch = 1 #1=เปิด 0=ปิด เอาไว้ปิดเปิดข้อความคำถามแต่ละข้อ
word_number_ANS = 0 #indexที่กำหนด ข้อความอสดงผลเวลาที่ผู้เล่น ตอบabcd indexแต่ละอันมีค่าไม่เท่ากัน


word_result = word_result()
hint = hint()

name = input("Please enter a player name: ")

print(f"""
\tHello {name.capitalize()}.
Welcome to the adventure game.
""")

while True:
    # question1
    n,h,heart,word_result,word_number,word_switch = question_B(n,h,heart,word_result,word_number,word_switch)
    print(f"ข้อ :{n} จำนวนคำใบ้ที่ใช้ (ใช้ได้แค่1ครั้งเท่านั้น):{h} พลังชีวิต :{heart}")
    if heart <= 0 :
        print("ํYou Loss")
        break
    # question2
    n,h,heart,word_result,word_number,word_switch = question_C(n,h,heart,word_result,word_number,word_switch)
    print(f"ข้อ :{n} จำนวนคำใบ้ที่ใช้ (ใช้ได้แค่1ครั้งเท่านั้น):{h} พลังชีวิต :{heart}")
    if heart <= 0 :
        print("ํYou Loss")
        break
    # question3
    n,h,heart,word_result,word_number,word_switch = question_D(n,h,heart,word_result,word_number,word_switch)
    print(f"ข้อ :{n} จำนวนคำใบ้ที่ใช้ (ใช้ได้แค่1ครั้งเท่านั้น):{h} พลังชีวิต :{heart}")
    if heart <= 0 :
        print("ํYou Loss")
        break
    # question4
    n,h,heart,word_result,word_number,word_switch = question_4(n,h,heart,word_result,word_number,word_switch)
    print(f"ข้อ :{n} จำนวนคำใบ้ที่ใช้ (ใช้ได้แค่1ครั้งเท่านั้น):{h} พลังชีวิต :{heart}")
    if heart <= 0 :
        print("ํYou Loss")
        break
    # question5
    n,h,heart,word_result,word_number,word_switch = question_B(n,h,heart,word_result,word_number,word_switch)
    print(f"ข้อ :{n} จำนวนคำใบ้ที่ใช้ (ใช้ได้แค่1ครั้งเท่านั้น):{h} พลังชีวิต :{heart}")
    if heart <= 0 :
        print("ํYou Loss")
        break
    answer = 0 #ข้อ6
    # question6
    n,h,heart,word_result,word_number,word_switch,answer = question_A_2_Q6(n, h, heart, word_result, word_number, word_switch,answer)
    if heart <= 0 :
        print("ํYou Loss")
        break
    if answer.upper() == "B":
        continue
    print(f"ข้อ :{n} จำนวนคำใบ้ที่ใช้ (ใช้ได้แค่1ครั้งเท่านั้น):{h} พลังชีวิต :{heart}")
    # question7
    n,h,heart,word_result,word_number,word_switch = question_A_3(n,h,heart,word_result,word_number,word_switch)
    print(f"ข้อ :{n} จำนวนคำใบ้ที่ใช้ (ใช้ได้แค่1ครั้งเท่านั้น):{h} พลังชีวิต :{heart}")
    if heart <= 0 :
        print("ํYou Loss")
        break
    # question8
    n,h,heart,word_result,word_number,word_switch = question_A_2_Q8(n, h, heart, word_result, word_number, word_switch)
    print(f"ข้อ :{n} จำนวนคำใบ้ที่ใช้ (ใช้ได้แค่1ครั้งเท่านั้น):{h} พลังชีวิต :{heart}")
    if heart > 0 :
        print("ํ**ยินดีด้วยคุณชนะ**")
    elif heart <= 0 :
        print("ํYou Loss")
    break
print(f"เกมผจญภัยจบแล้ว ขอบคุณ {name.capitalize} ที่มาเล่นเกมของเรา.จากผู้พัฒนา")