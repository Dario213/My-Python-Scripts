from tkinter import *

root = Tk()

entry = Entry(root, width = 50, fg = "red", borderwidth = 5)
entry.pack()
entry.insert(0, "Enter your name: ")

def my_click():
    hello = "Hello " + entry.get()
    my_label = Label(root, text = hello)
    my_label.pack()


my_button = Button(root, text = "Enter your Name", command = my_click)
my_button.pack()



root.mainloop()
