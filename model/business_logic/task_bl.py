from model.data_access.task_da import TaskDA
from model.entity.task import Task
from datetime import datetime

class TaskBl:
    def save(self,  id, description, deadline):
        task = Task(id , description, deadline)
        if not task.deadline < datetime.now():
            task_da = TaskDA()
            task_da.save(task)
        else:
            raise ValueError('deadline should be in present or future')

    def edit(self, task):
        task_da = TaskDA()
        task_da.edit(task)

    def delete(self, id):
        task_da = TaskDA()
        task_da.delete(id)

    def add(self, id):
        task_da = TaskDA()
        task_da.add(id)
