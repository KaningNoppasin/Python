ps = int(input("input:"))

constellations = ['ชวด', 'ฉลู', 'เถาะ', 'ขาล', 'มะโรง', 'มะเส็ง','มะเมีย', 'มะแม', 'วอก', 'ระกา', 'จอ', 'กุน']

k = (ps+5)%12

print(constellations[k])