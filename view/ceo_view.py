from tkinter import *
import tkinter.ttk as ttk
from controller.task_controller import TaskController
from controller.todolist_controller import TodoListController
from model.entity.task import Task
import tkinter.messagebox as msg
from model.entity.todolist import TodoList
from PIL import Image, ImageTk
import os
import pickle
from view.employee_view import EmployeeView


class CeoView:
    def add_btn(self):
        task_controller = TaskController()

        description_value = self.description_text.get("1.0", END).strip()
        task_id = self.task_id.get()
        title = self.title.get()
        deadline = self.deadline.get()
        assigned_to = self.assigned_to.get()
        is_done = self.is_done.get()

        status, message = task_controller.save(
            description_value,
            task_id,
            title,
            deadline,
            assigned_to,
            is_done
        )

        if status:
            self.table.insert('', END, values=(
                task_id,
                title,
                description_value,
                deadline,
                assigned_to,
                is_done
            ))
            msg.showinfo('Success!', 'Task added successfully!')
            todo_list = TodoList()
            todo_list.add_task(self.task)
        else:
            msg.showerror('Error!', 'Task could not be added!')

    def save_btn(self):
        todo_list = TodoList()
        todo_list_controller = TodoListController()
        status, message = todo_list_controller.save(
            todo_list.tasks.get()
        )
        if status:
            msg.showinfo('Success!', message)
        else:
            msg.showerror('Error!', message)

    def load_employees(self):
        if not os.path.exists():
            return []
        with open(, "rb") as f:
           employees = pickle.load(f)
           return [emp.username for emp in employees]
        # todo

    def load_tasks_for_employee(self, employee_username):
        selected_username = self.employees_combo.get()
        self.clear_btn()
        for task in self.all_tasks:
            if task.assigned_to == selected_username:
                self.table.insert('', END, values=(
                    task.id,
                    task.title,
                    task.description,
                    task.deadline,
                    task.assigned_to,
                    task.is_done
                ))
        #todo

    def clear_btn(self):
        self.table.delete(*self.table.get_children())
        self.task_id.set(0)
        self.title.set('')
        self.description_text.delete('1.0', END)
        self.deadline.set('')
        self.assigned_to.set('')
        self.is_done.set(False)

    def send_btn(self):
        selected_username = self.assigned_to.get()
        if not selected_username:
            msg.showerror("Error", "Please select an employee from the list.")
            return

    #todo

        employee_tasks = []
        for row in self.table.get_children():
            values = self.table.item(row, 'values')
            if values[4] == selected_username:  # ستون assigned_to
                task = {
                    'id': values[0],
                    'description': values[1],
                    'deadline': values[2],
                    'status': values[3],
                }
                employee_tasks.append(task)

        if employee_tasks:
            EmployeeView(selected_username, employee_tasks)
        else:
            msg.showinfo("Info", "No tasks assigned to this employee.")
            #todo


    def edit_btn(self):
        pass

    def delete_btn(self):
        pass

    def table_select(self,event):
        pass

    def __init__(self):
        self.all_tasks = []
        if os.path.exists("tasks.dat"):
            with open("tasks.dat", "rb") as f:
                self.all_tasks = pickle.load(f)

        self.win = Tk()
        self.win.geometry('1100x500')
        self.win.title('Ceo')

        bg = Image.open('v1.jpg')
        bg = bg.resize((1100, 500))
        self.bg_img = ImageTk.PhotoImage(bg)

        bg_label = Label(self.win, image=self.bg_img)
        bg_label.place(x=-2, y=0)

        self.task_id = IntVar()
        self.title = StringVar()
        self.deadline = StringVar()
        self.assigned_to = StringVar()
        self.is_done = BooleanVar()

        Label(self.win, text='task id').place(x=50, y=30)
        Entry(self.win, textvariable=self.task_id, state='readonly').place(x=110, y=30)

        Label(self.win, text='description').place(x=25, y=70)
        self.description_text = Text(self.win, height=5, width=30)
        self.description_text.place(x=110, y=70)

        Label(self.win, text='deadline').place(x=35, y=175)
        Entry(self.win, textvariable=self.deadline).place(x=110, y=175)

        Label(self.win, text='status').place(x=48, y=215)
        Entry(self.win, textvariable=self.is_done, state='readonly').place(x=110, y=215)

        Label(self.win, text='username').place(x=29, y=255)
        Entry(self.win, textvariable=self.assigned_to).place(x=110, y=255)

        Label(self.win, text='employees').place(x=825, y=350)
        employees_list = self.load_employees()
        self.employees_combo = ttk.Combobox(self.win, textvariable=self.assigned_to, state='readonly',
                                            values=employees_list)
        self.employees_combo.place(x=900, y=350)
        self.employees_combo.bind("<<ComboboxSelected>>", self.load_tasks_for_employee)


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

        Button(self.win, text='save', command=self.save_btn).place(x=80, y=360, width=70, height=40)
        Button(self.win, text='clear', command=self.clear_btn).place(x=160, y=360, width=70, height=40)
        Button(self.win, text='send', command=self.send_btn).place(x=240, y=360, width=70, height=40)
        Button(self.win, text='add', command=self.add_btn).place(x=80, y=310, width=230, height=40)
        Button(self.win, text='edit', command=self.edit_btn).place(x=80, y=410, width=110, height=40)
        Button(self.win, text='delete', command=self.delete_btn).place(x=200, y=410, width=110, height=40)
        Button(self.win,text='add user').place(x=1000, y=20)

        self.win.mainloop()


ceoview = CeoView()
