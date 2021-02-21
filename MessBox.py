from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


root = Tk()
root.title('Message Box')
root.iconphoto(True, PhotoImage(file = 'images/python.png'))

# showinfo "ok", showwarning "ok", showerror "ok", askquestion yes no, askokcancel 1 0, askyesno 1 0

def popup():
    response = messagebox.askokcancel("This is my Popup!", "Hello World")
    Label(root, text = response).pack()

    if response == 1:
        Label(root, text = "Heck Yess!").pack()
    else:
        Label(root, text = "WHY NOT!").pack()


Button(root, text = "Popup", command = popup).pack()


root.mainloop()
