from tkinter import *
import tkinter.ttk as ttk
from controller.user_controller import UserController
import tkinter.messagebox as msg
from model.entity.user import User


class AddUser:
    def save_btn(self):
        usercontroller = UserController()
        status, message = usercontroller.save(
            self.code.get(),
            self.name.get(),
            self.family.get(),
            self.username.get(),
            self.password.get(),
            self.role.get()
        )
        if status:
            self.table.insert("", END, values=(
                self.code.get(),
                self.name.get(),
                self.family.get(),
                self.username.get(),
                self.password.get(),
                self.role.get()

            ))
            msg.showinfo('success', message)
        else:
            msg.showerror('error', message)

    def edit_btn(self):
        selected_item = self.table.selection()
        if not selected_item:
            msg.showerror('Error', 'Please select a user to edit.')
            return
        usercontroller = UserController()
        status, message = usercontroller.edit(
            self.code.get(),
            self.name.get(),
            self.family.get(),
            self.username.get(),
            self.password.get(),
            self.role.get()
        )
        if status:
            self.table.insert("", END, values=(
                self.code.get(),
                self.name.get(),
                self.family.get(),
                self.username.get(),
                self.password.get(),
                self.role.get()
                # todo
            ))
            msg.showinfo('success', message)
        else:
            msg.showerror('error', message)

    def delete_btn(self):
        selected_item = self.table.selection()
        if not selected_item:
            msg.showerror('Error', 'Please select a user to delete.')
            return
        user_code = self.table.item(selected_item[0])['values'][0]
        usercontroller = UserController()
        status, message = usercontroller.delete(user_code)
        if status:
            self.table.delete(selected_item[0])
            msg.showinfo('Success!', 'Task deleted successfully!')
        else:
            msg.showerror('Error!', 'Task could not be deleted!')

    def search_by_username_btn(self):
        usercontroller = UserController()
        status, user = usercontroller.find_by_username(
            self.username.get()
        )
        if status:
            self.table.delete(*self.table.get_children())
            self.table.insert('', 'end', values=(
                user.code,
                user.name,
                user.family,
                user.username,
                user.role
            ))

            msg.showinfo('Success', 'User found!')
        else:
            msg.showerror('Error', 'user not found!')

    def load_users_to_table(self):
        usercontroller = UserController()
        all_users = usercontroller.find_all()
        for user in all_users:
            self.table.insert("", END, values=(user))

    def table_select(self):
        user = User(*self.table.item(self.table.focus())['values'])
        self.code.set(user.code)
        self.name.set(user.name)
        self.family.set(user.family)
        self.username.set(user.username)
        self.password.set('********')
        self.role.set(user.role)

    def __init__(self):
        self.win = Tk()
        self.win.title("Employee View")
        self.win.geometry("1100x570")

        self.code = IntVar()
        self.name = StringVar()
        self.family = StringVar()
        self.username = StringVar()
        self.password = StringVar()
        self.role = StringVar(value='employee')
        self.find_by_family = StringVar()

        Label(self.win, text='code :', bg="LightSkyBlue4").place(x=99, y=20)
        Entry(self.win, textvariable=self.name, state='readonly').place(x=150, y=20)

        Label(self.win, text='Name :', bg="LightSkyBlue4").place(x=99, y=60)
        Entry(self.win, textvariable=self.name).place(x=150, y=60)

        Label(self.win, text='Family :', bg="LightSkyBlue4").place(x=96, y=100)
        Entry(self.win, textvariable=self.family).place(x=150, y=100)

        Label(self.win, text='Username :', bg="LightSkyBlue4").place(x=79, y=140)
        Entry(self.win, textvariable=self.username).place(x=150, y=140)

        Label(self.win, text='Password :', bg="LightSkyBlue4").place(x=83, y=180)
        Entry(self.win, textvariable=self.password).place(x=150, y=180)

        Label(self.win, text='Role :', bg="LightSkyBlue4").place(x=110, y=220)
        ttk.Combobox(self.win, values=['ceo', 'employee'], state='readonly').place(x=150, y=220)

        Label(self.win, text='users').place(x=755, y=335)
        self.users_combo =(ttk.Combobox(self.win,state='readonly'))
        user_controller = UserController()
        users = user_controller.username_list()
        self.users_combo['values'] = users


        Label(self.win, text='find by username').place(x=690, y=375)
        Entry(self.win, textvariable=self.find_by_family).place(x=800, y=375)

        Button(self.win, text='save', command=self.save_btn, bg="seashell").place(x=100, y=335, width=80, height=30)
        Button(self.win, text='edit', command=self.edit_btn, bg="seashell").place(x=220, y=335, width=80, height=30)
        Button(self.win, text='delete', command=self.delete_btn, bg="seashell").place(x=340, y=335, width=80, height=30)
        Button(self.win, text='search', command=self.search_by_username_btn).place(x=940, y=370, width=80, height=30)

        self.table = ttk.Treeview(self.win, columns=[1, 2, 3, 4, 5, 6], show='headings')
        self.table.place(x=360, y=30)

        self.table.heading(1, text='code')
        self.table.heading(2, text='name')
        self.table.heading(3, text='family')
        self.table.heading(4, text='username')
        self.table.heading(5, text='password')
        self.table.heading(6, text='role')

        self.table.column(1, width=70)
        self.table.column(2, width=120)
        self.table.column(3, width=120)
        self.table.column(4, width=120)
        self.table.column(5, width=120)
        self.table.column(6, width=100)

        self.load_users_to_table()
        self.table.bind('<<TreeviewSelect>>', self.table_select)

        self.win.mainloop()


adduser = AddUser()
