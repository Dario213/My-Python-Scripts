from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from sys import exit
import smtplib, ssl
import time


root = Tk()
root.title('Customer Review')
root.iconphoto(True, PhotoImage(file = 'images/python.png'))
root.geometry("400x200")

def SendEmail(grade):
	port = 465 # For SSL
	smtp_server = "smtp.gmail.com"
	sender_email = f"{mail_adress_ent.get()}"
	reciever_email = "my.python.projects2@gmail.com"
	password = f"{mail_password_ent.get()}"

	message = """\
Subject: Customer Review from {}.


Your employee has just been reviewed by {} from {}!
Here is what {} thinks of your employee.

Employee reviewed: {}
Grade earned: {}

Here is {}'s explanation of why he thinks your customer deserved his grade:


{}""".format(f_name_ent.get() + " " + l_name_ent.get(), f_name_ent.get() + " " + l_name_ent.get(), adress_ent.get(), f_name_ent.get(), clicked.get(), grade, f_name_ent.get(), text_widget.get("1.0", END))

	context = ssl.create_default_context()

	with smtplib.SMTP_SSL(smtp_server, port, context = context) as server:
		server.login(sender_email, password)
		server.sendmail(sender_email, reciever_email, message)

	label = Label(submit, text = "THANK YOU FOR YOUR TIME!").grid(row = 6, column = 0) 
	time.sleep(3)
	exit(0)

def Submit(Graded):
	global submit
	submit = Tk()
	submit.title('Send Email')
	submit.geometry('400x400')

	
	global f_name_ent
	global l_name_ent
	global adress_ent
	global mail_adress_ent
	global mail_password_ent
	f_name_ent = Entry(submit, width = 30, borderwidth=2)
	f_name_ent.grid(row = 0, column = 1, pady = 3)
	l_name_ent = Entry(submit, width = 30, borderwidth=2)
	l_name_ent.grid(row = 1, column = 1, pady = 3)
	adress_ent = Entry(submit, width = 30, borderwidth=2)
	adress_ent.grid(row = 2, column = 1, pady = 3)
	mail_adress_ent = Entry(submit, width = 30, borderwidth=2)
	mail_adress_ent.grid(row=3, column=1, pady = (20, 3))
	mail_password_ent = Entry(submit, width = 30, borderwidth=2)
	mail_password_ent.grid(row=4,column=1)


	f_name_lbl = Label(submit, text = "First name:	").grid(row=0, column=0, stick = W)
	l_name_lbl = Label(submit, text = "Last name:	").grid(row=1, column=0, stick = W)
	adress_lbl = Label(submit, text = "Adress:      ").grid(row=2, column=0, stick = W)
	mail_adress_lbl = Label(submit, text = "Mail adress: ").grid(row=3, column=0, pady = (20, 3), stick = W)
	mail_password_lbl = Label(submit, text = "Password:    ").grid(row=4,column=0, stick = W)


	send_btn = Button(submit, text = f"Send Email With Poll Results of {clicked.get()}", command =lambda: SendEmail(Graded)).grid(row=5, column=0, columnspan = 2, pady = 20, stick = W)

# Because indent matters

def ConfirmSelected():
	response = messagebox.askokcancel("Open New Window", "Confirming Selection will open \nNew Window in wich you will fill\nThe poll about selected employee.\n\n\nDeclining will shut down the app.")
	if response == 0:
		exit(0)
	else:
		global poll
		poll = Tk()
		poll.title('Poll')
		poll.geometry("400x600")

		poll_frame = LabelFrame(poll, text = f"Grade {clicked.get()}", padx = 25, pady = 25)
		poll_frame.grid(row=0, column=0, padx = 10, pady = 10)



		GRADES = [
			("Very Bad", "Very Bad"),
			("Bad", "Bad"),
			("Good", "Good"),
			("Very Good", "Very Good"),
			("Perfect", "Perfect"),
		]

		global emp_grade
		emp_grade = StringVar(poll)
		emp_grade.set("Good")

		for text, grade in GRADES:
			Radiobutton(poll_frame, text = text, variable = emp_grade, value = grade, tristatevalue = 0).pack(anchor = W)

		prompt_lbl = Label(poll_frame, text = "If you want to explain your choice we would aprecciate it:").pack(anchor = W)

		global text_widget
		text_widget = Text(poll_frame, width = 40, height = 20, borderwidth = 3)
		text_widget.pack(anchor = W)

		submit_btn = Button(poll, text = "Send your review", command = lambda: Submit(emp_grade.get()))
		submit_btn.grid(row=1, column=0)

	
#Indent matters

frame = LabelFrame(root, text = "Customer Selection", padx = 25, pady = 25)
frame.grid(row=0, column=0, padx = 10, pady = 10)

employees = [
     "Dario Adamovic",
     "Dino Adamovic",
     "Danijela Adamovic",
     "Goran Adamovic",
     "Blaženka Adamovic",
     "Max"
]

global clicked
clicked = StringVar()
clicked.set("Select an employee you wish to review.")

drop = OptionMenu(frame, clicked, *employees)
drop.grid(row=0, column=0)

confirm_selection_btn = Button(frame, text = "Confirm Selection", command = ConfirmSelected).grid(row=1, column=0)



root.mainloop()
