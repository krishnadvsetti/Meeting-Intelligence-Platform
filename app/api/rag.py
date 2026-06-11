from fastapi import APIRouter
from pydantic import BaseModel

from app.rag.rag_pipeline import answer_question

router = APIRouter()


class QuestionRequest(BaseModel):
    question: str


@router.post("/ask")
def ask_question(request: QuestionRequest):

    answer = answer_question(
        request.question
    )

    return {
        "question": request.question,
        "answer": answer
    }