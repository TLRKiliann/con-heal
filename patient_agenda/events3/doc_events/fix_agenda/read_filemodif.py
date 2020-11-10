#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
from tkinter import messagebox
import os


fen=Tk()
fen.title("RDV have changed")
fen.configure(background='cyan')

# To place side by side labelo + entrylab
top=Frame(fen, bg='cyan')
bottom=Frame(fen, bg='cyan')
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

labelo=Label(fen, text="RDV have changed",
    font='Arial 18 bold', fg='navy', bg='cyan')
labelo.pack(in_=top, side=LEFT, padx=5, pady=20)

with open('./newpatient/entryfile3.txt', 'r') as filename:
    line1=filename.readline()

textname=StringVar()
entryName=Entry(fen, textvariable=textname)
textname.set(line1)
entryName.pack(in_=top, side=LEFT, padx=10, pady=20)

def msgBox():
    messagebox.showwarning('WARNING',
        'Error during function call for : ' + line1)

def importFilesFromDir():
    for path, dirs, files in os.walk('./patient_agenda/events3/doc_events/'
        'fix_agenda/agenda_saved/'):
        for file in files:
            read_f = open(os.path.join(path,file),'r')
            content = read_f.readlines()
            for li in content:
                li.replace('{', '')
                li.replace('}', '')
                textBox.insert(END, li)

textBox=Text(fen, height=15, width=60, font=18)
textBox.pack(padx=30, pady=30)

try:
    importFilesFromDir()
except OSError as io_err:
    print("+ Error for calling function !")
    print(io_err)
    msgBox()

def saveData():
    with open('./patient_agenda/events3/doc_events/'
        'fix_agenda/modifrdv.txt', 'w') as textfile2:
        textfile2.writelines(textBox.get("0.0", "end-1c") + "\n")

buttonSave=Button(fen, text="Save", width=8, bd=3,
    fg='yellow', bg='navy',
    activebackground='dark turquoise', 
    highlightbackground='light sky blue', command=saveData)
buttonSave.pack(side='left', padx=10, pady=10)

buttonClose=Button(fen, text="Quit", width=8, bd=3,
    fg='white', bg='navy', activebackground='dark turquoise',
    highlightbackground='light sky blue', command=quit)
buttonClose.pack(side='right', padx=10, pady=10)

fen.mainloop()
