import smtplib, ssl

port = 465 # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "my.python.projects1@gmail.com"
reciever_email = "my.python.projects2@gmail.com"
password = input("Type your password and press enter: ")
message = """\
Subject: Hi There

This is a message sent from python."""

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context = context) as server:
	server.login(sender_email, password)
	server.sendmail(sender_email, reciever_email, message)