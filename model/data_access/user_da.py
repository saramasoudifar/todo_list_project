import os
import pickle

class UserDa:
    def __init__(self):
        self.file_path = 'user.dat'

    def read_from_file(self):
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, 'rb') as f:
            return pickle.load(f)

    def save(self, user_list):
        file = open(self.file_path, 'wb')
        pickle.dump(user_list, file)
        file.close()

    def enter(self,name,family,username,password,role):
        pass

