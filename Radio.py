from tkinter import *

root = Tk()
root.title('Radio Choices')
root.iconphoto(True, PhotoImage(file = 'images/python.png'))


#r = IntVar()
#r.set("2")

TOPPINGS = [
    ("Pepperroni", "Pepperroni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
]

pizza = StringVar()
pizza.set("Pepperroni")

for text, topping in TOPPINGS:
    Radiobutton(root, text = text, variable = pizza, value = topping).pack(anchor = W)

def clicked(value):
    my_label = Label(root, text = value)
    my_label.pack()


#Radiobutton(root, text = "Option 1", variable = r, value = 1, command = lambda: clicked(r.get())).pack()
#Radiobutton(root, text = "Option 2", variable = r, value = 2, command = lambda: clicked(r.get())).pack()

#my_label = Label(root, text = pizza.get())
#my_label.pack()

my_button = Button(root, text = "Click Me!", command = lambda: clicked(pizza.get()))
my_button.pack()

root.mainloop()
