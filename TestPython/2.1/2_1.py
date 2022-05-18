# import math as m
filepath = "C:/Users/numchann/Desktop/TestPython/2.1/data.txt"
f = open(filepath, "r",encoding='utf-8')        # "w"เขียน "r" อ่าน

n = 0
sum_1 = 0
min_1 = m.inf
max_1 = 0
list_s = []
for i in f:
    s = float(i[10:])
    list_s.append(s)
    # if  max_1 < s:
    #     max_1 = s
    # if s < min_1:
    #     min_1 = s
    sum_1 += s      # sum_1 = sum_1 + s
    n += 1

f.close()
avg = sum_1/n
print(f"""
ค่าเฉลี่ย {avg:.2f}
ค่าสูงสุด {max(list_s)}
ค่าต่ำสุด   {min(list_s)}
""")
# print(f"""
# ค่าเฉลี่ย {avg:.2f}
# ค่าสูงสุด {max_1}
# ค่าต่ำสุด   {min_1}
# """)
