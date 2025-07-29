from model.data_access.todo_list_da import TodoListDa
from model.entity.todo import TodoList
from datetime import datetime

class TodoListBl:
    def save(self, id, date, employee_username):
        todo_list = TodoList(id, date, employee_username)
        if not todo_list.date < datetime.now():
            todo_da = TodoListDa()
            todo_da.save(todo_list)
        else:
            raise ValueError('date should be in present or future')


    def edit(self, id, date, employee_username):
        todo_da = TodoListDa()
        todo_da.edit(id, date, employee_username)


    def delete(self, id):
        todo_da = TodoListDa()
        todo_da.delete(id)


    def send(self, id, date, employee_username):
        todo_da = TodoListDa()
        todo_da.send(id, date, employee_username)


    def update(self, id, date, employee_username):
        todo_da = TodoListDa()
        todo_da.update(id, date, employee_username)