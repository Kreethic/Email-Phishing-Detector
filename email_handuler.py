import imaplib
import email
import time

# Configuration
EMAIL_ADDRESS = 'analysing gmail'   # Replace with your email
EMAIL_PASSWORD = 'app-password'         # Replace with your password or app-specific password
IMAP_SERVER = 'imap.gmail.com'           # Replace with your email provider's IMAP server

def connect_to_email():
    # Connect to the IMAP server and log in
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    return mail

def fetch_emails(mail):
    mail.select("inbox")
    result, data = mail.search(None, "UNSEEN")
    email_ids = data[0].split()[:10]  # Limit to first 10 unread emails
    emails = []
    for email_id in email_ids:
        try:
            result, msg_data = mail.fetch(email_id, "(RFC822)")
        except Exception as e:
            print(f"Connection lost while fetching {email_id}, reconnecting...")
            mail = connect_to_email()
            mail.select("inbox")
            result, msg_data = mail.fetch(email_id, "(RFC822)")
        try:
            msg = email.message_from_bytes(msg_data[0][1])
            email_info = {
                'from': msg['From'],
                'subject': msg['Subject'],
                'body': "",
                'id': email_id.decode() if isinstance(email_id, bytes) else str(email_id)
            }
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        email_info['body'] = part.get_payload(decode=True).decode(errors='ignore') if part.get_payload(decode=True) else ""
                        break
            else:
                email_info['body'] = msg.get_payload(decode=True).decode(errors='ignore') if msg.get_payload(decode=True) else ""
            emails.append(email_info)
            time.sleep(0.1)  # Add a short delay
        except Exception as e:
            print(f"Error processing email {email_id}: {e}")
    return emails

def close_connection(mail):
    mail.logout()
    mail.logout()
