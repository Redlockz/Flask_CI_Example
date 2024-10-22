"""
This module provides functionality to send emails using SMTP.
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(form_data):
    """
    Sends an email using the provided form data.

    Args:
        form_data (dict): A dictionary containing the email details.
            - 'email': The sender's email address.
            - 'receiver': The receiver's email address.
            - 'subject': The subject of the email.
            - 'body': The body of the email.
    """
    ## This is created for a Gmail account using an 'App Password'
    ## To create this, use the following steps:
    ## 1. Create a Gmail account with MFA enabled
    ## 2. Go to https://support.google.com/mail/answer/185833?hl=en (As of time of writing) and use the link provided to create an App Password
    ## 3. Create App Password for 'Mail' and use this password in the 'passwd' variable
    ## 4. This will allow you to send emails from the account without having to use the actual password
    ## Make sure to keep this password safe as it is essentially the password for the account
    ## Never let this enter your commit history
    ## Malicious users will abuse you mail for spamming, phishing, etc.
    sender = None
    passwd = None
    if sender is None or passwd is None:
        print("Please provide a valid Gmail address and password")
        raise Exception(f"Invalid email address and/or password. { sender }, { passwd } were given as arguments.")
    # Create the email message
    message = MIMEMultipart()
    message["From"] = form_data['email']
    message["To"] = form_data['receiver']
    message["Subject"] = form_data['subject']
    body = form_data['body']
    message.attach(MIMEText(body, 'plain'))

    # Add logging
    print("Sending email...")
    print(f"From: {message['From']}")
    print(f"To: {message['To']}")
    print(f"Subject: {message['Subject']}")
    print(f"Body: {body}")
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, passwd)

    print("SMTP connection established")

    text = message.as_string()
    server.sendmail(sender, form_data['receiver'], text)
    print("Email sent successfully")
