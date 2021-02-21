from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


root = Tk()
root.title('Slider')
root.iconphoto(True, PhotoImage(file = 'images/python.png'))



def ShowValue(var):
    root.geometry(str(horizontal.get()) + "x400")

# Don't place slider in same line as defining it


horizontal = Scale(root, from_ = 400, to = 1000, orient = HORIZONTAL, command = ShowValue)
horizontal.pack()







root.mainloop()
