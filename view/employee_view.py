from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import tkinter.messagebox as msg
import os

from controller.todolist_controller import TodoListController


class EmployeeView:
    def save_btn(self):
        pass

    def update_btn(self):
        pass

    def __init__(self,username):
        self.win = Tk()
        self.win.title("Employee View")
        self.win.geometry("800x570")

        self.employee_username = StringVar(value=username)

        current_dir = os.path.dirname(__file__)
        image_path = os.path.join(current_dir, 'v4.jpg')
        bg = Image.open(image_path)
        bg = bg.resize((800, 570))
        self.bg_img = ImageTk.PhotoImage(bg)

        bg_label = Label(self.win, image=self.bg_img)
        bg_label.place(x=-2, y=0)

        Label(self.win, text="username :").place(x=70, y=40)
        Entry(self.win, state='readonly', textvariable=self.employee_username).place(x=140, y=40)

        Label(self.win, text="TodoList :").place(x=500, y=410)
        self.list_id_combo = (ttk.Combobox(self.win,state ='readonly'))
        self.list_id_combo.place(x=570, y=410)
        todo_controller = TodoListController()
        id_list = todo_controller.todolist_id_by_username(self.employee_username.get())
        self.win.mainloop['values']= id_list


        self.table = ttk.Treeview(self.win, columns=[1, 2, 3, 4], show='headings')
        self.table.place(x=80, y=110)

        self.table.heading(1, text='id')
        self.table.heading(2, text='description')
        self.table.heading(3, text='deadline')
        self.table.heading(4, text='status')

        self.table.column(1, width=70)
        self.table.column(2, width=250)
        self.table.column(3, width=170)
        self.table.column(4, width=150)

        Button(self.win, text='Save', command=self.save_btn).place(x=90, y=400, height=40, width=100)
        Button(self.win , text='Update', command=self.update_btn).place(x=220, y=400, height=40, width=100)

        self.win.mainloop()


employee_1 = EmployeeView('sara_masoudi')
