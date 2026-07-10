from google.adk.agents import Agent

from ..tools import (
    remember_note,
    recall_notes,
)

memory_agent = Agent(
    name="memory_agent",
    model="gemini-2.5-flash",
    description="Handles memory operations.",
    instruction="""
You are responsible for memory.

Remember information.

Recall stored notes.

Never answer unrelated questions.
""",
    tools=[
        remember_note,
        recall_notes,
    ],
)