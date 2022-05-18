def protectedInput(text):
    inputString = input(text)
    while len(inputString) == 0:
        print("Try again")
        inputString = input(text)
    else:
        return inputString

for i in range(10):
    x = protectedInput("\ninputtest:\t")
    print(x)