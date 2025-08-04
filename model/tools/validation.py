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

    if not (type(user.role) == str and re.match(r'^(ceo|employee)$', user.role)):
        raise ValueError('Invalid role')



def task_validator(task):
    if not (type(task.title) == str and re.match(r'^[a-zA-Z\s]{3,30}$', task.title)):
        raise ValueError('Invalid title')

    if not (type(task.description) == str and re.match(r'^[a-zA-Z0-9_@.,:]{3,200}$', task.description)):
        raise ValueError(
            'task should be in english,only allowed to use (a-zA-Z0-9_@.,:) and 3 to 200 character long')

def date_deadline_validator(date):
    if not datetime.strptime(date, '%Y-%m-%d').date():
        raise ValueError('Invalid date')


def todolist_validator(todolist):
    if not (type(todolist.owner_username)== str and re.match(r'^[a-zA-Z\s]{3,30}$', todolist.owner_username)):
        raise ValueError('Invalid username')



