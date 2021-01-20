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
    s = ttk.Style()
    s.theme_use('alt')
    s.configure('blue.Horizontal.TProgressbar',
        troughcolor = '#4d4d4d',
        troughrelief = 'flat',
        background = '#2f92ff')

    pb_hD = ttk.Progressbar(root,
        style = 'blue.Horizontal.TProgressbar',
        orient = 'horizontal',
        length = 200,
        mode = 'indeterminate')
    pb_hD.pack()
    pb_hD.start(20)
    root.mainloop()

def process_of_unknown_duration(root):
    """
        Define the process of unknown duration
        with root as one of the input And once
        done, add root.quit() at the end.
    """
    time.sleep(2)
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt22/paramdata22.txt",
        "./param/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt22/diastol.json",
        "./param/aspifile22/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    thirdproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt22/dlr.json",
        "./param/aspifile22/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    forthproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt22/freq.json",
        "./param/aspifile22/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    fivthproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt22/gly.json",
        "./param/aspifile22/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(fivthproc.stderr))
    sixthproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt22/puls.json",
        "./param/aspifile22/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(sixthproc.stderr))
    sevenproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt22/sat.json",
        "./param/aspifile22/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(sevenproc.stderr))
    eightproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt22/systol.json",
        "./param/aspifile22/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(eightproc.stderr))
    ninethproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt22/temp.json",
        "./param/aspifile22/"], stderr=subprocess.PIPE)
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
