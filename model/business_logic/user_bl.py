from model.data_access.user_da import UserDa

class UserBl:
    def save(self, name,family,username,password,role):
            user_da = UserDa()
            user_da.save(name,family,username,password,role)

    def find_by_username_pass(self, role, username, password):
        user_da = UserDa()
        user_da.find_by_username_pass(role, username, password)

    def enter(self,name,family,username,password,role):
        user_da = UserDa()
        user_da.enter(name,family,username,password,role)


#todo:mishe inja goft ke age user save bud savesh nakon?