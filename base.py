from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


root = Tk()
root.title('NewWindows')
root.iconphoto(True, PhotoImage(file = 'images/python.png'))

def open():
    global my_img
    top = Toplevel()
    top.title('Second Window')
    my_img = ImageTk.PhotoImage(Image.open("images/Osijek.jpg"))
    lbl = Label(top, image = my_img).pack()
    btn2 = Button(top, text = "Close", command = top.destroy).pack()


btn = Button(root, text = "Open Second Window", command = open).pack()




mainloop()
