import sqlite3


class UserRepository:
    def connect(self):
        self.connection = sqlite3.connect('todolist_db.sqlite')
        self.cursor = self.connection.cursor()

    def disconnect(self,commit=False):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def save(self, user):
        self.connect()
        self.cursor.execute('INSERT INTO user (code,name,family,username,password,role) values (%s,%s,%s,%s,%s,%s)',
                       [user.code, user.name, user.family, user.username, user.password, user.role])
        self.disconnect(commit=True)

    def edit(self, user):
        self.connect()
        self.cursor.execute('update user set name=?, family =? ,username=?,password=?,role=? where code = ?',
                       [user.code, user.name, user.family, user.username, user.password, user.role])
        self.disconnect(commit=True)

    def delete(self, code):
        self.connect()
        self.cursor.execute('delete from user where code = ?', [code])
        self.disconnect(commit=True)

    def find_all(self):
        self.connect()
        self.cursor.execute('select * from user')
        user_list = self.cursor.fetchall()
        self.disconnect()
        return user_list

    def find_by_username(self, username):
        self.connect()
        self.cursor.execute('select * from user where username = ?',
                       [username])
        user = self.cursor.fetchone()
        self.disconnect()
        return user


    def find_by_username_password_role(self, username, password,role):
        self.connect()
        self.cursor.execute('select * from user where username = ? and password = ? and role = ?',
                            [username, password,role])
        user =  self.cursor.fetchone()
        self.disconnect()
        return user

    def username_list(self):
        self.connect()
        self.cursor.execute('SELECT username FROM user')
        users = [row[0] for row in self.cursor.fetchall()]
        self.disconnect()
        return users

    def employee_username_list(self):
        self.connect()
        self.cursor.execute('SELECT username FROM user WHERE role = "employee"')
        users = [row[0] for row in self.cursor.fetchall()]
        self.disconnect()
        return users

