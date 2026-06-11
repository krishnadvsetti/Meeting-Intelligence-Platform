from app.services.transcript_loader import load_transcript
from app.rag.chunker import chunk_text

transcript = load_transcript(
    "data/transcripts/meeting_001.txt"
)

chunks = chunk_text(transcript)

print(f"Total chunks: {len(chunks)}")

print("\nFIRST CHUNK:\n")
print(chunks[0])