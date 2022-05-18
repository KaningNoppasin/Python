sum_m = 0
def m(d):
    sum_m = 0
    sum_w = 0
    for i in range(1,d+1):
        d_in1 = int(input(f"day{i} ->in1:\t"))
        # d_in2 = int(input(f"day{i} ->in2:\t"))
        # d_in3 = int(input(f"day{i} ->in3:\t"))
        print("---------------------------------------")
        d_out1 = int(input(f"day{i} ->out1:\t"))
        # d_out2 = int(input(f"day{i} ->out2:\t"))
        # d_out3 = int(input(f"day{i} ->out3:\t"))
        print("---------------------------------------")
        sum_din123 = d_in1#+d_in2+d_in3
        sum_dout123 = d_out1#+d_out2+d_out3
        sum_m += sum_din123-sum_dout123
        sum_w += sum_din123-sum_dout123
        print(f"""
Day {i}
sumin = {sum_din123}
sumout = {sum_dout123}
sum_d = {sum_din123-sum_dout123}
sum_m = {sum_m}
        """)
        print("---------------------------------------")
        if i%7 == 0:
            print(f"\nWeek {int(i/7)} \nsumweek {int(i/7)} = {sum_w} \n")
            print("---------------------------------------")
            sum_w = 0
    return sum_m
# jan
sum_m1 = m(31)
print(f"sum jan={sum_m1}")
