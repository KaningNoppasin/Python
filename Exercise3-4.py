import random
t = random.randint(100_000, 1_000_000)
#t = 74_913  #20 48 33
h = t//3600
m = (t%3600)//60
s = (t%3600)%60
print(f"เวลา{t}วินาที เท่ากับ {h}ชั่วโมง {m}นาที {s}วินาที")