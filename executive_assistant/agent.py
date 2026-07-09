from google.adk.agents import Agent

from .prompt import EXECUTIVE_PROMPT
from .tools import (
    get_current_time,
    calculate,
    remember_note,
    recall_notes,
)


root_agent = Agent(
    name="executive_assistant",
    model="gemini-2.5-flash",
    description="An Executive AI Assistant built with Google ADK.",
    instruction=EXECUTIVE_PROMPT,
    tools=[
        get_current_time,
        calculate,
        remember_note,
        recall_notes,
    ],
)