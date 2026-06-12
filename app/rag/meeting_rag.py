from app.rag.chunker import chunk_text
from app.rag.embeddings import create_embeddings
from app.rag.vector_store import store_chunks
from app.rag.rag_pipeline import answer_question


def ask_meeting_question(
    transcript: str,
    question: str
):

    chunks = chunk_text(transcript)

    embeddings = create_embeddings(chunks)

    store_chunks(
        chunks,
        embeddings
    )

    return answer_question(question)