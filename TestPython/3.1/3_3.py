# word = input("ใส่ประโยคภาษาอังกฤษ :").split()
# # n = 0   #n=จำนวนสระ
# # z = 0   #z=เป็นอักษรตัวที่
# for x in word :
#     # for i in x :
#     #     z += 1
#         # if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or \
#         #     i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
#         #     n += 1
#     n = x.count("a")+x.count("e")+x.count("i")+x.count("o")+x.count("u")\
#         +x.count("A")+x.count("E")+x.count("I")+x.count("O")+x.count("U")
#     z = len(x)
#     print(f"คำว่า {x} \tมี \t{z} อักษร มีสระ\t{n}ตัว ")
# # else :
# #     print(f"ข้อความ\t{a}\tมี่สระทั้งหมด\t{n} ตัว")

word = input("ใส่ประโยคภาษาอังกฤษ :").split()
# [kill,this,love]
# 1 x=kill
# 2 x=this
# 3 x=love
for x in word :
    n = x.count("a")+x.count("e")+x.count("i")+x.count("o")+x.count("u")\
        +x.count("A")+x.count("E")+x.count("I")+x.count("O")+x.count("U")
    z = len(x)
    print(f"คำว่า {x} \tมี \t{z} อักษร มีสระ\t{n}ตัว ")