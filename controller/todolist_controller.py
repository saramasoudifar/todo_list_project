from model.business_logic.todolist_bl import TodoListBl
from model.entity.todolist import TodoList



class TodoListController:
    def save(self, list_id ,date , owner_username):
        try:
            todolist = TodoList(list_id ,date , owner_username)
            todolist_bl = TodoListBl()
            todolist_bl.save(todolist)
            return True , f'Todolist saved successfully'
        except Exception as e:
            return False , f'Error : {e}'

    def delete(self, list_id):
        try:
            todolist_bl = TodoListBl()
            todolist_bl.delete(list_id)
            return True , f'Todolist deleted successfully'
        except Exception as e:
            return False , f'Error : {e}'

    def find_by_username(self, owner_username):
        try:
            todolist_bl = TodoListBl()
            todolist = todolist_bl.find_by_username(owner_username)
            if todolist:
                return True ,todolist
            else:
                return False, "Todolist not found"
        except Exception as e:
            return False , f'Error : {e}'

    def find_by_id(self, list_id):
        try:
            todolist_bl = TodoListBl()
            todolist = todolist_bl.find_by_id(list_id)
            if todolist:
                return True ,todolist
            else:
                return False, "Todolist not found"
        except Exception as e:
            return False , f'Error : {e}'

    def todolist_id_by_username(self, owner_username):
        try:
            todolist_bl = TodoListBl()
            list_id = todolist_bl.todolist_id_by_username(owner_username)
            if list_id:
                return True ,list_id
            else:
                return False , None
        except Exception as e:
            return False , f'Error : {e}'

    def add_task_to_list(self, list_id, task):
        try:
            todolist_bl = TodoListBl()
            todolist_bl.add_task_to_list(list_id, task)
            return True , f'Task added to TodoList successfully'
        except Exception as e:
            return False , f'Error : {e}'

    def remove_task_from_list(self, list_id, task_id):
        try:
            todolist_bl = TodoListBl()
            todolist_bl.remove_task_from_list(list_id, task_id)
            return True , f'Task removed from TodoList successfully'
        except Exception as e:
            return False , f'Error : {e}'


