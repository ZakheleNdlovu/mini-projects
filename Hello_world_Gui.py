import tkinter

win = tkinter.Tk()
win.geometry('250x300')
win.resizable(False, False)

def hello():
    label.configure(text='Hello World!', width=12)

def goodbye():
    label.configure(text='Goodbye World!')

def clear():
    label.configure(text='')

label = tkinter.Label(win, font=('Ink Free', 25),width=12)
label.place(x=15 ,y=10)

button = tkinter.Button(win, text='Hello',padx=20, command=hello)
button.place(x=10, y=110)
button = tkinter.Button(win, text='Goodbye',padx=20, command=goodbye)
button.place(x=10, y=140)
button = tkinter.Button(win, text='Clear',padx=20, command=clear)
button.place(x=10, y=170)


win.mainloop()