import sqlite3


class TodoListRepository:
    def connect(self):
        self.connection = sqlite3.connect('todolist_db.sqlite')
        self.cursor = self.connection.cursor()

    def disconnect(self,commit=False):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def save(self,todolist):
        self.connect()
        self.cursor.execute('INSERT INTO todolist(list_id,date,owner_username) values (?,?,?)',
                            [todolist.list_id,todolist.date,todolist.owner_username])
        self.disconnect(commit=True)

    def delete(self,list_id):
        self.connect()
        self.cursor.execute('DELETE FROM todolist WHERE list_id=?',[list_id])
        self.disconnect(commit=True)

    def find_by_username(self,owner_username):
        self.connect()
        self.cursor.execute('SELECT * FROM todolist WHERE owner_username=?',[owner_username])
        todolist = self.cursor.fetchone()
        self.disconnect()
        return todolist

    def find_by_id(self,list_id):
        self.connect()
        self.cursor.execute('SELECT * FROM todolist WHERE list_id=?',[list_id])
        todolist = self.cursor.fetchone()
        self.disconnect()
        return todolist

    def todolist_id_by_username(self,owner_username):
        self.connect()
        self.cursor.execute('SELECT list_id from todolist where owner_username = ?',[owner_username])
        list_id = [row[0] for row in self.cursor.fetchall()]
        self.disconnect()
        return list_id

    def add_task_to_list(self, list_id, task):
        self.connect()
        self.cursor.execute("INSERT INTO task (task_id, title, description, deadline, is_done, assigned_to, list_id) values (?,?,?,?,?,?,?)",
                            [task.task_id,task.title,task.description,task.deadline,int(task.is_done),task.assigned_to,list_id])
        self.disconnect(commit=True)


    def remove_task_from_list(self, list_id, task_id):
        self.connect()
        self.cursor.execute('DELETE FROM task WHERE task_id = ? and list_id=?',[task_id,list_id])
        self.disconnect(commit=True)