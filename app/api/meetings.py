from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.meeting import Meeting
from app.models.meeting_request import MeetingCreate

router = APIRouter()


@router.post("/meetings")
def create_meeting(
    request: MeetingCreate,
    db: Session = Depends(get_db)
):

    meeting = Meeting(
        title=request.title,
        transcript=request.transcript,
        source=request.source
    )

    db.add(meeting)
    db.commit()
    db.refresh(meeting)

    return {
        "id": meeting.id,
        "title": meeting.title
    }


@router.get("/meetings")
def list_meetings(
    db: Session = Depends(get_db)
):

    meetings = db.query(Meeting).all()

    return [
        {
            "id": meeting.id,
            "title": meeting.title,
            "source": meeting.source
        }
        for meeting in meetings
    ]