from pathlib import Path


def load_transcript(file_path: str):
    return Path(file_path).read_text(
        encoding="utf-8",
        errors="ignore"
    )