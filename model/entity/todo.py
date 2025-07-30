from model.tools.validation import *


class TodoList:
    def __init__(self, list_id, date, employee_username):
        self.list_id = list_id
        self.date = date
        self.employee_username = employee_username
        self.tasks = []


    def __repr__(self):
        return f'todo list number {self.list_id}, date: {self.date}, employee : {self.employee_username}'


    def add_task(self,task):
        self.tasks.append(task)


    @property
    def list_id(self):
        return self._list_id

    @list_id.setter
    def list_id(self, value):
        self._list_id = value


    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        date_deadline_validator(value)
        self._date = value


    @property
    def employee_username(self):
        return self._employee_username

    @employee_username.setter
    def employee_username(self, value):
        todo_list_validator(value)
        self._employee_username = value




