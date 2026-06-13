from fastapi import APIRouter
from pydantic import BaseModel

from app.agents.meeting_agent import run_agent

router = APIRouter()


class AgentRequest(BaseModel):
    query: str


@router.post("/agent")
def chat_with_agent(
    request: AgentRequest
):

    response = run_agent(
        request.query
    )

    return {
        "response": response
    }