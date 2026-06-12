from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.meeting_service import (
    get_meeting_by_id
)
from app.services.action_item_service import (
    extract_action_items
)

router = APIRouter()


@router.post("/action-items/{meeting_id}")
def get_action_items(
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

    items = extract_action_items(
        meeting.transcript
    )

    return {
        "meeting_id": meeting.id,
        "title": meeting.title,
        "action_items": items
    }