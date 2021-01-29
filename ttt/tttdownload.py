#!/usr/bin/python3
# -*- coding : utf-8 -*-


"""
    Connecting the duration of progress bar
    with task = number of subprocess.
"""


from tkinter import messagebox
import subprocess


def downloadttt1():
    """
        to download ttt files from server before
        to start with ttt interface.
    """
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt1/Files1/intro_ttt.txt",
        "./ttt/doc_ttt/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File intro_ttt.txt downloaded !")
        messagebox.showinfo("INFO", "intro_ttt.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_ttt.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt1/Files1/convdose.json",
        "./ttt/doc_ttt/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("+ convdose.json downloaded...")
        messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("+ No convdose.json to download !")
        messagebox.showerror("Error", "No convdose.json to download !")

    thirdproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt1/Files1/intro_res.txt",
        "./ttt/doc_ttt/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("+ File intro_res.txt downloaded !")
        messagebox.showinfo("INFO", "intro_res.txt downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_res.txt to download !")

    forthproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt1/Files1/convres.json",
        "./ttt/doc_ttt/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("+ File convres.json downloaded !")
        messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No convres.json to download !")

def downloadttt2():
    """
        to download ttt files from server before
        to start with ttt interface.
    """
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt2/Files2/intro_ttt.txt",
        "./ttt/doc_ttt2/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File intro_ttt.txt downloaded !")
        messagebox.showinfo("INFO", "intro_ttt.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_ttt.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt2/Files2/convdose.json",
        "./ttt/doc_ttt2/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("+ convdose.json downloaded...")
        messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("+ No convdose.json to download !")
        messagebox.showerror("Error", "No convdose.json to download !")

    thirdproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt2/Files2/intro_res.txt",
        "./ttt/doc_ttt2/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("+ File intro_res.txt downloaded !")
        messagebox.showinfo("INFO", "intro_res.txt downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_res.txt to download !")

    forthproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt2/Files2/convres.json",
        "./ttt/doc_ttt2/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("+ File convres.json downloaded !")
        messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No convres.json to download !")

def downloadttt3():
    """
        to download ttt files from server before
        to start with ttt interface.
    """
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt3/Files3/intro_ttt.txt",
        "./ttt/doc_ttt3/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File intro_ttt.txt downloaded !")
        messagebox.showinfo("INFO", "intro_ttt.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_ttt.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt3/Files3/convdose.json",
        "./ttt/doc_ttt3/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("+ convdose.json downloaded...")
        messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("+ No convdose.json to download !")
        messagebox.showerror("Error", "No convdose.json to download !")

    thirdproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt3/Files3/intro_res.txt",
        "./ttt/doc_ttt3/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("+ File intro_res.txt downloaded !")
        messagebox.showinfo("INFO", "intro_res.txt downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_res.txt to download !")

    forthproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt3/Files3/convres.json",
        "./ttt/doc_ttt3/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("+ File convres.json downloaded !")
        messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No convres.json to download !")

def downloadttt4():
    """
        to download ttt files from server before
        to start with ttt interface.
    """
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt4/Files4/intro_ttt.txt",
        "./ttt/doc_ttt4/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File intro_ttt.txt downloaded !")
        messagebox.showinfo("INFO", "intro_ttt.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_ttt.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt4/Files4/convdose.json",
        "./ttt/doc_ttt4/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("+ convdose.json downloaded...")
        messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("+ No convdose.json to download !")
        messagebox.showerror("Error", "No convdose.json to download !")

    thirdproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt4/Files4/intro_res.txt",
        "./ttt/doc_ttt4/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("+ File intro_res.txt downloaded !")
        messagebox.showinfo("INFO", "intro_res.txt downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_res.txt to download !")

    forthproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt4/Files4/convres.json",
        "./ttt/doc_ttt4/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("+ File convres.json downloaded !")
        messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No convres.json to download !")

def downloadttt5():
    """
        to download ttt files from server before
        to start with ttt interface.
    """
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt5/Files5/intro_ttt.txt",
        "./ttt/doc_ttt5/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File intro_ttt.txt downloaded !")
        messagebox.showinfo("INFO", "intro_ttt.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_ttt.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt5/Files5/convdose.json",
        "./ttt/doc_ttt5/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("+ convdose.json downloaded...")
        messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("+ No convdose.json to download !")
        messagebox.showerror("Error", "No convdose.json to download !")

    thirdproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt5/Files5/intro_res.txt",
        "./ttt/doc_ttt5/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("+ File intro_res.txt downloaded !")
        messagebox.showinfo("INFO", "intro_res.txt downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_res.txt to download !")

    forthproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt5/Files5/convres.json",
        "./ttt/doc_ttt5/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("+ File convres.json downloaded !")
        messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No convres.json to download !")

def downloadttt6():
    """
        to download ttt files from server before
        to start with ttt interface.
    """
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt6/Files6/intro_ttt.txt",
        "./ttt/doc_ttt6/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File intro_ttt.txt downloaded !")
        messagebox.showinfo("INFO", "intro_ttt.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_ttt.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt6/Files6/convdose.json",
        "./ttt/doc_ttt6/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("+ convdose.json downloaded...")
        messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("+ No convdose.json to download !")
        messagebox.showerror("Error", "No convdose.json to download !")

    thirdproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt6/Files6/intro_res.txt",
        "./ttt/doc_ttt6/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("+ File intro_res.txt downloaded !")
        messagebox.showinfo("INFO", "intro_res.txt downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_res.txt to download !")

    forthproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt6/Files6/convres.json",
        "./ttt/doc_ttt6/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("+ File convres.json downloaded !")
        messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No convres.json to download !")

def downloadttt7():
    """
        to download ttt files from server before
        to start with ttt interface.
    """
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt7/Files7/intro_ttt.txt",
        "./ttt/doc_ttt7/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File intro_ttt.txt downloaded !")
        messagebox.showinfo("INFO", "intro_ttt.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_ttt.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt7/Files7/convdose.json",
        "./ttt/doc_ttt7/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("+ convdose.json downloaded...")
        messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("+ No convdose.json to download !")
        messagebox.showerror("Error", "No convdose.json to download !")

    thirdproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt7/Files7/intro_res.txt",
        "./ttt/doc_ttt7/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("+ File intro_res.txt downloaded !")
        messagebox.showinfo("INFO", "intro_res.txt downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_res.txt to download !")

    forthproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt7/Files7/convres.json",
        "./ttt/doc_ttt7/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("+ File convres.json downloaded !")
        messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No convres.json to download !")

def downloadttt8():
    """
        to download ttt files from server before
        to start with ttt interface.
    """
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt8/Files8/intro_ttt.txt",
        "./ttt/doc_ttt8/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File intro_ttt.txt downloaded !")
        messagebox.showinfo("INFO", "intro_ttt.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_ttt.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt8/Files8/convdose.json",
        "./ttt/doc_ttt8/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("+ convdose.json downloaded...")
        messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("+ No convdose.json to download !")
        messagebox.showerror("Error", "No convdose.json to download !")

    thirdproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt8/Files8/intro_res.txt",
        "./ttt/doc_ttt8/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("+ File intro_res.txt downloaded !")
        messagebox.showinfo("INFO", "intro_res.txt downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_res.txt to download !")

    forthproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt8/Files8/convres.json",
        "./ttt/doc_ttt8/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("+ File convres.json downloaded !")
        messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No convres.json to download !")

def downloadttt9():
    """
        to download ttt files from server before
        to start with ttt interface.
    """
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt9/Files9/intro_ttt.txt",
        "./ttt/doc_ttt9/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File intro_ttt.txt downloaded !")
        messagebox.showinfo("INFO", "intro_ttt.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_ttt.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt9/Files9/convdose.json",
        "./ttt/doc_ttt9/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("+ convdose.json downloaded...")
        messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("+ No convdose.json to download !")
        messagebox.showerror("Error", "No convdose.json to download !")

    thirdproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt9/Files9/intro_res.txt",
        "./ttt/doc_ttt9/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("+ File intro_res.txt downloaded !")
        messagebox.showinfo("INFO", "intro_res.txt downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_res.txt to download !")

    forthproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt9/Files9/convres.json",
        "./ttt/doc_ttt9/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("+ File convres.json downloaded !")
        messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No convres.json to download !")

def downloadttt10():
    """
        to download ttt files from server before
        to start with ttt interface.
    """
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt10/Files10/intro_ttt.txt",
        "./ttt/doc_ttt10/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File intro_ttt.txt downloaded !")
        messagebox.showinfo("INFO", "intro_ttt.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_ttt.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt10/Files10/convdose.json",
        "./ttt/doc_ttt10/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("+ convdose.json downloaded...")
        messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("+ No convdose.json to download !")
        messagebox.showerror("Error", "No convdose.json to download !")

    thirdproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt10/Files10/intro_res.txt",
        "./ttt/doc_ttt10/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("+ File intro_res.txt downloaded !")
        messagebox.showinfo("INFO", "intro_res.txt downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_res.txt to download !")

    forthproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt10/Files10/convres.json",
        "./ttt/doc_ttt10/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("+ File convres.json downloaded !")
        messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No convres.json to download !")

def downloadttt11():
    """
        to download ttt files from server before
        to start with ttt interface.
    """
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt11/Files11/intro_ttt.txt",
        "./ttt/doc_ttt11/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File intro_ttt.txt downloaded !")
        messagebox.showinfo("INFO", "intro_ttt.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_ttt.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt11/Files11/convdose.json",
        "./ttt/doc_ttt11/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("+ convdose.json downloaded...")
        messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("+ No convdose.json to download !")
        messagebox.showerror("Error", "No convdose.json to download !")

    thirdproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt11/Files11/intro_res.txt",
        "./ttt/doc_ttt11/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("+ File intro_res.txt downloaded !")
        messagebox.showinfo("INFO", "intro_res.txt downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_res.txt to download !")

    forthproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt11/Files11/convres.json",
        "./ttt/doc_ttt11/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("+ File convres.json downloaded !")
        messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No convres.json to download !")

def downloadttt12():
    """
        to download ttt files from server before
        to start with ttt interface.
    """
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt12/Files12/intro_ttt.txt",
        "./ttt/doc_ttt12/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File intro_ttt.txt downloaded !")
        messagebox.showinfo("INFO", "intro_ttt.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_ttt.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt12/Files12/convdose.json",
        "./ttt/doc_ttt12/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("+ convdose.json downloaded...")
        messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("+ No convdose.json to download !")
        messagebox.showerror("Error", "No convdose.json to download !")

    thirdproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt12/Files12/intro_res.txt",
        "./ttt/doc_ttt12/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("+ File intro_res.txt downloaded !")
        messagebox.showinfo("INFO", "intro_res.txt downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_res.txt to download !")

    forthproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt12/Files12/convres.json",
        "./ttt/doc_ttt12/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("+ File convres.json downloaded !")
        messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No convres.json to download !")

def downloadttt13():
    """
        to download ttt files from server before
        to start with ttt interface.
    """
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt13/Files13/intro_ttt.txt",
        "./ttt/doc_ttt13/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File intro_ttt.txt downloaded !")
        messagebox.showinfo("INFO", "intro_ttt.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_ttt.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt13/Files13/convdose.json",
        "./ttt/doc_ttt13/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("+ convdose.json downloaded...")
        messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("+ No convdose.json to download !")
        messagebox.showerror("Error", "No convdose.json to download !")

    thirdproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt13/Files13/intro_res.txt",
        "./ttt/doc_ttt13/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("+ File intro_res.txt downloaded !")
        messagebox.showinfo("INFO", "intro_res.txt downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_res.txt to download !")

    forthproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt13/Files13/convres.json",
        "./ttt/doc_ttt13/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("+ File convres.json downloaded !")
        messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No convres.json to download !")

def downloadttt14():
    """
        to download ttt files from server before
        to start with ttt interface.
    """
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt14/Files14/intro_ttt.txt",
        "./ttt/doc_ttt14/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File intro_ttt.txt downloaded !")
        messagebox.showinfo("INFO", "intro_ttt.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_ttt.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt14/Files14/convdose.json",
        "./ttt/doc_ttt14/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("+ convdose.json downloaded...")
        messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("+ No convdose.json to download !")
        messagebox.showerror("Error", "No convdose.json to download !")

    thirdproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt14/Files14/intro_res.txt",
        "./ttt/doc_ttt14/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("+ File intro_res.txt downloaded !")
        messagebox.showinfo("INFO", "intro_res.txt downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_res.txt to download !")

    forthproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt14/Files14/convres.json",
        "./ttt/doc_ttt14/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("+ File convres.json downloaded !")
        messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No convres.json to download !")

def downloadttt15():
    """
        to download ttt files from server before
        to start with ttt interface.
    """
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt15/Files15/intro_ttt.txt",
        "./ttt/doc_ttt15/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File intro_ttt.txt downloaded !")
        messagebox.showinfo("INFO", "intro_ttt.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_ttt.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt15/Files15/convdose.json",
        "./ttt/doc_ttt15/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("+ convdose.json downloaded...")
        messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("+ No convdose.json to download !")
        messagebox.showerror("Error", "No convdose.json to download !")

    thirdproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt15/Files15/intro_res.txt",
        "./ttt/doc_ttt15/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("+ File intro_res.txt downloaded !")
        messagebox.showinfo("INFO", "intro_res.txt downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_res.txt to download !")

    forthproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt15/Files15/convres.json",
        "./ttt/doc_ttt15/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("+ File convres.json downloaded !")
        messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No convres.json to download !")

def downloadttt16():
    """
        to download ttt files from server before
        to start with ttt interface.
    """
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt16/Files16/intro_ttt.txt",
        "./ttt/doc_ttt16/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File intro_ttt.txt downloaded !")
        messagebox.showinfo("INFO", "intro_ttt.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_ttt.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt16/Files16/convdose.json",
        "./ttt/doc_ttt16/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("+ convdose.json downloaded...")
        messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("+ No convdose.json to download !")
        messagebox.showerror("Error", "No convdose.json to download !")

    thirdproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt16/Files16/intro_res.txt",
        "./ttt/doc_ttt16/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("+ File intro_res.txt downloaded !")
        messagebox.showinfo("INFO", "intro_res.txt downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_res.txt to download !")

    forthproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt16/Files16/convres.json",
        "./ttt/doc_ttt16/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("+ File convres.json downloaded !")
        messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No convres.json to download !")

def downloadttt17():
    """
        to download ttt files from server before
        to start with ttt interface.
    """
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt17/Files17/intro_ttt.txt",
        "./ttt/doc_ttt17/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File intro_ttt.txt downloaded !")
        messagebox.showinfo("INFO", "intro_ttt.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_ttt.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt17/Files17/convdose.json",
        "./ttt/doc_ttt17/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("+ convdose.json downloaded...")
        messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("+ No convdose.json to download !")
        messagebox.showerror("Error", "No convdose.json to download !")

    thirdproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt17/Files17/intro_res.txt",
        "./ttt/doc_ttt17/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("+ File intro_res.txt downloaded !")
        messagebox.showinfo("INFO", "intro_res.txt downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_res.txt to download !")

    forthproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt17/Files17/convres.json",
        "./ttt/doc_ttt17/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("+ File convres.json downloaded !")
        messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No convres.json to download !")

def downloadttt18():
    """
        to download ttt files from server before
        to start with ttt interface.
    """
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt18/Files18/intro_ttt.txt",
        "./ttt/doc_ttt18/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File intro_ttt.txt downloaded !")
        messagebox.showinfo("INFO", "intro_ttt.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_ttt.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt18/Files18/convdose.json",
        "./ttt/doc_ttt18/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("+ convdose.json downloaded...")
        messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("+ No convdose.json to download !")
        messagebox.showerror("Error", "No convdose.json to download !")

    thirdproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt18/Files18/intro_res.txt",
        "./ttt/doc_ttt18/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("+ File intro_res.txt downloaded !")
        messagebox.showinfo("INFO", "intro_res.txt downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_res.txt to download !")

    forthproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt18/Files18/convres.json",
        "./ttt/doc_ttt18/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("+ File convres.json downloaded !")
        messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No convres.json to download !")

def downloadttt19():
    """
        to download ttt files from server before
        to start with ttt interface.
    """
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt19/Files19/intro_ttt.txt",
        "./ttt/doc_ttt19/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File intro_ttt.txt downloaded !")
        messagebox.showinfo("INFO", "intro_ttt.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_ttt.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt19/Files19/convdose.json",
        "./ttt/doc_ttt19/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("+ convdose.json downloaded...")
        messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("+ No convdose.json to download !")
        messagebox.showerror("Error", "No convdose.json to download !")

    thirdproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt19/Files19/intro_res.txt",
        "./ttt/doc_ttt19/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("+ File intro_res.txt downloaded !")
        messagebox.showinfo("INFO", "intro_res.txt downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_res.txt to download !")

    forthproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt19/Files19/convres.json",
        "./ttt/doc_ttt19/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("+ File convres.json downloaded !")
        messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No convres.json to download !")

def downloadttt20():
    """
        to download ttt files from server before
        to start with ttt interface.
    """
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt20/Files20/intro_ttt.txt",
        "./ttt/doc_ttt20/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File intro_ttt.txt downloaded !")
        messagebox.showinfo("INFO", "intro_ttt.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_ttt.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt20/Files20/convdose.json",
        "./ttt/doc_ttt20/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("+ convdose.json downloaded...")
        messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("+ No convdose.json to download !")
        messagebox.showerror("Error", "No convdose.json to download !")

    thirdproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt20/Files20/intro_res.txt",
        "./ttt/doc_ttt20/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("+ File intro_res.txt downloaded !")
        messagebox.showinfo("INFO", "intro_res.txt downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_res.txt to download !")

    forthproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt20/Files20/convres.json",
        "./ttt/doc_ttt20/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("+ File convres.json downloaded !")
        messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No convres.json to download !")

def downloadttt21():
    """
        to download ttt files from server before
        to start with ttt interface.
    """
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt21/Files21/intro_ttt.txt",
        "./ttt/doc_ttt21/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File intro_ttt.txt downloaded !")
        messagebox.showinfo("INFO", "intro_ttt.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_ttt.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt21/Files21/convdose.json",
        "./ttt/doc_ttt21/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("+ convdose.json downloaded...")
        messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("+ No convdose.json to download !")
        messagebox.showerror("Error", "No convdose.json to download !")

    thirdproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt21/Files21/intro_res.txt",
        "./ttt/doc_ttt21/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("+ File intro_res.txt downloaded !")
        messagebox.showinfo("INFO", "intro_res.txt downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_res.txt to download !")

    forthproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt21/Files21/convres.json",
        "./ttt/doc_ttt21/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("+ File convres.json downloaded !")
        messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No convres.json to download !")

def downloadttt22():
    """
        to download ttt files from server before
        to start with ttt interface.
    """
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt22/Files22/intro_ttt.txt",
        "./ttt/doc_ttt22/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File intro_ttt.txt downloaded !")
        messagebox.showinfo("INFO", "intro_ttt.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_ttt.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt22/Files22/convdose.json",
        "./ttt/doc_ttt22/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("+ convdose.json downloaded...")
        messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("+ No convdose.json to download !")
        messagebox.showerror("Error", "No convdose.json to download !")

    thirdproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt22/Files22/intro_res.txt",
        "./ttt/doc_ttt22/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("+ File intro_res.txt downloaded !")
        messagebox.showinfo("INFO", "intro_res.txt downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_res.txt to download !")

    forthproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt22/Files22/convres.json",
        "./ttt/doc_ttt22/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("+ File convres.json downloaded !")
        messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No convres.json to download !")

def downloadttt23():
    """
        to download ttt files from server before
        to start with ttt interface.
    """
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt23/Files23/intro_ttt.txt",
        "./ttt/doc_ttt23/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File intro_ttt.txt downloaded !")
        messagebox.showinfo("INFO", "intro_ttt.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_ttt.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt23/Files23/convdose.json",
        "./ttt/doc_ttt23/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("+ convdose.json downloaded...")
        messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("+ No convdose.json to download !")
        messagebox.showerror("Error", "No convdose.json to download !")

    thirdproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt23/Files23/intro_res.txt",
        "./ttt/doc_ttt23/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("+ File intro_res.txt downloaded !")
        messagebox.showinfo("INFO", "intro_res.txt downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_res.txt to download !")

    forthproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt23/Files23/convres.json",
        "./ttt/doc_ttt23/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("+ File convres.json downloaded !")
        messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No convres.json to download !")

def downloadttt24():
    """
        to download ttt files from server before
        to start with ttt interface.
    """
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt24/Files24/intro_ttt.txt",
        "./ttt/doc_ttt24/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File intro_ttt.txt downloaded !")
        messagebox.showinfo("INFO", "intro_ttt.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_ttt.txt to download !")

    secproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt24/Files24/convdose.json",
        "./ttt/doc_ttt24/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(secproc.stderr))
    if secproc.stderr == b'':
        print("+ convdose.json downloaded...")
        messagebox.showinfo("INFO", "convdose.json downloaded !")
    else:
        print("+ No convdose.json to download !")
        messagebox.showerror("Error", "No convdose.json to download !")

    thirdproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt24/Files24/intro_res.txt",
        "./ttt/doc_ttt24/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(thirdproc.stderr))
    if thirdproc.stderr == b'':
        print("+ File intro_res.txt downloaded !")
        messagebox.showinfo("INFO", "intro_res.txt downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No intro_res.txt to download !")

    forthproc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt24/Files24/convres.json",
        "./ttt/doc_ttt24/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(forthproc.stderr))
    if forthproc.stderr == b'':
        print("+ File convres.json downloaded !")
        messagebox.showinfo("INFO", "convres.json downloaded !")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No convres.json to download !")
