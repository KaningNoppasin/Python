fname = "kong"
lname = "ruksiam"
age = "80"
salary = 500.98755
fullname = fname+lname+age
print(fullname+"555")
print("ชื่อต้น:"+fname+"\tนามสกุล:"+lname+"\tอายุ:"+age)

text = "ชื่อต้น:{2}\tนามสกุล:{1}\tอายุ:{3} \tอาชีพ:{0} \tเงินเดือน:{4:.2f}"
print(text.format(fname,lname,age,"โปรแกรมเมอร์",salary))