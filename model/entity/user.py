from model.tools.validation import Validation

class User:
    def __init__(self,name,family,user,password,role):
        self.name = name
        self.family = family
        self.user = user
        self.password = password
        self.role = role

    def validate(self):
        validator = Validation()
        return validator.user_validator(self)

    def enter(self):
        pass

    def exit(x):
        pass