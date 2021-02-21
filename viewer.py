from tkinter import *
from PIL import ImageTk, Image
import sys

root = Tk()
root.title('PythonApp')
root.iconphoto(True, PhotoImage(file = 'images/python.png'))

my_img1 = ImageTk.PhotoImage(Image.open("images/Osijek.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/jamarin.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/tvrdava.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/python.png"))
my_img5 = ImageTk.PhotoImage(Image.open("images/jamarkoivko.jpg"))
my_img6 = ImageTk.PhotoImage(Image.open("images/jamarkozic.jpg"))
my_img7 = ImageTk.PhotoImage(Image.open("images/jaaurora.jpg"))
my_img8 = ImageTk.PhotoImage(Image.open("images/jalara.jpg"))
my_img9 = ImageTk.PhotoImage(Image.open("images/jafranfilip.jpg"))
my_img0 = ImageTk.PhotoImage(Image.open("images/kodmora.jpg"))


image_list = [
        my_img1,
        my_img2,
        my_img3,
        my_img4,
        my_img5,
        my_img6,
        my_img7,
        my_img8,
        my_img9,
        my_img0
]


status = Label(root, text = "Image 1 of 5")



my_label = Label(image = my_img1)
my_label.grid(row = 0, column = 0, columnspan = 3)


def forward(image_number):
    global my_label
    global forward_btn
    global back_btn

    my_label.grid_forget()
    my_label = Label(image = image_list[image_number-1])
    forward_btn = Button(root, text = ">>", command = lambda: forward(image_number+1))
    back_btn = Button(root, text = "<<", command = lambda: back(image_number-1))

    if image_number == 10:
        forward_btn = Button(root, text = ">>", state = DISABLED)


    my_label.grid(row = 0, column = 0, columnspan = 3)
    back_btn.grid(row = 1, column = 0)
    forward_btn.grid(row = 1, column = 2)




def back(image_number):
    global my_label
    global forward_btn
    global back_btn

    my_label.grid_forget()
    my_label = Label(image = image_list[image_number-1])
    forward_btn = Button(root, text = ">>", command = lambda: forward(image_number+1))
    back_btn = Button(root, text = "<<", command = lambda: back(image_number-1))


    if image_number == 1:
        back_btn = Button(root, text = "<<", state = DISABLED)

    my_label.grid(row = 0, column = 0, columnspan = 3)
    back_btn.grid(row = 1, column = 0)
    forward_btn.grid(row = 1, column = 2)






back_btn = Button(root, text = "<<", command = back, state = DISABLED)
forward_btn = Button(root, text = ">>", command = lambda: forward(2))
exit_btn = Button(root, text = "Exit Program", command = root.quit)


back_btn.grid(row = 1, column = 0)
exit_btn.grid(row = 1, column = 1)
forward_btn.grid(row = 1, column = 2)


root.mainloop()
