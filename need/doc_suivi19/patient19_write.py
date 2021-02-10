#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
import tkinter as tk
from tkinter import messagebox
import time
import os
import subprocess
from upload19 import needuploadata


root = tk.Tk()
root.title("Time-Track")
root.configure(background='DodgerBlue2')

# To place side by side labelo + entrylab
top = tk.Frame(root, bg='DodgerBlue2')
bottom = tk.Frame(root, bg='DodgerBlue2')
top.pack(side=tk.TOP)
bottom.pack(side=tk.BOTTOM, fill=BOTH, expand=YES)

labelo = tk.Label(root, text="Care and monitoring : ",
    font='Times 18 bold', fg='navy', bg='DodgerBlue2')
labelo.pack(in_=top, side=tk.LEFT, padx=5, pady=20)

with open('./newpatient/entryfile19.txt', 'r') as filename:
    line_a=filename.readline()
    line_b=filename.readline()
    line_c=filename.readline()

text_name = tk.StringVar()
Entryname = tk.Entry(root, textvariable=text_name)
text_name.set(line_a[:-1])
Entryname.pack(in_=top, side=tk.LEFT, padx=10, pady=20)

labelallergy = tk.Label(root, text="Allergy",
    font='Arial 18 bold', fg='coral', bg='DodgerBlue2')
labelallergy.pack(padx=5, pady=5)

text_aller = tk.StringVar()
Entryaller = tk.Entry(root, textvariable=text_aller, width=60)
text_aller.set(line_c[:-1])
Entryaller.pack(padx=10, pady=5)
def ajouterText():
    """
        To retrieve data 
        from initial textBox() 
    """
    textBox.delete('0.0', tk.END)
    textBox.insert(tk.INSERT, "En date du : ")
    textBox.insert(tk.END, time.strftime("%d/%m/%Y à %H:%M:%S :\n"))
    textBox.update()

def suiteBackup():
    """
        To save data into file patienx_14b.txt
        'ajouterText()' function is called at the end.
    """
    with open('./need/doc_suivi19/patient19_14b.txt', 'w') as namefile:
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
        if os.path.getsize('./need/doc_suivi19/main_14b.txt'):
            print("+ File 'main_14b.txt' exist !")
            with open('./need/doc_suivi19/main_14b.txt', 'a+') as namefile:
                namefile.write(textBox.get("0.0", "end-1c") + '\n\n')
    except FileNotFoundError as outcom:
        print("+ Sorry, file 'main_14b.txt' not exist !", outcom)
        print("+ File 'main_14b.txt' created !")
        with open('./need/doc_suivi19/main_14b.txt', 'a+') as namefile:
            namefile.write(textBox.get("0.0", "end-1c") + '\n\n')
    textBox.insert(tk.INSERT, "\n---Data saved !---")
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
        textBox.insert(tk.INSERT, "\n---Nothing has been saved !---")
        print("+ Nothing has been saved !")

def lectureFic():
    """
        To read file.
    """
    with open('./need/doc_suivi19/patient19_14b.txt', 'r') as f1read:
        print(f1read.read())
    subprocess.run('./need/doc_suivi19/patient19_read.py', check=True)

def importationFile(fichier, encodage="Utf-8"):
    """
        Import patientx_14b.txt file and read it.
    """
    try:        
        if os.path.getsize(fichier):
            print("+ File 'patient19_14b.txt' exist !")
            with open(fichier, 'r', encoding=encodage) as fileneeds:
                content=fileneeds.readlines()
                for li in content:
                    textBox.insert(tk.END, li)
    except FileNotFoundError as out_err:
        print("+ Sorry, file 'main_14b.txt' not exist !", out_err)

textBox = tk.Text(root, height=15, width=60, font=18, relief=SUNKEN)
textBox.pack(padx=30, pady=30)

buttonLire = tk.Button(root, text="Read", bd=3, width=10, 
    fg='cyan', bg='RoyalBlue3', activebackground='pale turquoise',
    activeforeground='navy', highlightbackground='light sky blue',
    command=lectureFic)
buttonLire.pack(side=tk.LEFT, padx=10, pady=10)

buttonEnter = tk.Button(root, text="Save", bd=3, width=10,
    fg='yellow', bg='RoyalBlue3', activebackground='pale turquoise',
    activeforeground='navy', highlightbackground='light sky blue',
    command=messFromSafeButt)
buttonEnter.pack(side=tk.LEFT, padx=10, pady=10)

buttonQuitter = tk.Button(root, text="Quit", bd=3, width=10,
    fg='white', bg='RoyalBlue3', activebackground='pale turquoise',
    activeforeground='navy', highlightbackground='light sky blue',
    command=quit)
buttonQuitter.pack(side=tk.RIGHT, padx=10, pady=10)

try:
    if os.path.getsize('./need/doc_suivi19/patient19_14b.txt'):
        importationFile('./need/doc_suivi19/patient19_14b.txt',
            encodage='Utf-8')
except FileNotFoundError as err_nffile:
    print(err_nffile)
    messagebox.showwarning("WARNING", "File does not exist or "
        "file not found !")

root.mainloop()
