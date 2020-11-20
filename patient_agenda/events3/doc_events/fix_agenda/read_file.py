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
top2 = Frame(fen, bg='cyan3')
top3 = Frame(fen, bg='cyan3')
bottom = Frame(fen, bg='cyan')
top.pack(side=TOP)
top2.pack(side=TOP)
top3.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

labelo = Label(fen, text="Appointments",
    font='Arial 18 bold', fg='navy', bg='cyan')
labelo.pack(in_=top, side=LEFT, pady=5)

with open('./newpatient/entryfile3.txt', 'r') as filename:
    line1 = filename.readline()

textentry = StringVar()
entrylab = Entry(fen, textvariable=textentry, width=20, 
    highlightbackground='grey', bd=3)
textentry.set(line1)
entrylab.pack(in_=top, side=LEFT, padx=10, pady=10)

def janSearch():
    pass

buttonJan = Button(fen, text="Jan", font='Arial 12 bold', bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='dark turquoise',
    command=janSearch)
buttonJan.pack(in_=top2, side=LEFT, padx=10, pady=10)

def febSearch():
    pass

buttonFeb = Button(fen, text="Feb", font='Arial 12 bold', bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='dark turquoise',
    command=febSearch)
buttonFeb.pack(in_=top2, side=LEFT, padx=10, pady=10)

def marSearch():
    pass

buttonMar = Button(fen, text="Mar", font='Arial 12 bold', bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='dark turquoise',
    command=marSearch)
buttonMar.pack(in_=top2, side=LEFT, padx=10, pady=10)

def avrSearch():
    pass

buttonAvr = Button(fen, text="Avr", font='Arial 12 bold', bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='dark turquoise',
    command=avrSearch)
buttonAvr.pack(in_=top2, side=LEFT, padx=10, pady=10)

def maiSearch():
    pass

buttonMay = Button(fen, text="May", font='Arial 12 bold', bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='dark turquoise',
    command=maiSearch)
buttonMay.pack(in_=top2, side=LEFT, padx=10, pady=10)

def junSearch():
    pass

buttonJun = Button(fen, text="Jun", font='Arial 12 bold', bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='dark turquoise',
    command=junSearch)
buttonJun.pack(in_=top2, side=LEFT, padx=10, pady=10)

def julSearch():
    pass

buttonJul = Button(fen, text="Jul", font='Arial 12 bold', bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='dark turquoise',
    command=julSearch)
buttonJul.pack(in_=top3, side=LEFT, padx=10, pady=10)

def augSearch():
    pass

buttonAug = Button(fen, text="Aug", font='Arial 12 bold', bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='dark turquoise',
    command=augSearch)
buttonAug.pack(in_=top3, side=LEFT, padx=10, pady=10)

def sepSearch():
    pass

buttonSep = Button(fen, text="Sep", font='Arial 12 bold', bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='dark turquoise',
    command=sepSearch)
buttonSep.pack(in_=top3, side=LEFT, padx=10, pady=10)

def octSearch():
    pass

buttonOct = Button(fen, text="Oct", font='Arial 12 bold', bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='dark turquoise',
    command=octSearch)
buttonOct.pack(in_=top3, side=LEFT, padx=10, pady=10)

def novSearch():
    pass

buttonNov = Button(fen, text="Nov", font='Arial 12 bold', bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='dark turquoise',
    command=novSearch)
buttonNov.pack(in_=top3, side=LEFT, padx=10, pady=10)

def decSearch():
    pass

buttonDec = Button(fen, text="Dec", font='Arial 12 bold', bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='dark turquoise',
    command=decSearch)
buttonDec.pack(in_=top3, side=LEFT, padx=10, pady=10)

def msgBox():
    messagebox.showwarning('WARNING',
        'Error during function call for : ' + line1)

def importFilesFromDir():
    for path, dirs, files in os.walk('./patient_agenda/'\
        'events3/doc_events/fix_agenda/agenda_saved/'):
        for file in files:
            read_f = open(os.path.join(path, file),'r')
            content = read_f.readlines()
            for li in content:
                li.replace('{', '')
                li.replace('}', '')
                textBox.insert(END, li)

textBox = Text(fen, height=20, width=60, font=18)
textBox.pack(in_=bottom, padx=20, pady=10)

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
buttonClose.pack(in_=bottom, side='right', padx=20, pady=10)

fen.mainloop()
