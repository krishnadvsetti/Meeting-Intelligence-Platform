import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


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