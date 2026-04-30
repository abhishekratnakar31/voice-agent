# main.py

from fastapi import FastAPI
from tools import add_task, list_tasks, delete_task, update_task
from memory import add_memory, get_all_memory
from agent import run_agent
from fastapi import UploadFile, File
from fastapi.responses import HTMLResponse, FileResponse

from speech.stt import transcribe

from speech.tts import speak

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agent still alive. Surprisingly."}


@app.post("/add")
def add(data: dict):
    return add_task(data["task"])


@app.get("/list")
def list_all():
    return list_tasks()


@app.delete("/delete")
def delete(data: dict):
    return delete_task(data["task"])


@app.put("/update")
def update(data: dict):
    return update_task(data["old"], data["new"])



@app.post("/memory/add")

def add_mem(data: dict):

    return add_memory(data["info"])

@app.get("/memory")

def list_mem():

    return get_all_memory()

@app.post("/chat")

def chat(data: dict):

    return run_agent(data["message"])

@app.post("/voice")
async def voice_chat(file: UploadFile = File(...)):
    # 1. Save audio
    with open("input.wav", "wb") as f:
        f.write(await file.read())

    # 2. STT
    user_text = transcribe("input.wav")
    print("USER:", user_text)

    # 3. Agent
    response = run_agent(user_text)
    print("AGENT RAW:", response)

    # 4. Extract reply
    if isinstance(response, dict):
        reply_text = response.get("reply") or str(response)
    else:
        reply_text = str(response)

    print("FINAL REPLY:", reply_text)

    # 5. TTS
    audio_path = speak(reply_text)

    return {
        "user": user_text,
        "reply": reply_text,
        "audio": audio_path
    }

@app.get("/app")
def get_app():
    with open("index.html", "r") as f:
        return HTMLResponse(content=f.read())

@app.get("/audio")
def get_audio():
    import os
    if os.path.exists("output.mp3"):
        return FileResponse("output.mp3", media_type="audio/mpeg")
    return {"error": "No audio"}