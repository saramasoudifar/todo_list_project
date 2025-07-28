from model.tools.validation import Validation


class Task:
    def __init__(self, id, description, deadline):
        self.id = id
        self.description = description
        self.deadline = deadline
        self.completed = False

    def validate(self):
        validator = Validation()
        return validator.task_validator(self)


    def to_tuple(self):
        return (self.id, self.description, self.deadline)

