from model.business_logic.task_bl import TaskBl

class TaskController:
    def save(self, task_id, title, description, deadline, assigned_to):
        try:
            task_bl = TaskBl()
            task_bl.save(task_id, title, description, deadline, assigned_to)
            return True, 'Task saved successfully'
        except Exception as e:
            return False, f'Error: {str(e)}'

    def edit(self, task):
        try:
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

    def add(self, task_id, title, description, deadline, assigned_to):
        try:
            task_bl = TaskBl()
            task_bl.add(task_id, title, description, deadline, assigned_to)
            return True, 'Task added successfully'
        except Exception as e:
            return False, f'Error: {str(e)}'
