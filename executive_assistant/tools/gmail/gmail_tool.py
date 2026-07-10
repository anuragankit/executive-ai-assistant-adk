from googleapiclient.discovery import build

from .auth import get_gmail_credentials


def fetch_emails(query: str = "is:unread", max_results: int = 5):
    """
    Fetch emails matching a Gmail search query.
    """

    creds = get_gmail_credentials()

    service = build(
        "gmail",
        "v1",
        credentials=creds,
    )

    results = (
        service.users()
        .messages()
        .list(
            userId="me",
            q=query,
            maxResults=max_results,
        )
        .execute()
    )

    messages = results.get("messages", [])

    emails = []

    for msg in messages:

        message = (
            service.users()
            .messages()
            .get(
                userId="me",
                id=msg["id"],
            )
            .execute()
        )

        headers = message["payload"]["headers"]

        sender = ""
        subject = ""

        for header in headers:

            if header["name"] == "From":
                sender = header["value"]

            elif header["name"] == "Subject":
                subject = header["value"]

        snippet = message.get("snippet", "")

        emails.append(
            {
                "sender": sender,
                "subject": subject,
                "snippet": snippet,
            }
        )

    return emails


def get_unread_emails(max_results: int = 5) -> str:
    """
    Returns unread emails.
    """

    emails = fetch_emails(
        query="is:unread",
        max_results=max_results,
    )

    if not emails:
        return "You have no unread emails."

    output = []

    for email in emails:

        output.append(
            f"""
From: {email['sender']}
Subject: {email['subject']}
Snippet: {email['snippet']}
""".strip()
        )

    return "\n\n".join(output)

def get_recent_emails(limit: int = 10) -> str:
    """
    Returns the latest emails.
    """

    emails = fetch_emails(
        query="",
        max_results=limit,
    )

    if not emails:
        return "No recent emails found."

    output = []
    for email in emails:
        output.append(
            f"""
    From: {email["sender"]}
    Subject: {email["subject"]}
    Snippet: {email["snippet"]}
    """.strip()
    )
        
    return "\n\n".join(output)