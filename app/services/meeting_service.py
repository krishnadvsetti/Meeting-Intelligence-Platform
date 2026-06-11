from sqlalchemy.orm import Session
from app.models.meeting import Meeting


def get_meeting_by_id(
    meeting_id: int,
    db: Session
):
    return (
        db.query(Meeting)
        .filter(Meeting.id == meeting_id)
        .first()
    )