#!/usr/bin/python3
# -*- coding : utf-8 -*-


"""
    Connecting the duration of progress bar
    with task = number of subprocess.
"""


from tkinter import messagebox
from vmed.medbar import medata
import subprocess


def medownload1():
    """
        to download med files from server before
        to start with med interface.
    """
    medata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt1/Files1/resultvmed.txt",
        "./vmed/doc_vmed/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File resultvmed.txt downloaded !")
        messagebox.showinfo("INFO", "resultvmed.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No resultvmed.txt to download !")

def medownload2():
    """
        to download med files from server before
        to start with med interface.
    """
    medata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt2/Files2/resultvmed2.txt",
        "./vmed/doc_vmed2/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File resultvmed2.txt downloaded !")
        messagebox.showinfo("INFO", "resultvmed2.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No resultvmed2.txt to download !")

def medownload3():
    """
        to download med files from server before
        to start with med interface.
    """
    medata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt3/Files3/resultvmed3.txt",
        "./vmed/doc_vmed3/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File resultvmed3.txt downloaded !")
        messagebox.showinfo("INFO", "resultvmed3.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No resultvmed3.txt to download !")

def medownload4():
    """
        to download med files from server before
        to start with med interface.
    """
    medata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt4/Files4/resultvmed4.txt",
        "./vmed/doc_vmed4/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File resultvmed4.txt downloaded !")
        messagebox.showinfo("INFO", "resultvmed4.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No resultvmed4.txt to download !")

def medownload5():
    """
        to download med files from server before
        to start with med interface.
    """
    medata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt5/Files5/resultvmed5.txt",
        "./vmed/doc_vmed5/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File resultvmed5.txt downloaded !")
        messagebox.showinfo("INFO", "resultvmed5.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No resultvmed5.txt to download !")

def medownload6():
    """
        to download med files from server before
        to start with med interface.
    """
    medata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt6/Files6/resultvmed6.txt",
        "./vmed/doc_vmed6/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File resultvmed6.txt downloaded !")
        messagebox.showinfo("INFO", "resultvmed6.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No resultvmed6.txt to download !")

def medownload7():
    """
        to download med files from server before
        to start with med interface.
    """
    medata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt7/Files7/resultvmed7.txt",
        "./vmed/doc_vmed7/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File resultvmed7.txt downloaded !")
        messagebox.showinfo("INFO", "resultvmed7.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No resultvmed7.txt to download !")

def medownload8():
    """
        to download med files from server before
        to start with med interface.
    """
    medata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt8/Files8/resultvmed8.txt",
        "./vmed/doc_vmed8/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File resultvmed8.txt downloaded !")
        messagebox.showinfo("INFO", "resultvmed8.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No resultvmed8.txt to download !")

def medownload9():
    """
        to download med files from server before
        to start with med interface.
    """
    medata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt9/Files9/resultvmed9.txt",
        "./vmed/doc_vmed9/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File resultvmed9.txt downloaded !")
        messagebox.showinfo("INFO", "resultvmed9.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No resultvmed9.txt to download !")

def medownload10():
    """
        to download med files from server before
        to start with med interface.
    """
    medata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt10/Files10/resultvmed10.txt",
        "./vmed/doc_vmed10/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File resultvmed10.txt downloaded !")
        messagebox.showinfo("INFO", "resultvmed10.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No resultvmed10.txt to download !")

def medownload11():
    """
        to download med files from server before
        to start with med interface.
    """
    medata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt11/Files11/resultvmed11.txt",
        "./vmed/doc_vmed11/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File resultvmed11.txt downloaded !")
        messagebox.showinfo("INFO", "resultvmed11.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No resultvmed11.txt to download !")

def medownload12():
    """
        to download med files from server before
        to start with med interface.
    """
    medata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt12/Files12/resultvmed12.txt",
        "./vmed/doc_vmed12/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File resultvmed12.txt downloaded !")
        messagebox.showinfo("INFO", "resultvmed12.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No resultvmed12.txt to download !")

def medownload13():
    """
        to download med files from server before
        to start with med interface.
    """
    medata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt13/Files13/resultvmed13.txt",
        "./vmed/doc_vmed13/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File resultvmed13.txt downloaded !")
        messagebox.showinfo("INFO", "resultvmed13.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No resultvmed13.txt to download !")

def medownload14():
    """
        to download med files from server before
        to start with med interface.
    """
    medata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt14/Files14/resultvmed14.txt",
        "./vmed/doc_vmed14/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File resultvmed14.txt downloaded !")
        messagebox.showinfo("INFO", "resultvmed14.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No resultvmed14.txt to download !")

def medownload15():
    """
        to download med files from server before
        to start with med interface.
    """
    medata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt15/Files15/resultvmed15.txt",
        "./vmed/doc_vmed15/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File resultvmed15.txt downloaded !")
        messagebox.showinfo("INFO", "resultvmed15.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No resultvmed15.txt to download !")

def medownload16():
    """
        to download med files from server before
        to start with med interface.
    """
    medata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt16/Files16/resultvmed16.txt",
        "./vmed/doc_vmed16/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File resultvmed16.txt downloaded !")
        messagebox.showinfo("INFO", "resultvmed16.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No resultvmed16.txt to download !")

def medownload17():
    """
        to download med files from server before
        to start with med interface.
    """
    medata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt17/Files17/resultvmed17.txt",
        "./vmed/doc_vmed17/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File resultvmed17.txt downloaded !")
        messagebox.showinfo("INFO", "resultvmed17.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No resultvmed17.txt to download !")

def medownload18():
    """
        to download med files from server before
        to start with med interface.
    """
    medata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt18/Files18/resultvmed18.txt",
        "./vmed/doc_vmed18/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File resultvmed18.txt downloaded !")
        messagebox.showinfo("INFO", "resultvmed18.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No resultvmed18.txt to download !")

def medownload19():
    """
        to download med files from server before
        to start with med interface.
    """
    medata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt19/Files19/resultvmed19.txt",
        "./vmed/doc_vmed19/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File resultvmed19.txt downloaded !")
        messagebox.showinfo("INFO", "resultvmed19.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No resultvmed19.txt to download !")

def medownload20():
    """
        to download med files from server before
        to start with med interface.
    """
    medata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt20/Files20/resultvmed20.txt",
        "./vmed/doc_vmed20/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File resultvmed20.txt downloaded !")
        messagebox.showinfo("INFO", "resultvmed20.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No resultvmed20.txt to download !")

def medownload21():
    """
        to download med files from server before
        to start with med interface.
    """
    medata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt21/Files21/resultvmed21.txt",
        "./vmed/doc_vmed21/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File resultvmed21.txt downloaded !")
        messagebox.showinfo("INFO", "resultvmed21.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No resultvmed21.txt to download !")

def medownload22():
    """
        to download med files from server before
        to start with med interface.
    """
    medata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt22/Files22/resultvmed22.txt",
        "./vmed/doc_vmed22/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File resultvmed22.txt downloaded !")
        messagebox.showinfo("INFO", "resultvmed22.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No resultvmed22.txt to download !")

def medownload23():
    """
        to download med files from server before
        to start with med interface.
    """
    medata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt23/Files23/resultvmed23.txt",
        "./vmed/doc_vmed23/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File resultvmed23.txt downloaded !")
        messagebox.showinfo("INFO", "resultvmed23.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No resultvmed23.txt to download !")

def medownload24():
    """
        to download med files from server before
        to start with med interface.
    """
    medata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt24/Files24/resultvmed24.txt",
        "./vmed/doc_vmed24/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File resultvmed24.txt downloaded !")
        messagebox.showinfo("INFO", "resultvmed24.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No resultvmed24.txt to download !")
