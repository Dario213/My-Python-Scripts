from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import smtplib, ssl



port = 465 # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "my.python.projects1@gmail.com"
reciever_email = "my.python.projects2@gmail.com"



root = Tk()
root.title('Untitled')
root.iconphoto(True, PhotoImage(file = 'images/python.png'))
root.geometry("400x400")



root.mainloop()
