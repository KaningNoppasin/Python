
n = int(input('กรุณาใส่ตัวเลขจำนวนเต็ม >> '))
remain = n
digit = 0
result = ''

#จะใช้เทคนิคการนำตัวเลขที่คัดแยกในลูปก่อนๆ นี้
#มาวางต่อท้ายเลขที่คัดแยกได้ในลูปนี้ โดยคั่นด้วยเครื่องหมาย ','
while remain != 0:
    digit = remain % 1000
    if result == '':
        result = str(digit)
    else:
        result = str(digit) + ', ' + result

    remain = remain // 1000

print('ตัวเลขที่แยกได้คือ: ', result)
