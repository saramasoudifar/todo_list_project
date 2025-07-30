from model.entity.todo import TodoList
from model.tools.validation import *


class Task:
    def __init__(self, task_id, description, deadline, status):
        self.task_id = task_id
        self.description = description
        self.deadline = deadline
        self.status = status


    def __repr__(self):
        return f'task number {self.task_id} , deadline: {self.deadline},status : {self.status}'


    def to_tuple(self):
        return (self.task_id, self.description, self.deadline, self.status)


    def pin_task_to_list(self,todo_list_id):
       pass


#todo:mikham id ye todo list ro be task bedim ke bere ru un list beshine

    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value


    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        task_validator(value)
        self._description = value


    @property
    def deadline(self):
        return self._deadline

    @deadline.setter
    def deadline(self, value):
        date_deadline_validator(value)
        self._deadline = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


