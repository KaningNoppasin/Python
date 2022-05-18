x = input("ค่า:")
a = 0
s = 0
for i in x :
    i = int(i)
    if i > a:
        a = i
    s += i
print(a,"ค่าสูงสุด")
print(s,"ผลรวม")