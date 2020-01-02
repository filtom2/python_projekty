from tkinter import * 

class PCButtons:

    def __init__(self, master):     #master,root = main window
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text='Print Message', command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text='quit', command=frame.quit)
        self.quitButton.pack(side=LEFT)


    def printMessage(self):
        print('This is Message')

root = Tk()
b = PCButtons(root)
root.mainloop()