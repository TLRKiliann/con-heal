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
    ntry_txt = tk.StringVar()
    self.entryname = tk.Entry(self.can, textvariable=ntry_txt, width=20)
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

    self.x3, self.y3 = 200, 150
    self.labl_mob = tk.Label(self.can, text='--- Mobilisation ---',
        font="Times 14 bold", width=21,
        height=1, bg='RoyalBlue3', fg='white')
    self.labl_mob = self.can.create_window(self.x3, self.y3,
        window = self.labl_mob)

    self.x4, self.y4 = 200, 175
    CheckVar1 = tk.IntVar()
    self.C1 = tk.Checkbutton(self.can, text="Canne", fg='navy',
        bg='cyan', variable=CheckVar1,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C1 = self.can.create_window(self.x4, self.y4,
        window = self.C1)

    self.x5, self.y5 = 200, 197
    CheckVar2 = tk.IntVar()
    self.C2 = tk.Checkbutton(self.can, text="Tintebin", fg='navy',
        bg='cyan', variable=CheckVar2,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C2 = self.can.create_window(self.x5, self.y5,
        window = self.C2)

    self.x6, self.y6 = 200, 219
    CheckVar3 = tk.IntVar()
    self.C3 = tk.Checkbutton(self.can, text="Rollator", fg='navy',
        bg='cyan', variable=CheckVar3,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C3 = self.can.create_window(self.x6, self.y6,
        window = self.C3)

    self.x7, self.y7 = 200, 241
    CheckVar4 = tk.IntVar()
    self.C4 = tk.Checkbutton(self.can, text="Fauteuil Roulant", fg='navy',
        bg='cyan', variable=CheckVar4,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C4 = self.can.create_window(self.x7, self.y7,
        window = self.C4)

    self.x10, self.y10 = 200, 400
    self.labl_appa = tk.Label(self.can, text='--- Appareillage ---',
        font="Times 14 bold", width=21,
        height=1, bg='RoyalBlue3', fg='white')
    self.labl_appa = self.can.create_window(self.x10, self.y10,
        window = self.labl_appa)

    self.x11, self.y11 = 200, 425
    CheckVar5 = tk.IntVar()
    self.C5 = tk.Checkbutton(self.can, text="Veine-flon", fg='navy',
        bg='cyan', variable=CheckVar5,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C5 = self.can.create_window(self.x11, self.y11,
        window = self.C5)

    self.x12, self.y12 = 200, 447
    CheckVar6 = tk.IntVar()
    self.C6 = tk.Checkbutton(self.can, text="Pace-maker", fg='navy',
        bg='cyan', variable=CheckVar6,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C6 = self.can.create_window(self.x12, self.y12,
        window = self.C6)

    self.x13, self.y13 = 200, 469
    CheckVar7 = tk.IntVar()
    self.C7 = tk.Checkbutton(self.can, text="Pompe à insuline", fg='navy',
        bg='cyan', variable=CheckVar7,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C7 = self.can.create_window(self.x13, self.y13,
        window = self.C7)

    self.x14, self.y14 = 200, 491
    CheckVar8 = tk.IntVar()
    self.C8 = tk.Checkbutton(self.can, text="PCA (anthalgie)", fg='navy',
        bg='cyan', variable=CheckVar8,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C8 = self.can.create_window(self.x14, self.y14,
        window = self.C8)

    self.x15, self.y15 = 200, 513
    CheckVar9 = tk.IntVar()
    self.C9 = tk.Checkbutton(self.can, text="VAC (escarre)", fg='navy',
        bg='cyan', variable=CheckVar9,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C9 = self.can.create_window(self.x15, self.y15,
        window = self.C9)

    self.x16, self.y16 = 200, 535
    CheckVar10 = tk.IntVar()
    self.C10 = tk.Checkbutton(self.can, text="Lunettes", fg='navy',
        bg='cyan', variable=CheckVar10,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C10 = self.can.create_window(self.x16, self.y16,
        window = self.C10)

    self.x17, self.y17 = 200, 557
    CheckVar11 = tk.IntVar()
    self.C11 = tk.Checkbutton(self.can, text="Lunettes à O²", fg='navy',
        bg='cyan', variable=CheckVar11,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C11 = self.can.create_window(self.x17, self.y17,
        window = self.C11)

    self.x18, self.y18 = 200, 579
    CheckVar12 = tk.IntVar()
    self.C12 = tk.Checkbutton(self.can, text="Appareils auditifs", fg='navy',
        bg='cyan', variable=CheckVar12,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C12 = self.can.create_window(self.x18, self.y18,
        window = self.C12)

    self.x30, self.y30 = 800, 150
    self.labl_appa = tk.Label(self.can, text='--- Drains ---',
        font="Times 14 bold", width=65,
        height=1, bg='RoyalBlue3', fg='white')
    self.labl_appa = self.can.create_window(self.x30, self.y30,
        window = self.labl_appa)

    self.x31, self.y31 = 600, 175
    CheckVar13 = tk.IntVar()
    self.C13 = tk.Checkbutton(self.can, text="Mèche", fg='navy',
        bg='cyan', variable=CheckVar13,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C13 = self.can.create_window(self.x31, self.y31,
        window = self.C13)

    self.x32, self.y32 = 600, 197
    CheckVar14 = tk.IntVar()
    self.C14 = tk.Checkbutton(self.can, text="Drain thoracique", fg='navy',
        bg='cyan', variable=CheckVar14,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C14 = self.can.create_window(self.x32, self.y32,
        window = self.C14)

    self.x33, self.y33 = 600, 219
    CheckVar15 = tk.IntVar()
    self.C15 = tk.Checkbutton(self.can, text="Drain de Redon", fg='navy',
        bg='cyan', variable=CheckVar15,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C15 = self.can.create_window(self.x33, self.y33,
        window = self.C15)

    self.x34, self.y34 = 600, 241 # sonde nasogastrique
    CheckVar16 = tk.IntVar()
    self.C16 = tk.Checkbutton(self.can, text="Drain de Kher", fg='navy',
        bg='cyan', variable=CheckVar16,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C16 = self.can.create_window(self.x34, self.y34,
        window = self.C16)

    self.x35, self.y35 = 600, 263
    CheckVar17 = tk.IntVar()
    self.C17 = tk.Checkbutton(self.can, text="Drain de Blake", fg='navy',
        bg='cyan', variable=CheckVar17,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C17 = self.can.create_window(self.x35, self.y35,
        window = self.C17)

    self.x36, self.y36 = 600, 285
    CheckVar18 = tk.IntVar()
    self.C18 = tk.Checkbutton(self.can, text="Drain de Penrose", fg='navy',
        bg='cyan', variable=CheckVar18,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C18 = self.can.create_window(self.x36, self.y36,
        window = self.C18)

    self.x37, self.y37 = 600, 307
    CheckVar19 = tk.IntVar()
    self.C19 = tk.Checkbutton(self.can, text="Drain de Mikulicz", fg='navy',
        bg='cyan', variable=CheckVar19,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C19 = self.can.create_window(self.x37, self.y37,
        window = self.C19)

    self.x38, self.y38 = 1000, 175
    CheckVar20 = tk.IntVar()
    self.C20 = tk.Checkbutton(self.can, text="DVP (ventri.-peri.)", fg='navy',
        bg='cyan', variable=CheckVar20,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C20 = self.can.create_window(self.x38, self.y38,
        window = self.C20)

    self.x39, self.y39 = 1000, 197
    CheckVar120 = tk.IntVar()
    self.C120 = tk.Checkbutton(self.can, text="DVP (ventri.-peri.)", fg='navy',
        bg='cyan', variable=CheckVar120,
        onvalue=1, offvalue=0, height=1,
        width=120, anchor="w")
    self.C120 = self.can.create_window(self.x39, self.y39,
        window = self.C120)

    self.x50, self.y50 = 800, 400
    self.labl_proth = tk.Label(self.can, text='--- Prothesis ---',
        font="Times 14 bold", width=65,
        height=1, bg='RoyalBlue3', fg='white')
    self.labl_proth = self.can.create_window(self.x50, self.y50,
        window = self.labl_proth)

    self.x51, self.y51 = 600, 425
    CheckVar21 = tk.IntVar()
    self.C21 = tk.Checkbutton(self.can, text="PTH G", fg='navy',
        bg='cyan', variable=CheckVar21,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C21 = self.can.create_window(self.x51, self.y51,
        window = self.C21)

    self.x52, self.y52 = 600, 447
    CheckVar22 = tk.IntVar()
    self.C22 = tk.Checkbutton(self.can, text="PTH D", fg='navy',
        bg='cyan', variable=CheckVar22,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C22 = self.can.create_window(self.x52, self.y52,
        window = self.C22)

    self.x53, self.y53 = 600, 469
    CheckVar23 = tk.IntVar()
    self.C23 = tk.Checkbutton(self.can, text="PTG G", fg='navy',
        bg='cyan', variable=CheckVar23,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C23 = self.can.create_window(self.x53, self.y53,
        window = self.C23)

    self.x54, self.y54 = 600, 491
    CheckVar24 = tk.IntVar()
    self.C24 = tk.Checkbutton(self.can, text="PTG D", fg='navy',
        bg='cyan', variable=CheckVar24,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C24 = self.can.create_window(self.x54, self.y54,
        window = self.C24)

    self.x55, self.y55 = 600, 513
    CheckVar25 = tk.IntVar()
    self.C25 = tk.Checkbutton(self.can, text="PTE(I) G", fg='navy',
        bg='cyan', variable=CheckVar25,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C25 = self.can.create_window(self.x55, self.y55,
        window = self.C25)

    self.x56, self.y56 = 600, 535
    CheckVar26 = tk.IntVar()
    self.C26 = tk.Checkbutton(self.can, text="PTE(I) D", fg='navy',
        bg='cyan', variable=CheckVar26,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C26 = self.can.create_window(self.x56, self.y56,
        window = self.C26)

    self.x57, self.y57 = 600, 557
    CheckVar27 = tk.IntVar()
    self.C27 = tk.Checkbutton(self.can, text="PTC G", fg='navy',
        bg='cyan', variable=CheckVar27,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C27 = self.can.create_window(self.x57, self.y57,
        window = self.C27)

    self.x58, self.y58 = 600, 579
    CheckVar28 = tk.IntVar()
    self.C28 = tk.Checkbutton(self.can, text="PTC D", fg='navy',
        bg='cyan', variable=CheckVar28,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C28 = self.can.create_window(self.x58, self.y58,
        window = self.C28)

    self.x59, self.y59 = 1000, 425
    CheckVar29 = tk.IntVar()
    self.C29 = tk.Checkbutton(self.can, text="Prothèse oculaire", fg='navy',
        bg='cyan', variable=CheckVar29,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C29 = self.can.create_window(self.x59, self.y59,
        window = self.C29)

    self.x60, self.y60 = 1000, 447
    CheckVar30 = tk.IntVar()
    self.C30 = tk.Checkbutton(self.can, text="Prothèse(s) dentaire(s)", fg='navy',
        bg='cyan', variable=CheckVar30,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C30 = self.can.create_window(self.x60, self.y60,
        window = self.C30)

    self.x61, self.y61 = 1000, 469
    CheckVar31 = tk.IntVar()
    self.C31 = tk.Checkbutton(self.can, text="Prothèse(s) dentaire(s)", fg='navy',
        bg='cyan', variable=CheckVar31,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C31 = self.can.create_window(self.x61, self.y61,
        window = self.C31)

    self.x62, self.y62 = 1000, 491
    CheckVar32 = tk.IntVar()
    self.C32 = tk.Checkbutton(self.can, text="Prothèse(s) maxilaire", fg='navy',
        bg='cyan', variable=CheckVar32,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C32 = self.can.create_window(self.x62, self.y62,
        window = self.C32)

    self.x63, self.y63 = 1000, 513
    CheckVar33 = tk.IntVar()
    self.C33 = tk.Checkbutton(self.can, text="Prothèse(s) nasale", fg='navy',
        bg='cyan', variable=CheckVar33,
        onvalue=1, offvalue=0, height=1,
        width=20, anchor="w")
    self.C33 = self.can.create_window(self.x63, self.y63,
        window = self.C33)

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
