# agent.py
import os

from dotenv import load_dotenv
from groq import Groq
from tools import add_task, list_tasks, delete_task, update_task
from memory import add_memory_if_important
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

SYSTEM_PROMPT = """
You are a smart voice assistant.

Rules:
- Use tools for task management (add, update, delete, list)
- Store important info in memory
- Respond normally otherwise
"""

def run_agent(user_input: str):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ],
        tools=[
            {
                "type": "function",
                "function": {
                    "name": "add_task",
                    "description": "Add a task",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "task": {"type": "string"}
                        },
                        "required": ["task"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "list_tasks",
                    "description": "List all tasks",
                    "parameters": {"type": "object", "properties": {}}
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "delete_task",
                    "description": "Delete a task",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "task": {"type": "string"}
                        },
                        "required": ["task"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "update_task",
                    "description": "Update a task",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "old_task": {"type": "string"},
                            "new_task": {"type": "string"}
                        },
                        "required": ["old_task", "new_task"]
                    }
                }
            }
        ]
    )

    message = response.choices[0].message

    # 🧠 If tool is called
    if message.tool_calls:
        tool_call = message.tool_calls[0]
        name = tool_call.function.name
        import json
        try:
            args = json.loads(tool_call.function.arguments)
        except Exception:
            args = {}

        if name == "add_task":
            return add_task(**args)
        elif name == "list_tasks":
            return list_tasks()
        elif name == "delete_task":
            return delete_task(**args)
        elif name == "update_task":
            return update_task(**args)

    # 🧠 Normal reply
    reply = message.content

    # store memory
    add_memory_if_important(user_input)

    return {"reply": reply}