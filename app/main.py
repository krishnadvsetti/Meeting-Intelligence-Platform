from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.rag import router as rag_router
from app.api.summary import router as summary_router
from app.api.action_items import router as action_router
from app.api.meetings import router as meetings_router
from app.api.audio import (router as audio_router)
from app.api.agent import (
    router as agent_router
)


app = FastAPI(
    title="Meeting Intelligence Platform"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API routes
app.include_router(rag_router)
app.include_router(summary_router)
app.include_router(action_router)
app.include_router(meetings_router)
app.include_router(audio_router)
app.include_router(agent_router)



@app.get("/")
def root():
    return {
        "message": "Meeting Intelligence Platform"
    }