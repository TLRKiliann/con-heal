#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
from tkinter import messagebox
import time
import os
import subprocess


root=Tk()
root.title("Diagnostics and ATCD")
root.configure(background='cyan')

# To place side by side labelo + entrylab
top = Frame(root, bg='cyan')
bottom = Frame(root, bg='cyan')
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

labelo=Label(root, text="Diagnostics and ATCD for : ",
    font='Arial 18 bold', fg='navy', bg='cyan')
labelo.pack(in_=top, side=LEFT, padx=5, pady=20)

with open('./newpatient/entryfile14.txt', 'r') as filename:
    line_a=filename.readline()
    line_b=filename.readline()
    line_c=filename.readline()

textname=StringVar()
entryName=Entry(root, textvariable=textname)
textname.set(line_a[:-1])
entryName.pack(in_=top, side=LEFT, padx=10, pady=20)

labelallergy=Label(root, text="Allergy",
    font='Arial 18 bold', fg='coral', bg='cyan')
labelallergy.pack(padx=5, pady=10)

entrytext=StringVar()
entrytext.set(line_c[:-1])
entryName=Entry(root, textvariable=entrytext, width=60)
entryName.pack(padx=10, pady=10)

def retrieve_input():
    file = open('./diag/doc_diag14/diagrecap14.txt', 'w')
    file.write(textBox.get("1.0","end-1c") + "\n\n")
    file.close()

def messFromSafeButt():
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
    file = open('./diag/doc_diag14/diagrecap14.txt', 'r')
    print(file.read())
    file.close()
    subprocess.call('./diag/doc_diag14/diag_read.py')

def importationFile(fichier, encodage="Utf-8"):
    file = open(fichier, 'r', encoding=encodage)
    content=file.readlines()
    file.close()
    for li in content:
        textBox.insert(END, li)

textBox=Text(root, height=15, width=60, font=18, relief=SUNKEN)
#textBox.insert(INSERT, "En date du : ")
#textBox.insert(END, time.strftime("%d/%m/%Y à %H:%M:%S :\n"))
textBox.pack(padx=30, pady=30)

buttonLire=Button(root, text="Read", width=10, bd=3,
    fg='cyan', bg='RoyalBlue3',
    activebackground='dark turquoise', activeforeground='navy',
    highlightbackground='light sky blue', command=lectureFic)
buttonLire.pack(side='left', padx=10, pady=10)

buttonEnter=Button(root, text="Save", width=10, bd=3,
    fg='yellow', bg='RoyalBlue3',
    activebackground='dark turquoise', activeforeground='navy',
    highlightbackground='light sky blue', command=messFromSafeButt)
buttonEnter.pack(side='left', padx=10, pady=10)

buttonQuitter=Button(root, text="Quit", width=10, bd=3,
    fg='white', bg='RoyalBlue3',
    activebackground='cyan', activeforeground='navy',
    highlightbackground='light sky blue', command=quit)
buttonQuitter.pack(side='right', padx=10, pady=10)

try:
    if os.path.getsize('./diag/doc_diag14/diagrecap14.txt'):
        importationFile('./diag/doc_diag14/diagrecap14.txt', 
            encodage="Utf-8")
except FileNotFoundError as err_file:
    print(err_file)
    messagebox.showwarning("WARNING", "File does not exist or "
        "file not found !")

mainloop()
