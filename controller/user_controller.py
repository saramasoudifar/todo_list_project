from model.entity.user import User
from model.business_logic.user_bl import UserBl


class UserController:
    def save(self, name,family,username,password,role):
        try:
            user = User(name,family,username,password,role)
            user_bl = UserBl()
            user_bl.save(name,family,username,password,role)
            return f'User Saved!\n{user}'
        except Exception as e:
            return f'Error: {str(e)}'

    def find_by_username_pass(self,role,username,password):
        try:
            user_bl = UserBl()
            user_bl.find_by_username_pass(role, username, password)
            return f'User Found!'
        except Exception as e:
            return f'Error: {str(e)}'

    def enter(self, name,family,username,password,role):
        try:
            user_bl = UserBl()
            user_bl.enter(name,family,username,password,role)
            return 'welcome!'
        except Exception as e:
            return f'Error: {str(e)}'