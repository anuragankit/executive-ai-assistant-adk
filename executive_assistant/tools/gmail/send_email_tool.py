from ...guardrails import validate_email_input
from email.mime.text import MIMEText
import base64

from googleapiclient.discovery import build

from .auth import get_gmail_credentials


def send_email(
    to: str,
    subject: str,
    body: str,
) -> str:
    """
    Sends an email using Gmail.
    """

    # ---------- Guardrail ----------
    valid, message = validate_email_input(
        to,
        subject,
        body,
    )

    if not valid:
        return message

    # ---------- Gmail ----------
    creds = get_gmail_credentials()

    service = build(
        "gmail",
        "v1",
        credentials=creds,
    )

    message = MIMEText(body)

    message["to"] = to
    message["subject"] = subject

    raw = base64.urlsafe_b64encode(
        message.as_bytes()
    ).decode()

    service.users().messages().send(
        userId="me",
        body={
            "raw": raw,
        },
    ).execute()

    return f"Email sent successfully to {to}."