import pickle

from model.entity.employee import Employee

employees = [
    Employee("sara", "Sara Masoudifar"),
    Employee("ali", "Ali Rezaei"),
    Employee("reza", "Reza Ahmadi"),
]

with open("employees.dat", "wb") as f:
    pickle.dump(employees, f)