#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
from tkinter import messagebox
import sys


fen = Tk()
fen.title("Reader BMI")
fen.configure(background='DodgerBlue2')

# To place side by side labelo + entrylab
top = Frame(fen, bg='DodgerBlue2')
bottom = Frame(fen, bg='DodgerBlue2')
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

labelo = Label(fen, text="BMI results : ", width=15,
    font='Times 18 bold', fg='white', bg='DodgerBlue2')
labelo.pack(in_=top, side=LEFT, pady=20)

labelallergy = Label(fen, text="Allergy",
    font='Arial 18 bold', fg='coral', bg='DodgerBlue2')
labelallergy.pack(padx=5, pady=5)

# To read name in Entry widget
with open('./newpatient/entryfile24.txt', 'r') as filename:
    line_a = filename.readline()
    line_b = filename.readline()
    line_c = filename.readline()

text_name = StringVar()
text_name.set(line_a[:-1])
Entryname = Entry(fen, textvariable=text_name)
Entryname.pack(in_=top, side=LEFT, pady=20)

text_all = StringVar()
text_all.set(line_c[:-1])
Entryall = Entry(fen, textvariable=text_all, width=60)
Entryall.pack(padx=10, pady=5)

def importationFile(fichier, encodage="Utf-8"):
    file = open(fichier, 'r', encoding=encodage)
    content = file.readlines()
    file.close()
    for li in content:
        textBox.insert(END, li)

def msgBox():
    messagebox.showinfo('Info', 'File bmi24.txt does not exist')

textBox = Text(fen, height=15, width=60, font=18)
textBox.pack(padx=30, pady=30)

buttonClose = Button(fen, text="Quit", width=10, bd=3,
    fg='cyan', bg='RoyalBlue3', activebackground='pale turquoise', 
    activeforeground='navy', highlightbackground='cyan',
    command=quit)
buttonClose.pack(side='right', padx=10, pady=10)

try:
    importationFile('./calBmi/bmi24.txt', encodage="Utf-8")
except FileNotFoundError as error_call:
    print("+ Import bmi.txt for " + line_a + " failed !")
    msgBox()

fen.mainloop()
