import sqlite3

connection = sqlite3.connect('todolist_db.sqlite')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS user (
    code integer PRIMARY KEY autoincrement,
    name text NOT NULL,
    family text NOT NULL,
    username TEXT not null unique,
    password text NOT NULL,
    role TEXT not null
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS todolist (
    list_id INTEGER PRIMARY KEY AUTOINCREMENT,
    date date not null,
    owner_username TEXT not null
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS task (
    task_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT not null,
    description TEXT not null,
    deadline date NOT NULL,
    assigned_to TEXT not null,
    list_id INTEGER NOT NULL,
    is_done tinyint default 0
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS todolist_task (
    list_id INTEGER,
    task_id INTEGER,
    PRIMARY KEY (list_id, task_id)
)
''')

connection.commit()
cursor.close()
connection.close()

print(" دیتابیس ساخته شد")
