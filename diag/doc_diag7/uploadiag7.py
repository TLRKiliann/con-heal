#!/usr/bin/python3
# -*- coding : utf-8 -*-


from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess
import time
import threading


def managetask(root):
    root.title("Upload")
    style = ttk.Style()
    style.theme_use('alt')
    style.configure('blue.Horizontal.TProgressbar',
        troughcolor = '#4d4d4d',
        troughrelief = 'flat',
        background = '#2f92ff')

    pb = ttk.Progressbar(root,
        style = 'blue.Horizontal.TProgressbar',
        orient = 'horizontal',
        length = 200,
        mode = 'indeterminate')
    pb.pack()
    pb.start(10)
    root.mainloop()

def process_unknown_duration(root):
    """
        To upload file from doc_diag7 to server
    """
    time.sleep(1)
    proc = subprocess.run(["scp", "./diag/doc_diag7/diagrecap7.txt",
        "pi@192.168.18.12:~/tt_doc/doc_txt7/Files7/diagrecap7.txt"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File diagrecap7.txt uploaded !")
        #messagebox.showinfo("INFO", "diagrecap7.txt uploaded...")
    else:
        print("+ No file to upload !")
        messagebox.showerror("Error", "No diagrecap7.txt to upload...")
    root.quit()

def diagupload():
    root = tk.Tk()
    treat = threading.Thread(target=process_unknown_duration, args=(root,))
    treat.start()
    managetask(root)  # This will block while the mainloop runs
    treat.join()
    root.destroy()
