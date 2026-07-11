def validate_email_input(to, subject, body):
    if not to.strip():
        return False, "Recipient email cannot be empty."

    if "@" not in to:
        return False, "Invalid email address."

    if not subject.strip():
        return False, "Subject cannot be empty."

    if not body.strip():
        return False, "Body cannot be empty."

    return True, ""