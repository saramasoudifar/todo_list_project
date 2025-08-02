from model.tools.validation import *


class Task:
    def __init__(self, task_id, title, description, deadline, assigned_to):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.deadline = deadline
        self.assigned_to = assigned_to
        self.is_done = False

    def __repr__(self):
        return f'task number {self.task_id} ,title :{self.title}, deadline: {self.deadline},status : {self.is_done}'

    def to_tuple(self):
        return (self.task_id, self.description, self.deadline, self.is_done)
#todo

    @property
    def id(self):
        return self._task_id

    @id.setter
    def id(self, value):
        self._task_id = value


    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        task_validator(value)
        self._title = value

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
    def assigned_to(self):
        return self._assigned_to

    @assigned_to.setter
    def assigned_to(self, value):
        self._assigned_to = value


