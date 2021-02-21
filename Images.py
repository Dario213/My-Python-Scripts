from tkinter import *
from PIL import ImageTk, Image
import sys

root = Tk()
root.title('PythonApp')
root.iconphoto(True, PhotoImage(file = 'images/python.png'))

my_img = ImageTk.PhotoImage(Image.open("images/Osijek.jpg"))
my_label = Label(image = my_img)
my_label.pack()



root.mainloop()
