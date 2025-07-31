from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import tkinter.messagebox as msg


class EmployeeView:
    def __init__(self, username, task_list):
        self.win = Toplevel()
        self.win.title("Employee View")
        self.win.geometry("800x570")

        self.employee_username = StringVar(value=username)

        bg = Image.open('v4.jpg')
        bg = bg.resize((800, 570))
        self.bg_img = ImageTk.PhotoImage(bg)

        bg_label = Label(self.win, image=self.bg_img)
        bg_label.place(x=-2, y=0)

        Label(self.win, text="Employee Name :").place(x=40, y=40)
        Entry(self.win, state='readonly', textvariable=self.employee_username).place(x=140, y=40)

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


        for task in task_list:
            self.table.insert('', END, values=(
                task['id'],
                task['description'],
                task['deadline'],
                task['status']
            ))

        Button(self.win, text='Save', command=self.save_btn).place(x=100, y=400, height=40, width=100)

    def save_btn(self):
        msg.showinfo("Saved", "Tasks saved successfully.")


