class TaskManager:
    def __init__(self):
        self.display_tasks = False

    def toggle(self):
        self.display_tasks = not self.display_tasks

    def display(self, pm):
        if self.display_tasks:
            return f'Task Manager: {", ".join(pm.running_processes)}'
        else:
            return ''