#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
import tkinter as tk
from tkinter import messagebox
import time
import os
import subprocess
from uploadiag1 import diagupload
#import sys


root = tk.Tk()
root.title("Diagnostics and ATCD")
root.configure(background='DodgerBlue2')

# To place side by side labelo + entrylab
top = tk.Frame(root, bg='DodgerBlue2')
bottom = tk.Frame(root, bg='DodgerBlue2')
top.pack(side=tk.TOP)
bottom.pack(side=tk.BOTTOM, fill=BOTH, expand=YES)

labelo = tk.Label(root, text="Diagnostics and ATCD for : ",
    font='Arial 18 bold', fg='white', bg='DodgerBlue2')
labelo.pack(in_=top, side=tk.LEFT, padx=5, pady=20)

with open('./newpatient/entryfile.txt', 'r') as filename:
    line_a=filename.readline()
    line_b=filename.readline()
    line_c=filename.readline()

textname = tk.StringVar()
entryName = tk.Entry(root, textvariable=textname)
textname.set(line_a[:-1])
entryName.pack(in_=top, side=tk.LEFT, padx=10, pady=20)

labelallergy = tk.Label(root, text="Allergy",
    font='Arial 18 bold', fg='coral', bg='DodgerBlue2')
labelallergy.pack(padx=5, pady=10)

entrytext = tk.StringVar()
entrytext.set(line_c[:-1])
entryName = tk.Entry(root, textvariable=entrytext, width=60)
entryName.pack(padx=10, pady=10)

def retrieve_input():
    file = open('./diag/doc_diag/diagrecap1.txt', 'w')
    file.write(textBox.get("1.0","end-1c") + "\n\n")
    file.close()

def retrieve_upload():
    diagupload()

def messFromSafeButt():
    MsgBox = messagebox.askquestion("Confirm","Are you sure ?\n"
        "It will save all data !")
    if MsgBox == 'yes':
        retrieve_input()
        retrieve_upload()
        textBox.insert(tk.INSERT, "\n---Data saved !---")
        print("+ Data saved !")
    else:
        textBox.insert(tk.INSERT, "Nothing has been saved !")
        print("+ Nothing has been saved !")

def lectureFic():
    file = open('./diag/doc_diag/diagrecap1.txt', 'r')
    print(file.read())
    file.close()
    subprocess.call('./diag/doc_diag/diag_read.py')

def importationFile(fichier, encodage="Utf-8"):
    file = open(fichier, 'r', encoding=encodage)
    content=file.readlines()
    file.close()
    for li in content:
        textBox.insert(tk.END, li)

textBox=Text(root, height=15, width=60, font=18, relief=SUNKEN)
#textBox.insert(tk.INSERT, "En date du : ")
#textBox.insert(tk.END, time.strftime("%d/%m/%Y à %H:%M:%S :\n"))
textBox.pack(padx=30, pady=30)

buttonLire = tk.Button(root, text="Read", width=10, bd=3,
    fg='cyan', bg='RoyalBlue3',
    activebackground='pale turquoise', activeforeground='navy',
    highlightbackground='light sky blue', command=lectureFic)
buttonLire.pack(side=tk.LEFT, padx=10, pady=10)

buttonEnter = tk.Button(root, text="Save", width=10, bd=3,
    fg='yellow', bg='RoyalBlue3',
    activebackground='pale turquoise', activeforeground='navy',
    highlightbackground='light sky blue', command=messFromSafeButt)
buttonEnter.pack(side=tk.LEFT, padx=10, pady=10)

buttonQuitter = tk.Button(root, text="Quit", width=10, bd=3,
    fg='white', bg='RoyalBlue3',
    activebackground='pale turquoise', activeforeground='navy',
    highlightbackground='light sky blue', command=quit)
buttonQuitter.pack(side=tk.RIGHT, padx=10, pady=10)

try:
    if os.path.getsize('./diag/doc_diag/diagrecap1.txt'):
        importationFile('./diag/doc_diag/diagrecap1.txt', 
            encodage="Utf-8")
except FileNotFoundError as err_file:
    print(err_file)
    messagebox.showwarning("WARNING", "File does not exist or " 
        "file not found !")

root.mainloop()
