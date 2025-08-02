import sqlite3


class UserRepository:
    def save(self, user):
        connection = sqlite3.connect('todolist_db.sqlite')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO user (code,name,family,username,password,role) values (%s,%s,%s,%s,%s,%s)',
                       [user.code, user.name, user.family, user.username, user.password, user.role])

        connection.commit()
        cursor.close()
        connection.close()

    def edit(self, user):
        connection = sqlite3.connect('todolist_db.sqlite')
        cursor = connection.cursor()
        cursor.execute('update user set name=?, family =? ,username=?,password=?,role=? where code = ?',
                       [user.code, user.name, user.family, user.username, user.password, user.role])

        connection.commit()
        cursor.close()
        connection.close()

    def delete(self, code):
        connection = sqlite3.connect('todolist_db.sqlite')
        cursor = connection.cursor()
        cursor.execute('delete from user where code = ?', [code])
        connection.commit()
        cursor.close()
        connection.close()

    def find_all(self):
        connection = sqlite3.connect('todolist_db.sqlite')
        cursor = connection.cursor()
        cursor.execute('select * from user')
        cursor.close()
        connection.close()

    def find_by_username(self, username):
        connection = sqlite3.connect('todolist_db.sqlite')
        cursor = connection.cursor()
        cursor.execute('select * from user where username = ?',
                       [username])

        cursor.close()
        connection.close()
