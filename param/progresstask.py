#!/usr/bin/python3
# -*- coding : utf-8 -*-


from tkinter import *
import tkinter as tk
from tkinter import ttk
import time
import os
import sys
import subprocess
import threading


#Define your Progress Bar function, 
def task(root):
    root.title("Downloading")
    ft = ttk.Frame()
    ft.pack(expand=True, fill=BOTH, side=TOP)
    pb_hD = ttk.Progressbar(ft, length=200, orient='horizontal', mode='indeterminate')
    pb_hD.pack(expand=True, fill=BOTH, side=TOP)
    pb_hD.start(50)
    root.mainloop()

# Define the process of unknown duration with root as one of the input And once done,
# add root.quit() at the end.
def process_of_unknown_duration(root):
    time.sleep(0.1)
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt7/paramdata7.txt",
        "./param/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt7/diastol.json",
        "./param/aspifile7/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    thirdproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt7/dlr.json",
        "./param/aspifile7/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    forthproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt7/freq.json",
        "./param/aspifile7/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    fivthproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt7/gly.json",
        "./param/aspifile7/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(fivthproc.stderr))
    sixthproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt7/puls.json",
        "./param/aspifile7/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(sixthproc.stderr))
    sevenproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt7/sat.json",
        "./param/aspifile7/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(sevenproc.stderr))
    eightproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt7/systol.json",
        "./param/aspifile7/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(eightproc.stderr))
    ninethproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt7/temp.json",
        "./param/aspifile7/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(ninethproc.stderr))
    print('Done')
    # linux, mac
    print('My pid is', os.getpid())
    root.quit() # To destroy threading

def Main():
    root = tk.Tk()
    t1 = threading.Thread(target=process_of_unknown_duration, args=(root,))
    print(t1)
    t1.start()
    task(root) # This will block while the mainloop runs
    t1.join()
    root.destroy() # To destroy completely window
