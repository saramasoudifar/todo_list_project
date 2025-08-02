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
        user_rep.find_all()

    def find_by_username(self, username):
        user_rep = UserRepository()
        user_rep.find_by_username(username)
