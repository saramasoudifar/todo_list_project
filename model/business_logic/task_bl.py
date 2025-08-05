from model.repository.task_repository import TaskRepository
from datetime import datetime


class TaskBl:
    def save(self, task):
        if datetime.now().year + 1 > task.deadline >= datetime.now():
            task_rep = TaskRepository()
            task_rep.save(task)
        else:
            raise ValueError('Deadline should be in the present or near future.')

    def edit(self, task):
        task_rep = TaskRepository()
        task_rep.edit(task)

    def delete(self, task_id):
        task_rep = TaskRepository()
        task_rep.delete(task_id)

    def find_by_id(self, task_id):
        task_rep = TaskRepository()
        task = task_rep.find_by_id(task_id)
        if task:
            return task
        else:
            raise ValueError('Task not found')

    def find_by_title(self, title):
        task_rep = TaskRepository()
        task = task_rep.find_by_title(title)
        if task:
            return task
        else:
            raise ValueError('Task not found')

    def max_task_id(self):
        task_rep = TaskRepository()
        id = task_rep.max_task_id()
        return id

    def get_tasks_by_list_id(self, list_id):
        task_rep = TaskRepository()
        tasks = task_rep.get_tasks_by_list_id(list_id)
        if tasks:
            return tasks
        else:
            raise ValueError('TodoList not found')

    def update_status_only(self, task_id, is_done):
        task_rep = TaskRepository()
        task_rep.update_status_only(task_id, is_done)


