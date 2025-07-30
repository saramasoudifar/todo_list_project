from model.data_access.todo_list_da import TodoListDa
from model.entity.todo import TodoList
from datetime import datetime

class TodoListBl:
    def save(self, list_id, date, employee_username):
        todo_list = TodoList(list_id, date, employee_username)
        if not todo_list.date < datetime.now():
            todo_da = TodoListDa()
            todo_da.save(todo_list)
        else:
            raise ValueError('date should be in present or future')


    def edit(self, list_id, date, employee_username):
        todo_da = TodoListDa()
        todo_da.edit(list_id, date, employee_username)


    def delete(self, list_id):
        todo_da = TodoListDa()
        todo_da.delete(list_id)


    def send(self, list_id, date, employee_username):
        todo_da = TodoListDa()
        todo_da.send(list_id, date, employee_username)


    def update(self, list_id, date, employee_username):
        todo_da = TodoListDa()
        todo_da.update(list_id, date, employee_username)