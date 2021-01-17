#!/usr/bin/python3
# -*- coding : utf-8 -*-


import tkinter as tk
from tkinter import ttk
from time import sleep
import subprocess

teams = range(4)

def button_command():

    popup = tk.Tk()
    popup.title("Loading window")
    popup.configure(bg="DodgerBlue2")
    tk.Label(popup, text="Loading...").grid(row=0,column=0)

    progress = 0
    progress_var = tk.DoubleVar()
    progress_bar = ttk.Progressbar(popup, length=300, variable=progress_var, maximum=4)
    progress_bar.grid(row=1, column=0)#.pack(fill=tk.X, expand=1, side=tk.BOTTOM)
    popup.pack_slaves()

    progress_step = float(5.5/len(teams))
    for team in teams:
        popup.update()
        sleep(1) # launch task
        progress += progress_step
        progress_var.set(progress)

    #Y a pas plus propre ? Non, je ne crois pas (pas trouvé mieux pour le moment...)
    #cmd = 'python3 angel.py'
    #os.system(cmd)
    #Oui il y a mieux! subprocess passe par POSIX.sh et il retourne les erreurs python
    #dans la console contrairement à os.system qui lui est par défaut et ne prend pas le 
    #même chemin d'accès.
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
    #popup.destroy()
    return 0

button_command()
