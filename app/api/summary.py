from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.meeting_service import get_meeting_by_id
from app.services.summary_service import generate_summary

router = APIRouter()


@router.post("/summary/{meeting_id}")
def summarize_meeting(
    meeting_id: int,
    db: Session = Depends(get_db)
):

    meeting = get_meeting_by_id(
        meeting_id,
        db
    )

    if not meeting:
        raise HTTPException(
            status_code=404,
            detail="Meeting not found"
        )

    summary = generate_summary(
        meeting.transcript
    )

    return {
        "meeting_id": meeting.id,
        "title": meeting.title,
        "summary": summary
    }