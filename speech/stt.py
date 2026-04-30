import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def transcribe(file_path: str):
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    with open(file_path, "rb") as audio:
        transcript = client.audio.transcriptions.create(
            model="whisper-large-v3",
            file=(file_path, audio.read())
        )
    return transcript.text