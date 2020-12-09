#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
from tkinter import messagebox
import os


fen=Tk()
fen.title("Time-Track")
fen.configure(background='DodgerBlue2')

# To place side by side labelo + entrylab
top = Frame(fen, bg='DodgerBlue2')
bottom = Frame(fen, bg='DodgerBlue2')
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

labelo=Label(fen, text="Care and monitoring : ",
    font='Times 18 bold', fg='navy', bg='DodgerBlue2')
labelo.pack(in_=top, side=LEFT, padx=5, pady=20)

# To read name in Entry widget
with open('./newpatient/entryfile2.txt', 'r') as filename:
    line_a=filename.readline()
    line_b=filename.readline()
    line_c=filename.readline()

text_name=StringVar()
text_name.set(line_a[:-1])
Entryname=Entry(fen, textvariable=text_name)
Entryname.pack(in_=top, side=LEFT, padx=10, pady=20)

labelallergy=Label(fen, text="Allergy",
    font='Arial 18 bold', fg='coral', bg='DodgerBlue2')
labelallergy.pack(padx=5, pady=5)

text_all=StringVar()
text_all.set(line_c[:-1])
Entryall=Entry(fen, textvariable=text_all, width=60)
Entryall.pack(padx=10, pady=5)

def importationFile(fichier, encodage="Utf-8"):
    file = open(fichier, 'r', encoding=encodage)
    content=file.readlines()
    file.close()
    for li in content:
        textBox.insert(END, li)

textBox=Text(fen, height=15, width=60, font=18, relief=SUNKEN)
textBox.pack(padx=30, pady=30)

buttonClose=Button(fen, text="Quit", width=10, bd=3,
    fg='white', bg='RoyalBlue3',
    activebackground='dark turquoise', activeforeground='navy',
    highlightbackground='light sky blue', command=quit)
buttonClose.pack(side='right', padx=10, pady=10)

try:
    if os.path.getsize('./14besoins/doc_suivi2/main_14b.txt'):
        importationFile('./14besoins/doc_suivi2/main_14b.txt',
            encodage="Utf-8")
except FileNotFoundError as err_nffile:
    print(err_nffile)
    messagebox.showwarning("WARNING", "File does not exist or "
        "file not found !")

fen.mainloop()
