#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from subprocess import run
from tt_download import launchdownload


window = tk.Tk()
window.style=ttk.Style()
window.title('ACCESS')
window.configure(bg='RoyalBlue3')

def hangonwin():
    """
        For security
        this function
        prevent to close
        window by x button
    """
    window.update()

window.protocol('WM_DELETE_WINDOW', hangonwin)

def closeWindow():
    """
        Class call from 
        heal_track.py !
    """
    window.destroy()
    launchdownload()


def validentry():
    """
        To validate entree
        from user.
    """
    namenter = entryname.get()
    passentry = getpass.get()
    MSGBox = messagebox.askyesno('INFO', 'Do you want to validate for access ?')
    if MSGBox == 1:
        if entryname.get() == "root" and getpass.get() == "root":
            messagebox.showinfo('INFO', 'Ok ! You get access !')
            closeWindow()
        elif entryname.get() == "koa" and getpass.get() == "tree":
            messagebox.showinfo('INFO', 'Ok ! You get access !')
            closeWindow()
        else:
            messagebox.showwarning("Warning", "Password or Username failed !")

labelname = ttk.Label(window, text='Enter username :',
    font=('Times New Roman', 14, 'bold'),
    foreground="white", background="RoyalBlue3")
labelname.pack(pady=10)

entryname = StringVar()
namenter = ttk.Entry(window, textvariable=entryname)
namenter.pack(padx=10)

labelpass = ttk.Label(window, text='Enter password :',
    font=('Times New Roman', 14, 'bold'),
    foreground="white", background="RoyalBlue3")
labelpass.pack(pady=10)

getpass = StringVar()
passentry = ttk.Entry(window, textvariable=getpass, show='*')
passentry.pack(padx=10)

buttonvalidate = tk.Button(window, text='Validate',
    foreground='yellow', background='navy',
    command=validentry)
buttonvalidate.pack(pady=10)

window.mainloop()
