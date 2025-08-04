from model.entity.user import User
from model.business_logic.user_bl import UserBl


class UserController:
    def save(self, code, name, family, username, password, role):
        try:
            user = User(code, name, family, username, password, role)
            user_bl = UserBl()
            user_bl.save(user)
            return True, f'user saved successfully'
        except Exception as e:
            raise ValueError(f'Error saving user {code}: {e}')

    def edit(self, code, name, family, username, password, role):
        try:
            user = User(code, name, family, username, password, role)
            user_bl = UserBl()
            user_bl.edit(user)
            return True, f'user edited successfully'
        except Exception as e:
            raise ValueError(f'Error editing user {code}: {e}')

    def delete(self, code):
        try:
            user_bl = UserBl()
            user_bl.edit(code)
            return True, f'user deleted successfully'
        except Exception as e:
            raise ValueError(f'Error deleting user {code}: {e}')

    def find_all(self):
        try:
            user_bl = UserBl()
            user_list = user_bl.find_all()
            return True, user_list
        except Exception as e:
            raise ValueError(f'Error : {e}')

    def find_by_username(self, username):
        try:
            user_bl = UserBl()
            user = user_bl.find_by_username(username)
            return True, user
        except Exception as e:
            raise ValueError(f'Error finding user {username}: {e}')

    def find_by_username_password_role(self, username, password, role):
        try:
            user_bl = UserBl()
            user = user_bl.find_by_username_password_role(username, password, role)
            return True, user
        except Exception as e:
            raise ValueError(f'Error : {e}')

    def username_list(self):
        try:
            user_bl = UserBl()
            user_list = user_bl.username_list()
            return True, user_list
        except Exception as e:
            raise ValueError(f'Error : {e}')

    def employee_username_list(self):
        try:
            user_bl = UserBl()
            user_list = user_bl.employee_username_list()
            return True, user_list
        except Exception as e:
            raise ValueError(f'Error : {e}')

