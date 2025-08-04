from model.repository.user_repository import UserRepository


class UserBl:
    def save(self, user):
        if user.username == f'{user.name}_{user.family}':
            user_rep = UserRepository()
            user_rep.save(user)
        else:
            raise ValueError('Invalid username')

    def edit(self, user):
        if user.username == f'{user.name}_{user.family}':
            user_rep = UserRepository()
            user_rep.save(user)
        else:
            raise ValueError('Invalid username')


    def delete(self):
        user_rep = UserRepository()
        user_rep.delete(self)

    def find_all(self):
        user_rep = UserRepository()
        user_list = user_rep.find_all()
        return user_list

    def find_by_username(self, username):
        user_rep = UserRepository()
        user = user_rep.find_by_username(username)
        if user:
            return user
        else:
            raise ValueError('username not found')

    def find_by_username_password_role(self, username, password,role):
        user_rep = UserRepository()
        user = user_rep.find_by_username_password_role(username, password, role)
        if user:
            return user
        else:
            raise ValueError('user not found')

    def username_list(self):
        user_rep = UserRepository()
        user_list = user_rep.username_list()
        return user_list

    def employee_username_list(self):
        user_rep = UserRepository()
        user_list = user_rep.employee_username_list()
        return user_list
