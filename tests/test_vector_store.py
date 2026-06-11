from app.services.transcript_loader import load_transcript
from app.rag.chunker import chunk_text
from app.rag.embeddings import create_embeddings
from app.rag.vector_store import store_chunks, search

transcript = load_transcript(
    "data/transcripts/meeting_001.txt"
)

chunks = chunk_text(transcript)

embeddings = create_embeddings(chunks)

store_chunks(chunks, embeddings)

query = "What concerns were raised about parking?"

query_embedding = create_embeddings([query])[0]

results = search(query_embedding)

print(results["documents"][0])