# Voice AI Agent 🎙️🤖

A smart, voice-controlled AI assistant that manages a To-Do list using function calling (tools) and remembers important information over time. 

Built with **FastAPI**, **Groq (Llama-3.3-70B & Whisper-large-v3)**, and a beautiful Vanilla JS/CSS glassmorphism frontend.

---

## ✨ Features
- **🗣️ Voice Interface:** Speak to the agent using your microphone, and it will respond with text-to-speech! 
- **🛠️ Tool-Based To-Do Management:** The AI can intelligently call functions to:
  - `add_task`
  - `list_tasks`
  - `update_task`
  - `delete_task` (Fuzzy and case-insensitive matching)
- **🧠 Memory System:** The agent automatically detects important information (like deadlines, birthdays, or meetings) and commits them to long-term JSON memory so it doesn't forget.
- **⚡ Ultra-Fast Processing:** Uses Groq's insanely fast inference for both Llama 3.3 70B (LLM) and Whisper (Speech-to-Text).

---

## 🚀 Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/abhishekratnakar31/voice-agent.git
cd voice-agent
```

### 2. Create a Virtual Environment (Recommended)
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install fastapi uvicorn groq gtts python-multipart pydantic python-dotenv
```

### 4. Setup Environment Variables
Duplicate the example environment file:
```bash
cp .env.example .env
```
Then, open the `.env` file and add your Groq API key:
```env
GROQ_API_KEY=gsk_your_actual_groq_api_key_here
```

---

## 🎮 How to Run

Start the FastAPI server:
```bash
uvicorn main:app --reload
```
*Note: Ensure you are running this from inside your activated `venv`.*

Once the server is running, open your web browser and go to:
👉 **[http://127.0.0.1:8000/app](http://127.0.0.1:8000/app)**

---

## 🧪 Testing the Agent

Click the Microphone button on the web interface, grant microphone permissions, and try saying:
- *"Add a task to submit my physics assignment."*
- *"What tasks do I have on my to-do list right now?"*
- *"Delete the physics assignment task."*
- *"Remember that my brother's birthday is on October 12th."*

Click the Microphone button again to stop recording. The AI will process your command, execute any necessary backend tools, and read its response out loud to you!
