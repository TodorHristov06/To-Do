class Task:
    def __init__(self, id, title, completed=False, due_date=None, priority=None,category=None):
        self.id = id
        self.title = title
        self.completed = completed
        self.due_date = due_date
        self.priority = priority
        self.category = category

    def mark_done(self):
        self.completed = True
    
    def to_dict(self):
        return (
            {
                "id": self.id,
                "title": self.title,
                "completed": self.completed,
                "due_date": self.due_date,
                "priority": self.priority,
                "category": self.category,
            }
        )
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            title=data["title"],
            completed=data.get("completed", False),
            due_date=data.get("due_date"),
            priority=data.get("priority"),
            category=data.get("category"),
        )
    
    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f"[{self.id}] {self.title} - {status}"