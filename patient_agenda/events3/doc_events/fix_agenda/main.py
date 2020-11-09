#!/usr/bin/python3
# -*- coding:utf-8 -*-


import tkinter
from tkinter import *
import time
import json
import os
import subprocess
from tkinter import messagebox
from itertools import *


gui = Tk()

gui.title("Save changes !")
gui.configure(bg='cyan')

labelTit = Label(gui)
labelTit = Label(text="Save changes !", font=("Arial 16 bold"),
    fg='navy', bg='cyan')
labelTit.grid(sticky='e', row=0, column=1, pady=10)

labelDate = Label(gui)
labelDate = Label(text='Search date to modify : ', font='12', 
    fg='navy', bg='cyan')
labelDate.grid(sticky='e', row=1, column=1)

with open('./newpatient/entryfile3.txt', 'r') as filename:
    line1 = filename.readline()

textname = StringVar()
entryName = Entry(gui, textvariable=textname)
textname.set(line1)
entryName.grid(row=0, column=2, pady=10)

def searchExpress():
    """
        To read multiples files in a directory
    """
    mot = regexpi_var.get()
    for path, dirs, files in os.walk('./patient_agenda/events3/doc_events/'
        'fix_agenda/agenda_saved/'):
        for file in files:
            read_f = open(os.path.join(path, file), 'r')
            lines = read_f.readlines()
            for i in range(len(lines)):
                line = lines[i]
                if mot in line:
                    print("Nous y voici !") 
                    print(lines[i])
                    print(lines[i+1])
                    textBox.insert(INSERT, lines[i])
                    textBox.insert(INSERT, lines[i+1])
                    textBox.insert(INSERT, lines[i+2])

def save_input():
    """
        Save data from modification rdv textbox !
        To copy to a txt file of a directory
        since a read file and from text widget
        by lines ;) !
    """
    magicword = regexpi_var.get()
    for path, dirs, files in os.walk('./patient_agenda/events3/doc_events/'
        'fix_agenda/agenda_saved/'):
        for file in files:
            read_f = open(os.path.join(path, file), 'r')
            for line in read_f:
                for i in line:
                    noway = "Fixed on :"
                    if line[0:10] == noway:
                        print("+ There is noway : ")
                        print(line[0:10])
                        write_f = open(os.path.join(path, file), 'a+')
                    elif magicword in line:
                        print("+ It is magicword : ")
                        print(line[0:10])
                        write_f = open(os.path.join(path, file), 'a+')
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
    subprocess.run('./patient_agenda/events3/doc_events/fix_agenda/'
        'read_filemodif.py', check=True)

def deleteTextbox():
    textBox.delete('0.0', "end-1c")

reachDate = Entry(gui)
regexpi_var = StringVar()
reachDate = Entry(textvariable=regexpi_var)
reachDate.grid(row=1, column=2, padx=5, pady=10)

buttonSearch = Button(gui)
buttonSearch = Button(text='Search', width=8, bd=3,
    fg='yellow', bg='navy', highlightbackground='light sky blue',
    activebackground='dark turquoise', command=searchExpress)
buttonSearch.grid(row=1, column=3, padx=5)

textBox = Text(gui, height=15, width=60, font=18)
textBox.grid(row=4, column=1, columnspan=3, padx=30, pady=30)

buttonSave = Button(gui, text="1-Save", width=8, bd=3,
    fg='yellow', bg='navy', highlightbackground='light sky blue',
    activebackground='dark turquoise', command = messFromSafeButt)
buttonSave.grid(sticky='w', row=5, column=1, padx=10, pady=10)

buttonModif = Button(gui, text="2-Read changes", width=12, bd=3,
    fg='yellow', bg='navy', highlightbackground='light sky blue',
    activebackground='dark turquoise', command = modifList)
buttonModif.grid(sticky='e', row=5, column=1, padx=10, pady=10)

buttonDelete = Button(gui, text="Clear", width=8, bd=3,
    fg='cyan', bg='navy', highlightbackground='light sky blue',
    activebackground='dark turquoise', command = deleteTextbox)
buttonDelete.grid(sticky='w', row=5, column=2, padx=10, pady=10)

buttonQuit = Button(gui)
buttonQuit = Button(text='Quit', width=8, bd=3,
    fg='white', bg='navy', highlightbackground='light sky blue',
    activebackground='dark turquoise', command=quit)
buttonQuit.grid(sticky='e', row=5, column=3, padx=10, pady=10)

gui.mainloop()
