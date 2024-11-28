import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd

# Email server configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = 'yamini582006@gmail.com'
SENDER_PASSWORD = 'qemg fgtb lxzz ixbg'

# Base URL for phishing links (replace with local Flask server IP)
TRACKING_URL = 'https://c51f-2401-4900-2310-c68a-e9c3-692-8f67-3d91.ngrok-free.app/track-click?email='

# Read recipient list from CSV
recipients = pd.read_csv('email_list.csv')

def send_emails():
    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)

        # Loop through each recipient
        for _, row in recipients.iterrows():
            redirecting = '&redirect=https://aakashkumar-2005.github.io/Phishing_Awareness_IT_Head-/'
            recipient_email = row['Email']
            tracking_link = TRACKING_URL + recipient_email + redirecting

            # Create the email content
            subject ="Immediate System Update Required for Security Compliance "
            body = f"""
            Dear [Employee Name],
            
            Our systems require an urgent update to ensure protection against emerging threats. This update is critical to safeguarding company data and maintaining compliance with IT security policies.

            To proceed, follow the link below to install the update:

            {tracking_link}

            Kindly Update it as soon as possible or else your access to key systems may be temporarily restricted.


            Best regards,
            [IT Head Name]
            Head of IT
            TVS Mobility
            """
            

            # Create the MIME message
            msg = MIMEMultipart()
            msg['From'] = SENDER_EMAIL
            msg['To'] = recipient_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # Send the email
            server.send_message(msg)
            print(f"Email sent to {recipient_email}")

        # Close the server
        server.quit()
        print("All emails sent successfully.")

    except Exception as e:
        print(f"Error: {e}")


# Send the emails
send_emails()


#python emailsend.py  command to run this ..
# for tracking url , the command is " ngrok http 5000"