def quarantine_email(mail, email_id):
    # Create quarantine mailbox if it doesn't exist
    try:
        mail.create("Quarantine")
    except:
        pass  # Already exists
    
    # Copy the email to Quarantine
    mail.copy(email_id, "Quarantine")
    
    # Mark as deleted in inbox
    mail.store(email_id, '+FLAGS', '\\Deleted')
    
    # Expunge to remove
    mail.expunge()
    
    print(f"Email {email_id} quarantined.")
