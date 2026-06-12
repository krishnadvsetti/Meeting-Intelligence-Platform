from mcp.server.fastmcp import FastMCP

from app.db.session import SessionLocal
from app.models.meeting import Meeting

from app.services.summary_service import (
    generate_summary
)

from app.services.action_item_service import (
    extract_action_items
)

from app.rag.meeting_rag import (
    ask_meeting_question
)

mcp = FastMCP("Meeting Intelligence")


@mcp.tool()
def list_meetings():

    db = SessionLocal()

    try:

        meetings = db.query(Meeting).all()

        return [
            {
                "id": meeting.id,
                "title": meeting.title,
                "source": meeting.source
            }
            for meeting in meetings
        ]

    finally:
        db.close()


@mcp.tool()
def get_meeting(
    meeting_id: int
):

    db = SessionLocal()

    try:

        meeting = (
            db.query(Meeting)
            .filter(Meeting.id == meeting_id)
            .first()
        )

        if not meeting:
            return {
                "error": "Meeting not found"
            }

        return {
            "id": meeting.id,
            "title": meeting.title,
            "transcript": meeting.transcript,
            "source": meeting.source
        }

    finally:
        db.close()


@mcp.tool()
def summarize_meeting(
    meeting_id: int
):

    db = SessionLocal()

    try:

        meeting = (
            db.query(Meeting)
            .filter(Meeting.id == meeting_id)
            .first()
        )

        if not meeting:
            return "Meeting not found"

        return generate_summary(
            meeting.transcript
        )

    finally:
        db.close()


@mcp.tool()
def get_action_items(
    meeting_id: int
):

    db = SessionLocal()

    try:

        meeting = (
            db.query(Meeting)
            .filter(Meeting.id == meeting_id)
            .first()
        )

        if not meeting:
            return "Meeting not found"

        return extract_action_items(
            meeting.transcript
        )

    finally:
        db.close()


@mcp.tool()
def ask_meeting(
    meeting_id: int,
    question: str
):

    db = SessionLocal()

    try:

        meeting = (
            db.query(Meeting)
            .filter(Meeting.id == meeting_id)
            .first()
        )

        if not meeting:
            return "Meeting not found"

        return ask_meeting_question(
            meeting.transcript,
            question
        )

    finally:
        db.close()