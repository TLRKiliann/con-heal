#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
import tkinter as tk
from tkinter import messagebox
import time
import subprocess


def doc_medical1(self):
    """
        Main function called since main app
        heal_track.py for displaying all
        DMST (Document Medical Soins Transmissions).
    """
    self.can.delete(ALL)
    self.can.configure(background='DodgerBlue2')

    self.x1, self.y1 = 530, 45
    self.labl_name = tk.Label(self.can, text="DMST",
        font=('helvetica', 18, 'bold'), width=8,
        height=2, bg='DodgerBlue2', fg='white')
    self.wlabl_name = self.can.create_window(self.x1, self.y1,
        window = self.labl_name)

    with open('./newpatient/entryfile.txt', 'r') as filename2:
        a_linedmst = filename2.readline()
        b_linedmst = filename2.readline()
        c_linedmst = filename2.readline()

    self.x2, self.y2 = 670, 45
    ntry_txt = StringVar()
    self.entryname = Entry(self.can, textvariable=ntry_txt)
    ntry_txt.set(a_linedmst[:-1])
    self.wentryname = self.can.create_window(self.x2, self.y2,
        window = self.entryname)

    self.x3, self.y3 = 300, 100
    self.labl_title = tk.Label(self.can, text='--- Personal Data ---',
        font="Times 14 bold", width=60,
        height=1, bg='RoyalBlue3', fg='white')
    self.wlabl_title = self.can.create_window(self.x3, self.y3,
        window = self.labl_title)

    self.x4, self.y4 = 120, 140
    self.LabDate = tk.Label(self.can, text="Date : ", width=15, font=12,
        fg='white', bg='DodgerBlue2', anchor='e')
    self.wLabDate_window = self.can.create_window(self.x4, self.y4, window=self.LabDate)

    self.x5, self.y5 = 120, 170
    self.LabHour = tk.Label(self.can, text="Hour : ", width=15, font=12,
        fg='white', bg='DodgerBlue2', anchor='e')
    self.wLabHour_window = self.can.create_window(self.x5, self.y5, window=self.LabHour)

    self.x6, self.y6 = 120, 200
    self.LabName = tk.Label(self.can, text="Patient name : ", width=15, font=12,
        fg='white', bg='DodgerBlue2', anchor='e')
    self.wLabName_window = self.can.create_window(self.x6, self.y6, window=self.LabName)

    self.x7, self.y7 = 120, 230
    self.birth_lab = tk.Label(self.can, text="Birthday : ", width=15, font=12,
        fg='white', bg='DodgerBlue2', anchor='e')
    self.wbirth_lab_window = self.can.create_window(self.x7, self.y7, window=self.birth_lab)

    self.x8, self.y8 = 120, 260
    self.allerlab = tk.Label(self.can, text="Allergy : ", width=15, font=12,
        fg='white', bg='DodgerBlue2', anchor='e')
    self.wallerlab_window = self.can.create_window(self.x8, self.y8, window=self.allerlab)

    self.x9, self.y9 = 290, 140
    self.time_string = tk.IntVar()
    self.textDate = tk.Entry(self.can, textvariable=self.time_string,
        highlightbackground='grey', bd=3)
    self.time_string.set(time.strftime("%d/%m/%Y"))
    self.wtextDate_window = self.can.create_window(self.x9, self.y9, window=self.textDate)

    self.x10, self.y10 = 290, 170
    self.time_Htring = tk.IntVar()
    self.textHour = tk.Entry(self.can, textvariable=self.time_Htring,
        highlightbackground='grey', bd=3)
    self.time_Htring.set(time.strftime("%H:%M:%S"))
    self.wtextHour_window = self.can.create_window(self.x10, self.y10, window=self.textHour)

    self.x11, self.y11 = 290, 200
    self.ent_name = tk.IntVar()
    self.txt_name = tk.Entry(self.can, textvariable=self.ent_name,
        highlightbackground='grey', bd=3)
    self.ent_name.set(a_linedmst[:-1])
    self.wtxt_name_window = self.can.create_window(self.x11, self.y11, window=self.txt_name)

    self.x12, self.y12 = 290, 230
    self.nt_birth = tk.IntVar()
    self.s_birth = tk.Entry(self.can, textvariable=self.nt_birth,
        highlightbackground='grey', bd=3)
    self.nt_birth.set(b_linedmst[:-1])
    self.ws_birth_window = self.can.create_window(self.x12, self.y12, window=self.s_birth)

    self.x13, self.y13 = 290, 260
    self.allertxt = tk.StringVar()
    self.allername = tk.Entry(self.can, textvariable=self.allertxt,
        highlightbackground='grey', bd=3)
    self.allertxt.set(c_linedmst[:-1])
    self.wallername_window = self.can.create_window(self.x13, self.y13, window=self.allername)

    def recordata():
        print("Date : " + time.strftime("%d/%m/%Y"))
        print("Nom du patient : ", txt_name.get())
        with open('./auxequip/doc_equip/auxiliary1.txt', 'a+') as file:
            file.write("----------------------------------------------------------\n")
            file.write("Date : ")
            file.write(time.strftime("%d/%m/%Y")+ '\n')
            file.write("Hour : ")
            file.write(time.strftime("%H:%M:%S")+ '\n')
            file.write("Patient name : ")
            file.write(txt_name.get() + '\n')
            file.write("Birthday : ")
            file.write(nt_birth.get() + '\n')
            file.write("Allergy : ")
            file.write(allername.get() + '\n')

    def uptoserv():
        """
            To upload data on server after creating files
        """
        proc = subprocess.run(["scp", "./medidoc/rslt_dmst1.txt",
            "pi@192.168.18.12:~/tt_doc/doc_txt1/Files1/rslt_dmst1.txt"],
            stderr=subprocess.PIPE)
        print("Result SCP transfert : %s" % repr(proc.stderr))
        if proc.stderr == b'':
            print("+ File rslt_dmst1.txt uploaded !")
            messagebox.showinfo("INFO", "rslt_dmst1.txt uploaded...")
        else:
            print("+ No file to upload !")
            messagebox.showerror("Error", "No rslt_dmst1.txt to upload...")

    def msgvalidate():
        messagebox.showinfo("Confirmation", "Record confirmed and finished !")

    def record_alldata():
        MsgBox = messagebox.askyesno('Record', 'Results will be saved, ok ?')
        if MsgBox == 1:
            print("Ok, data saved !")
            recordata()
            uptoserv()
            msgvalidate()
            self.showPatients()
        else:
            messagebox.showinfo('Return', 'Ok, nothing has changed...')

    def way_back():
        try:
            self.can.delete(ALL)
            self.showPatients()
        except (OSError, ValueError) as p_out:
            print("Error from labo to way out", p_out)

    # Button save and quit
    self.x64, self.y64 = 790, 620
    self.buttonsave = tk.Button(self.can, text="Save", width=10, bd=3,
        fg='yellow', bg='RoyalBlue3', activebackground='pale turquoise',
        highlightbackground='cyan', command=record_alldata)
    self.buttonsave = self.can.create_window(self.x64, self.y64,
        window = self.buttonsave)

    self.x65, self.y65 = 1110, 620
    self.buttonquit = tk.Button(self.can, text='Return to main menu', width=20, bd=3,
        fg='white', bg='RoyalBlue3', activebackground='pale turquoise',
        highlightbackground='cyan', command=way_back)
    self.buttonquit = self.can.create_window(self.x65, self.y65,
        window = self.buttonquit)

    self.can.configure(scrollregion=self.can.bbox(ALL))
