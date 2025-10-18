from models import Task


class TaskManager:
    def __init__(self):
        self.tasks = {}
    
    def add_task(self, task: Task):
        self.tasks[task.id] = task
    
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

    