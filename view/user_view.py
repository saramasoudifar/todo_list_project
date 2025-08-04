from controller.user_controller import UserController
from tkinter import *
import tkinter.messagebox as msg
from PIL import Image, ImageTk
from tkinter import ttk
import os


class UserView:
    def enter_btn(self):
        user_controller = UserController()
        status, user_or_message = user_controller.find_by_username_password_role(
            self.username.get(),
            self.password.get(),
            self.role.get()
        )
        if status:
            self.win.destroy()
            if  user_or_message.role == 'ceo':
                from view.ceo_view import CeoView
                self.ceo = CeoView()
            if user_or_message.role == 'employee':
                from view.employee_view import EmployeeView
                self.employee = EmployeeView(user_or_message.username)

            msg.showinfo('Success!','welcome!')
        else:
            msg.showerror('Error!','username not found')


    def exit_btn(self):
        self.win.destroy()



    def __init__(self):
        self.win = Tk()
        self.win.geometry("400x500")
        self.win.title('Todo List')

        current_dir = os.path.dirname(__file__)  # مسیر فعلی فایل user_view.py
        image_path = os.path.join(current_dir, 'bg6.jpg')
        bg = Image.open(image_path)
        bg = bg.resize((400,600))
        self.bg_img=ImageTk.PhotoImage(bg)

        bg_label = Label(self.win,image=self.bg_img)
        bg_label.place(x=-2,y=0)

        self.username = StringVar()
        self.password = StringVar()
        self.role = StringVar(value='employee')


        Label(self.win, text='Username :',bg="LightSkyBlue4").place(x=79, y=120)
        Entry(self.win, textvariable=self.username).place(x=150, y=120)

        Label(self.win, text='Password :',bg="LightSkyBlue4").place(x=83, y=160)
        Entry(self.win, textvariable=self.password).place(x=150, y=160)

        Label(self.win, text='Role :',bg="LightSkyBlue4").place(x=110, y=220)
        ttk.Combobox(self.win, textvariable=self.role,values=['ceo','employee'],state='readonly').place(x=150, y=220)


        Button(self.win, text='enter',command=self.enter_btn,bg="seashell").place(x=100, y=335, width=80, height=30)
        Button(self.win, text='exit',command=self.exit_btn,bg="seashell").place(x=220, y=335, width=80, height=30)

        self.win.mainloop()


userview = UserView()
