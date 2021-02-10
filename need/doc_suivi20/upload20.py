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
    time.sleep(1)
    proc = subprocess.run(["scp", "./need/doc_suivi20/main_14b.txt",
        "pi@192.168.18.12:~/tt_doc/doc_txt20/Files20/main_14b.txt"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File main_14b.txt uploaded !")
        #messagebox.showinfo("INFO", "main_14b.txt uploaded...")
    else:
        print("+ No file to upload !")
        messagebox.showerror("Error", "No main_14b.txt to upload...")

    secproc = subprocess.run(["scp", "./need/doc_suivi20/patient20_14b.txt",
        "pi@192.168.18.12:~/tt_doc/doc_txt20/Files20/patient20_14b.txt"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("+ File patient20_14b.txt uploaded !")
        #messagebox.showinfo("INFO", "patient20_14b.txt uploaded...")
    else:
        print("+ No file to upload !")
        messagebox.showerror("Error", "No patient20_14b.txt to upload...")
    print('Upload done !')
    root.quit()

def needuploadata():
    root = tk.Tk()
    treat = threading.Thread(target=process_unknown_duration, args=(root,))
    treat.start()
    managetask(root)  # This will block while the mainloop runs
    treat.join()
    root.destroy()
