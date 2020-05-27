import tkinter
from tkinter import messagebox

def mytext():
    messagebox.showinfo('Message', entry.get())

win = tkinter.Tk()
win.geometry('300x300')

entry = tkinter.Entry(win, justify=tkinter.CENTER)
entry.pack()

button = tkinter.Button(win, text='Add', command=mytext)
button.pack()

win.mainloop()