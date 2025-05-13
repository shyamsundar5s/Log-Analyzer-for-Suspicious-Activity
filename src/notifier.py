# Module for sending notifications
import smtplib
from email.mime.text import MIMEText

def send_notification(subject, body):
    # Example for email notification
    sender_email = "your_email@example.com"
    receiver_email = "admin@example.com"
    password = "your_password"

    msg = MIMEText(str(body))
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
