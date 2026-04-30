# speech/tts.py

from gtts import gTTS
import os

def speak(text: str):
    file_path = "output.mp3"
    tts = gTTS(text=text)
    tts.save(file_path)
    return file_path