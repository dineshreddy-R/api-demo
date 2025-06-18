import smtplib
from email.message import EmailMessage


sender_mail ="dinedinesh191@gmail.com"
app_password="zpmm fdmi wxfg itjs"

receiver_mail = "thathireddydineshreddy4@gmail.com"
subject ="this mail send by bot"
body=("this is mail is send by using python code "
         "hello dinesh reddy")

msg = EmailMessage()
msg["from"] = sender_mail
msg["to"] = receiver_mail
msg["subject"] = subject
msg.set_content(body)

with smtplib.SMTP_SSL("SMTP.gmail.com",465) as smtp:
    smtp.login(sender_mail,app_password)
    smtp.send_message(msg)

print("✅ gmail sent ")