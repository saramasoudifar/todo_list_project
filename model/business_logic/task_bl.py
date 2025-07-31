from model.data_access.task_da import TaskDA
from model.entity.task import Task
from datetime import datetime

class TaskBl:
    def save(self, task_id, title, description, deadline, assigned_to):
        task = Task(task_id, title, description, deadline, assigned_to)
        if task.deadline >= datetime.now():
            task_da = TaskDA()
            task_da.add(task_id, title, description, deadline, assigned_to)
        else:
            raise ValueError('Deadline should be in the present or future.')

    def edit(self, task):
        task_da = TaskDA()
        task_da.edit(task.id, task)

    def delete(self, task_id):
        task_da = TaskDA()
        task_da.delete(task_id)

    def add(self, task_id, title, description, deadline, assigned_to):
        task_da = TaskDA()
        task_da.add(task_id, title, description, deadline, assigned_to)

    def get_tasks_by_employee(self, username):
        task_da = TaskDA()
        return task_da.get_tasks_by_employee(username)
