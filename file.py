from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('File')
root.iconphoto(True, PhotoImage(file = 'images/python.png'))



def OpenFile():
    global my_img
    root.filename = filedialog.askopenfilename(initialdir = "images/", title = "Select A File", filetypes = (("png files", "*.png"), ("jpg files", "*.jpg"), ("all files", "*.*")))
    my_label = Label(root, text = root.filename).pack()
    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image = my_img).pack()
    open_img_button.state = DISABLED


open_img_button = Button(root, text = "Open A file", command = OpenFile).pack()


root.mainloop()
