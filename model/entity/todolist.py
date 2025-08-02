class TodoList:
    def __init__(self):
        self.tasks = []


    def add_task(self,task):
        self.tasks.append(task)

    def get_tasks_for_user(self, user):
        return [task for task in self.tasks if task.assigned_to == user]

    def get_all_tasks(self):
        return self.tasks

    def delete_task_by_id(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]








