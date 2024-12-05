import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd

# Email server configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = 'yamini582006@gmail.com'
SENDER_PASSWORD = 'qemg fgtb lxzz ixbg'

# Base URL for phishing links (replace with your ngrok public URL)
TRACKING_URL = 'https://1d6f-2405-201-e006-1075-f99e-7f9d-ccc2-cb66.ngrok-free.app/track-click?email='

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
            recipient_name = row['Name']  # Fetch name
            recipient_email = row['Email']
            redirecting = '&redirect=https://aakashkumar-2005.github.io/Phishing_Awareness_IT_Head-/'
            tracking_link = TRACKING_URL + recipient_email + redirecting

            # Create the email content
            subject = "Immediate System Update Required for Security Compliance"
            body = f"""
            <html>
            <body>
                <p>Dear {recipient_name},</p> <!-- Insert Name -->

                <p>Our systems require an urgent update to ensure protection against emerging threats. This update is critical to safeguarding company data and maintaining compliance with IT security policies.</p>

                <p>To proceed, please click the link below:</p>

                <p><a href="{tracking_link}" style="color: blue; text-decoration: underline;">Click Here to Update</a></p>

                <p>Kindly complete this update as soon as possible, or your access to key systems may be temporarily restricted.</p>

                <p>Best regards,<br>
                [IT Head Name]<br>
                Head of IT<br>
                TVS Mobility</p>
            </body>
            </html>
            """

            # Create the MIME message
            msg = MIMEMultipart()
            msg['From'] = SENDER_EMAIL
            msg['To'] = recipient_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'html'))  # Ensure email body is HTML

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
