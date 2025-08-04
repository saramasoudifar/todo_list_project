from model.entity.task import Task
from model.tools.validation import date_deadline_validator, todolist_validator


class TodoList:
    def __init__(self,list_id ,date , owner_username):
        self.list_id = list_id
        self.date = date
        self.owner_username = owner_username
        self.tasks = []


    def add_task(self,task:Task):
        if task.assigned_to == self.owner_username:
            self.tasks.append(task)
        else:
            raise ValueError("Task assigned to a different user")

    def remove_task_by_id(self, task_id):
        self.tasks = [t for t in self.tasks if t.task_id != task_id]

    def get_all_tasks(self):
        return self.tasks

    def get_completed_tasks(self):
        return [t for t in self.tasks if t.is_done]

    def get_pending_tasks(self):
        return [t for t in self.tasks if not t.is_done]


    @property
    def todolist_id(self):
        return self._todolist_id

    @todolist_id.setter
    def todolist_id(self, value):
        self._todolist_id = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        date_deadline_validator(value)
        self._date = value

    @property
    def owner_username(self):
        return

    @owner_username.setter
    def owner_username(self, value):
        todolist_validator(value)
        self._owner_username = value








