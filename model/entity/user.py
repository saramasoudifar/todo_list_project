from model.tools.validation import *

class User:
    def __init__(self,name,family,username,password,role):
        self.name = name
        self.family = family
        self.username = username
        self.password = password
        self.role = role


    def __repr__(self):
        return f'the user {self.name} {self.family}.role: {self.role}'



    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        user_validator(value)
        self._name = value


    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, value):
        user_validator(value)
        self._family = value


    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        user_validator(value)
        self._username = value


    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        user_validator(value)
        self._password = value


    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        user_validator(value)
        self._role = value


