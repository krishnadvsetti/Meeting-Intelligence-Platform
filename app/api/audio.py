from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends
)

from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.meeting import Meeting
from app.services.transcription_service import (
    transcribe_audio
)

router = APIRouter()


@router.post("/upload-audio")
async def upload_audio(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        buffer.write(
            await file.read()
        )

    transcript = transcribe_audio(
        file_path
    )

    meeting = Meeting(
        title=file.filename,
        transcript=transcript,
        source="audio"
    )

    db.add(meeting)
    db.commit()
    db.refresh(meeting)

    return {
    "meeting_id": meeting.id,
    "title": meeting.title,
    "source": meeting.source,
    "transcript": transcript
}