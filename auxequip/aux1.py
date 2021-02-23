#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
import tkinter as tk
from tkinter import messagebox
import subprocess
import time

def auxi_equip1(self):
    """
        Main function called since main app
        heal_track.py for displaying auxiliary
        equipement.
        Lunettes, dentier, prothèse aud,
        PTH D G, PTG D G, PTE(I) D G
        
    """
    self.can.delete(ALL)
    self.can.configure(background='DodgerBlue2')

    self.x1, self.y1 = 530, 45
    self.labl_name = tk.Label(self.can, text="Auxiliary Equipement",
        font=('helvetica', 18, 'bold'), width=20,
        height=2, bg='DodgerBlue2', fg='white')
    self.labl_name = self.can.create_window(self.x1, self.y1,
        window = self.labl_name)

    with open('./newpatient/entryfile.txt', 'r') as filename:
        line1 = filename.readline()

    self.x2, self.y2 = 760, 45
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
            endfile.write("---------------------------------------------------------\n")

        print(CheckVar1.get())
        if CheckVar1.get()==1:
            print("+ Canne was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as file:
                file.write("# Canne : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Canne ok, nothing to do")
            
        print(CheckVar2.get())
        if CheckVar2.get()==1:
            print("+ Tintebin (ttb) (FR) was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as file:
                file.write("# Tintebin (ttb) : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Tintebin (ttb) ok, nothing to do")

        print(CheckVar3.get())
        if CheckVar3.get()==1:
            print("+ Rollator was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as file:
                file.write("# Rollator : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Rollator ok, nothing to do")
            
        print(CheckVar4.get())
        if CheckVar4.get()==1:
            print("+ Fauteuil Roulant (FR) was checked !")
            with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as file:
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

    self.x3, self.y3 = 250, 150
    self.labl_mob = tk.Label(self.can, text='--- Mobilisation ---',
        font="Times 14 bold", width=24,
        height=1, bg='RoyalBlue3', fg='white')
    self.labl_mob = self.can.create_window(self.x3, self.y3,
        window = self.labl_mob)

    self.x4, self.y4 = 250, 175
    CheckVar1 = tk.IntVar()
    self.C1 = tk.Checkbutton(self.can, text="Canne", fg='navy',
        bg='cyan', variable=CheckVar1,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C1 = self.can.create_window(self.x4, self.y4,
        window = self.C1)

    self.x5, self.y5 = 250, 197
    CheckVar2 = tk.IntVar()
    self.C2 = tk.Checkbutton(self.can, text="Tintebin", fg='navy',
        bg='cyan', variable=CheckVar2,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C2 = self.can.create_window(self.x5, self.y5,
        window = self.C2)

    self.x6, self.y6 = 250, 219
    CheckVar3 = tk.IntVar()
    self.C3 = tk.Checkbutton(self.can, text="Rollator", fg='navy',
        bg='cyan', variable=CheckVar3,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C3 = self.can.create_window(self.x6, self.y6,
        window = self.C3)

    self.x7, self.y7 = 250, 241
    CheckVar4 = tk.IntVar()
    self.C4 = tk.Checkbutton(self.can, text="Fauteuil Roulant", fg='navy',
        bg='cyan', variable=CheckVar4,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C4 = self.can.create_window(self.x7, self.y7,
        window = self.C4)

    self.x10, self.y10 = 250, 300
    self.labl_appa = tk.Label(self.can, text='--- Appareillage ---',
        font="Times 14 bold", width=24,
        height=1, bg='RoyalBlue3', fg='white')
    self.labl_appa = self.can.create_window(self.x10, self.y10,
        window = self.labl_appa)

    self.x11, self.y11 = 250, 325
    CheckVar5 = tk.IntVar()
    self.C5 = tk.Checkbutton(self.can, text="Veine-flon", fg='navy',
        bg='cyan', variable=CheckVar5,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C5 = self.can.create_window(self.x11, self.y11,
        window = self.C5)

    self.x12, self.y12 = 250, 347
    CheckVar6 = tk.IntVar()
    self.C6 = tk.Checkbutton(self.can, text="Pace-maker", fg='navy',
        bg='cyan', variable=CheckVar6,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C6 = self.can.create_window(self.x12, self.y12,
        window = self.C6)

    self.x13, self.y13 = 250, 369
    CheckVar7 = tk.IntVar()
    self.C7 = tk.Checkbutton(self.can, text="Pompe à insuline", fg='navy',
        bg='cyan', variable=CheckVar7,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C7 = self.can.create_window(self.x13, self.y13,
        window = self.C7)

    self.x14, self.y14 = 250, 391
    CheckVar8 = tk.IntVar()
    self.C8 = tk.Checkbutton(self.can, text="PCA (anthalgie)", fg='navy',
        bg='cyan', variable=CheckVar8,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C8 = self.can.create_window(self.x14, self.y14,
        window = self.C8)

    self.x15, self.y15 = 250, 413
    CheckVar9 = tk.IntVar()
    self.C9 = tk.Checkbutton(self.can, text="Drain pleural", fg='navy',
        bg='cyan', variable=CheckVar9,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C9 = self.can.create_window(self.x15, self.y15,
        window = self.C9)

    self.x16, self.y16 = 250, 435
    CheckVar10 = tk.IntVar()
    self.C10 = tk.Checkbutton(self.can, text="DVP (ventri.-peri.)", fg='navy',
        bg='cyan', variable=CheckVar10,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C10 = self.can.create_window(self.x16, self.y16,
        window = self.C10)

    self.x17, self.y17 = 250, 457
    CheckVar11 = tk.IntVar()
    self.C11 = tk.Checkbutton(self.can, text="VAC (escarre)", fg='navy',
        bg='cyan', variable=CheckVar11,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C11 = self.can.create_window(self.x17, self.y17,
        window = self.C11)

    self.x30, self.y30 = 800, 200
    self.labl_proth = tk.Label(self.can, text='--- Prothesis ---',
        font="Times 14 bold", width=60,
        height=1, bg='RoyalBlue3', fg='white')
    self.labl_proth = self.can.create_window(self.x30, self.y30,
        window = self.labl_proth)

    # Button save and quit
    self.x64, self.y64 = 850, 620
    self.buttonsave = tk.Button(self.can, text="Save", width=10, bd=3,
        fg='yellow', bg='RoyalBlue3', activebackground='pale turquoise',
        highlightbackground='cyan', command=transwritedata)
    self.buttonsave = self.can.create_window(self.x64, self.y64,
        window = self.buttonsave)

    self.x65, self.y65 = 1100, 620
    self.buttonquit = tk.Button(self.can, text='Return to main menu', width=20, bd=3,
        fg='white', bg='RoyalBlue3', activebackground='pale turquoise',
        highlightbackground='cyan', command=wayout)
    self.buttonquit = self.can.create_window(self.x65, self.y65,
        window = self.buttonquit)

    self.can.configure(scrollregion=self.can.bbox(ALL))
