from tkinter import *
import tkinter.ttk as ttk
from controller.user_controller import UserController
import tkinter.messagebox as msg


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
            self.table.insert("", END, values = (
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
#todo
            ))
            msg.showinfo('success', message)
        else:
            msg.showerror('error', message)

    def delete_btn(self):
        usercontroller = UserController()
        status, message = usercontroller.delete(
            self.code.get()
        )
        if status:
            pass

         #todo





            msg.showinfo('success', message)
        else:
            msg.showerror('error', message)

    def search_by_username_btn(self):
        usercontroller = UserController()
        status, message = usercontroller.find_by_username(
            self.username.get()
        )
        if status:

            #todo




            msg.showinfo('success', message)
        else:
            msg.showerror('error', message)

    def load_all(self):
        usercontroller = UserController()
        status, message = usercontroller.find_all()
        if status:
            pass
  #todo

    def __init__(self):
        self.win = Tk()
        self.win.title("Employee View")
        self.win.geometry("1100x570")

        self.load_all()

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
        ttk.Combobox(self.win, values=['users'], state='readonly').place(x=800, y=335)
        # todo

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

        self.win.mainloop()


adduser = AddUser()
