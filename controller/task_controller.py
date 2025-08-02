from model.business_logic.task_bl import TaskBl
from model.entity.task import Task

class TaskController:
    def save(self, task_id, title, description, deadline, assigned_to):
        try:
            task = Task(task_id, title, description, deadline, assigned_to)
            task_bl = TaskBl()
            task_bl.save(task_id, title, description, deadline, assigned_to)
            return True, 'Task saved successfully'
        except Exception as e:
            return False, f'Error: {str(e)}'

    def edit(self, task_id, title, description, deadline, assigned_to):
        try:
            task = Task(task_id, title, description, deadline, assigned_to)
            task_bl = TaskBl()
            task_bl.edit(task_id, title, description, deadline, assigned_to)
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

    def get_tasks_by_employee(self, username):
        pass

    #todo


