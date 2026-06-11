from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Text
from pydantic import BaseModel
class MeetingCreate(BaseModel):
    title: str
    transcript: str
    source: str | None = None




class Base(DeclarativeBase):
    pass


class Meeting(Base):
    __tablename__ = "meetings"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    transcript = Column(Text, nullable=False)
    source = Column(String, nullable=True)
