import json
import os

TASK_FILE = "db.json"


def save(data:dict):
    try:
        with open(TASK_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except FileExistsError:
        print("Error, file does not exists")


def load():
    try:
        if not os.path.exists(TASK_FILE):
            return []
        with open(TASK_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error, file not found")


def get_task(idx):
    tasks = load()
    for task in tasks:
        if task["id"] == idx:
            return task
    else:
        return None