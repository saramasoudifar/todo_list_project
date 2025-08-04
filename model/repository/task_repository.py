import sqlite3


class TaskRepository():
    def connect(self):
        self.connection = sqlite3.connect('todolist_db.sqlite')
        self.cursor = self.connection.cursor()

    def disconnect(self, commit=False):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def save(self, task):
        self.connect()
        self.cursor.execute(
            'INSERT INTO tasks (task_id, title, description, deadline, assigned_to,list_id,task.is_done) values (%s,%s,%s,%s,%s,%s,%s)',
            [task.task_id, task.title, task.description, task.deadline, task.assigned_to, task.list_id, int(task.is_done)])
        self.disconnect(commit=True)

    def edit(self, task):
        self.connect()
        self.cursor.execute(
            'update user set title = ?, description = ?, deadline = ?, assigned_to = ?,list_id=? ,is_done =? where task_id = ?',
            [task.task_id, task.title, task.description, task.deadline, task.assigned_to, int(task.is_done)])
        self.disconnect(commit=True)

    def delete(self, task_id):
        self.connect()
        self.cursor.execute('delete from tasks where task_id = ?', [task_id])
        self.disconnect(commit=True)

    def find_by_id(self, task_id):
        self.connect()
        self.cursor.execute('select * from tasks where task_id = ?', [task_id])
        task = self.cursor.fetchone()
        self.disconnect()
        return task

    def find_by_title(self, title):
        self.connect()
        self.cursor.execute('select * from tasks where title = ?', [title])
        task = self.cursor.fetchall()
        self.disconnect()
        return task

    def max_task_id(self):
        self.connect()
        self.cursor.execute('select max(task_id) from tasks')
        max_id = self.cursor.fetchone()
        self.disconnect()
        return max_id[0] if max_id[0] is not None else 0

    def get_tasks_by_list_id(self, list_id):
        self.connect()
        self.cursor.execute('SELECT * FROM task WHERE list_id = ?', [list_id])
        tasks = self.cursor.fetchall()
        self.disconnect()
        return tasks
