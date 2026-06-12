from app.rag.embeddings import create_embeddings
from app.rag.vector_store import search
from app.llm.gemini_client import model


def answer_question(question: str):

    query_embedding = create_embeddings([question])[0]

    results = search(query_embedding)

    context = "\n\n".join(results["documents"][0])

    prompt = f"""
You are an AI Meeting Intelligence Assistant.

Use only the provided meeting context.

If the answer is not found in the context, say:
'I could not find that information in the meeting transcript.'

Meeting Context:
{context}

Question:
{question}

Answer:
"""

    response = model.generate_content(prompt)

    return response.text