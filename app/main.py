from fastapi import FastAPI
from app.api.rag import router as rag_router

app = FastAPI(
    title="Meeting Intelligence Platform"
)

app.include_router(rag_router)


@app.get("/")
def root():
    return {
        "message": "Meeting Intelligence Platform"
    }