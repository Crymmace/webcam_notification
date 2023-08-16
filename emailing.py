import imghdr
import os
import smtplib
import ssl
from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv()


def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "Motion Detected!"
    email_message.set_content("Motion was detected!")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    host = "smtp.office365.com"
    port = 587

    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    receiver = os.getenv("USERNAME")
    context = ssl.create_default_context()

    with smtplib.SMTP(host, port) as server:
        server.starttls(context=context)
        server.ehlo()
        server.login(username, password)
        server.sendmail(username, receiver, email_message.as_string())

