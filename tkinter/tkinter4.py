from tkinter import *

root = Tk()


def printName(event):
    print('Hello my name is Program.')


button_1 = Button(root, text='Print name')
button_1.bind("<Button-1>", printName)
button_1.grid(row=1)

root.mainloop()