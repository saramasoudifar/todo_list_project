import re
from datetime import datetime


def user_validator(user):
    if not (type(user.name) == str and re.match(r'^[a-zA-Z\s]{3,30}$', user.name)):
        raise ValueError('Invalid name')

    if not (type(user.family) == str and re.match(r'^[a-zA-Z\s]{3,30}$', user.family)):
        raise ValueError('Invalid family')

    if not (type(user.username) == str and re.match(r'^[a-zA-Z0-9_]{8,15}$', user.username)):
        raise ValueError('Invalid username')

    if not (type(user.password) == str and re.match(r'^[a-zA-Z0-9@#$!%&]{3,30}$', user.password)):
        raise ValueError('Invalid password')


def task_validator(task):
    if not (type(task.description) == str and re.match(r'^[a-zA-Z0-9_@.,:]{3,200}$', task.description)):
        raise ValueError(
            'task should be in english,only allowed to use (a-zA-Z0-9_@.,:) and 3 to 200 character long')


def todo_list_validator(todo_list):
    if not (type(todo_list.employee_username) == str and re.match(r'^[a-zA-Z0-9_]{8,15}$',
                                                                  todo_list.employee_username)):
        raise ValueError('Invalid employee username')


def date_deadline_validator(date):
    if not datetime.strptime(date, '%Y-%m-%d').date():
        raise ValueError('Invalid date')


# todo:bayad username pass ba database check beshe
# todo:nmidonm chejori role ro inja ja bedam
# todo:mikham age tarikh eshtebah zad qabul nakone
# todo:id systemi bashe dasti nabashe
# todo:tarikh part qabul nakone
