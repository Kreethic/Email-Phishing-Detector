# Email-Phishing-Detector

Email Phishing Detector
An automated Python-based email security tool that scans incoming emails for phishing attempts, quarantines suspicious messages, and sends real-time alerts. This project helps protect users from malicious emails by detecting HTTP links and checking URLs against VirusTotal's database.

Features
IMAP Email Scanning: Connects to Gmail (or other IMAP servers) to fetch unread emails
Phishing Detection:
Identifies HTTP links (non-secure)
Checks URLs against VirusTotal API for malicious content
Automatic Quarantine: Moves suspicious emails to a dedicated "Quarantine" mailbox
Real-time Alerts: Sends email notifications when threats are detected
Logging: Stores flagged emails in a local SQLite database for review
Error Handling: Includes reconnection logic for stable IMAP connections
Prerequisites
Python 3.6+
Gmail account with IMAP enabled
VirusTotal API key (free tier available)
Required Python packages: imaplib, email, requests, smtplib, sqlite3 (built-in), base64, re
Installation
Clone this repository:

Install dependencies:

Configure your credentials:

Edit email_handler.py and replace:
EMAIL_ADDRESS with your Gmail address
EMAIL_PASSWORD with your Gmail app password (not regular password)
Edit phishing_detection.py and replace api_key with your VirusTotal API key
Edit alert.py and update sender/recipient email addresses and app password
Configuration
Gmail Setup
Enable IMAP in your Gmail settings
Generate an App Password for secure access:
Go to Google Account settings > Security > App passwords
Generate a password for "Mail"
VirusTotal API
Sign up for a free account at VirusTotal
Get your API key from the dashboard
Replace the placeholder in phishing_detection.py
Usage
Run the main script to scan for phishing emails:

The script will:

Connect to your email server
Fetch up to 10 unread emails from your inbox
Analyze each email for suspicious content
Quarantine any emails containing HTTP links or malicious URLs
Send alert emails with details of flagged messages
Log all flagged emails to phishing_alerts.db
How It Works
Email Fetching: Uses IMAP to retrieve unread emails from the inbox
Content Analysis:
Scans email body for HTTP links using regex
Extracts URLs and queries VirusTotal API for threat analysis
Quarantine Process: Moves flagged emails to a "Quarantine" IMAP folder
Alert System: Sends detailed notifications via SMTP
Logging: Maintains a database of all detected threats
Database
The project uses SQLite to store flagged emails in phishing_alerts.db with the following schema:

sender: Email sender address
subject: Email subject line
body: Full email content
Security Notes
Never commit API keys or passwords to version control
Use app-specific passwords instead of your main Gmail password
Consider running this on a secure, dedicated machine
Regularly review quarantined emails and update detection rules
Limitations
Currently limited to Gmail IMAP
Processes only the first 10 unread emails per run
Requires manual execution (not automated daemon)
Free VirusTotal API has rate limits
Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Disclaimer
This tool is for educational and personal use. Always verify security tools and never rely solely on automated detection for critical security decisions.

Grok Code Fast 1 • 1x
