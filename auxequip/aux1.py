#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
import tkinter as tk
from tkinter import messagebox
import time

def auxi_equip1(self):
    """
        Main function called since main app
        heal_track.py for displaying auxiliary
        equipement.
    """
    self.can.delete(ALL)
    self.can.configure(background='DodgerBlue2')

    self.x1, self.y1 = 540, 45
    self.labl_name = tk.Label(self.can, text="Auxiliary Equipement",
        font=('helvetica', 18, 'bold'), width=10,
        height=2, bg='DodgerBlue2', fg='white')
    self.labl_name = self.can.create_window(self.x1, self.y1,
        window = self.labl_name)

    with open('./newpatient/entryfile.txt', 'r') as filename:
        line1 = filename.readline()

    self.x2, self.y2 = 720, 45
    ntry_txt = StringVar()
    self.entryname = Entry(self.can, textvariable=ntry_txt, width=20)
    ntry_txt.set(line1[:-1])
    self.entryname = self.can.create_window(self.x2, self.y2,
        window = self.entryname)

    def recordaux():
        print("Date : " + time.strftime("%d/%m/%Y"))
        print("Nom du patient : ", ntry_txt.get())
        with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as file:
            file.write("----------------------------------------------------------\n")
            file.write("Date : ")
            file.write(time.strftime("%d/%m/%Y")+ '\n')
            file.write("Patient name : ")
            file.write(ntry_txt.get() + '\n')

        with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as endfile:
            endfile.write("---------------------------------------------------------\n\n")

        print(CheckVar1.get())
        if CheckVar1.get()==1:
            print("+ Canne was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt.txt', 'a+') as file:
                file.write("# Canne : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Canne ok, nothing to do")
            
        print(CheckVar2.get())
        if CheckVar2.get()==1:
            print("+ Tintebin (ttb) (FR) was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt.txt', 'a+') as file:
                file.write("# Tintebin (ttb) : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Tintebin (ttb) ok, nothing to do")

        print(CheckVar3.get())
        if CheckVar3.get()==1:
            print("+ Rollator was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt.txt', 'a+') as file:
                file.write("# Rollator : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Rollator ok, nothing to do")
            
        print(CheckVar4.get())
        if CheckVar4.get()==1:
            print("+ Fauteuil Roulant (FR) was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt.txt', 'a+') as file:
                file.write("# Fauteuil Roulant (FR) : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Fauteuil Roulant (FR) ok, nothing to do")

    def uploadaux():
        """
            To upload data on server after creating files
        """
        proc = subprocess.run(["scp", "./auxequip/doc_equip/auxiliary1.txt",
            "pi@192.168.18.12:~/tt_doc/doc_txt1/Files1/auxiliary1.txt"],
            stderr=subprocess.PIPE)
        print("Result SCP transfert : %s" % repr(proc.stderr))
        if proc.stderr == b'':
            print("+ File auxiliary1.txt uploaded !")
            messagebox.showinfo("INFO", "auxiliary1.txt uploaded...")
        else:
            print("+ No file to upload !")
            messagebox.showerror("Error", "No auxiliary1.txt to upload...")

    def msgrec():
        messagebox.showinfo("Confirmation", "Record confirmed and finished !")

    def transwritedata():
        MsgBox = messagebox.askyesno('Record', 'Results will be saved, ok ?')
        if MsgBox == 1:
            print("Ok, data saved !")
            recordaux()
            uploadaux()
            msgrec()
            self.showPatients()
        else:
            messagebox.showinfo('Return', 'Ok, nothing has changed...')

    def wayout():
        try:
            self.can.delete(ALL)
            self.showPatients()
        except (OSError, ValueError) as p_out:
            print("Error from labo to way out", p_out)

    self.x3, self.y3 = 625, 100
    self.labl_title = tk.Label(self.can, text='--- Mobilisation ---',
        font="Times 14 bold", width=135,
        height=1, bg='RoyalBlue3', fg='white')
    self.labl_title = self.can.create_window(self.x3, self.y3,
        window = self.labl_title)

    self.x4, self.y4 = 134, 125
    CheckVar1 = tk.IntVar()
    self.C1 = tk.Checkbutton(self.can, text="Canne", fg='navy',
        bg='cyan', variable=CheckVar1,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C1 = self.can.create_window(self.x4, self.y4,
        window = self.C1)

    self.x5, self.y5 = 134, 148
    CheckVar2 = tk.IntVar()
    self.C2 = tk.Checkbutton(self.can, text="Tintebin", fg='navy',
        bg='cyan', variable=CheckVar2,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C2 = self.can.create_window(self.x5, self.y5,
        window = self.C2)

    self.x6, self.y6 = 134, 171
    CheckVar3 = tk.IntVar()
    self.C3 = tk.Checkbutton(self.can, text="Rollator", fg='navy',
        bg='cyan', variable=CheckVar3,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C3 = self.can.create_window(self.x6, self.y6,
        window = self.C3)

    self.x7, self.y7 = 134, 194
    CheckVar4 = tk.IntVar()
    self.C4 = tk.Checkbutton(self.can, text="Fauteuil Roulant", fg='navy',
        bg='cyan', variable=CheckVar4,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C4 = self.can.create_window(self.x7, self.y7,
        window = self.C4)

    # Button save and quit
    self.x64, self.y64 = 790, 620
    self.buttonsave = tk.Button(self.can, text="Save", width=10, bd=3,
        fg='yellow', bg='RoyalBlue3', activebackground='pale turquoise',
        highlightbackground='cyan', command=transwritedata)
    self.buttonsave = self.can.create_window(self.x64, self.y64,
        window = self.buttonsave)

    self.x65, self.y65 = 1110, 620
    self.buttonquit = tk.Button(self.can, text='Return to main menu', width=20, bd=3,
        fg='white', bg='RoyalBlue3', activebackground='pale turquoise',
        highlightbackground='cyan', command=wayout)
    self.buttonquit = self.can.create_window(self.x65, self.y65,
        window = self.buttonquit)

    self.can.configure(scrollregion=self.can.bbox(ALL))
