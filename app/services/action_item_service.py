from app.llm.gemini_client import model


def extract_action_items(transcript):

    prompt = f"""
You are an AI meeting assistant.

Extract action items from the meeting.

Return them as:

- Task
- Owner (if known)
- Deadline (if mentioned)

Meeting Transcript:

{transcript}
"""

    response = model.generate_content(prompt)

    return response.text