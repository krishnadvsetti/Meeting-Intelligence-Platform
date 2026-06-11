from fastapi import APIRouter

from app.models.transcript_request import TranscriptRequest
from app.services.action_item_service import (
    extract_action_items
)

router = APIRouter()


@router.post("/action-items")
def get_action_items(
    request: TranscriptRequest
):

    items = extract_action_items(
        request.transcript
    )

    return {
        "action_items": items
    }