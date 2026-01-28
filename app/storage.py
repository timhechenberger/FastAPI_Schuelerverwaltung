import json
from pathlib import Path

DATA_PATH = Path("/data/datensatz.json")

def load_students():
    if not DATA_PATH.exists():
        return []
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_students(students):
    DATA_PATH.parent.mkdir(exist_ok=True)
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(students, f, indent=4, ensure_ascii=False)
