from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import numpy as np 
import matplotlib.pyplot as plt 


root = Tk()
root.title('Plots')
root.iconphoto(True, PhotoImage(file = 'images/python.png'))
root.geometry("400x200")

def graph():
	house_prices = np.random.normal(200000, 25000, 5000)
	plt.pie(house_prices)
	plt.show()

my_button = Button(root, text = "Graph IT!", command = graph).pack()


root.mainloop()
