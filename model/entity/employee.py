class Employee:
    def __init__(self, username, full_name):
        self.username = username
        self.full_name = full_name

    def __repr__(self):
        return f"{self.full_name} ({self.username})"