list_1 = []
x = []
y = []
for i in range(1,6):
    list_1.append(int(input(f"number {i} :")))
# x = sorted(list_1)
# y = reversed(x)
list_1.sort()
print(f"min--->max {list_1} ")
list_1.reverse()
print(f"max--->min {list_1}")
# reversed()
# print(f"min--->max {x} max--->min {y}")
# print(f"min--->max {list_1.sort()} max--->min {list_1.reverse().sort()}")