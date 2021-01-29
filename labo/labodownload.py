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
        to download ttt files from server before
        to start with ttt interface.
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
