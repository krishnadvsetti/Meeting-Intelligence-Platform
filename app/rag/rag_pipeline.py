from app.rag.embeddings import create_embeddings
from app.rag.vector_store import search
from app.llm.gemini_client import model
from app.evaluation.evaluator import evaluate_response


def answer_question(question: str):

    query_embedding = create_embeddings(
        [question]
    )[0]

    results = search(
        query_embedding
    )

    retrieved_context = []

    if (
        results
        and "documents" in results
        and len(results["documents"]) > 0
    ):
        retrieved_context = (
            results["documents"][0]
        )

    context = "\n\n".join(
        retrieved_context
    )

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

    response = model.generate_content(
        prompt
    )

    answer = response.text

    evaluation = evaluate_response(
        question,
        retrieved_context,
        answer
    )

    return {
        "answer": answer,
        "evaluation": evaluation
    }