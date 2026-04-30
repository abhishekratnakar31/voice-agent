# tools.py

tasks = []

def add_task(task: str):
    tasks.append(task)
    return {"reply": f"I have added {task} to your to-do list."}

def list_tasks():
    if not tasks:
        return {"reply": "Your to-do list is currently empty."}
    return {"reply": "Here are your tasks: " + ", ".join(tasks)}

def delete_task(task: str):
    for t in tasks:
        if task.lower() in t.lower() or t.lower() in task.lower():
            tasks.remove(t)
            return {"reply": f"I have deleted the task: {t}"}
    return {"reply": f"Sorry, I couldn't find a task matching {task}."}

def update_task(old_task: str, new_task: str):
    for i, t in enumerate(tasks):
        if old_task.lower() in t.lower() or t.lower() in old_task.lower():
            tasks[i] = new_task
            return {"reply": f"I updated the task to: {new_task}"}
    return {"reply": f"Sorry, I couldn't find the task {old_task} to update."}