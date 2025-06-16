# Mason Jones
# CNE 350 Final
# Spring 2025
# code sourced from: https://randomnerdtutorials.com/raspberry-pi-send-email-python-smtp-server/

import smtplib
from email.message import EmailMessage

# sender and receiver emails
from_email_addr = "raspiemailtest1@gmail.com"
from_email_pass = "kpzd qoue szwh gdmp"
to_email_addr = input("Welcome Mason, who would you like to email today?\n>")

# email subject
subject = input("Please enter the subject title of your email.\n>")

# contents of email
body = input("Please enter the message you would like to send.\n>")

# sets the contents of the email
msg = EmailMessage()
msg.set_content(body)

# sets sender and receiver
msg['From'] = from_email_addr
msg['To'] = to_email_addr

# sets email subject
msg['Subject'] = subject

# Connecting to server and sending email
server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()
# Login to the SMTP server
server.login(from_email_addr, from_email_pass)

# Send the message
server.send_message(msg)

print(f'Email sent to {to_email_addr}')

#Disconnect from the Server
server.quit()
