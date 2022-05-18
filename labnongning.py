
a = 7
b = 11
print(f'ก่อนสลับค่า a = {a}, b = {b}')

c = a   #c=7 a=7 b=11
a = b   #c=7 a=11 b=11
b = c   #c=7 a=11 b=7
print(f'หลังสลับค่า a = {a}, b = {b}')
