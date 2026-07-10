from google.genai import Client

from .gmail_tool import get_recent_emails


def draft_reply() -> str:
    """
    Drafts a professional reply to the latest email.
    """

    latest_email = get_recent_emails(1)

    prompt = f"""
You are an executive assistant.

Read the email below and write a professional reply.

Email:

{latest_email}

Reply only with the email draft.
"""

    client = Client()

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text