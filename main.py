from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import Combobox
from tkinter import messagebox


def clicked():

    txt_original = txt.get(1.0, END)
    txt_lenght=len(txt_original)-1
    txt2.delete(1.0, END)
    if int(spin.get())>0:
        if ((combo2.get()=='Зашифровать') | (combo2.get()=='Расшифровать')):
            if combo2.get()=='Зашифровать':
                row_count=int(spin.get())
                colums_count=int(((txt_lenght/row_count)+1))

            if combo2.get() == 'Расшифровать':
                colums_count = int(spin.get())
                row_count = int(((txt_lenght / colums_count) + 1))


            for i in range (0, row_count):
                for j in range(0, colums_count):
                    if i+j*row_count<len(txt_original)-1:
                        txt2.insert(INSERT, txt_original[i+j*row_count])
                    else:
                        break

        else:
            messagebox.showinfo('Ошибка!', f'Вы неверно ввели действие! (Зашифровать или Расшифровать)')

    else:
        messagebox.showinfo('Ошибка!', f' Количество символов в строке должно быть больше 0')


window = Tk()
window.title("Система шифрования Сцитала (Скитала)")
window.geometry('500x200')

lbl = Label(window, text="кол-во символов в строке")
lbl.grid(column=0, row=2)

spin = Spinbox(window, from_=0, to=100, width=5)
spin.grid(column=0, row=3)


combo2 = Combobox(window)
combo2['values'] = ("Зашифровать", "Расшифровать")
combo2.current(0)
combo2.grid(column=0, row=4)



btn = Button(window, text="Получить ответ", command=clicked)
btn.grid(column=0, row=5)
lbl = Label(window)


txt = scrolledtext.ScrolledText(window, width=40, height=1)
txt.grid(column=2, row=0)

txt2 = scrolledtext.ScrolledText(window, width=40, height=1)
txt2.grid(column=2, row=6)


window.mainloop()

