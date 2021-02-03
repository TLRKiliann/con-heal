#!/usr/bin/python3
# -*- coding : utf-8 -*-


"""
    Connecting the duration of progress bar
    with task = number of subprocess.
"""


from tkinter import messagebox
from diagloadbar import needata
import subprocess


def needload1():
    """
        to download med files from server before
        to start with med interface.
    """
    needata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt1/Files1/diagrecap1.txt",
        "./diag/doc_diag/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File diagrecap.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No diagrecap.txt to download !")

def needload2():
    """
        to download med files from server before
        to start with med interface.
    """
    needata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt2/Files2/diagrecap2.txt",
        "./diag/doc_diag2/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File diagrecap2.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap2.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No diagrecap2.txt to download !")

def needload3():
    """
        to download med files from server before
        to start with med interface.
    """
    needata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt3/Files3/diagrecap3.txt",
        "./diag/doc_diag3/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File diagrecap3.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap3.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No diagrecap3.txt to download !")

def needload4():
    """
        to download med files from server before
        to start with med interface.
    """
    needata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt4/Files4/diagrecap4.txt",
        "./diag/doc_diag4/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File diagrecap4.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap4.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No diagrecap4.txt to download !")

def needload5():
    """
        to download med files from server before
        to start with med interface.
    """
    needata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt5/Files5/diagrecap5.txt",
        "./diag/doc_diag5/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File diagrecap5.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap5.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No diagrecap5.txt to download !")

def needload6():
    """
        to download med files from server before
        to start with med interface.
    """
    needata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt6/Files6/diagrecap6.txt",
        "./diag/doc_diag6/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File diagrecap6.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap6.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No diagrecap6.txt to download !")

def needload7():
    """
        to download med files from server before
        to start with med interface.
    """
    needata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt7/Files7/diagrecap7.txt",
        "./diag/doc_diag7/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File diagrecap7.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap7.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No diagrecap7.txt to download !")

def needload8():
    """
        to download med files from server before
        to start with med interface.
    """
    needata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt8/Files8/diagrecap8.txt",
        "./diag/doc_diag8/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File diagrecap8.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap8.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No diagrecap8.txt to download !")

def needload9():
    """
        to download med files from server before
        to start with med interface.
    """
    needata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt9/Files9/diagrecap9.txt",
        "./diag/doc_diag9/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File diagrecap9.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap9.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No diagrecap9.txt to download !")

def needload10():
    """
        to download med files from server before
        to start with med interface.
    """
    needata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt10/Files10/diagrecap10.txt",
        "./diag/doc_diag10/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File diagrecap10.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap10.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No diagrecap10.txt to download !")

def needload11():
    """
        to download med files from server before
        to start with med interface.
    """
    needata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt11/Files11/diagrecap11.txt",
        "./diag/doc_diag11/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File diagrecap11.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap11.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No diagrecap11.txt to download !")

def needload12():
    """
        to download med files from server before
        to start with med interface.
    """
    needata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt12/Files12/diagrecap12.txt",
        "./diag/doc_diag12/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File diagrecap12.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap12.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No diagrecap12.txt to download !")

def needload13():
    """
        to download med files from server before
        to start with med interface.
    """
    needata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt13/Files13/diagrecap13.txt",
        "./diag/doc_diag13/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File diagrecap13.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap13.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No diagrecap13.txt to download !")

def needload14():
    """
        to download med files from server before
        to start with med interface.
    """
    needata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt14/Files14/diagrecap14.txt",
        "./diag/doc_diag14/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File diagrecap14.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap14.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No diagrecap14.txt to download !")

def needload15():
    """
        to download med files from server before
        to start with med interface.
    """
    needata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt15/Files15/diagrecap15.txt",
        "./diag/doc_diag15/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File diagrecap15.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap15.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No diagrecap15.txt to download !")

def needload16():
    """
        to download med files from server before
        to start with med interface.
    """
    needata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt16/Files16/diagrecap16.txt",
        "./diag/doc_diag16/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File diagrecap16.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap16.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No diagrecap16.txt to download !")

def needload17():
    """
        to download med files from server before
        to start with med interface.
    """
    needata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt17/Files17/diagrecap17.txt",
        "./diag/doc_diag17/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File diagrecap17.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap17.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No diagrecap17.txt to download !")

def needload18():
    """
        to download med files from server before
        to start with med interface.
    """
    needata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt18/Files18/diagrecap18.txt",
        "./diag/doc_diag18/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File diagrecap18.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap18.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No diagrecap18.txt to download !")

def needload19():
    """
        to download med files from server before
        to start with med interface.
    """
    needata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt19/Files19/diagrecap19.txt",
        "./diag/doc_diag19/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File diagrecap19.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap19.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No diagrecap19.txt to download !")

def needload20():
    """
        to download med files from server before
        to start with med interface.
    """
    needata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt20/Files20/diagrecap20.txt",
        "./diag/doc_diag20/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File diagrecap20.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap20.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No diagrecap20.txt to download !")

def needload21():
    """
        to download med files from server before
        to start with med interface.
    """
    needata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt21/Files21/diagrecap21.txt",
        "./diag/doc_diag21/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File diagrecap21.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap21.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No diagrecap21.txt to download !")

def needload22():
    """
        to download med files from server before
        to start with med interface.
    """
    needata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt22/Files22/diagrecap22.txt",
        "./diag/doc_diag22/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File diagrecap22.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap22.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No diagrecap22.txt to download !")

def needload23():
    """
        to download med files from server before
        to start with med interface.
    """
    needata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt23/Files23/diagrecap23.txt",
        "./diag/doc_diag23/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File diagrecap23.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap23.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No diagrecap23.txt to download !")

def needload24():
    """
        to download med files from server before
        to start with med interface.
    """
    needata()
    proc = subprocess.run(["scp", "pi@192.168.18.12:~/tt_doc/doc_txt24/Files24/diagrecap24.txt",
        "./diag/doc_diag24/"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File diagrecap24.txt downloaded !")
        #messagebox.showinfo("INFO", "diagrecap24.txt downloaded")
    else:
        print("+ No file to download !")
        messagebox.showerror("Error", "No diagrecap24.txt to download !")
