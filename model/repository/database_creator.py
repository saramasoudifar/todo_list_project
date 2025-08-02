import sqlite3


def create_database():
    connection = sqlite3.connect('todolist_db.sqlite')
    cursor = connection.cursor()

    cursor.execute("""
    create table if not exists user (
        code integer primary key autoincrement,
        name text not null,
        family text not null,
        username text not null unique,
        password text not null,
        role text not null
        )""")

    cursor.execute("""
    create table if not exists tasks (
        task_id integer primary key autoincrement,
        title text not null,
        description text not null, 
        deadline date not null,
        assigned_to text not null
        )""")

    connection.commit()

    cursor.close()
    connection.close()
