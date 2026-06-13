from app.agents.meeting_agent import run_agent

print("\n=== LIST MEETINGS ===")
print(
    run_agent(
        "Show all meetings"
    )
)

print("\n=== SUMMARY ===")
print(
    run_agent(
        "Summarize meeting 2"
    )
)

print("\n=== ACTION ITEMS ===")
print(
    run_agent(
        "Get action items from meeting 2"
    )
)