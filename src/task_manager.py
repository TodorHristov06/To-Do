import json
import os
from models import Task

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
os.makedirs(DATA_DIR, exist_ok=True)

class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.next_id = 1

    def add_task(self, task: Task):
        self.tasks[task.id] = task
        self.next_id = max(self.next_id, task.id + 1)

    def create_task(self, title):
        task = Task(id=self.next_id, title=title)
        self.add_task(task)
        return task

    def remove_task(self, task_id: int):
        if task_id in self.tasks:
            del self.tasks[task_id]

    def mark_task_done(self, task_id: int):
        if task_id in self.tasks:
            self.tasks[task_id].mark_done()

    def get_all_tasks(self):
        return list(self.tasks.values())

    def get_pending_tasks(self):
        return [task for task in self.tasks.values() if not task.completed]

    def save_to_file(self, filename="tasks.json"):
        filepath = os.path.join(DATA_DIR, filename)
        data = [task.to_dict() for task in self.tasks.values()]
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"💾 Saved {len(data)} tasks in {filepath}")

    def load_from_file(self, filename="tasks.json"):
        filepath = os.path.join(DATA_DIR, filename)

        if not os.path.exists(filepath):
            print("⚠️ tasks.json not found — creating new file.")
            self.save_to_file(filename)
            return

        if os.path.getsize(filepath) == 0:
            print("⚠️ tasks.json is empty — no tasks to load.")
            return

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.tasks = {d["id"]: Task.from_dict(d) for d in data}
            self.next_id = max(self.tasks.keys(), default=0) + 1
            print(f"📂 Loaded {len(self.tasks)} tasks from {filepath}")
        except json.JSONDecodeError:
            print("❌ tasks.json is corrupted. Creating new empty file...")
            self.tasks = {}
            self.save_to_file(filename)
