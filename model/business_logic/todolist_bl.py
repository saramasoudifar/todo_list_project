from model.repository.todolist_repository import TodoListRepository
from datetime import datetime



class TodoListBl:
    def __init__(self):
        self.repository = TodoListRepository()

    def save(self, todolist):
        if datetime.now().year + 1 >todolist.date >= datetime.now():
            self.repository.save(todolist)
        else:
            raise ValueError('Deadline should be in the present or future.')

    def delete(self, list_id):
        self.repository.delete(list_id)

    def find_by_username(self, owner_username):
        todo_list = self.repository.find_by_username(owner_username)
        if todo_list:
            return todo_list
        else:
            raise ValueError('Todolist not found.')

    def find_by_id(self, list_id):
        todo_list = self.repository.find_by_id(list_id)
        if todo_list:
            return todo_list
        else:
            raise ValueError('Todolist not found.')

    def todolist_id_by_username(self, owner_username):
        list_id = self.repository.todolist_id_by_username(owner_username)
        if list_id:
            return list_id
        else:
            return None

    def add_task_to_list(self, list_id, task):
        self.repository.add_task_to_list(list_id, task)

    def remove_task_from_list(self, list_id, task_id):
        self.repository.remove_task_from_list(list_id, task_id)
