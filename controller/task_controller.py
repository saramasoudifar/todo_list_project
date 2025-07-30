from model.business_logic.task_bl import TaskBl



class TaskController:
    def save(self, task_id, description, deadline):
        try:
            task_bl = TaskBl()
            task_bl.save(task_id, description, deadline)
            return 'Task saved successfully'
        except Exception as e:
            return f'Error : {str(e)}'

    def edit(self, task):
        try:
            task_bl = TaskBl()
            task_bl.edit(task)
            return 'Task edited successfully'
        except Exception as e:
            return f'Error : {str(e)}'

    def delete(self, task_id):
        try:
            task_bl = TaskBl()
            task_bl.delete(task_id)
            return 'Task deleted successfully'
        except Exception as e:
            return f'Error : {str(e)}'

    def add(self, task_id):
        try:
            task_bl = TaskBl()
            task_bl.add(task_id)
            return 'Task deleted successfully'
        except Exception as e:
            return f'Error : {str(e)}'
