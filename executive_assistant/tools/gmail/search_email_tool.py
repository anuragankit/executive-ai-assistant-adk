from .gmail_tool import fetch_emails

def search_email(query: str, max_results: int = 5) -> str:
    """
    Searches Gmail using a Gmail query.
    """

    emails = fetch_emails(
        query=query,
        max_results=max_results,
    )

    if not emails:
        return "No matching emails found."

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