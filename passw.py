#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from subprocess import run


window = Tk()
window.title('ACCESS')
window.configure(bg='RoyalBlue4')

def closeWindow():
    """
        Class call from 
        heal_track.py !
    """
    window.destroy()

def validentry():
    """
        To validate entree
        from user.
    """
    namenter = entryname.get()
    passentry = entrypass.get()
    MSGBox = messagebox.askyesno('INFO', 'Do you want to validate for access ?')
    if MSGBox == 1:
        if entryname.get() == "root" and entrypass.get() == "root":
            messagebox.showinfo('INFO', 'Ok ! You get access !')
            closeWindow()
        # To escape close window...
        elif window == 0:
            messagebox.showwarning("Warning", "You couldn't close window !")
        else:
            messagebox.showwarning("Warning", "Password or Username failed !")

labelname = ttk.Label(window, text='Enter username :',
    font=('Times New Roman', 14, 'bold'),
    foreground="white", background="RoyalBlue4")
labelname.pack(pady=10)

entryname = StringVar()
namenter = ttk.Entry(window, textvariable=entryname)
namenter.pack(padx=10)

labelpass = ttk.Label(window, text='Enter password :',
    font=('Times New Roman', 14, 'bold'),
    foreground="white", background="RoyalBlue4")
labelpass.pack(pady=10)

entrypass = StringVar()
passentry = ttk.Entry(window, textvariable=entrypass)
passentry.pack(padx=10)

buttonvalidate = ttk.Button(window, text='Validate',
    command=validentry)
buttonvalidate.pack(pady=10)

mainloop()
