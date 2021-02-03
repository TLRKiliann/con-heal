#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter
from tkinter import *
from tkinter import messagebox
import time
import os
import subprocess
from need_upload.uploadbar import uploadmain
from need_upload.upload22 import needuploadata


root=Tk()
root.title("Time-Track")
root.configure(background='DodgerBlue2')

# To place side by side labelo + entrylab
top = Frame(root, bg='DodgerBlue2')
bottom = Frame(root, bg='DodgerBlue2')
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

labelo=Label(root, text="Care and monitoring : ",
    font='Times 18 bold', fg='navy', bg='DodgerBlue2')
labelo.pack(in_=top, side=LEFT, padx=5, pady=20)

with open('./newpatient/entryfile22.txt', 'r') as filename:
    line_a=filename.readline()
    line_b=filename.readline()
    line_c=filename.readline()

text_name=StringVar()
Entryname=Entry(root, textvariable=text_name)
text_name.set(line_a[:-1])
Entryname.pack(in_=top, side=LEFT, padx=10, pady=20)

labelallergy=Label(root, text="Allergy",
    font='Arial 18 bold', fg='coral', bg='DodgerBlue2')
labelallergy.pack(padx=5, pady=5)

text_aller=StringVar()
text_aller.set(line_c[:-1])
Entryaller=Entry(root, textvariable=text_aller, width=60)
Entryaller.pack(padx=10, pady=5)

def ajouterText():
    """
        To retrieve data 
        from initial textBox() 
    """
    textBox.delete('0.0', END)
    textBox.insert(INSERT, "En date du : ")
    textBox.insert(END, time.strftime("%d/%m/%Y à %H:%M:%S :\n"))
    textBox.update()

def suiteBackup():
    """
        To save data into file patienx_14b.txt
        'ajouterText()' function is called at the end.
    """
    with open('./need/doc_suivi22/patient22_14b.txt', 'w') as namefile:
        namefile.write("En date du : ")
        namefile.write(time.strftime("%d/%m/%Y à %H:%M:%S :\n"))
    messagebox.showinfo("INFO", "Data saved !")
    print("+ Data saved !")
    ajouterText()

def uploadfunc():
    needuploadata()

def saveData():
    """
        Test if file main_14b.txt exist and write data.
        A msg into textbox appear to informate user that
        data have been saved.
        'suiteBackup()' function is called at the end.
    """
    try:        
        if os.path.getsize('./need/doc_suivi22/main_14b.txt'):
            print("+ File 'main_14b.txt' exist !")
            with open('./need/doc_suivi22/main_14b.txt', 'a+') as namefile:
                namefile.write(textBox.get("0.0", "end-1c") + '\n\n')
    except FileNotFoundError as outcom:
        print("+ Sorry, file 'main_14b.txt' not exist !", outcom)
        print("+ File 'main_14b.txt' created !")
        with open('./need/doc_suivi22/main_14b.txt', 'a+') as namefile:
            namefile.write(textBox.get("0.0", "end-1c") + '\n\n')
    textBox.insert(INSERT, "\n---Data saved !---")
    suiteBackup()
    uploadfunc()

def messFromSafeButt():
    """
        To save data with button 'save'
        and to get function 'saveData()'
        if user wish to save. Else, user
        will be informed that data aren't 
        saved.
    """
    MsgBox = messagebox.askquestion("Confirm","Are you sure ?\n"
        "It will save all data !")
    if MsgBox == 'yes':
        saveData()
    else:
        textBox.insert(INSERT, "\n---Nothing has been saved !---")
        print("+ Nothing has been saved !")

def lectureFic():
    """
        To read file.
    """
    with open('./need/doc_suivi22/patient22_14b.txt', 'r') as f1read:
        print(f1read.read())
    subprocess.run('./need/doc_suivi22/patient22_read.py', check=True)

def importationFile(fichier, encodage="Utf-8"):
    """
        Import patientx_14b.txt file and read it.
    """
    try:        
        if os.path.getsize(fichier):
            print("+ File 'patient22_14b.txt' exist !")
            with open(fichier, 'r', encoding=encodage) as fileneeds:
                content=fileneeds.readlines()
                for li in content:
                    textBox.insert(END, li)
    except FileNotFoundError as out_err:
        print("+ Sorry, file 'main_14b.txt' not exist !", out_err)

textBox=Text(root, height=15, width=60, font=18, relief=SUNKEN)
textBox.pack(padx=30, pady=30)

buttonLire=Button(root, text="Read", bd=3, width=10, 
    fg='cyan', bg='RoyalBlue3', activebackground='pale turquoise',
    activeforeground='navy', highlightbackground='light sky blue',
    command=lectureFic)
buttonLire.pack(side='left', padx=10, pady=10)

buttonEnter=Button(root, text="Save", bd=3, width=10,
    fg='yellow', bg='RoyalBlue3', activebackground='pale turquoise',
    activeforeground='navy', highlightbackground='light sky blue',
    command=messFromSafeButt)
buttonEnter.pack(side='left', padx=10, pady=10)

buttonQuitter=Button(root, text="Quit", bd=3, width=10,
    fg='white', bg='RoyalBlue3', activebackground='pale turquoise',
    activeforeground='navy', highlightbackground='light sky blue',
    command=quit)
buttonQuitter.pack(side='right', padx=10, pady=10)

try:
    if os.path.getsize('./need/doc_suivi22/patient22_14b.txt'):
        importationFile('./need/doc_suivi22/patient22_14b.txt',
            encodage='Utf-8')
except FileNotFoundError as err_nffile:
    print(err_nffile)
    messagebox.showwarning("WARNING", "File does not exist or "
        "file not found !")

mainloop()
