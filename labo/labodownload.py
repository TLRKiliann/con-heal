#!/usr/bin/python3
# -*- coding : utf-8 -*-


"""
    Connecting the duration of progress bar
    with task = number of subprocess.
"""


from tkinter import messagebox
from labo.labobar import labodata
import subprocess


def labodownload1():
    """
        to download labo files from server before
        to start with labo interface.
    """
    labodata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt1/Files1/patient1_14b.txt",
        "./14besoins/doc_suivi/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File patient1_14b.txt downloaded !")
        messagebox.showinfo("INFO", "patient1_14b.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No patient1_14b.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt1/Files1/result.txt",
        "./labo/doc_labo/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("+ File result.txt downloaded !")
        messagebox.showinfo("INFO", "result.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No result.txt to download !")
