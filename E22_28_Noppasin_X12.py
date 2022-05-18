
Math = float(input("Math :"))*3
Phy = float(input("Phy :"))*2
Chame = float(input("Chame :"))*2
Thai = float(input("Thai :"))*2
Eng = float(input("Eng :"))*2
LabEMI = float(input("LabEMI :"))*2
Compro = float(input("Compro :"))*2
Mortor = float(input("Mortor :"))*2
Machine = float(input("Machine :"))*2
Circuit = float(input("Circuit :"))*2
        # \ ขึ้นบรรทัดใหม่
if (Math <= 12) and (Phy <= 8) and (Chame <= 8) and (LabEMI <= 8) and \
    (Compro <= 8) and (Mortor <= 8) and (Machine <= 8) and (Circuit <= 8) and (Thai <= 8) and (Eng <= 8):
    print("GPA={:.2f}".format((Math+Phy+Chame+Thai+Eng+LabEMI+Compro+Mortor+Machine+Circuit)/21))
else :
    print("Eror ***Grade <=4***")


'''
if (float(input("Math :"))*3 <= 12) and (float(input("Phy :"))*2 <= 8) and (float(input("Chame :"))*2 <= 8) and (float(input("Thai :"))*2 <= 8) and (float(input("Eng :"))*2 <= 8) and (float(input("LabEMI :"))*2 <= 8) and (float(input("Compro :"))*2 <= 8) and (float(input("Mortor :"))*2 <= 8) and (float(input("Machine :"))*2 <= 8) and (float(input("Circuit :"))*2) :
    print("GPA={:.2f}".format(((float(input("Math :"))*3)+(float(input("Phy :"))*2 <= 8)+(float(input("Chame :"))*2 <= 8)+(float(input("Thai :"))*2 <= 8)+(float(input("Eng :"))*2 <= 8)+(float(input("LabEMI :"))*2 <= 8)+(float(input("Compro :"))*2 <= 8)+(float(input("Mortor :"))*2 <= 8)+(float(input("Machine :"))*2 <= 8) +(float(input("Circuit :"))*2))/21))
else :
    print("Eror ***Grade <=4***")
'''