from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.meeting_service import get_meeting_by_id
from app.rag.meeting_rag import ask_meeting_question

router = APIRouter()


class QuestionRequest(BaseModel):
    question: str


@router.post("/ask/{meeting_id}")
def ask_question(
    meeting_id: int,
    request: QuestionRequest,
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

    answer = ask_meeting_question(
        meeting.transcript,
        request.question
    )

    return {
        "meeting_id": meeting.id,
        "question": request.question,
        "answer": answer
    }