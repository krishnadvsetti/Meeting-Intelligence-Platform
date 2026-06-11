from app.rag.rag_pipeline import answer_question
from app.evaluation.faithfulness import score_faithfulness
from app.rag.embeddings import create_embeddings
from app.rag.vector_store import search

question = "What concerns were raised about parking?"

query_embedding = create_embeddings([question])[0]

results = search(query_embedding)

context = "\n".join(results["documents"][0])

answer = answer_question(question)

score = score_faithfulness(
    question,
    context,
    answer
)

print("\nANSWER:\n")
print(answer)

print("\nFAITHFULNESS SCORE:\n")
print(score)