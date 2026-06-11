from app.rag.rag_pipeline import answer_question

response = answer_question(
    "What concerns were raised about parking?"
)

print(response)