from model.business_logic.task_bl import TaskBl



class TaskController:
    def save(self, id, description, deadline):
        try:
            task_bl = TaskBl()
            task_bl.save(id, description, deadline)
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

    def delete(self, id):
        try:
            task_bl = TaskBl()
            task_bl.delete(id)
            return 'Task deleted successfully'
        except Exception as e:
            return f'Error : {str(e)}'

    def add(self, id):
        try:
            task_bl = TaskBl()
            task_bl.add(id)
            return 'Task deleted successfully'
        except Exception as e:
            return f'Error : {str(e)}'
