from fastapi import APIRouter

from app.services.transcript_loader import load_transcript
from app.services.summary_service import generate_summary

router = APIRouter()


@router.post("/summary")
def summarize_meeting():

    transcript = load_transcript(
        "data/transcripts/meeting_001.txt"
    )

    summary = generate_summary(transcript)

    return {
        "summary": summary
    }