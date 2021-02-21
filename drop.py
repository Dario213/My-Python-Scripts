from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


root = Tk()
root.title('Untitled')
root.iconphoto(True, PhotoImage(file = 'images/python.png'))
root.geometry("400x400")


def Show():
    lbl = Label(root, text = clicked.get()).pack()

options = [
     "Monday",
     "Tuesday",
     "Wednesday",
     "Thursday",
     "Friday",
     "Saturday"
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

btn = Button(root, text = "ShowSelected", command = Show).pack()

root.mainloop()
