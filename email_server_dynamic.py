#Importing required libraries to build email server
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html =Template(Path('index.html').read_text())

# Email Credentials
your_email_address= 'baba.jager20@gmail.com'
your_email_password = 'Baba@jager2020'

#Email Headers [From, To & Subject]
email = EmailMessage()
email['from'] = 'Python Lover'
email['to'] = 'bipzification@gmail.com'
email['subject'] = 'Testing Email sent through Python'

#Email Message
email.set_content(html.substitute({'name': 'Mr. Bond'}), 'html')

#Sending Email
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(your_email_address, your_email_password)
    smtp.send_message(email)
    print("Sucessfully sent!")


