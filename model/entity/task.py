from model.entity.todo import TodoList
from model.tools.validation import *


class Task:
    def __init__(self, id, description, deadline):
        self.id = id
        self.description = description
        self.deadline = deadline
        self.completed = False


    def __repr__(self):
        return f'task number {self.id} , deadline: {self.deadline},status : {self.completed}'


    def to_tuple(self):
        return (self.id, self.description, self.deadline)


    def pin_task_to_list(self,todo_list_id):
       pass


#todo:mikham id ye todo list ro be task bedim ke bere ru un list beshine

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value


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


