
#ให้เดือนแรกเป็นช่องว่าง เพื่อใช้แทนเดือนลำดับที่ 0
#ดังนั้นลำดับของเดือนมกราคมก็จะเป็น 1 ตามที่เราเข้าใจ
months = ['', 'มกราคม', 'กุมภาพันธ์', 'มีนาคม', 'เมษายน', 'พฤษภาคม', 'มิถุนายน',
                 'กรกฎาคม', 'สิงหาคม', 'กันยายน', 'ตุลาคม', 'พฤศจิกายน', 'ธันวาคม']

#สร้างลิสต์ว่างแบบ 2 มิติ
days = []
for m in range(13):       #[[เดือน 0], [เดือน 1], [เดือน 2], ...[เดือน 12]]
    days.append([])
    for d in range(32):     #[[วันที่ 0, วันที่ 1, วันที่ 2, ..., วันที่ 31], [วันที่ 0, วันที่ 1, วันที่ 2, ..., วันที่ 31], ...]
        days[m].append('')

days[1][1] = 'วันขึ้นไปใหม่'
days[1][16] = 'วันครู'
days[2][14] = 'วันวาเลนไทน์'
days[4][6] = 'วันจักรี'
days[4][13] = 'วันสงกรานต์'
days[7][28] = 'วันเฉลิมพระชนมพรรษา ร.10'
days[8][12] = 'วันแม่'
days[10][23] = 'วันปิยมหาราช'
days[12][5] = 'วันพ่อ'
days[12][10] = 'วันรัฐธรรมนูญ'
days[12][25] = 'วันคริสต์มาส'
days[12][31] = 'วันสิ้นปี'

print('วันสำคัญในเดือนต่างๆ')

for m in range(len(days)):          # วนลูปตามจำนวนเดือน (0 - 12)
    important_days = ''

    for d in days[m]:                    # วนลูปตามจำนวนวันที่ของแต่ละเดือน
        if d != '':
            if important_days != '':
                important_days += ', '

            important_days += d

    #ถ้าเดือนนั้นมีวันสำคัญ ก็ให้แสดงออกไป
    if important_days != '':
        print(f'เดือน {months[m]} : {important_days}')
