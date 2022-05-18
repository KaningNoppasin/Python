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

name = input("Please enter a player name: ")
# name = "kaning"
n = 1   #จำนวนข้อ
h = 0   #จำนวนคำใบ้ที่ใช้
heart = 3   #พลังชีวิต

hint = hint()

# input str list txt if loop 

print(f"""
\tHello {name.capitalize()}.
Welcome to the adventure game.
""")

#loopซ้อนกันเนื่องจาก
# loopแรกจะเป็นตัวดำเนินเกมและจบเกมโดยเช็คค่าหัวใจว่าผู้เล่นแพ้รึยังถ้าผู้เล่นแพ้จะทำการจัดจบทันที 
# loopที่สองคือloopแต่ละข้อผู้เล่นต้องตอบคำถามให้ถูกจนกว่าจะถูกจึงสามารถเล่นด่านจ่อไปได้

while True:
    # First question
    # D คือคำตอบที่ถูก
    while True:
        print("""
First question:............ 
ANS a)..... b)..... c)..... d)..... 
If you want a hint, press h.
        """)
        question_1 = input("Your ANS: ")
        if question_1.upper() == "A":
            print("your ans is A")
            heart -= 1
            if heart <= 0 :
                break
            continue
        elif question_1.upper() == "B":
            print("your ans is B")
            heart -= 1
            if heart <= 0 :
                break
            continue
        elif question_1.upper() == "C":
            print("your ans is C")
            heart -= 1
            if heart <= 0 :
                break
            continue
        elif question_1.upper() == "D":
            print("your ans is D")
            heart += 1
            # if heart <= 0 :
            #     break
            n += 1
            break
        elif question_1.upper() == "H":
            if h == 0:
                print("your ans is H")
                print(f"The Hint -->{hint[n-1]}")
                h += 1
            elif h != 0:
                print("\n\t*** You use too many hints ***")
            continue
        else:
            print(f"\n\t *** Not have {question_1} in ans ***")
            continue

    if heart <= 0 :
        print("ํYou loss")
        break
    elif heart >= 0 :
        print("ํYou Win")
        break

#     # Second question
#     while True:
#         print("""
# Second question:............ 
# ANS a)..... b)..... c)..... d)..... 
# If you want a hint, press h.
#         """)
#         question_2 = input("Your ANS: ")
#         if question_2.upper() == "A":
#             print("your ans is A")
#             n += 1
#             break
#         elif question_2.upper() == "B":
#             print("your ans is B")
#             n += 1
#             break
#         elif question_2.upper() == "C":
#             print("your ans is C")
#             n += 1
#             break
#         elif question_2.upper() == "D":
#             print("your ans is D")
#             n += 1
#             break
#         elif question_2.upper() == "H":
#             if h == 0:
#                 print("your ans is H")
#                 print(f"The Hint -->{hint[n-1]}")
#                 h += 1
#             elif h != 0:
#                 print("\n\t*** You use too many hints ***")
#             continue
#         else:
#             print(f"\n\t *** Not have {question_2} in ans ***")
#             continue
#     # Third question
#     while True:
#         print("""
# Third question:............ 
# ANS a)..... b)..... c)..... d)..... 
# If you want a hint, press h.
#         """)
#         question_3 = input("Your ANS: ")
#         if question_3.upper() == "A":
#             print("your ans is A")
#             n += 1
#             break
#         elif question_3.upper() == "B":
#             print("your ans is B")
#             n += 1
#             break
#         elif question_3.upper() == "C":
#             print("your ans is C")
#             n += 1
#             break
#         elif question_3.upper() == "D":
#             print("your ans is D")
#             n += 1
#             break
#         elif question_3.upper() == "H":
#             if h == 0:
#                 print("your ans is H")
#                 print(f"The Hint -->{hint[n-1]}")
#                 h += 1
#             elif h != 0:
#                 print("\n\t*** You use too many hints ***")
#             continue
#         else:
#             print(f"\n\t *** Not have {question_3} in ans ***")
#             continue
#     print("end program")
