#!/usr/bin/python3
# -*-encoding:Utf-8-*-


from tkinter import *
from tkinter import messagebox
import os
from del_patient1 import *


def get(Nompatient, entree):
    """
    To delete patient name and all files by functions
    with a msgbox to verify the choice.
    """
    MsgBox = messagebox.askyesno('Save data', 'Do you want to delete ?')
    if MsgBox == 1:
        Nompatient = entree.get()
        print(Nompatient)
        if os.path.getsize('./newpatient/entryfile.txt'):
            with open('./newpatient/entryfile.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile1()
                    else:
                        print("Patient's Name does not exist")
    else:           
        messagebox.showinfo('Return', 'None file was found !')

    gui.destroy()

gui=Tk()
gui.title("Enter new patient")
gui.configure(bg='cyan')
#gui.geometry('300x200')

labelName = Label(gui)
labelName = Label(text='Enter NAME to delete : ',
    font="Times 14 bold",
    fg='RoyalBlue4', bg='cyan')
labelName.pack(pady=10)

Nompatient=StringVar()
Nompatient.set('Firstname + Lastname')
entree = Entry(gui, textvariable=Nompatient,
    highlightbackground='light sky blue', bd=4)
entree.pack()

bouton1 = Button(gui, text="Delete", fg='yellow', bg='RoyalBlue3',
    width=8, bd=4, highlightbackground='cyan', 
    command = lambda: get(Nompatient, entree))
bouton1.pack(side=LEFT, padx=10, pady=20)

buttQuit=Button(gui, text="Quit", fg='cyan', bg='RoyalBlue3',
    width=8, bd=4, highlightbackground='cyan',
    command=quit)
buttQuit.pack(side=LEFT, padx=10, pady=20)

gui.mainloop()
