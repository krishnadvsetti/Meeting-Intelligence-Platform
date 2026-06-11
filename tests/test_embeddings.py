from app.services.transcript_loader import load_transcript
from app.rag.chunker import chunk_text
from app.rag.embeddings import create_embeddings

transcript = load_transcript(
    "data/transcripts/meeting_001.txt"
)

chunks = chunk_text(transcript)

embeddings = create_embeddings(chunks)

print(f"Chunks: {len(chunks)}")
print(f"Embeddings: {len(embeddings)}")
print(f"Vector Size: {len(embeddings[0])}")