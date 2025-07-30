from tkinter import *
import tkinter.ttk as ttk
from controller.task_controller import TaskController
from controller.todo_list_controller import TodoListController
from model.entity.task import Task
import tkinter.messagebox as msg
from model.entity.todo import TodoList
from PIL import Image, ImageTk

employees_list = []


class CeoView:
    def add_btn(self):
        task_controller = TaskController()
        status, message = task_controller.save(
            self.task_id.get(),
            self.description.get(),
            self.deadline.get(),
            self.status.get()

        )

        if status:
            self.task = Task()
            self.task.to_tuple()
            self.table.insert('', END, values=(
                self.task_id.get(),
                self.description.get(),
                self.deadline.get(),
                self.status.get(),
                self.employee_username.get(),

            ))
            msg.showinfo('Success!', 'Task added successfully!')
            self.task = Task(self.task_id.get(), self.description.get(), self.deadline.get(), self.status)
            todo_list = TodoList(self.list_id.get(), self.date.get(), self.employee_username.get())
            todo_list.add_task(self.task)

        else:
            msg.showerror('Error!', 'Task could not be added!')

    def save_btn(self):
        todo_list_controller = TodoListController()
        status, message = todo_list_controller.save(
            self.list_id.get(),
            self.date.get(),
            self.employee_username.get(),
            self.tasks.get()
        )
        if status:
            msg.showinfo('Success!', 'Todo list saved successfully!')
        else:
            msg.showerror('Error!', 'TodoList could not be saved!')

    def clear_btn(self):
        pass



    def send_btn(self):
        pass



    def __init__(self):
        self.win = Tk()
        self.win.geometry('1100x500')
        self.win.title('Ceo')

        bg = Image.open('v1.jpg')
        bg = bg.resize((1100, 500))
        self.bg_img = ImageTk.PhotoImage(bg)

        bg_label = Label(self.win, image=self.bg_img)
        bg_label.place(x=-2, y=0)


        self.task_id = IntVar()
        self.description = StringVar()
        self.deadline = StringVar()
        self.status = BooleanVar()
        self.employee_username = StringVar()
        self.list_id = StringVar()
        self.date = StringVar()

        Label(self.win, text='task id').place(x=50, y=30)
        Entry(self.win, textvariable=self.task_id, state='readonly').place(x=110, y=30)

        Label(self.win, text='description').place(x=25, y=70)
        Text(self.win, height=5, width=30, ).place(x=110, y=70)

        Label(self.win, text='deadline').place(x=35, y=175)
        Entry(self.win, textvariable=self.deadline).place(x=110, y=175)

        Label(self.win, text='status').place(x=48, y=215)
        Entry(self.win, textvariable=self.status, state='readonly').place(x=110, y=215)
        # todo:its on the treeview

        Label(self.win, text='username').place(x=29, y=255)
        Entry(self.win, textvariable=self.employee_username).place(x=110, y=255)

        Label(self.win, text='employees').place(x=825, y=350)
        ttk.Combobox(self.win, textvariable=self.employee_username, state='readonly', values=employees_list).place(
            x=900, y=350)

        Label(self.win, text='TodoList id').place(x=400, y=30)
        Entry(self.win, textvariable=self.list_id, state='readonly').place(x=480, y=30)

        Label(self.win, text='date').place(x=850, y=30)
        Entry(self.win, textvariable=self.date).place(x=890, y=30)

        self.table = ttk.Treeview(self.win, columns=[1, 2, 3, 4, 5], show='headings')
        self.table.place(x=390, y=70)

        self.table.heading(1, text='id')
        self.table.heading(2, text='description')
        self.table.heading(3, text='deadline')
        self.table.heading(4, text='status')
        self.table.heading(5, text='employee username')

        self.table.column(1, width=50)
        self.table.column(2, width=250)
        self.table.column(3, width=120)
        self.table.column(4, width=100)
        self.table.column(5, width=150)

        Button(self.win, text='save',command= self.save_btn).place(x=80, y=360, width=70, height=40)
        Button(self.win, text='clear',command=self.clear_btn).place(x=160, y=360, width=70, height=40)
        Button(self.win, text='send',command=self.send_btn).place(x=240, y=360, width=70, height=40)
        Button(self.win, text='add',command=self.add_btn).place(x=80, y=310, width=230, height=40)

        self.win.mainloop()


ceoview = CeoView()
