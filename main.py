from email_handler import connect_to_email, fetch_emails
from phishing_detection import check_url_virustotal, contains_http_link
from quarantine import quarantine_email
from alert import send_alert_email
from logger import log_flagged_email

def run():
    # Connect to the email server
    mail = connect_to_email()  
    
    # Fetch unread emails
    emails = fetch_emails(mail)  
    
    # Print the fetched emails
    import datetime
    if not emails:
        print("No unread emails found.")
        send_alert_email("Email Scan Result", "No unread emails found.")
    else:
        suspicious_found = False
        for email in emails:
            print(f"From: {email['from']}")
            print(f"Subject: {email['subject']}")
            print(f"Body: {email['body']}\n")  # Print the body content

            # Check for HTTP (not HTTPS) links
            http_link = contains_http_link(email['body'])
            if http_link:
                suspicious_found = True
                quarantine_email(mail, email['id'])  # Quarantine the email
                alert_message = (
                    f"Suspicious email detected (HTTP link) and quarantined.\n\n"
                    f"Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                    f"From: {email['from']}\n"
                    f"Subject: {email['subject']}\n"
                    f"Body: {email['body']}\n"
                    f"HTTP Link: {http_link}\n"
                )
                send_alert_email("Phishing Alert", alert_message)
                log_flagged_email(email)
                continue  # Skip further checks if HTTP link is found

            # Check if the email body contains a phishing URL (VirusTotal)
            suspicious_url = check_url_virustotal(email['body'])
            if suspicious_url:
                suspicious_found = True
                quarantine_email(mail, email['id'])  # Quarantine the email
                alert_message = (
                    f"Suspicious email detected and quarantined.\n\n"
                    f"Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                    f"From: {email['from']}\n"
                    f"Subject: {email['subject']}\n"
                    f"Body: {email['body']}\n"
                    f"Phishing URL: {suspicious_url}\n"
                )
                send_alert_email("Phishing Alert", alert_message)  # Send detailed alert
                log_flagged_email(email)  # Log the flagged email
        if not suspicious_found:
            print("No suspicious emails found.")
            send_alert_email("Email Scan Result", "No suspicious emails found.")

if __name__ == "__main__":
    run()
