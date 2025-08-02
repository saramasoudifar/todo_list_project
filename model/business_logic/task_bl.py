from model.repository.task_repository import TaskRepository
from datetime import datetime


class TaskBl:
    def save(self, task):
        if task.deadline >= datetime.now():
            task_rep = TaskRepository()
            task_rep.save(task)
        else:
            raise ValueError('Deadline should be in the present or future.')

    def edit(self, task):
        task_rep = TaskRepository()
        task_rep.edit(task)

    def delete(self, task_id):
        task_rep = TaskRepository()
        task_rep.delete(task_id)

    def add(self, task):
        pass

    def get_tasks_by_employee(self, username):
        task_da = TaskDA()
        return task_da.get_tasks_by_employee(username)

#todo:akhari