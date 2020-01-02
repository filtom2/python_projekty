from tkinter import * 


def doNothing():
    print('ok ok I wont..')

root = Tk()

#   **** Mainmenu *****

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)      #adding item
menu.add_cascade(label='File', menu=subMenu)    #telling it how to behave
subMenu.add_command(label='New project...', command=doNothing)
subMenu.add_command(label='New file ...', command=doNothing)
subMenu.add_separator()
subMenu.add_command(label='exit', command=root.quit)

editMenu = Menu(menu)   #adding item
menu.add_cascade(label='Edit', menu=editMenu)      #telling it how to behave
editMenu.add_command(label='redo', command=doNothing)

viewMenu = Menu(menu)
menu.add_cascade(label='View', menu=viewMenu)
viewMenu.add_command(label='Appearence', command=doNothing)
viewMenu.add_separator()
viewMenu.add_command(label='Explorer', command=doNothing)

#   **** Toolbar ****

toolbar = Frame(root, bg='blue')

insertButton = Button(toolbar, text='insert image', command=doNothing)
insertButton.pack(side=LEFT, padx=2, pady=2)          #padx,pady = extra space 
printButton = Button(toolbar, text='print', command=doNothing)
printButton.pack(side=LEFT, padx=2,pady=2)

toolbar.pack(side=TOP, fill=X)

root.mainloop()