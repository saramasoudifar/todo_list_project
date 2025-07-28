import re
from datetime import datetime


class Validation:
    def user_validator(self, user):
        try:
            re.match(r'^[a-zA-Z0-9_]{8,15}$',user.username)
            re.match(r'^[a-zA-Z0-9@#$!%&]{3,30}$', user.password)
        except:
            raise ValueError('Invalid username or password')

    def task_validator(self, task):
        try:
            re.match(r'^[a-zA-Z0-9_@.,:]{3,200}$',task)

        except:
            raise ValueError('task should be in english,only allowed to use (a-zA-Z0-9_@.,:) and 3 to 200 character long')


    def date_validator(self, date):
        try:
          datetime.strptime(date, '%Y-%m-%d')

        except:
            raise ValueError('deadline should be in YYYY-MM-DD format')

# todo:bayad username pass ba database check beshe
#todo:nmidonm chejori role ro inja ja bedam
#todo:mikham age tarikh eshtebah zad qabul nakone
