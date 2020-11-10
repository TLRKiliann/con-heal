#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
from tkinter import messagebox
import os


fen=Tk()
fen.title("RDV set up")
fen.configure(background='cyan')

# To place side by side labelo + entrylab
top = Frame(fen, bg='cyan')
bottom = Frame(fen, bg='cyan')
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

labelo = Label(fen, text="RDV set up",
    font='Arial 18 bold', fg='navy', bg='cyan')
labelo.pack(in_=top, side=LEFT, padx=5, pady=20)

with open('./newpatient/entryfile19.txt', 'r') as filename:
    line1 = filename.readline()

textentry = StringVar()
textentry.set(line1)
entrylab = Entry(fen, textvariable=textentry)
entrylab.pack(in_=top, side=LEFT, padx=10, pady=20)

def msgBox():
    messagebox.showwarning('WARNING',
        'Error during function call for : ' + line1)

def importFilesFromDir():
    for path, dirs, files in os.walk('./patient_agenda/'
        'events19/doc_events/fix_agenda/agenda_saved/'):
        for file in files:
            read_f = open(os.path.join(path, file),'r')
            content = read_f.readlines()
            for li in content:
                li.replace('{', '')
                li.replace('}', '')
                textBox.insert(END, li)

textBox = Text(fen, height=15, width=60, font=18)
textBox.pack(padx=30, pady=30)

try:
    importFilesFromDir()
except OSError as io_err:
    print("+ Error for calling function !")
    print(io_err)
    msgBox()

buttonClose = Button(fen, text="Quit", width=8, bd=3,
    fg='white', bg='RoyalBlue3',
    highlightbackground='light sky blue',
    activebackground='dark turquoise', command=quit)
buttonClose.pack(side='right', padx=10, pady=10)

fen.mainloop()
