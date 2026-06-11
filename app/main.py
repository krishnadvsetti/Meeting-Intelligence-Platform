from fastapi import FastAPI

app = FastAPI(
    title="Meeting Intelligence Platform",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "status": "running",
        "project": "Meeting Intelligence Platform"
    }