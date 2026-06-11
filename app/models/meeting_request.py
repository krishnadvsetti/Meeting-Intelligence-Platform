from pydantic import BaseModel


class MeetingCreate(BaseModel):
    title: str
    transcript: str
    source: str | None = None