# memory.py

import json

FILE = "memory.json"

def load_memory():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_memory_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f)

def add_memory(info: str):
    memory = load_memory()
    memory.append(info)
    save_memory_data(memory)
    return {"message": f"Stored memory: {info}"}

def get_all_memory():
    return {"memory": load_memory()}

def should_store(text: str):
    keywords = ["exam", "meeting", "birthday", "deadline", "important"]
    return any(word in text.lower() for word in keywords)

def add_memory_if_important(text: str):
    if should_store(text):
        return add_memory(text)
    return {"message": "Not important enough to store"}