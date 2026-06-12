from faster_whisper import WhisperModel

model = WhisperModel(
    "base",
    device="cpu"
)


def transcribe_audio(
    file_path: str
):

    segments, _ = model.transcribe(
        file_path
    )

    transcript = " ".join(
        segment.text
        for segment in segments
    )

    return transcript