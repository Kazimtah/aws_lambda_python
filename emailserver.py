from email.message import EmailMessage
import smtplib
from string import Template
from pathlib import Path
from datetime import datetime

html_template = Template(Path('./template1.html').read_text())

print(html_template)
print(html_template.is_valid())
current_date = datetime.now()
html_content = html_template.substitute({"name":'Bobdgan',"date": current_date})


myemail = EmailMessage()
myemail['from'] = 'bogdan'
myemail['to'] = 'test@test.com'
myemail['subject'] = "Hello from ptyhon"
myemail.set_content(html_content, "html")


with smtplib.SMTP(host='127.0.0.1', port= 2525) as smtp_server:
    smtp_server.ehlo()
    #smtp_server.starttls()
    #smtp_server.login('username', 'password')
    smtp_server.send_message(myemail)
    print("Email was sent")
#print(type(myemail))