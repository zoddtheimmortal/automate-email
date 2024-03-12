from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from dotenv import load_dotenv
import smtplib
import os

load_dotenv()

email=os.getenv('EMAIL_ADDR')
password=os.getenv('EMAIL_PASSWD')
to=email
print(f"Email: {email}\nPassword: {password}")

smtp=smtplib.SMTP('smtp.gmail.com',587)
smtp.ehlo()
smtp.starttls()
smtp.login(user=email,password=password)

def send_email(i):
    print(f"Sending mail {i}...")
    message = MIMEMultipart()
    message["From"] = email
    message["To"] = email
    message["Subject"] = f"Test email {i} from Python"

    body = f"This is a test email {i} sent from Python"
    message.attach(MIMEText(body, "plain"))

    smtp.send_message(from_addr=email,to_addrs=to,msg=message)

if __name__ == "__main__":
    # for i in range(10):
    send_email(0)
    
    smtp.quit()