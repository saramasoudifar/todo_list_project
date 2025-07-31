from model.entity.todo import TodoList
from model.business_logic.todo_list_bl import TodoListBl

class TodoListController:

    def save(self):
        try:
            todo_list = TodoList()
            todo_bl = TodoListBl()
            todo_bl.save(todo_list)
            return 'Saved successfully!'
        except Exception as e:
            return f'Error: {str(e)}'

    def edit(self):
        try:
            todo_list = TodoList()
            todo_bl = TodoListBl()
            todo_bl.edit(todo_list)
            return ' Todo list edited successfully!'
        except Exception as e:
            return f'Error: {str(e)}'

    def delete(self):
        try:
            todo_bl = TodoListBl()
            todo_bl.delete()
            return ' Todo list deleted successfully!'
        except Exception as e:
            return f'Error: {str(e)}'

    def send(self):
        try:
            todo_list = TodoList()
            todo_bl = TodoListBl()
            todo_bl.send(todo_list)
            return ' Todo list has been sent to {todo_list.employee_username}!'
        except Exception as e:
            return f'Error: {str(e)}'

    def update(self):
        try:
            todo_list = TodoList()
            todo_bl = TodoListBl()
            todo_bl.update(todo_list)
            return ' Todo list updated!}!'
        except Exception as e:
            return f'Error: {str(e)}'