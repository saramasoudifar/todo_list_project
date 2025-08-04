from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import tkinter.messagebox as msg
import os
from controller.task_controller import TaskController

from controller.todolist_controller import TodoListController


class EmployeeView:
    def save_btn(self):
        pass

    def update_btn(self):
        pass

    def load_tasks(self, event):
        selected_list_id = self.list_id_combo.get()
        self.table.delete(*self.table.get_children())

        task_controller = TaskController()
        status, tasks = task_controller.find_by_id(int(selected_list_id))

        if status:
            for task in tasks:
                self.table.insert('', END, values=(task.task_id,task.title, task.description, task.deadline,
                                                   'done' if task.is_done else 'not done'))

    def __init__(self, username):
        self.win = Tk()
        self.win.title("Employee View")
        self.win.geometry("850x570")

        self.employee_username = StringVar()
        self.employee_username.set(username)
        self.date = StringVar()
        self.list_id = IntVar()

        current_dir = os.path.dirname(__file__)
        image_path = os.path.join(current_dir, 'v4.jpg')
        bg = Image.open(image_path)
        bg = bg.resize((850, 570))
        self.bg_img = ImageTk.PhotoImage(bg)

        bg_label = Label(self.win, image=self.bg_img)
        bg_label.place(x=-2, y=0)

        Label(self.win, text="username :").place(x=70, y=40)
        Entry(self.win, state='readonly', textvariable=self.employee_username).place(x=140, y=40)

        Label(self.win, text="TodoList id :").place(x=70, y=80)
        Entry(self.win, textvariable=self.list_id, state='readonly').place(x=140, y=80)


        Label(self.win, text="date :").place(x=540, y=80)
        Entry(self.win, textvariable=self.date, state='readonly').place(x=580, y=80)


        Label(self.win, text="TodoList :").place(x=500, y=410)
        self.list_id_combo = (ttk.Combobox(self.win, state='readonly'))
        self.list_id_combo.place(x=570, y=410)
        todo_controller = TodoListController()
        id_list = todo_controller.todolist_id_by_username(self.employee_username.get())
        self.list_id_combo['values'] = id_list

        self.list_id_combo.bind("<<ComboboxSelected>>", self.load_tasks)

        self.table = ttk.Treeview(self.win, columns=[1, 2, 3, 4,5], show='headings')
        self.table.place(x=70, y=110)

        self.table.heading(1, text='id')
        self.table.heading(2, text='title')
        self.table.heading(3, text='description')
        self.table.heading(4, text='deadline')
        self.table.heading(5, text='status')

        self.table.column(1, width=70)
        self.table.column(2, width=70)
        self.table.column(3, width=250)
        self.table.column(4, width=170)
        self.table.column(5, width=150)

        Button(self.win, text='Save', command=self.save_btn).place(x=90, y=400, height=40, width=100)
        Button(self.win, text='Update', command=self.update_btn).place(x=220, y=400, height=40, width=100)

        self.win.mainloop()


employee_1 = EmployeeView('sara_masoudi')
