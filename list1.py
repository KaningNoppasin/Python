info = [['Som',53],['Oak',71],['May',80]]
z = 0
b = 99999999
for n in info :
    print(n[0],n[1])
    if z < n[1]:
        z = n[1]
    if b > n[1]:
        b = n[1]
else:
    print(f"""
dont!
Min = {b}
Max = {z}
    """)
    