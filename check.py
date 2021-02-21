from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


root = Tk()
root.title('Untitled')
root.iconphoto(True, PhotoImage(file = 'images/python.png'))
root.geometry("400x400")


variable = StringVar()

chk = Checkbutton(root, text = "I dare you to check this box!", variable = variable, onvalue = "on", offvalue = "off")
chk.deselect()
chk.pack()

my_label = Label(root, text = variable.get()).pack()


def Show():
    my_label = Label(root, text = variable.get()).pack()





btn = Button(root, text = "Show Selection", command = Show)
btn.pack()

root.mainloop()
