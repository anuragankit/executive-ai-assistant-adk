from google.genai import Client

from .gmail_tool import get_recent_emails


def summarize_inbox() -> str:
    """
    Returns an executive summary of the latest emails.
    """

    emails = get_recent_emails(10)

    prompt = f"""
You are an Executive AI Assistant.

Summarize the following inbox.

Mention:
- Urgent emails
- Important emails
- Promotional emails
- Any action items

Inbox:

{emails}
"""

    client = Client()

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text