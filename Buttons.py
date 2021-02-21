from tkinter import *

root = Tk()

def my_click():
    my_label = Label(root, text = "Look I Clicked a Button!")
    my_label.pack()


my_button = Button(root, text = "Click Me!", command = my_click)
my_button.pack()



root.mainloop()
