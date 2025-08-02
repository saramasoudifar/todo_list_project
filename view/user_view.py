from controller.user_controller import UserController
from tkinter import *
import tkinter.messagebox as msg
from PIL import Image, ImageTk


class UserView:
    def enter_btn(self):
        user_controller = UserController()
        status, message = user_controller.enter(
            self.name.get(),
            self.family.get(),
            self.username.get(),
            self.password.get(),
            self.role.get()
        )
        if status:
            msg.showinfo('Success!',message)
        else:
            msg.showerror('Error!',message)


    def exit_btn(self):
        self.win.destroy()



    def __init__(self):
        self.win = Tk()
        self.win.geometry("400x500")
        self.win.title('Todo List')

        bg=Image.open('bg6.jpg')
        bg = bg.resize((400,600))
        self.bg_img=ImageTk.PhotoImage(bg)

        bg_label = Label(self.win,image=self.bg_img)
        bg_label.place(x=-2,y=0)

        self.name = StringVar()
        self.family = StringVar()
        self.username = StringVar()
        self.password = StringVar()
        self.role = BooleanVar()

        Label(self.win, text='Name :',bg="LightSkyBlue4").place(x=99, y=60)
        Entry(self.win, textvariable=self.name).place(x=150, y=60)

        Label(self.win, text='Family :',bg="LightSkyBlue4").place(x=96, y=100)
        Entry(self.win, textvariable=self.family).place(x=150, y=100)

        Label(self.win, text='Username :',bg="LightSkyBlue4").place(x=79, y=140)
        Entry(self.win, textvariable=self.username).place(x=150, y=140)

        Label(self.win, text='Password :',bg="LightSkyBlue4").place(x=83, y=180)
        Entry(self.win, textvariable=self.password).place(x=150, y=180)

        Label(self.win, text='Role :',bg="LightSkyBlue4").place(x=110, y=220)
        Checkbutton(self.win, text='ceo',variable= self.role,bg="LightSkyBlue4").place(x=150, y=220)
        Checkbutton(self.win, text='employee',variable= self.role,bg="LightSkyBlue4").place(x=210, y=220)

        Button(self.win, text='enter',command=self.enter_btn,bg="seashell").place(x=100, y=335, width=80, height=30)
        Button(self.win, text='exit',command=self.exit_btn,bg="seashell").place(x=220, y=335, width=80, height=30)

        self.win.mainloop()


userview = UserView()

#todo:role
