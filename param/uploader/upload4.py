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
    pb.start(20)
    root.mainloop()

def process_unknown_duration(root):
    time.sleep(2)
    proc = subprocess.run(["scp", "./param/paramdata4.txt",
        "pi@192.168.18.12:~/tt_doc/doc_txt4/Files4/paramdata4.txt"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File paramdata4.txt uploaded !")
        #messagebox.showinfo("INFO", "paramdata4.txt uploaded...")
    else:
        print("+ No file to upload !")
        messagebox.showerror("Error", "No paramdata4.txt to upload...")

    secproc = subprocess.run(["scp", "./param/aspifile2/diastol.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt4/Files4/diastol.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("+ File diastol.json uploaded !")
        #messagebox.showinfo("INFO", "diastol.json uploaded...")
    else:
        print("+ No file to upload !")
        messagebox.showerror("Error", "No diastol.json to upload...")

    thirdproc = subprocess.run(["scp", "./param/aspifile2/systol.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt4/Files4/systol.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("+ File systol.json uploaded !")
        #messagebox.showinfo("INFO", "systol.json uploaded...")
    else:
        print("+ No file to upload !")
        messagebox.showerror("Error", "No systol.json to upload...")

    fourproc = subprocess.run(["scp", "./param/aspifile2/dlr.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt4/Files4/dlr.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(fourproc.stderr))
    if fourproc.stderr == b'':
        print("+ File dlr.json uploaded !")
        #messagebox.showinfo("INFO", "dlr.json uploaded...")
    else:
        print("+ No file to upload !")
        messagebox.showerror("Error", "No dlr.json to upload...")

    fiveproc = subprocess.run(["scp", "./param/aspifile2/freq.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt4/Files4/freq.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(fiveproc.stderr))
    if fiveproc.stderr == b'':
        print("+ File freq.json uploaded !")
        #messagebox.showinfo("INFO", "freq.json uploaded...")
    else:
        print("+ No file to upload !")
        messagebox.showerror("Error", "No freq.json to upload...")

    sixproc = subprocess.run(["scp", "./param/aspifile2/gly.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt4/Files4/gly.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(sixproc.stderr))
    if sixproc.stderr == b'':
        print("+ File gly.json uploaded !")
        #messagebox.showinfo("INFO", "gly.json uploaded...")
    else:
        print("+ No file to upload !")
        messagebox.showerror("Error", "No gly.json to upload...")

    sevenproc = subprocess.run(["scp", "./param/aspifile2/puls.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt4/Files4/puls.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(sevenproc.stderr))
    if sevenproc.stderr == b'':
        print("+ File puls.json uploaded !")
        #messagebox.showinfo("INFO", "puls.json uploaded...")
    else:
        print("+ No file to upload !")
        messagebox.showerror("Error", "No puls.json to upload...")

    eightproc = subprocess.run(["scp", "./param/aspifile2/sat.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt4/Files4/sat.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(eightproc.stderr))
    if eightproc.stderr == b'':
        print("+ File sat.json uploaded !")
        #messagebox.showinfo("INFO", "sat.json uploaded...")
    else:
        print("+ No file to upload !")
        messagebox.showerror("Error", "No sat.json to upload...")

    nineproc = subprocess.run(["scp", "./param/aspifile2/temp.json",
        "pi@192.168.18.12:~/tt_doc/doc_txt4/Files4/temp.json"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(nineproc.stderr))
    if nineproc.stderr == b'':
        print("+ File temp.json uploaded !")
        #messagebox.showinfo("INFO", "temp.json uploaded...")
    else:
        print("+ No file to upload !")
        messagebox.showerror("Error", "No temp.json to upload...")
    print('Upload done')
    root.quit()

def uploadata():
    root = tk.Tk()
    treat = threading.Thread(target=process_unknown_duration, args=(root,))
    treat.start()
    managetask(root)  # This will block while the mainloop runs
    treat.join()
    root.destroy()
