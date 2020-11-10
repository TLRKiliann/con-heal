#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter
from tkinter import *
import os
import subprocess
import time
import shutil
from tkinter import messagebox


fen = Tk()
fen.title("Agenda")
fen.configure(background='cyan')

# To place side by side labelo + entrylab
top = Frame(fen, bg='cyan')
bottom = Frame(fen, bg='cyan')
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

labelo = Label(fen, text="Agenda",
    font='Arial 18 bold',
    fg='navy', bg='cyan')
labelo.pack(in_=top, side=LEFT, padx=5, pady=20)

with open('./newpatient/entryfile14.txt', 'r') as filename:
    line1 = filename.readline()

textname = StringVar()
entryName = Entry(fen, textvariable=textname)
textname.set(line1)
entryName.pack(in_=top, side=LEFT, padx=10, pady=20)

def importationFile(fichier):
    file = open(fichier, 'r')
    content = file.readlines()
    file.close()
    for li in content:
        textBox.insert(END, li)
        textBox.insert(END, '\n')
        textBox.delete('2.0')
        textBox.delete('end-3c')
        textBox.update()

def retrieve_input():
    """
        To retrieve data from messFromSafeButt() function
        to create a copy after backup and remove all files 
        that were used to create it.
    """
    inputValue = textBox.get("1.0", "end-1c" + '\n')
    print(inputValue)
    file = open('./patient_agenda/events14/doc_events/'\
        'fix_agenda/fixed_rdv.txt', 'w')
    file.write(textBox.get("1.0", "end-1c") + '\n\n')
    file.close()

    # Create the directory 
    # 'agenda_saved' in 
    # './patient_agenda/events14/doc_events/fix_agenda' 

    topath = './patient_agenda/events14/doc_events/'\
    'fix_agenda/agenda_saved'

    try:
        os.mkdir(topath)
    except OSError as err_alert:
        print(err_alert)
    
    origin_path = './patient_agenda/events14/doc_events/'\
    'fix_agenda/fixed_rdv.txt'
    main_path = './patient_agenda/events14/doc_events/'\
    'fix_agenda/agenda_saved/'

    files = [None] * 100
    for x in range(0, 100):
        files[x] = "file" + str(x) + ".txt"
        if not os.path.exists(main_path + files[x]):
            shutil.copy(origin_path, main_path + files[x])
            break
        elif os.path.exists(main_path + files[x]):
            x += 1
        else:
            print("+ Out of range !!! (more than 100 files)")
            break

    os.remove('./patient_agenda/events14/doc_events/fix_agenda/fixed_rdv.txt')
    os.remove('./patient_agenda/events14/doc_events/fix_agenda/patient_value.json')
    os.remove('./patient_agenda/events14/doc_events/patient_rdv.json')
    os.remove('./patient_agenda/events14/patient_calendar.txt')

    print("+ os.listdir after new file created : ")
    print(os.listdir('./patient_agenda/events14/doc_events/'\
        'fix_agenda/agenda_saved/'))
    
def messFromSafeButt():
    """
        To save data when user
        click button save.
    """
    MsgBox = messagebox.askquestion("Confirm","Are you sure ?\n"
        "It will save all data !")
    if MsgBox == 'yes':
        retrieve_input()
        textBox.insert(INSERT, "\n---Data saved !---")
        print("+ Data saved !")
    else:
        textBox.insert(INSERT, "Nothing has been saved !")
        print("+ Nothing has been saved !")

def lectureFic():
    """
        To read file, app open
        file fixed rdv to read on it.
    """
    subprocess.run('./patient_agenda/events14/doc_events/'\
        'fix_agenda/read_file.py', check=True)

def changeText():
    """
        To modify rdv in agenda.
    """
    subprocess.run('./patient_agenda/events14/doc_events/'\
        'fix_agenda/main.py', check=True)

textBox = Text(fen, height=15, width=60, font=18)
textBox.insert(INSERT, "Fixed on : ")
textBox.insert(END, time.strftime("%d/%m/%Y, %H:%M:%S") + ' :\n')
textBox.pack(padx=30, pady=30)

try:
    if os.path.getsize('./patient_agenda/events14/doc_events/'\
        'fix_agenda/patient_value.json'):
        print("+ File 'patient_value.json exist' !")
        importationFile('./patient_agenda/events14/doc_events/'\
            'fix_agenda/patient_value.json')
except FileNotFoundError as nf_file:
    print("+ File 'patient_value.json' does not exist !")
    print(nf_file)

buttonSave = Button(fen, text="Save", width=8, bd=3,
    fg='yellow', bg='RoyalBlue3',activebackground='dark turquoise',
    highlightbackground='light sky blue', command=messFromSafeButt)
buttonSave.pack(side='left', padx=10, pady=10)

buttonRead = Button(fen, text="Read", width=8, bd=3,
    fg='cyan', bg='RoyalBlue3', activebackground='dark turquoise',
    highlightbackground='light sky blue', command=lectureFic)
buttonRead.pack(side='left', padx=10, pady=10)

buttonDel = Button(fen, text="Modify RDV", width=10, bd=3,
    fg='cyan', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='dark turquoise', command=changeText)
buttonDel.pack(side='left', padx=10, pady=10)

buttonClose = Button(fen, text="Quit", width=8, bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='dark turquoise', command=quit)
buttonClose.pack(side='right', padx=10, pady=10)

fen.mainloop()
