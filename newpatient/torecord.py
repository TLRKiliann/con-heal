#!/usr/bin/python3
# -*-encoding:Utf-8-*-


"""
    To record a new patient
    in text zone (entree cap)
"""


from tkinter import *
from tkinter import messagebox
import os
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError as err_report4:
    print("+ An error occured about pymysql !", err_report4)
    pass


gui=Tk()
gui.title("Enter new patient")
gui.configure(bg='cyan')
#gui.geometry('300x200')

def get(Nompatient, entree, Birthvalue, Birth_entree):
    """
        Add a patient with
        the add button
    """
    mot = "-"

    Nompatient = entree.get()
    Birthvalue = Birth_entree.get()
    print(Nompatient)
    print(Birthvalue)

    if mot == '-':
        if os.path.getsize('./newpatient/entryfile.txt'):
            with open('./newpatient/entryfile.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot in line:
                        searchLine1(Nompatient, Birthvalue)
    else:
        print("There is no file to edit as entryfile.txt")

    if mot == '--':
        if os.path.getsize('./newpatient/entryfile2.txt'):
            with open('./newpatient/entryfile2.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot in line:
                        searchLine1(Nompatient, Birthvalue)
    else:
        print("There is no file to edit as entryfile2.txt")

    gui.destroy()

def searchLine1(Nompatient, Birthvalue):
    """
        To save new patient name
        by a msgbox and write the
        new name in an entryfile.txt
    """
    MsgBox = messagebox.askyesno('Save data', 'Do you want to save ?')
    if MsgBox == 1:
        file = open('./newpatient/entryfile.txt', 'w')
        file.write(Nompatient + '\n')
        file.write(Birthvalue + '\n')
        file.close()

labelName = Label(gui)
labelName = Label(text='Enter NAME : ',
    font="Times 14 bold",
    fg='RoyalBlue4', bg='cyan')
labelName.pack(pady=10)

Nompatient=StringVar()
Nompatient.set('Firstname + Lastname')
entree = Entry(gui, textvariable=Nompatient,
    highlightbackground='light sky blue', bd=4)
entree.pack()

labelBirth = Label(gui)
labelBirth = Label(text='Birth Date : ', font="Times 14 bold",
    fg='RoyalBlue4', bg='cyan')
labelBirth.pack(pady=10)

Birthvalue=StringVar()
Birthvalue.set('Format: 00/00/0000')
Birth_entree = Entry(gui, textvariable=Birthvalue,
    highlightbackground='light sky blue',
    bd=4)
Birth_entree.pack()

bouton1 = Button(gui, text="Enter", width=8, bd=4,
    fg='yellow', bg='RoyalBlue3',
    highlightbackground='light sky blue',
    activebackground='dark turquoise',
    command = lambda: get(Nompatient, entree, Birthvalue, Birth_entree))
bouton1.pack(side=LEFT, padx=10, pady=20)

buttQuit=Button(gui, text="Quit", width=8, bd=4,
    fg='cyan', bg='RoyalBlue3',
    highlightbackground='light sky blue',
    activebackground='dark turquoise', command=quit)
buttQuit.pack(side=LEFT, padx=10, pady=20)

gui.mainloop()
