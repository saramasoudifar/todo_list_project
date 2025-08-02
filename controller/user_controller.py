from model.entity.user import User
from model.business_logic.user_bl import UserBl


class UserController:
    def save(self, code, name, family, username, password, role):
        try:
            user = User(code, name, family, username, password, role)
            user_bl = UserBl()
            user_bl.save(user)
        except Exception as e:
            raise ValueError(f'Error saving user {code}: {e}')

    def edit(self, code, name, family, username, password, role):
        try:
            user = User(code, name, family, username, password, role)
            user_bl = UserBl()
            user_bl.edit(user)
        except Exception as e:
            raise ValueError(f'Error editing user {code}: {e}')

    def delete(self, code):
        try:
            user_bl = UserBl()
            user_bl.edit(code)
        except Exception as e:
            raise ValueError(f'Error deleting user {code}: {e}')

    def find_all(self):
        try:
            user_bl = UserBl()
            user_bl.find_all()
        except Exception as e:
            raise ValueError(f'Error : {e}')

    def find_by_username(self, username):
        try:
            user_bl = UserBl()
            user_bl.find_by_username(username)
        except Exception as e:
            raise ValueError(f'Error finding user {username}: {e}')
