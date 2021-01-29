#!/usr/bin/python3
# -*- coding : utf-8 -*-


"""
    Connecting the duration of progress bar
    with task = number of subprocess.
"""


from tkinter import *
import tkinter as tk
from tkinter import messagebox
import subprocess


def downloadttt1():
    """
        to download ttt files from server before
        to start with ttt interface.
    """
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt1/Files1/intro_ttt.txt",
        "./ttt/doc_ttt/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File intro_ttt.txt downloaded !")
        #messagebox.showinfo("INFO", "intro_ttt.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_ttt.txt to download")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt1/Files1/convdose.json",
        "./ttt/doc_ttt/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("+ convdose.json downloaded...")
        #messagebox.showinfo("INFO", "convdose.json downloaded")
    else:
        print("+ No convdose.json to download !")
        messagebox.showerror("Error", "No convdose.json to download !")

    thirdproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt1/Files1/intro_res.txt",
        "./ttt/doc_ttt/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("+ File intro_res.txt downloaded !")
        #messagebox.showinfo("INFO", "intro_res.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_res.txt to download")

    forthproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt1/Files1/convres.json",
        "./ttt/doc_ttt/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("+ File convres.json downloaded !")
        #messagebox.showinfo("INFO", "convres.json downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No convres.json to download")

def downloadttt2():
    """
        to download ttt files from server before
        to start with ttt interface.
    """
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt2/Files2/intro_ttt.txt",
        "./ttt/doc_ttt2/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File intro_ttt.txt downloaded !")
        #messagebox.showinfo("INFO", "intro_ttt.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_ttt.txt to download")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt2/Files2/convdose.json",
        "./ttt/doc_ttt2/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("+ convdose.json downloaded...")
        #messagebox.showinfo("INFO", "convdose.json downloaded")
    else:
        print("+ No convdose.json to download !")
        messagebox.showerror("Error", "No convdose.json to download !")

    thirdproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt2/Files2/intro_res.txt",
        "./ttt/doc_ttt2/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("+ File intro_res.txt downloaded !")
        #messagebox.showinfo("INFO", "intro_res.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_res.txt to download")

    forthproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt2/Files2/convres.json",
        "./ttt/doc_ttt2/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("+ File convres.json downloaded !")
        #messagebox.showinfo("INFO", "convres.json downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No convres.json to download")


