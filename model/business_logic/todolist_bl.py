from model.repository.todo_list_da import TodoListDa
from model.entity.todolist import TodoList


class TodoListBl:
    def __init__(self):
        self.todo_da = TodoListDa()

    def save(self, tasks):
        self.todo_da.save(tasks)

    def send(self, todo_list):
        pass

    def update(self, todo_list):
        pass

    def get_tasks_for_employee(self, employee_username):
        todo_lists = self.todo_da.read_from_file()
        if not todo_lists:
            return []
        tasks = []
        for todo_list in todo_lists:
            tasks.extend(todo_list.get_tasks_for_user(employee_username))
        return tasks

#todo:tabe akhar bayad eslah she