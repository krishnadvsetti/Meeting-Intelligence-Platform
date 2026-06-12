from app.llm.gemini_client import model


def generate_summary(transcript: str):

    prompt = f"""
You are an AI Meeting Intelligence Assistant.

Create a concise executive summary of the meeting.

Transcript:
{transcript}

Summary:
"""

    response = model.generate_content(prompt)

    return response.text