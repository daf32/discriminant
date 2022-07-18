from tkinter import *
from tkinter import messagebox
import math
window = Tk()
window.geometry('250x300')
window.title('Решатель уравнений')
window.resizable(False,False)
def click(event):
    messagebox.showinfo('Что хранится в event?', event)
window.bind('<Double-Button-1>', click)
def equate(event):
    try:    
        a = int(entry_a.get())
        b = int(entry_b.get())
        c = int(entry_c.get())
        answer = messagebox.askyesno('Проверка',f'Вы уверены, что хотите решить это уравнение со значениями {a},{b},{c}')
        d = b**2 - 4 * a * c
        if d > 0:
            output.delete(0.0, END)
            output.insert(END,f'Дискриминант равен {d}\n')
            x1=((-b)-math.sqrt(d))/(2*a)
            x2=((-b)+math.sqrt(d))/(2*a)
            output.insert(END,f'x1 = {x1}\n')
            output.insert(END,f'x2 = {x2}\n')

        if d < 0:
            output.delete(0.0, END)
            output.insert(END,f'Дискриминант равен {d}\n')
            output.insert(END,'уравнение не имеет решений\n')
    except ValueError:
        messagebox.showwarning('Внимание','Введите a,b и c!')
label_frame1 = LabelFrame(text = 'введите исходные данные')
label_frame1.grid(padx=10,pady=10)
entry_a = Entry(label_frame1,width=3)
entry_a.grid(padx=5,pady=5,row=0,column=1)
label1 = Label(label_frame1,text='x**2')
label1.grid(padx=5,pady=5,row=0,column=2)
entry_b = Entry(label_frame1,width=3)
entry_b.grid(padx=5,pady=5,row=0,column=3)
label2 = Label(label_frame1,text='x')
label2.grid(padx=5,pady=5,row=0,column=4)
entry_c = Entry(label_frame1,width=3)
entry_c.grid(padx=5,pady=5,row=0,column=5)
label3 = Label(label_frame1,text='= 0')
label3.grid(padx=5,pady=5,row=0,column=6)
label_frame2 = LabelFrame(text = 'Решение')
label_frame2.grid(padx=10,pady=10)
output = Text(label_frame2,width=27,height=8)
output.grid(padx=5,pady=10)
entry_a.bind('<F1>', lambda event: messagebox.showinfo('Информация', f'Введите число a'))
entry_b.bind('<F1>', lambda event: messagebox.showinfo('Информация', f'Введите число b'))
entry_c.bind('<F1>', lambda event: messagebox.showinfo('Информация', f'Введите число c'))
window.bind('<Return>',lambda event: equate(event))
window.bind('<Control-Key-1>',lambda event: entry_a.focus())
window.bind('<Control-Key-2>',lambda event: entry_b.focus())
window.bind('<Control-Key-3>',lambda event: entry_c.focus())
entry_a.bind('<FocusIn>', lambda event: entry_a.delete(0,END))
entry_b.bind('<FocusIn>', lambda event: entry_b.delete(0,END))
entry_c.bind('<FocusIn>', lambda event: entry_c.delete(0,END))
window.mainloop()


