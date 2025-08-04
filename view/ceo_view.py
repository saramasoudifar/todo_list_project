from tkinter import *
import tkinter.ttk as ttk
from controller.task_controller import TaskController
from controller.user_controller import UserController
from model.entity.task import Task
import tkinter.messagebox as msg
from model.entity.todolist import TodoList
from PIL import Image, ImageTk
import os
from datetime import datetime



class CeoView:
    def add_btn(self):
        task_controller = TaskController()

        task_id = self.task_id.get()
        title = self.title.get()
        description_value = self.description_text.get("1.0", END).strip()
        deadline = self.deadline.get()
        assigned_to = self.assigned_to.get()
        list_id=self.list_id.get()
        is_done = self.is_done.get()

        status, message = task_controller.save(
            task_id,
            title,
            description_value,
            deadline,
            assigned_to,
            list_id,
            is_done
        )
        if status:
            self.table.insert('', END, values=(
                task_id,
                title,
                description_value,
                deadline,
                assigned_to,
                list_id,
                is_done
            ))
            msg.showinfo('Success!', 'Task added successfully!')
            owner_username = assigned_to
            task = Task(task_id, title, description_value, deadline, assigned_to,list_id, is_done)
            todo_list = TodoList(list_id, self.date.get() ,owner_username)
            todo_list.add_task(task)
        else:
            msg.showerror('Error!', 'Task could not be added!')

    def save_btn(self):
        pass

    # todo:todo list save beshe

    def clear_btn(self):
        self.table.delete(*self.table.get_children())
        self.title.set('')
        self.description_text.delete('1.0', END)
        self.deadline.set('')
        self.assigned_to.set('')
        self.is_done.set(False)

        task_controller = TaskController()
        max_id = task_controller.max_task_id()
        self.task_id.set(max_id + 1)

    def send_btn(self):
        pass

    # todo

    def edit_btn(self):
        selected_item = self.table.selection()
        if not selected_item:
            msg.showerror('Error', 'Please select a task to edit.')
            return
        task_controller = TaskController()
        status, message = task_controller.edit(
            self.task_id.get(),
            self.title.get(),
            self.description_text.get("1.0", END).strip(),
            self.deadline.get(),
            self.assigned_to.get(),
            self.is_done.get()
        )
        if status:
            self.table.item('', values=(
                self.task_id.get(),
                self.title.get(),
                self.description_text.get("1.0", END).strip(),
                self.deadline.get(),
                self.assigned_to.get(),
                self.is_done.get()
            ))
            msg.showinfo('Success!', 'Task edited successfully!')
        else:
            msg.showerror('Error!', 'Task could not be edited!')

    def delete_btn(self):
        selected_item = self.table.selection()
        if not selected_item:
            msg.showerror("Error", "Please select a task to delete.")
            return

        task_id = self.table.item(selected_item[0])['values'][0]
        task_controller = TaskController()
        status, message = task_controller.delete(task_id)
        if status:
            self.table.delete(selected_item[0])
            msg.showinfo('Success!', 'Task deleted successfully!')
        else:
            msg.showerror('Error!', 'Task could not be deleted!')

    def table_select(self, event):
        task = Task(*self.table.item(self.table.focus())['values'])
        self.task_id.set(task.task_id)
        self.title.set(task.title)
        self.description_text.delete('1.0', END)
        self.description_text.insert(END, task.description)
        self.deadline.set(task.deadline)
        self.assigned_to.set(task.assigned_to)
        self.is_done.set(task.is_done)

    def add_user(self):
        from view.add_user import AddUser
        self.add_user = AddUser()

    def __init__(self):
        self.win = Tk()
        self.win.geometry('1100x500')
        self.win.title('Ceo')

        current_dir = os.path.dirname(__file__)  # مسیر فعلی فایل user_view.py
        image_path = os.path.join(current_dir, 'v1.jpg')
        bg = Image.open(image_path)
        bg = bg.resize((1100, 500))
        self.bg_img = ImageTk.PhotoImage(bg)

        bg_label = Label(self.win, image=self.bg_img)
        bg_label.place(x=-2, y=0)

        self.task_id = IntVar()
        self.title = StringVar()
        self.deadline = datetime
        self.assigned_to = StringVar()
        self.list_id = IntVar()
        self.is_done = BooleanVar()

        self.date = datetime

        Label(self.win, text='task id').place(x=50, y=25)
        Entry(self.win, textvariable=self.task_id, state='readonly').place(x=110, y=25)

        Label(self.win, text='task title').place(x=40, y=65)
        Entry(self.win, textvariable=self.title).place(x=110, y=65)

        Label(self.win, text='description').place(x=25, y=100)
        self.description_text = Text(self.win, height=5, width=30)
        self.description_text.place(x=110, y=100)

        Label(self.win, text='deadline').place(x=35, y=195)
        Entry(self.win, textvariable=self.deadline).place(x=110, y=195)

        Label(self.win, text='status').place(x=48, y=235)
        Entry(self.win, textvariable=self.is_done, state='readonly').place(x=110, y=235)

        Label(self.win, text='username').place(x=29, y=275)
        Entry(self.win, textvariable=self.assigned_to).place(x=110, y=275)

        Label(self.win, text='employees').place(x=825, y=350)
        self.employees_combo = ttk.Combobox(self.win, textvariable=self.assigned_to, state='readonly')
        self.employees_combo.place(x=900, y=350)
        user_controller = UserController()
        employees = user_controller.employee_username_list()
        self.employees_combo['values'] = employees

        self.table = ttk.Treeview(self.win, columns=[1, 2, 3, 4, 5, 6], show='headings')
        self.table.place(x=380, y=70)

        self.table.heading(1, text='id')
        self.table.heading(2, text='title')
        self.table.heading(3, text='description')
        self.table.heading(4, text='deadline')
        self.table.heading(5, text='assigned to')
        self.table.heading(6, text='status')

        self.table.column(1, width=50)
        self.table.column(2, width=100)
        self.table.column(3, width=200)
        self.table.column(4, width=120)
        self.table.column(5, width=150)
        self.table.column(6, width=80)

        self.table.bind("<<TreeviewSelect>>", self.table_select)

        Button(self.win, text='save', command=self.save_btn).place(x=80, y=360, width=70, height=40)
        Button(self.win, text='clear', command=self.clear_btn).place(x=160, y=360, width=70, height=40)
        Button(self.win, text='send', command=self.send_btn).place(x=240, y=360, width=70, height=40)
        Button(self.win, text='add', command=self.add_btn).place(x=80, y=310, width=230, height=40)
        Button(self.win, text='edit', command=self.edit_btn).place(x=80, y=410, width=110, height=40)
        Button(self.win, text='delete', command=self.delete_btn).place(x=200, y=410, width=110, height=40)
        Button(self.win, text='add user', command=self.add_user).place(x=1000, y=20)

        self.win.mainloop()

ceoview = CeoView()
