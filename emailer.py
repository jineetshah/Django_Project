import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()


def send_email(subject, body, receiver_email, sender_email, sender_password):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    try:
        # Create a MIMEText object to represent the email body
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Create an SMTP session
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Email could not be sent. Error: {str(e)}")


if __name__ == "__main__":
    send_email('Email Notification',
               'This is a test email notification from Python.',
               'habhagat2003@gmail.com', os.environ['TEST_EMAIL'],
               os.environ['TEST_EMAIL_PASSWORD'])
