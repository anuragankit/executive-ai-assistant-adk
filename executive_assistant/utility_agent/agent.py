from google.adk.agents import Agent

from ..tools import (
    calculate,
    get_current_time,
)

utility_agent = Agent(
    name="utility_agent",
    model="gemini-2.5-flash",
    description="Handles utility operations.",
    instruction="""
You answer utility requests.

Use tools.

Never calculate manually.

Use the time tool whenever needed.
""",
    tools=[
        calculate,
        get_current_time,
    ],
)