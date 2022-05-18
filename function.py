# def my_function():
#     print("Hello from a function")
# print("Line1")
# print("Line2")
# my_function()
# print("Line3")
# print("Line4")

# def my_function(lastname):
#     print(lastname+"KMUTNB")
# my_function("Nana")
# my_function("Dedu")
# my_function("Lulu")

# def summation(a,b):
#     c = a+b
#     print("a = ",a)
#     print("b = ",b)
#     print("a+b = ",c)
# x = 10
# y = 5
# summation(y, x)

# summation(5,10)

# def summation(a,b=6):
#     c = a+b
#     print("a = ",a)
#     print("b = ",b)
#     print("a+b = ",c)
# x = 10
# y = 5
# summation(x,y)

# def summation(a,b):
#     c = a+b
#     print("a = ",a)
#     print("b = ",b)
#     print("a+b = ",c)
# summation(b = 5,a = 10)

def printinfo(*vartuple):
    for var in vartuple:
        # print(type(vartuple))
        print("output of virtuple arg is :",var)
printinfo(10)
print("----------------------------------")
printinfo(70,60,50)

# def summation(a,b):
#     c = a+b
#     return c
# x = summation(5, 10)
# print("a+b = ",x)