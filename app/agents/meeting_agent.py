import json

from app.llm.gemini_client import model

from app.mcp.server import (
    list_meetings,
    summarize_meeting,
    get_action_items
)


def run_agent(user_query: str):

    prompt = f"""
You are a Meeting Intelligence Agent.

Available tools:

1. list_meetings
   Use when the user wants to see meetings.

2. summarize_meeting
   Requires:
   meeting_id

3. get_action_items
   Requires:
   meeting_id

Return ONLY valid JSON.

Examples:

{{
    "tool": "list_meetings"
}}

{{
    "tool": "summarize_meeting",
    "meeting_id": 2
}}

{{
    "tool": "get_action_items",
    "meeting_id": 2
}}

User Query:
{user_query}
"""

    response = model.generate_content(prompt)

    try:

        tool_response = response.text.strip()

        tool_response = (
            tool_response
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        tool_call = json.loads(
            tool_response
        )

    except Exception as e:

        return (
            f"Tool parsing failed: "
            f"{str(e)}\n\n"
            f"Raw response:\n"
            f"{response.text}"
        )

    tool = tool_call["tool"]

    if tool == "list_meetings":
        return list_meetings()

    if tool == "summarize_meeting":
        return summarize_meeting(
            tool_call["meeting_id"]
        )

    if tool == "get_action_items":
        return get_action_items(
            tool_call["meeting_id"]
        )

    return "Unknown tool selected."

def run_agent(user_query: str):

    query = user_query.lower()

    if "list" in query or "show" in query:
        return list_meetings()

    if "summary" in query:
        meeting_id = int(query.split()[-1])
        return summarize_meeting(meeting_id)

    if "action" in query:
        meeting_id = int(query.split()[-1])
        return get_action_items(meeting_id)

    return "Unknown request"