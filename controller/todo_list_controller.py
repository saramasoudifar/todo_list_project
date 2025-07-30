from model.entity.todo import TodoList
from model.business_logic.todo_list_bl import TodoListBl

class TodoListController:

    def save(self, list_id, date, employee_username):
        try:
            todo_list = TodoList(list_id, date, employee_username)
            todo_bl = TodoListBl()
            todo_bl.save(list_id, date, employee_username)
            return ' Saved successfully!'
        except Exception as e:
            return f'Error: {str(e)}'

    def edit(self,  list_id, date, employee_username):
        try:
            todo_list = TodoList(list_id, date, employee_username)
            todo_bl = TodoListBl()
            todo_bl.edit(list_id, date, employee_username)
            return ' Todo list edited successfully!'
        except Exception as e:
            return f'Error: {str(e)}'

    def delete(self, list_id):
        try:
            todo_bl = TodoListBl()
            todo_bl.delete(list_id)
            return ' Todo list deleted successfully!'
        except Exception as e:
            return f'Error: {str(e)}'

    def send(self,list_id, date, employee_username):
        try:
            todo_list = TodoList(list_id, date, employee_username)
            todo_bl = TodoListBl()
            todo_bl.send(list_id, date, employee_username)
            return ' Todo list has been sent to {todo_list.employee_username}!'
        except Exception as e:
            return f'Error: {str(e)}'

    def update(self,list_id, date, employee_username):
        try:
            todo_list = TodoList(list_id, date, employee_username)
            todo_bl = TodoListBl()
            todo_bl.update(list_id, date, employee_username)
            return ' Todo list updated!}!'
        except Exception as e:
            return f'Error: {str(e)}'