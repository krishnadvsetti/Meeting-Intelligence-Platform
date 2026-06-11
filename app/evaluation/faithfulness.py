import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def score_faithfulness(
    question,
    context,
    answer
):

    prompt = f"""
You are evaluating a RAG system.

Question:
{question}

Retrieved Context:
{context}

Generated Answer:
{answer}

Give a faithfulness score from 1 to 10.

Return only the number.
"""

    response = model.generate_content(
        prompt
    )

    return response.text.strip()