#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter
from tkinter import *
from tkinter import messagebox
import time
import os
import subprocess


root=Tk()
root.title("Care and monitoring")
root.configure(background='cyan')

# To place side by side labelo + entrylab
top = Frame(root, bg='cyan')
bottom = Frame(root, bg='cyan')
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

labelo=Label(root, text="Care and monitoring : ",
    font='Times 18 bold', fg='navy', bg='cyan')
labelo.pack(in_=top, side=LEFT, padx=5, pady=20)

labelallergy=Label(root, text="Allergy",
    font='Arial 18 bold', fg='coral', bg='cyan')
labelallergy.pack(padx=5, pady=5)

# To read name and allergy in Entry widget
with open('./newpatient/entryfile.txt', 'r') as filename:
    line_a=filename.readline()
    line_b=filename.readline()
    line_c=filename.readline()

text_name=StringVar()
Entryname=Entry(root, textvariable=text_name)
text_name.set(line_a)
Entryname.pack(in_=top, side=LEFT, padx=10, pady=20)

text_aller=StringVar()
text_aller.set(line_c)
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
    with open('./14besoins/doc_suivi/patient1_14b.txt', 'w') as namefile:
        namefile.write("En date du : ")
        namefile.write(time.strftime("%d/%m/%Y à %H:%M:%S :\n"))
    messagebox.showinfo("INFO", "Data saved !")
    print("+ Data saved !")
    ajouterText()

def saveData():
    """
        To record data from result.txt
        and from patient1_14b.txt into 
        txt main file
    """
    try:        
        if os.path.getsize('./14besoins/doc_suivi/main_14b.txt'):
            print("+ File 'main_14b.txt' exist !")
            with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as namefile:
                namefile.write(textBox.get("0.0", "end-1c") + '\n\n')
    except FileNotFoundError as outcom:
        print("+ Sorry, file 'main_14b.txt' not exist !")
        print(str(outcom))
        print("+ File 'main_14b.txt' created !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as namefile:
            namefile.write(textBox.get("0.0", "end-1c") + '\n\n')
    textBox.insert(INSERT, "\n---Data saved !---")
    suiteBackup()

def messFromSafeButt():
    MsgBox = messagebox.askquestion("Confirm","Are you sure ?\n"
        "It will save all data !")
    if MsgBox == 'yes':
        saveData()
    else:
        textBox.insert(INSERT, "\n---Nothing has been saved !---")
        print("+ Nothing has been saved !")

def lectureFic():
    with open('./14besoins/doc_suivi/patient1_14b.txt', 'r') as f1read:
        print(f1read.read())
    subprocess.run('./14besoins/doc_suivi/patient1_read.py', check=True)

def importationFile(fichier, encodage="Utf-8"):
    """
        To test if txt
        patient exist
    """
    try:        
        if os.path.getsize(fichier):
            print("+ File 'patient1_14b.txt' exist !")
            with open(fichier, 'r', encoding=encodage) as fileneeds:
                content=fileneeds.readlines()
                for li in content:
                    textBox.insert(END, li)
    except FileNotFoundError as outcom:
        print("+ Sorry, file 'main_14b.txt' not exist !")
        print(str(outcom))

textBox=Text(root, height=15, width=60, font=18, relief=SUNKEN)
#textBox.insert(INSERT, "En date du : ")
#textBox.insert(END, time.strftime("%d/%m/%Y à %H:%M:%S :"))
textBox.pack(padx=30, pady=30)

buttonLire=Button(root, text="Read", fg='cyan', bg='RoyalBlue3',
    activebackground='dark turquoise', activeforeground='navy',
    bd=3, width=10, highlightbackground='light sky blue', command=lectureFic)
buttonLire.pack(side='left', padx=10, pady=10)

buttonEnter=Button(root, text="Save", fg='yellow', bg='RoyalBlue3',
    activebackground='dark turquoise', activeforeground='navy',
    bd=3, width=10, highlightbackground='light sky blue', command=messFromSafeButt)
buttonEnter.pack(side='left', padx=10, pady=10)

buttonQuitter=Button(root, text="Quit", fg='white', bg='RoyalBlue3',
    width=10, activebackground='cyan', activeforeground='navy',
    bd=3, highlightbackground='light sky blue', command=quit)
buttonQuitter.pack(side='right', padx=10, pady=10)

try:
    if os.path.getsize('./14besoins/doc_suivi/patient1_14b.txt'):
        importationFile('./14besoins/doc_suivi/patient1_14b.txt', encodage='Utf-8')
except FileNotFoundError as err_nffile:
    print("+ File not found !")
    print(str(err_nffile))
    messagebox.showwarning("WARNING", "File does not exist or file not found !")

mainloop()
