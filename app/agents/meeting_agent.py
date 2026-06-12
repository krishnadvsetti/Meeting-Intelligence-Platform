from app.mcp.server import (
    list_meetings,
    get_meeting,
    summarize_meeting,
    get_action_items,
    ask_meeting
)


def run_agent(user_query: str):

    query = user_query.lower()

    if "list" in query or "meetings" in query:
        return list_meetings()

    if "summary" in query:

        meeting_id = int(
            query.split()[-1]
        )

        return summarize_meeting(
            meeting_id
        )

    if "action" in query:

        meeting_id = int(
            query.split()[-1]
        )

        return get_action_items(
            meeting_id
        )

    return (
        "I do not know which tool "
        "to use yet."
    )