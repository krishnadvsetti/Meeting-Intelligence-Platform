import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


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