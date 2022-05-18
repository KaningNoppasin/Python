import tkinter as tk


def show_multiply():
    number = int(number_input.get())

    if number == 0:
        output_label.configure(text='ผิดที่ไว้ใจ')
        return

    output = ''
    for i in range(1, 13):
        output += str(number) + ' x ' + str(i)
        output += ' = ' + str(number * i) + '\n'

    output_label.configure(text=output)


window = tk.Tk()
window.title('JustPython')
window.minsize(width=400, height=400)

title_label = tk.Label(master=window, text='สูตรคูณแม่')
title_label.pack(pady=(20, 5))

number_input = tk.Entry(master=window)
number_input.pack(pady=(5, 5))

output_button = tk.Button(
    master=window, text='ได้แก่', command=show_multiply,
    width=20, height=2
)
output_button.pack(pady=(5, 5))

output_label = tk.Label(master=window)
output_label.pack(pady=(10, 10))

window.mainloop()