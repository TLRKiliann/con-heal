#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *


class Window(Frame):
    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        Frame.__init__(self, master, bg='RoyalBlue4')                  
        self.master = master
        self.init_window()

    def init_window(self):
        # changing the title of our master widget      
        self.master.title("Time-Track")
        self.pack(fill=BOTH, expand=1)

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label="Patient contact", command=self.patient)
        file.add_command(label="Familiy contact", command=self.family)
        file.add_command(label="Dr contact", command=self.doctor)
        file.add_command(label="Home care system", command=self.reseau)
        file.add_command(label="Legal guardian", command=self.curateur)
        file.add_separator()
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)

        edit = Menu(menu)
        edit.add_command(label="Patient")
        edit.add_command(label="Familiy")
        edit.add_command(label="Doctor")
        edit.add_command(label="Home care system")
        edit.add_command(label="Legal guardian")
        menu.add_cascade(label="Edit", menu=edit)

    def patient(self):
        pass

    def family(self):
        pass

    def doctor(self):
        pass

    def reseau(self):
        pass

    def curateur(self):
        pass

    def client_exit(self):
        exit()

root = Tk()
root.geometry("800x400")
app = Window(root)
root.mainloop()
