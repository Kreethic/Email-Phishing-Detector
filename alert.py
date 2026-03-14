import smtplib
from email.mime.text import MIMEText

def send_alert_email(subject, message):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    alert_email = "gmail"  # Sender (must match app password)
    alert_password = "password"  # App password

    # Change this to a different email for instant alert delivery
    recipient_email = "alert mail"  # <-- Set to another email for testing

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = alert_email
    msg['To'] = recipient_email

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(alert_email, alert_password)
            server.sendmail(alert_email, recipient_email, msg.as_string())
        print(f"Alert email sent to {recipient_email}.")
    except Exception as e:
        print(f"Failed to send alert email: {e}")
