import os
import pickle

class TodoListDa:
    def __init__(self):
        self.file_path = 'todo_list.dat'

    def read_from_file(self):
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, 'rb') as f:
            return pickle.load(f)

    def save(self, todo_list):
        with open(self.file_path, "wb") as f:
            pickle.dump(todo_list, f)

    def send(self, list_id, date, employee_username):
        pass