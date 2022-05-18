# ธิติวุฒิ โพธิ์สัมพันธ์สิงห์ เลขที่ 9 E22
# นภสินธุ์ เรนเรื่อง เลขที่ 28 E22

#แปลงอุณหภูมิ

while True:
    def Noppasin_28():
        a = 0
        while (a == 0):
            temp = input("อุณหภูมิ (C,F,K) :")
            degree= int(temp[:-1])           #ลบหน่วยข้างหลังที่เป็นstrออก แล้วแปลงเป็นint
            unit=temp[-1].upper()            #เอาตัวท้ายสุดแล้วปรับเป็นตัวพิมใหญ่
            if unit == "C" or unit == "K" or unit == "F":   #ตรวจสอบหน่วย
                a=1
                break
            else:                              #ถ้าหน่วยผิดต้องกรอกใหม่
                print("หน่วยผิด!!!!!!!!!!")
                continue
        return temp,degree,unit
    def Thitiwut_09():
        if unit=="C":                   #รับอุณหภูมิC
            result=degree
        elif unit=="F":                 #เป็นการคำนวณอุณหภูมิจากFเป็นC
            result=(degree-32)*5/9
        elif unit=="K":                 #เป็นการคำนวณอุณหภูมิจากKเป็นC
            result=degree-273
        unit_result="เซลเซียส"
        return unit_result,result 
    # x= สภาพอากาศ (น้อยกว่า-30อันตรายกับร่างกาย -30-->0หนาวจัด 0-->18 หนาวเย็น 18-->25เย็นสบาย 
    #  25-->30ปกติ 30-->40ร้อน 40-->50ร้อนจัด มากกว่า50เป็นอันตรายกับร่างกาย)
    def weather_1():
        if (result<=-30) or (50<=result):
            weather="อันตรายกับร่างกาย"
        elif -30<result<=0:
            weather="หนาวจัด"
        elif 0<result<=18:
            weather="หนาวเย็น"
        elif 18<result<=25:
            weather="เย็นสบาย"
        elif 25<result<=30:
            weather="ปกติ"
        elif 30<result<=40:
            weather="ร้อน"
        elif 40<result<50:
            weather="ร้อนจัด"
        return weather
    
    temp,degree,unit = Noppasin_28()
    Thitiwut_09()
    unit_result,result = Thitiwut_09()
    weather = weather_1()
    print(f"อุณหภูมิ :{temp.upper()} \tมีค่า :{result:.2f} {unit_result} \tสภาพอากาศ :{weather}")