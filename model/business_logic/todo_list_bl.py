from model.data_access.todo_list_da import TodoListDa
from model.entity.todo import TodoList
from datetime import datetime

class TodoListBl:
    def __init__(self):
        self.todo_da = TodoListDa()

    def save(self, list_id, date, employee_username):
        todo_list = TodoList(list_id, date, employee_username)
        if not todo_list.date < datetime.now():
            self.todo_da.save(todo_list)
        else:
            raise ValueError('date should be in present or future')

    def edit(self, todo_list: TodoList):
        self.todo_da.edit(todo_list)

    def delete(self, list_id):
        self.todo_da.delete(list_id)

    def get_tasks_for_employee(self, employee_username):
        todo_lists = self.todo_da.read_from_file()
        if not todo_lists:
            return []
        tasks = []
        for todo_list in todo_lists:
            tasks.extend(todo_list.get_tasks_for_user(employee_username))
        return tasks
