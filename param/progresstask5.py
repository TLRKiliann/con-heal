#!/usr/bin/python3
# -*- coding : utf-8 -*-


"""
    Connecting the duration of progress bar
    with task = number of subprocess.
"""


from tkinter import *
import tkinter as tk
from tkinter import ttk
import threading
import time
import subprocess
import os


def task(root):
    """
        Define Progress Bar function
    """
    root.title("Downloading")
    ft = ttk.Frame()
    ft.pack(expand=True, fill=BOTH, side=TOP)
    pb_hD = ttk.Progressbar(ft, length=200, orient='horizontal',
        mode='indeterminate', maximum=20)
    pb_hD.pack(expand=True, fill=BOTH, side=TOP)
    pb_hD.start(50)
    root.mainloop()

def process_of_unknown_duration(root):
    """
        Define the process of unknown duration
        with root as one of the input And once
        done, add root.quit() at the end.
    """
    time.sleep(0.2)
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt5/paramdata5.txt",
        "./param/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt5/diastol.json",
        "./param/aspifile5/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    thirdproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt5/dlr.json",
        "./param/aspifile5/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    forthproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt5/freq.json",
        "./param/aspifile5/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    fivthproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt5/gly.json",
        "./param/aspifile5/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(fivthproc.stderr))
    sixthproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt5/puls.json",
        "./param/aspifile5/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(sixthproc.stderr))
    sevenproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt5/sat.json",
        "./param/aspifile5/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(sevenproc.stderr))
    eightproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt5/systol.json",
        "./param/aspifile5/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(eightproc.stderr))
    ninethproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt5/temp.json",
        "./param/aspifile5/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(ninethproc.stderr))
    print('Done')
    # linux, mac
    print('My pid is', os.getpid())
    root.quit() # To destroy threading

def Main():
    """
        To start app with thread !
    """
    root = tk.Tk()
    t1 = threading.Thread(target=process_of_unknown_duration, args=(root,))
    #print(t1)
    t1.start()
    print("Download...")
    task(root) # This will block while the mainloop runs
    t1.join()
    root.destroy() # To destroy completely window
