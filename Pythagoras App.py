import tkinter as tk
import math
def number():
    try:
        a = float(A_input.get())
        b = float(B_input.get())

    except:
        output_label.configure(text='ไม่สามารถคำนวนได้ โปรดใส่ค่าใหม่ด้วยครับ')
        return
    output= ''
    output=math.sqrt(a**2 + b**2)
    output='C = '+str(output)

    output_label.configure(text=output)

window = tk.Tk()
window.title('Pythagoras')
window.minsize(width=500, height=300)

title_Label=tk.Label(master=window,text='Input A')
title_Label.pack()

A_input=tk.Entry(master=window)
A_input.pack(pady=20)

text_Label=tk.Label(master=window,text='Input B')
text_Label.pack()

B_input=tk.Entry(master=window)
B_input.pack()

go_button=tk.Button(master=window,text='OK', command=number)
go_button.pack()

output_label= tk.Label(master=window)
output_label.pack()

window.mainloop()

