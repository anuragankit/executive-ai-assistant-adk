# Enterprise AI Executive Assistant

An enterprise-grade AI Executive Assistant built using Google's Agent Development Kit (ADK). The assistant can understand natural language requests, access Gmail, perform utility tasks, maintain persistent conversation memory, and orchestrate multiple specialized agents to complete user requests.

---

## Features

- Multi-Agent Architecture using Google ADK
- Gmail Integration
  - Read Emails
  - Send Emails
- Persistent Memory
  - Stores conversation history
  - Maintains context across sessions
- Utility Tools
  - Calculator
  - Current Time
- Guardrails for safer tool execution
- Natural Language Interface powered by Gemini
- Modular and scalable architecture
- Easy to extend with additional agents and tools

---

## Tech Stack

- Python
- Google Agent Development Kit (ADK)
- Vertex AI / Gemini
- Gmail API
- Google OAuth 2.0
- Google Cloud Platform (GCP)

---

## Project Structure

```text
executive_assistant/
│
├── .adk/
├── callbacks/
│   ├── __init__.py
│   ├── before_tool.py
│   ├── after_tool.py
│   └── on_tool_error.py
│
├── gmail_agent/
│   ├── __init__.py
│   └── agent.py
│
├── guardrails/
│   ├── __init__.py
│   └── email_guardrails.py
│
├── logs/
│
├── memory_agent/
│   ├── __init__.py
│   └── agent.py
│
├── tools/
│   ├── gmail/
│   │   └── __init__.py
│   ├── __init__.py
│   ├── calculator_tool.py
│   ├── notes_tool.py
│   └── time_tool.py
│
├── utility_agent/
│   ├── __init__.py
│   └── agent.py
│
├── prompts/
│
├── __init__.py
├── agent.py
├── prompt.py
├── tools.py
├── orion_memory.db
│
├── .dockerignore
├── .env
├── .env.example
├── .gitignore
├── credentials.json
├── Dockerfile
├── LICENSE
├── README.md
├── requirements.txt
└── main.py
```

## Architecture

```
                User
                  │
                  ▼
          Root ADK Agent
                  │
     ┌────────────┼────────────┐
     ▼            ▼            ▼
 Gmail Agent  Memory Agent  Utility Agent
     │            │            │
 Gmail API   Persistent DB   Calculator/Time
```

The Root Agent routes user requests to the appropriate specialized agent. Each agent is responsible for a specific domain, making the application modular and easy to maintain.

---

## How It Works

### Gmail Agent

Responsible for interacting with Gmail using the Gmail API.

Capabilities:
- Read emails
- Search inbox
- Send emails

---

### Memory Agent

Maintains long-term conversation context.

Capabilities:
- Store conversations
- Retrieve previous interactions
- Personalize responses

---

### Utility Agent

Provides common utility functions.

Capabilities:
- Mathematical calculations
- Current date and time

---

## Authentication

The application uses Google OAuth 2.0 for Gmail authentication.

Required OAuth Scopes:

- gmail.readonly
- gmail.send

A `token.json` file is generated after successful authentication and is used for subsequent API requests.

---

## Installation

Clone the repository

```bash
git clone https://github.com/anuragankit/executive-ai-assistant-adk.git

cd executive-ai-assistant-adk
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

```bash
python main.py
```

---

## Example Commands

```
Read my latest emails

Send an email to John

What time is it?

Calculate (234 * 98) + 127

Remember that my manager's name is Rahul

What did I tell you yesterday?
```

---

## Security

- OAuth 2.0 Authentication
- Protected API Keys using environment variables
- Guardrails before tool execution
- Sensitive files excluded using `.gitignore`

---

## Future Improvements

- Google Calendar Integration
- Google Drive Integration
- Slack Integration
- Microsoft Outlook Support
- RAG-based Enterprise Knowledge Search
- Voice Interaction
- Multi-user Authentication
- Docker Deployment
- Kubernetes Deployment

---

## Learning Outcomes

This project helped me gain practical experience with:

- Google Agent Development Kit (ADK)
- Multi-Agent Systems
- Agent Routing
- Tool Calling
- Google Vertex AI
- Gemini Models
- Gmail API
- OAuth Authentication
- Persistent Memory
- Guardrails
- Enterprise AI Application Design

---

## Author

**Ankit Anurag**

LinkedIn: https://www.linkedin.com/in/ankit-anurag-901881259/

GitHub: https://github.com/anuragankit

---

## License

This project is created for educational and portfolio purposes.
