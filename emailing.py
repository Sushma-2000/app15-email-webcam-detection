import smtplib
from email.message import EmailMessage
import filetype
from dotenv import load_dotenv
import os

load_dotenv()
sender = "pythonapp277@gmail.com"
password = os.getenv("PASSWORD")
receiver = sender

def send_email(image_path):
    print("send email function started")
    email_message = EmailMessage()
    email_message["Subject"] = "Hey new customer showed up!"
    email_message.set_content("Hey!! we just saw new customer")

    with open(image_path,"rb") as file:
        content = file.read()

    email_message.add_attachment(content, maintype = "image", subtype=filetype.guess(content).extension)
    gmail = smtplib.SMTP("smtp.gmail.com",587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(sender,password)
    gmail.sendmail(sender,receiver,email_message.as_string())
    gmail.quit()
    print("send email function ended")

if __name__ == "__main__":
    send_email("images/19.png")