#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter
from tkinter import *
from tkinter import messagebox
import json
import time
import os
import subprocess
from itertools import *


gui = Tk()
gui.title("Save changes !")
gui.configure(bg='cyan')

labelTit = Label(gui, text="Save changes !", font=("Arial 16 bold"),
    fg='navy', bg='cyan')
labelTit.grid(sticky='e', row=0, column=1, pady=10)

labelDate = Label(gui, text='Search date to modify : ', font='12', 
    fg='navy', bg='cyan')
labelDate.grid(sticky='e', row=1, column=1)

with open('./newpatient/entryfile16.txt', 'r') as filename:
    line1 = filename.readline()

textname = StringVar()
entryName = Entry(gui, textvariable=textname)
textname.set(line1)
entryName.grid(row=0, column=2, pady=10)

def searchExpress():
    """
        To read multiples files in a directory
    """
    try:
        mot = regexpi_var.get()
        for path, dirs, files in os.walk('./patient_agenda/events16/'\
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                read_f = open(os.path.join(path, file), 'r')
                lines = read_f.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot in line:
                        print("Nous y voici !")
                        print(lines[i-1])
                        print(lines[i])
                        print(lines[i+1])
                        print(lines[i+2])
                        print(lines[i+3])
                        textBox.insert(INSERT, lines[i-1])
                        textBox.insert(INSERT, lines[i])
                        textBox.insert(INSERT, lines[i+1])
                        textBox.insert(INSERT, lines[i+2])
                        textBox.insert(INSERT, lines[i+3])
    except IndexError as ind_err:
        print("+ Index out of range", ind_err)

def save_input():
    """
        Save data from modification rdv textbox !
        To copy to a txt file of a directory
        since a read file and from text widget
        by lines ;) !
    """
    magicword = regexpi_var.get()
    for path, dirs, files in os.walk('./patient_agenda/events16/'\
        'doc_events/fix_agenda/agenda_saved/'):
        for file in files:
            read_f = open(os.path.join(path, file), 'r')
            for line in read_f:
                for i in line:
                    noway = "Fixed on :"
                    if line[0:10] == noway:
                        print("+ There is noway : ")
                        print(line[0:10])
                    elif magicword in line:
                        print("+ It is magicword : ")
                        print(line[0:10])
                        write_f = open(os.path.join(path, file), 'w')
                        write_f.writelines(textBox.get("0.0", "end-1c") + "\n")
                        print("Modification finish")
                        break
                    else:
                        print("None file has been writted")
                        break

def messFromSafeButt():
    MsgBox = messagebox.askquestion("Confirm","Are you sure ?\n"
        "It will save all data !")
    if MsgBox == 'yes':
        save_input()
        textBox.insert(INSERT, "\n---Data saved !---")
        print("+ Data saved !")
    else:
        textBox.insert(INSERT, "Nothing has been saved !")
        print("+ Nothing has been saved !")

def modifList():
    """
        To read file modifrdv.txt
    """
    subprocess.run('./patient_agenda/events16/doc_events/'\
        'fix_agenda/read_file.py', check=True)

def deleteTextbox():
    textBox.delete('0.0', "end-1c")

regexpi_var = StringVar()
reachDate = Entry(gui, textvariable=regexpi_var)
reachDate.grid(row=1, column=2, pady=10)

textBox = Text(gui, height=15, width=60, font=18)
textBox.grid(row=4, column=1, columnspan=3, padx=30, pady=30)

buttonSearch = Button(gui, text='Search', width=8, bd=3,
    fg='yellow', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='dark turquoise', command=searchExpress)
buttonSearch.grid(row=1, column=3, padx=5)

buttonSave = Button(gui, text="Save", width=8, bd=3,
    fg='yellow', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='dark turquoise', command = messFromSafeButt)
buttonSave.grid(sticky='w', row=5, column=1, padx=10, pady=10)

buttonModif = Button(gui, text="Read", width=8, bd=3,
    fg='cyan', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='dark turquoise', command = modifList)
buttonModif.grid(sticky='e', row=5, column=1, padx=10, pady=10)

buttonDelete = Button(gui, text="Clear", width=8, bd=3,
    fg='cyan', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='dark turquoise', command = deleteTextbox)
buttonDelete.grid(sticky='w', row=5, column=2, padx=10, pady=10)

buttonQuit = Button(gui, text='Quit', width=8, bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='dark turquoise', command=quit)
buttonQuit.grid(sticky='e', row=5, column=3, padx=10, pady=10)

gui.mainloop()
