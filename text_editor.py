from tkinter import *
from tkinter import scrolledtext, messagebox # Окно для ввода текста, всплывающее окно
from tkinter.ttk import Combobox, Checkbutton  # выпадающий список, чекбокс


def click_btn():
    res = 'Я же просил!!!! {}\nВаш выбор {}\n {}, {}'.format(txt.get(), combo.get(), chk_state.get(), res1)
    lbl.configure(text=res, fg='red')


def clicked():
    lbl.configure(text=selected.get())
    messagebox.showinfo('Заголовок', 'Текст')


window = Tk()  # Инициализация окна
window.title('Test_window')  # Название окна
window.geometry('1000x500')  # Размер окна
###############################################################################################################
lbl = Label(window, text='Привет', font=('Arial Bold', 50), fg='green')  # Вставка текста в окно
# bg - изменение цвета заливки текста   fg - изменение цвета шрифта текста
lbl.grid(column=0, row=0)  # Размещение текста
###############################################################################################################
btn = Button(window, text='Не нажимай!!', font=('Arial Bold', 10), bg='green', fg='white',
             command=click_btn)  # Вставка кнопки в окно
# bg - изменение цвета заливки кнопки   fg - изменение цвета шрифта кнопки
# command - вызывает функцию click_btn которая меняет lbl на новые данные
btn.grid(column=1, row=0)  # Размещение кнопки
###############################################################################################################
txt = Entry(window, width=20, state='disabled')  # Пользовательский ввод
# txt = Entry(window,width=10, state='disabled')  state='disabled' отключает возможность ввода в окно
txt.focus()  # держит постоянный фокус на вводе
txt.grid(column=2, row=2)
###############################################################################################################
combo = Combobox(window)  # Выпадающий список
combo['values'] = (1, 2, 3, 4, 5, "Текст")
combo.current(0)  # вариант по умолчанию (индекс списка combo['values'])
combo.grid(column=0, row=2)
###############################################################################################################
chk_state = BooleanVar()  # Чекбокс
chk_state.set(False)  # проверка состояния чекбокса (False- отжат по дефолту, True- нажат по дефолту)
chk = Checkbutton(window, text='Выбрать', var=chk_state)
# var=chk_state значек флажка выбора
chk.grid(column=0, row=3)
###############################################################################################################
selected = IntVar()  # Избранная Radio Button
rad1 = Radiobutton(window, text='Первый', value=1, variable=selected)
rad2 = Radiobutton(window, text='Второй', value=2, variable=selected)
rad3 = Radiobutton(window, text='Третий', value=3, variable=selected)
btn = Button(window, text="Клик", command=clicked)
lbl = Label(window)
rad1.grid(column=0, row=5)
rad2.grid(column=1, row=5)
rad3.grid(column=2, row=5)
btn.grid(column=4, row=5)
lbl.grid(column=0, row=6)
###############################################################################################################
txt1 = scrolledtext.ScrolledText(window, width=40, height=10)  # текстовая область
txt1.grid(column=0, row=7)
txt1.insert(INSERT, 'Текстовое поле')
# txt1.delete(1.0, END)  # мы передали координаты очистки
###############################################################################################################
#всплывающее окно
# messagebox.showinfo('Заголовок', 'Текст') # Нужно запихивать в функцию, иначе всплывает сразу после запуска
# messagebox.showwarning('Заголовок', 'Текст')  # показывает предупреждающее сообщение
# messagebox.showerror('Заголовок', 'Текст')  # показывает сообщение об ошибке

# Показ диалоговых окон с выбором варианта
res1 = messagebox.askquestion('Заголовок', 'Текст')
# res1 = messagebox.askyesno('Заголовок', 'Текст')
# res1 = messagebox.askyesnocancel('Заголовок', 'Текст')
# res1 = messagebox.askokcancel('Заголовок', 'Текст')
# res1 = messagebox.askretrycancel('Заголовок', 'Текст')
###############################################################################################################
spin = Spinbox(window, from_=0, to=100, width=5) # Добавление SpinBox
# spin = Spinbox(window, values=(3, 8, 11), width=5) # Добавление SpinBox c указанием диапозона (values)

# var = IntVar() # Добавление SpinBox c указанием диапозона и дефолтной настройкой
# var.set(36)
# spin = Spinbox(window, from_=0, to=100, width=5, textvariable=var)

spin.grid(column=0, row=8)

window.mainloop()  # Функция зацикливания окна


