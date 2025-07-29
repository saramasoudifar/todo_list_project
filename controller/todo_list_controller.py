from model.entity.todo import TodoList
from model.business_logic.todo_list_bl import TodoListBl

class TodoListController:

    def save(self, id, date, employee_username):
        try:
            todo_list = TodoList(id, date, employee_username)
            todo_bl = TodoListBl()
            todo_bl.save(id, date, employee_username)
            return ' Saved successfully!'
        except Exception as e:
            return f'Error: {str(e)}'

    def edit(self,  id, date, employee_username):
        try:
            todo_list = TodoList(id, date, employee_username)
            todo_bl = TodoListBl()
            todo_bl.edit(id, date, employee_username)
            return ' Todo list edited successfully!'
        except Exception as e:
            return f'Error: {str(e)}'

    def delete(self, id):
        try:
            todo_bl = TodoListBl()
            todo_bl.delete(id)
            return ' Todo list deleted successfully!'
        except Exception as e:
            return f'Error: {str(e)}'

    def send(self,id, date, employee_username):
        try:
            todo_list = TodoList(id, date, employee_username)
            todo_bl = TodoListBl()
            todo_bl.send(id, date, employee_username)
            return ' Todo list has been sent to {todo_list.employee_username}!'
        except Exception as e:
            return f'Error: {str(e)}'

    def update(self,id, date, employee_username):
        try:
            todo_list = TodoList(id, date, employee_username)
            todo_bl = TodoListBl()
            todo_bl.update(id, date, employee_username)
            return ' Todo list updated!}!'
        except Exception as e:
            return f'Error: {str(e)}'