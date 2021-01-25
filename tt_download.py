#!/usr/bin/python3
# -*- coding : utf-8 -*-


"""
    Connecting the duration of progress bar
    with task = number of subprocess.
"""


from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import threading
import time
import subprocess
import os
from shootransfert import loaderfile


def task(root):
    """
        Define Progress Bar function
    """
    root.title("Downloading")
    style = ttk.Style()
    style.theme_use('alt')
    style.configure('blue.Horizontal.TProgressbar',
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
    proc = subprocess.run(["scp", "-r", "pi@192.168.18.12:~/tt_doc/doc_txt1/Files1",
        "./Backup/"], stderr=subprocess.PIPE, check=True)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ Folder Files1 downloaded...")
        #messagebox.showinfo("INFO", "paramdata7.txt downloaded")
    else:
        print("+ No folder Files1 to download !")
        messagebox.showerror("Error", "No folder Files1 to download !")

    secproc = subprocess.run(["scp", "-r", "pi@192.168.18.12:~/tt_doc/doc_txt2/Files2",
        "./Backup/"], stderr=subprocess.PIPE, check=True)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("+ Folder Files2 downloaded...")
        #messagebox.showinfo("INFO", "diastol.json downloaded")
    else:
        print("+ No folder Files2 to download !")
        messagebox.showerror("Error", "No folder Files2 to download !")

    thirdproc = subprocess.run(["scp", "-r", "pi@192.168.18.12:~/tt_doc/doc_txt3/Files3",
        "./Backup/"], stderr=subprocess.PIPE, check=True)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("+ Folder Files3 downloaded...")
        #messagebox.showinfo("INFO", "dlr.json downloaded")
    else:
        print("+ No folder Files3 to download !")
        messagebox.showerror("Error", "No folder Files3 to download !")

    forthproc = subprocess.run(["scp", "-r", "pi@192.168.18.12:~/tt_doc/doc_txt4/Files4",
        "./Backup/"], stderr=subprocess.PIPE, check=True)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("+ Folder Files4 downloaded...")
        #messagebox.showinfo("INFO", "freq.json downloaded")
    else:
        print("+ No folder Files4 to download !")
        messagebox.showerror("Error", "No folder Files4 to download !")

    fivthproc = subprocess.run(["scp", "-r", "pi@192.168.18.12:~/tt_doc/doc_txt5/Files5",
        "./Backup/"], stderr=subprocess.PIPE, check=True)
    print("Result SCP transfert : %s" % repr(fivthproc.stderr))
    if fivthproc.stderr == b'':
        print("+ Folder Files5 downloaded...")
        #messagebox.showinfo("INFO", "gly.json downloaded")
    else:
        print("+ No folder Files5 to download !")
        messagebox.showerror("Error", "No folder Files5 to download !")

    sixthproc = subprocess.run(["scp", "-r", "pi@192.168.18.12:~/tt_doc/doc_txt6/Files6",
        "./Backup/"], stderr=subprocess.PIPE, check=True)
    print("Result SCP transfert : %s" % repr(sixthproc.stderr))
    if sixthproc.stderr == b'':
        print("+ Folder Files6 downloaded...")
        #messagebox.showinfo("INFO", "puls.json downloaded")
    else:
        print("+ No folder Files6 to download !")
        messagebox.showerror("Error", "No folder Files6 to download !")

    sevenproc = subprocess.run(["scp", "-r", "pi@192.168.18.12:~/tt_doc/doc_txt7/Files7",
        "./Backup/"], stderr=subprocess.PIPE, check=True)
    print("Result SCP transfert : %s" % repr(sevenproc.stderr))
    if sevenproc.stderr == b'':
        print("+ Folder Files7 downloaded...")
        #messagebox.showinfo("INFO", "sat.json downloaded")
    else:
        print("+ No folder Files7 to download !")
        messagebox.showerror("Error", "No folder Files7 to download !")

    eightproc = subprocess.run(["scp", "-r", "pi@192.168.18.12:~/tt_doc/doc_txt8/Files8",
        "./Backup/"], stderr=subprocess.PIPE, check=True)
    print("Result SCP transfert : %s" % repr(eightproc.stderr))
    if eightproc.stderr == b'':
        print("+ Folder Files8 downloaded...")
        #messagebox.showinfo("INFO", "systol.json downloaded")
    else:
        print("+ No folder Files8 to download !")
        messagebox.showerror("Error", "No folder Files8 to download !")

    ninethproc = subprocess.run(["scp", "-r", "pi@192.168.18.12:~/tt_doc/doc_txt9/Files9",
        "./Backup/"], stderr=subprocess.PIPE, check=True)
    print("Result SCP transfert : %s" % repr(ninethproc.stderr))
    if ninethproc.stderr == b'':
        print("+ Folder Files9 downloaded...")
        #messagebox.showinfo("INFO", "temp.json downloaded")
    else:
        print("+ No folder Files9 to download !")
        messagebox.showerror("Error", "No folder Files9 to download !")

    tenproc = subprocess.run(["scp", "-r", "pi@192.168.18.12:~/tt_doc/doc_txt10/Files10",
        "./Backup/"], stderr=subprocess.PIPE, check=True)
    print("Result SCP transfert : %s" % repr(tenproc.stderr))
    if tenproc.stderr == b'':
        print("+ Folder Files10 downloaded...")
        #messagebox.showinfo("INFO", "temp.json downloaded")
    else:
        print("+ No folder Files10 to download !")
        messagebox.showerror("Error", "No folder Files10 to download !")

    eleventhproc = subprocess.run(["scp", "-r", "pi@192.168.18.12:~/tt_doc/doc_txt11/Files11",
        "./Backup/"], stderr=subprocess.PIPE, check=True)
    print("Result SCP transfert : %s" % repr(eleventhproc.stderr))
    if eleventhproc.stderr == b'':
        print("+ Folder Files11 downloaded...")
        #messagebox.showinfo("INFO", "temp.json downloaded")
    else:
        print("+ No folder Files11 to download !")
        messagebox.showerror("Error", "No folder Files11 to download !")

    twelvthproc = subprocess.run(["scp", "-r", "pi@192.168.18.12:~/tt_doc/doc_txt12/Files12",
        "./Backup/"], stderr=subprocess.PIPE, check=True)
    print("Result SCP transfert : %s" % repr(twelvthproc.stderr))
    if twelvthproc.stderr == b'':
        print("+ Folder Files12 downloaded...")
        #messagebox.showinfo("INFO", "temp.json downloaded")
    else:
        print("+ No folder Files12 to download !")
        messagebox.showerror("Error", "No folder Files12 to download !")

    thirthproc = subprocess.run(["scp", "-r", "pi@192.168.18.12:~/tt_doc/doc_txt13/Files13",
        "./Backup/"], stderr=subprocess.PIPE, check=True)
    print("Result SCP transfert : %s" % repr(thirthproc.stderr))
    if thirthproc.stderr == b'':
        print("+ Folder Files13 downloaded...")
        #messagebox.showinfo("INFO", "temp.json downloaded")
    else:
        print("+ No folder Files13 to download !")
        messagebox.showerror("Error", "No folder Files13 to download !")

    fourteenproc = subprocess.run(["scp", "-r", "pi@192.168.18.12:~/tt_doc/doc_txt14/Files14",
        "./Backup/"], stderr=subprocess.PIPE, check=True)
    print("Result SCP transfert : %s" % repr(fourteenproc.stderr))
    if fourteenproc.stderr == b'':
        print("+ Folder Files14 downloaded...")
        #messagebox.showinfo("INFO", "temp.json downloaded")
    else:
        print("+ No folder Files14 to download !")
        messagebox.showerror("Error", "No folder Files14 to download !")

    fivteenthproc = subprocess.run(["scp", "-r", "pi@192.168.18.12:~/tt_doc/doc_txt15/Files15",
        "./Backup/"], stderr=subprocess.PIPE, check=True)
    print("Result SCP transfert : %s" % repr(fivteenthproc.stderr))
    if fivteenthproc.stderr == b'':
        print("+ Folder Files15 downloaded...")
        #messagebox.showinfo("INFO", "temp.json downloaded")
    else:
        print("+ No folder Files15 to download !")
        messagebox.showerror("Error", "No folder Files15 to download !")

    sixteenthproc = subprocess.run(["scp", "-r", "pi@192.168.18.12:~/tt_doc/doc_txt16/Files16",
        "./Backup/"], stderr=subprocess.PIPE, check=True)
    print("Result SCP transfert : %s" % repr(sixteenthproc.stderr))
    if sixteenthproc.stderr == b'':
        print("+ Folder Files16 downloaded...")
        #messagebox.showinfo("INFO", "temp.json downloaded")
    else:
        print("+ No folder Files16 to download !")
        messagebox.showerror("Error", "No folder Files16 to download !")

    seventeenthproc = subprocess.run(["scp", "-r", "pi@192.168.18.12:~/tt_doc/doc_txt17/Files17",
        "./Backup/"], stderr=subprocess.PIPE, check=True)
    print("Result SCP transfert : %s" % repr(seventeenthproc.stderr))
    if seventeenthproc.stderr == b'':
        print("+ Folder Files17 downloaded...")
        #messagebox.showinfo("INFO", "temp.json downloaded")
    else:
        print("+ No folder Files17 to download !")
        messagebox.showerror("Error", "No folder Files17 to download !")

    eighteenthproc = subprocess.run(["scp", "-r", "pi@192.168.18.12:~/tt_doc/doc_txt18/Files18",
        "./Backup/"], stderr=subprocess.PIPE, check=True)
    print("Result SCP transfert : %s" % repr(eighteenthproc.stderr))
    if eighteenthproc.stderr == b'':
        print("+ Folder Files18 downloaded...")
        #messagebox.showinfo("INFO", "temp.json downloaded")
    else:
        print("+ No folder Files18 to download !")
        messagebox.showerror("Error", "No folder Files18 to download !")

    ninteenthproc = subprocess.run(["scp", "-r", "pi@192.168.18.12:~/tt_doc/doc_txt19/Files19",
        "./Backup/"], stderr=subprocess.PIPE, check=True)
    print("Result SCP transfert : %s" % repr(ninteenthproc.stderr))
    if ninteenthproc.stderr == b'':
        print("+ Folder Files19 downloaded...")
        #messagebox.showinfo("INFO", "temp.json downloaded")
    else:
        print("+ No folder Files19 to download !")
        messagebox.showerror("Error", "No folder Files19 to download !")

    twentythproc = subprocess.run(["scp", "-r", "pi@192.168.18.12:~/tt_doc/doc_txt20/Files20",
        "./Backup/"], stderr=subprocess.PIPE, check=True)
    print("Result SCP transfert : %s" % repr(twentythproc.stderr))
    if twentythproc.stderr == b'':
        print("+ Folder Files20 downloaded...")
        #messagebox.showinfo("INFO", "temp.json downloaded")
    else:
        print("+ No folder Files20 to download !")
        messagebox.showerror("Error", "No folder Files20 to download !")

    twentyoneproc = subprocess.run(["scp", "-r", "pi@192.168.18.12:~/tt_doc/doc_txt21/Files21",
        "./Backup/"], stderr=subprocess.PIPE, check=True)
    print("Result SCP transfert : %s" % repr(twentyoneproc.stderr))
    if twentyoneproc.stderr == b'':
        print("+ Folder Files21 downloaded...")
        #messagebox.showinfo("INFO", "temp.json downloaded")
    else:
        print("+ No folder Files21 to download !")
        messagebox.showerror("Error", "No folder Files21 to download !")

    twentytwoproc = subprocess.run(["scp", "-r", "pi@192.168.18.12:~/tt_doc/doc_txt22/Files22",
        "./Backup/"], stderr=subprocess.PIPE, check=True)
    print("Result SCP transfert : %s" % repr(twentytwoproc.stderr))
    if twentytwoproc.stderr == b'':
        print("+ Folder Files22 downloaded...")
        #messagebox.showinfo("INFO", "temp.json downloaded")
    else:
        print("+ No folder Files22 to download !")
        messagebox.showerror("Error", "No folder Files22 to download !")

    twentythreeproc = subprocess.run(["scp", "-r", "pi@192.168.18.12:~/tt_doc/doc_txt23/Files23",
        "./Backup/"], stderr=subprocess.PIPE, check=True)
    print("Result SCP transfert : %s" % repr(twentythreeproc.stderr))
    if twentythreeproc.stderr == b'':
        print("+ Folder Files23 downloaded...")
        #messagebox.showinfo("INFO", "temp.json downloaded")
    else:
        print("+ No folder Files23 to download !")
        messagebox.showerror("Error", "No folder Files23 to download !")

    twentyfourproc = subprocess.run(["scp", "-r", "pi@192.168.18.12:~/tt_doc/doc_txt24/Files24",
        "./Backup/"], stderr=subprocess.PIPE, check=True)
    print("Result SCP transfert : %s" % repr(twentyfourproc.stderr))
    if twentyfourproc.stderr == b'':
        print("+ Folder Files24 downloaded...")
        #messagebox.showinfo("INFO", "temp.json downloaded")
    else:
        print("+ No folder Files24 to download !")
        messagebox.showerror("Error", "No folder Files24 to download !")

    print('Done')
    # linux, mac
    print('My pid is', os.getpid())
    root.quit() # To destroy threading

def launchdownload():
    """
        To start app with thread !
    """
    root = tk.Tk()
    treat = threading.Thread(target=process_of_unknown_duration, args=(root,))
    #print(treat)
    treat.start()
    print("Download...")
    task(root) # This will block while the mainloop runs
    treat.join()
    root.destroy() # To destroy completely window
    shootransfert()
