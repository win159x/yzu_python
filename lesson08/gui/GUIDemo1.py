import tkinter

win = tkinter.Tk()

win.title('我的小視窗')
label = tkinter.Label(win, text='Hello')
label.pack()
win.geometry('300x300')

win.mainloop()