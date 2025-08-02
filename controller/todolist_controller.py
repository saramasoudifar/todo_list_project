from model.business_logic.todolist_bl import TodoListBl

class TodoListController:
    def save(self,tasks):
        try:
            todo_bl = TodoListBl()
            todo_bl.save(tasks)
            return True,'Saved successfully!'
        except Exception as e:
            return False, f'Error: {str(e)}'

    def send(self,todo_list):
        try:
            todo_bl = TodoListBl()
            todo_bl.send(todo_list)
            return True ,' Todo list has been sent to {todo_list.employee_username}!'
        except Exception as e:
            return False ,f'Error: {str(e)}'

    def update(self,todo_list):
        try:
            todo_bl = TodoListBl()
            todo_bl.update(todo_list)
            return True ,' Todo list updated!}!'
        except Exception as e:
            return False ,f'Error: {str(e)}'


        def get_tasks_for_employee(self, employee_username):
            pass