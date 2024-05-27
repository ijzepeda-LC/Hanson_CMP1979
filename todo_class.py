class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if task:
            self.tasks.append(task)
            return "Task added."
        else:
            return "Task cannot be empty."

    def view_tasks(self):
        return self.tasks

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            return f"Removed task: {removed_task}"
        else:
            return "Invalid index."

    def clear_tasks(self):
        self.tasks = []
        return "All tasks cleared."