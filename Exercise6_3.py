list_n = []
for i in range(1,7):
    list_n.append(int(input(f"st {i}:")))
x = 0
n = 0
for x in list_n:
    n += 1
    if x >= max(list_n)-10:
        g = "A"
    elif x >= max(list_n)-20:
        g = "B"
    elif x >= max(list_n)-30:
        g = "C"
    elif x >= max(list_n)-40:
        g = "D"
    else :
        g = "F"
    print(f"st{n} grade {g}")