score = float(input("Score :"))

if 100 >= score >= 80:
    print("A")
elif 80 > score >= 75 :
    print("B+")
elif 75 > score >= 70 :
    print("B")
elif 70 > score >= 65 :
    print("C+")
elif 65 > score >= 60 :
    print("C")
elif 60 > score >= 55 :
    print("D+")
elif 50 > score >= 50 :
    print("D")
elif 50 > score >= 0:
    print("F")
else :
    print("Error score only 0-100")