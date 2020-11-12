#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from subprocess import run
from heal_track import Application


window = Tk()
window.title('ACCESS')
window.configure(bg='DodgerBlue2')

def closeWindow():
    """
        Class call from 
        heal_track.py !
    """
    window.destroy()
    Application()

def validentry():
    """
        To validate entree
        from user.
    """
    namenter = entryname.get()
    passentry = entrypass.get()
    MSGBox = messagebox.askyesno('INFO', 'Do you want to validate for access ?')
    if MSGBox == 1:
        if entryname.get() == "ck" and entrypass.get() == "123":
            messagebox.showinfo('INFO', 'Right, you get access !')
            closeWindow()
        else:
            messagebox.showinfo('INFO', 'Password or Username failed !')
            window.destroy()

labelname = Label(window, text='Enter username :',
    font=('Times New Roman', 14, 'bold'),
    foreground="white", background="DodgerBlue2")
labelname.pack(pady=10)

entryname = StringVar()
namenter = Entry(window, textvariable=entryname)
namenter.pack(padx=10)

labelpass = Label(window, text='Enter password :',
    font=('Times New Roman', 14, 'bold'),
    foreground="white", background="DodgerBlue2")
labelpass.pack(pady=10)

entrypass = StringVar()
passentry = Entry(window, textvariable=entrypass)
passentry.pack(padx=10)

buttonvalidate = Button(window, text='Validate',
    command=validentry)
buttonvalidate.pack(pady=10)

mainloop()
