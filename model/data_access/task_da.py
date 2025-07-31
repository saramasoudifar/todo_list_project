import os
import pickle
from model.entity.task import Task


class TaskDA:
    def __init__(self):
        self.file_path = 'task.dat'

    def read_from_file(self):
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, 'rb') as f:
            return pickle.load(f)

    def save(self, task_list):
        file = open(self.file_path, 'wb')
        pickle.dump(task_list, file)
        file.close()


    def add(self,  task_id,title, description, deadline, assigned_to):
        task_list = self.read_from_file()
        task = Task(task_id, title, description, deadline, assigned_to)
        task_list.append(task)
        self.save(task_list)

    def delete(self, task_id):
        task_list = self.read_from_file()
        task_list = [t for t in task_list if t.id != task_id]
        self.save(task_list)

    def edit(self, task_id , updated_task):
        task_list = self.read_from_file()
        for i, t in enumerate(task_list):
            if t.id == task_id:
                task_list[i] = updated_task
                break
        self.save(task_list)

    def get_tasks_by_employee(self, username):
        task_list = self.read_from_file()
        return [t for t in task_list if t.assigned_to == username]
