from model.business_logic.task_bl import TaskBl
from model.entity.task import Task


class TaskController:
    def save(self,task_id, title, description, deadline, assigned_to,list_id,is_done):
        try:
            task = Task(task_id, title, description, deadline, assigned_to,list_id,is_done)
            task_bl = TaskBl()
            task_bl.save(task)
            return True, 'Task saved successfully'
        except Exception as e:
            return False, f'Error: {str(e)}'

    def edit(self, task_id, title, description, deadline, assigned_to,list_id,is_done):
        try:
            task = Task(task_id, title, description, deadline, assigned_to,list_id,is_done)
            task_bl = TaskBl()
            task_bl.edit(task)
            return True, 'Task edited successfully'
        except Exception as e:
            return False, f'Error: {str(e)}'

    def delete(self, task_id):
        try:
            task_bl = TaskBl()
            task_bl.delete(task_id)
            return True, 'Task deleted successfully'
        except Exception as e:
            return False, f'Error: {str(e)}'

    def find_by_id(self, task_id):
        try:
            task_bl = TaskBl()
            task = task_bl.find_by_id(task_id)
            return True, task
        except Exception as e:
            return False, f'Error: {str(e)}'

    def find_by_title(self, title):
        try:
            task_bl = TaskBl()
            task = task_bl.find_by_title(title)
            return True, task
        except Exception as e:
            return False, f'Error: {str(e)}'

    def max_task_id(self):
        try:
            task_bl = TaskBl()
            max_id = task_bl.max_task_id()
            return True, max_id
        except Exception as e:
            return False, f'Error: {str(e)}'

    def get_tasks_by_list_id(self, list_id):
        try:
            task_bl = TaskBl()
            tasks = task_bl.get_tasks_by_list_id(list_id)
            return True, tasks
        except Exception as e:
            return False, f'Error: {str(e)}'

