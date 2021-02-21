#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
import tkinter as tk
from tkinter import messagebox
import time
import os
import subprocess


def doc_medical1(self):
    """
        Main function called since main app
        heal_track.py for displaying all
        DMST (Document Medical Soins Transmissions).
    """
    self.can.delete(ALL)
    self.can.configure(background='DodgerBlue2')

    self.x1, self.y1 = 500, 45
    self.labl_name = tk.Label(self.can, text="DMST",
        font=('helvetica', 18, 'bold'), width=8,
        height=2, bg='DodgerBlue2', fg='white')
    self.wlabl_name = self.can.create_window(self.x1, self.y1,
        window = self.labl_name)

    with open('./newpatient/entryfile.txt', 'r') as filename2:
        a_linedmst = filename2.readline()
        b_linedmst = filename2.readline()
        c_linedmst = filename2.readline()
        d_linedmst = filename2.readline()

    self.x2, self.y2 = 640, 45
    ntry_txt = StringVar()
    self.entryname = Entry(self.can, textvariable=ntry_txt)
    ntry_txt.set(a_linedmst[:-1])
    self.wentryname = self.can.create_window(self.x2, self.y2,
        window = self.entryname)

    self.x3, self.y3 = 250, 100
    self.labl_title = tk.Label(self.can, text='--- Personal Data ---',
        font="Times 14 bold", width=60,
        height=1, bg='RoyalBlue3', fg='white')
    self.wlabl_title = self.can.create_window(self.x3, self.y3,
        window = self.labl_title)

    self.x33, self.y33 = 870, 100
    self.labl_title = tk.Label(self.can, text='--- Admin Data ---',
        font="Times 14 bold", width=60,
        height=1, bg='RoyalBlue3', fg='white')
    self.wlabl_title = self.can.create_window(self.x33, self.y33,
        window = self.labl_title)

    self.x4, self.y4 = 90, 140
    self.LabDate = tk.Label(self.can, text="Date : ", width=15, font=12,
        fg='white', bg='DodgerBlue2', anchor='e')
    self.wLabDate_window = self.can.create_window(self.x4, self.y4, window=self.LabDate)

    # Admin from contact col 2
    self.x44, self.y44 = 870, 240
    self.t44 = tk.Text(self.can, height=11, width=50, font=18, relief=SUNKEN)
    self.wt44_window = self.can.create_window(self.x44, self.y44, window=self.t44)

    def importationAdmin(fichier, encodage="Utf-8"):
        filecontact = open(fichier, 'r', encoding=encodage)
        content = filecontact.readlines()
        filecontact.close()
        for li in content:
            self.t44.insert(END, li)

    try:
        if os.path.getsize('./contact/conpact/finalfile1.txt'):
            importationAdmin('./contact/conpact/finalfile1.txt', encodage="Utf-8")
    except FileNotFoundError as no_file:
        print("+ File finalfile1 not found !")
        messagebox.showinfo('INFO', 'File finalfile1 not found !')

    self.x45, self.y45 = 870, 380
    self.lbl_doc = tk.Label(self.can, text='--- Doctor Data ---',
        font="Times 14 bold", width=60,
        height=1, bg='RoyalBlue3', fg='white')
    self.wlbl_doc = self.can.create_window(self.x45, self.y45,
        window = self.lbl_doc)

    # Doctor from contact col 2
    self.x47, self.y47 = 870, 490
    self.t47 = tk.Text(self.can, height=8, width=50, font=18, relief=SUNKEN)
    self.wt47_window = self.can.create_window(self.x47, self.y47, window=self.t47)

    def importationDoc1(fichier, encodage="Utf-8"):
        filecontdoc = open(fichier, 'r', encoding=encodage)
        content = filecontdoc.readlines()
        filecontdoc.close()
        for li in content:
            self.t47.insert(END, li)

    try:
        if os.path.getsize('./contact/conpact/finaldoc1.txt'):
            importationDoc1('./contact/conpact/finaldoc1.txt', encodage="Utf-8")
    except FileNotFoundError as no_file:
        print("+ File finaldoc1 not found !")
        messagebox.showinfo('INFO', 'File finaldoc1 not found !')

    # Doctor2 from contact col 2
    self.x48, self.y48 = 870, 670
    self.t48 = tk.Text(self.can, height=8, width=50, font=18, relief=SUNKEN)
    self.wt48_window = self.can.create_window(self.x48, self.y48, window=self.t48)

    def importationDoc2(fichier, encodage="Utf-8"):
        filedoc2 = open(fichier, 'r', encoding=encodage)
        content = filedoc2.readlines()
        filedoc2.close()
        for li in content:
            self.t48.insert(END, li)

    try:
        if os.path.getsize('./contact/conpact/finaldoc2.txt'):
            importationDoc2('./contact/conpact/finaldoc2.txt', encodage="Utf-8")
    except FileNotFoundError as no_file:
        print("+ File finaldoc2 not found !")
        messagebox.showinfo('INFO', 'File finaldoc2 not found !')

    # Doctor2 from contact col 2
    self.x49, self.y49 = 870, 850
    self.t49 = tk.Text(self.can, height=8, width=50, font=18, relief=SUNKEN)
    self.wt49_window = self.can.create_window(self.x49, self.y49, window=self.t49)

    def importationDoc3(fichier, encodage="Utf-8"):
        filedoc3 = open(fichier, 'r', encoding=encodage)
        content = filedoc3.readlines()
        filedoc3.close()
        for li in content:
            self.t49.insert(END, li)

    try:
        if os.path.getsize('./contact/conpact/finaldoc3.txt'):
            importationDoc3('./contact/conpact/finaldoc3.txt', encodage="Utf-8")
    except FileNotFoundError as no_file:
        print("+ File finaldoc3.txt not found !")
        messagebox.showinfo('INFO', 'File finaldoc3.txt not found !')

    # Family contact from contact col 2
    self.x50, self.y50 = 870, 960
    self.lbl_fam = tk.Label(self.can, text='--- Family Data ---',
        font="Times 14 bold", width=60,
        height=1, bg='RoyalBlue3', fg='white')
    self.wlbl_fam = self.can.create_window(self.x50, self.y50,
        window = self.lbl_fam)

    self.x51, self.y51 = 870, 1050
    self.t51 = tk.Text(self.can, height=6, width=50, font=18, relief=SUNKEN)
    self.wt51_window = self.can.create_window(self.x51, self.y51, window=self.t51)

    def importationFam(fichier, encodage="Utf-8"):
        filedoc3 = open(fichier, 'r', encoding=encodage)
        content = filedoc3.readlines()
        filedoc3.close()
        for li in content:
            self.t51.insert(END, li)

    try:
        if os.path.getsize('./contact/conpact/finalfam1.txt'):
            importationFam('./contact/conpact/finalfam1.txt', encodage="Utf-8")
    except FileNotFoundError as no_file:
        print("+ File finalfam1.txt not found !")
        messagebox.showinfo('INFO', 'File finalfam1.txt not found !')

    # Home Care System contact from contact col 2
    self.x52, self.y52 = 870, 1140
    self.lbl_heal = tk.Label(self.can, text='--- Home Care System Data ---',
        font="Times 14 bold", width=60,
        height=1, bg='RoyalBlue3', fg='white')
    self.wlbl_heal = self.can.create_window(self.x52, self.y52,
        window = self.lbl_heal)

    self.x53, self.y53 = 870, 1230
    self.t53 = tk.Text(self.can, height=6, width=50, font=18, relief=SUNKEN)
    self.wt53_window = self.can.create_window(self.x53, self.y53, window=self.t53)

    def importationHealOne(fichier, encodage="Utf-8"):
        filehcs = open(fichier, 'r', encoding=encodage)
        content = filehcs.readlines()
        filehcs.close()
        for li in content:
            self.t53.insert(END, li)

    try:
        if os.path.getsize('./contact/conpact/finalhcs1.txt'):
            importationHealOne('./contact/conpact/finalhcs1.txt', encodage="Utf-8")
    except FileNotFoundError as no_file:
        print("+ File finalhcs1.txt not found !")
        messagebox.showinfo('INFO', 'File finalhcs1.txt not found !')

    self.x54, self.y54 = 870, 1370
    self.t54 = tk.Text(self.can, height=6, width=50, font=18, relief=SUNKEN)
    self.wt54_window = self.can.create_window(self.x54, self.y54, window=self.t54)

    def importationHealTwo(fichier, encodage="Utf-8"):
        filehcs2 = open(fichier, 'r', encoding=encodage)
        content = filehcs2.readlines()
        filehcs2.close()
        for li in content:
            self.t54.insert(END, li)

    try:
        if os.path.getsize('./contact/conpact/finalhcs2.txt'):
            importationHealTwo('./contact/conpact/finalhcs2.txt', encodage="Utf-8")
    except FileNotFoundError as no_file:
        print("+ File finalhcs2.txt not found !")
        messagebox.showinfo('INFO', 'File finalhcs2.txt not found !')

    self.x55, self.y55 = 870, 1510
    self.t55 = tk.Text(self.can, height=6, width=50, font=18, relief=SUNKEN)
    self.wt55_window = self.can.create_window(self.x55, self.y55, window=self.t55)

    def importationHealThree(fichier, encodage="Utf-8"):
        filehcs3 = open(fichier, 'r', encoding=encodage)
        content = filehcs3.readlines()
        filehcs3.close()
        for li in content:
            self.t55.insert(END, li)

    try:
        if os.path.getsize('./contact/conpact/finalhcs3.txt'):
            importationHealThree('./contact/conpact/finalhcs3.txt', encodage="Utf-8")
    except FileNotFoundError as no_file:
        print("+ File finalhcs3.txt not found !")
        messagebox.showinfo('INFO', 'File finalhcs3.txt not found !')

    self.x5, self.y5 = 90, 170
    self.LabHour = tk.Label(self.can, text="Hour : ", width=15, font=12,
        fg='white', bg='DodgerBlue2', anchor='e')
    self.wLabHour_window = self.can.create_window(self.x5, self.y5, window=self.LabHour)

    self.x6, self.y6 = 90, 200
    self.LabName = tk.Label(self.can, text="Patient name : ", width=15, font=12,
        fg='white', bg='DodgerBlue2', anchor='e')
    self.wLabName_window = self.can.create_window(self.x6, self.y6, window=self.LabName)

    self.x7, self.y7 = 90, 230
    self.birth_lab = tk.Label(self.can, text="Birthday : ", width=15, font=12,
        fg='white', bg='DodgerBlue2', anchor='e')
    self.wbirth_lab_window = self.can.create_window(self.x7, self.y7, window=self.birth_lab)

    self.x8, self.y8 = 90, 260
    self.allerlab = tk.Label(self.can, text="Allergy : ", width=15, font=12,
        fg='white', bg='DodgerBlue2', anchor='e')
    self.wallerlab_window = self.can.create_window(self.x8, self.y8, window=self.allerlab)

    self.x8, self.y8 = 65, 290
    self.allerlab = tk.Label(self.can, text="Transmi. disease : ", width=20, font=12,
        fg='white', bg='DodgerBlue2', anchor='e')
    self.wallerlab_window = self.can.create_window(self.x8, self.y8, window=self.allerlab)

    self.x9, self.y9 = 30, 320 # +30
    self.diaglab = tk.Label(self.can, text="Diagnostics : ", width=15, font=12,
        fg='white', bg='DodgerBlue2', anchor='e')
    self.wdiaglab_window = self.can.create_window(self.x9, self.y9, window=self.diaglab)

    self.x10, self.y10 = 260, 140
    self.time_string = tk.IntVar()
    self.textDate = tk.Entry(self.can, textvariable=self.time_string,
        highlightbackground='grey', bd=3)
    self.time_string.set(time.strftime("%d:%m:%Y"))
    self.wtextDate_window = self.can.create_window(self.x10, self.y10, window=self.textDate)

    self.x11, self.y11 = 260, 170
    time_Htring = tk.IntVar()
    self.textHour = tk.Entry(self.can, textvariable=time_Htring,
        highlightbackground='grey', bd=3)
    time_Htring.set(time.strftime("%H:%M:%S"))
    self.wtextHour_window = self.can.create_window(self.x11, self.y11, window=self.textHour)

    self.x12, self.y12 = 260, 200
    ent_name = tk.StringVar()
    self.txt_name = tk.Entry(self.can, textvariable=ent_name,
        highlightbackground='grey', bd=3)
    ent_name.set(a_linedmst[:-1])
    self.wtxt_name_window = self.can.create_window(self.x12, self.y12, window=self.txt_name)

    self.x13, self.y13 = 260, 230
    nt_birth = tk.StringVar()
    self.s_birth = tk.Entry(self.can, textvariable=nt_birth,
        highlightbackground='grey', bd=3)
    nt_birth.set(b_linedmst[:-1])
    self.ws_birth_window = self.can.create_window(self.x13, self.y13, window=self.s_birth)

    self.x14, self.y14 = 260, 260
    allertxt = tk.StringVar()
    self.allername = tk.Entry(self.can, textvariable=allertxt,
        highlightbackground='grey', bd=3)
    allertxt.set(c_linedmst[:-1])
    self.wallername_window = self.can.create_window(self.x14, self.y14, window=self.allername)

    self.x14, self.y14 = 260, 290
    transdis = tk.StringVar()
    self.transmission = tk.Entry(self.can, textvariable=transdis,
        highlightbackground='grey', bd=3)
    transdis.set(d_linedmst[:-1])
    self.wtransmission_window = self.can.create_window(self.x14, self.y14, window=self.transmission)

    #Textbox for diag 1
    self.x15, self.y15 = 250, 440
    self.t15 = tk.Text(self.can, height=10, width=50, font=18, relief=SUNKEN)
    self.wt15_window = self.can.create_window(self.x15, self.y15, window=self.t15)

    # Display text in textbox from diag file
    try:
        with open('./diag/doc_diag/diagrecap1.txt', 'r') as filediag:
            linesdiag = filediag.readlines()
            for i in range(0, len(linesdiag)):
                for line in linesdiag:
                    line.replace('{', '')
                    line.replace('}', '')
                    line = linesdiag[i]
                    self.t15.insert(tk.INSERT, linesdiag[i])
                    self.t15.insert(tk.INSERT, linesdiag[i+1])
                    self.t15.insert(tk.INSERT, linesdiag[i+2])
                    self.t15.insert(tk.INSERT, linesdiag[i+3])
                    self.t15.insert(tk.INSERT, linesdiag[i+4])
                    self.t15.insert(tk.INSERT, linesdiag[i+5])
                    self.t15.insert(tk.INSERT, linesdiag[i+6])
                    break
                self.t15.insert(tk.INSERT,
                    "All diagnostics done...")
                break
    except FileNotFoundError as infofileout:
        print("File 1 has not been found", infofileout)
    except IndexError as inforange:
        self.t15.insert(tk.INSERT, "All diagnostics done...")
        print("List 1 got less than 6 lines", inforange)
    else:
        ("Error unknow 1 (for diag)")

    # Labl + Textbox + func to read in ttt files
    self.x16, self.y16 = 80, 560
    self.tttlab = tk.Label(self.can, text="Treatments + Reserves : ", width=25, font=12,
        fg='white', bg='DodgerBlue2', anchor='e')
    self.wtttlab_window = self.can.create_window(self.x16, self.y16, window=self.tttlab)

    self.x17, self.y17 = 250, 680
    self.t17 = tk.Text(self.can, height=10, width=50, font=18, relief=SUNKEN)
    self.wt17_window = self.can.create_window(self.x17, self.y17, window=self.t17)

    def importationFile(fichier, encodage="Utf-8"):
        file = open(fichier, 'r', encoding=encodage)
        content=file.readlines()
        file.close()
        for li in content:
            self.t17.insert(END, li)

    def importationFile2(fichier2, encodage="Utf-8"):
        file2 = open(fichier2, 'r', encoding=encodage)
        content=file2.readlines()
        file2.close()
        for li2 in content:
            self.t17.insert(END, li2)

    try:
        if os.path.getsize('./ttt/doc_ttt/intro_ttt.txt'):
            importationFile('./ttt/doc_ttt/intro_ttt.txt', encodage="Utf-8")
    except FileNotFoundError as no_file:
        print("+ File intro_ttt not found !")
        messagebox.showinfo('INFO', 'File intro_ttt not found !')

    try:
        if os.path.getsize('./ttt/doc_ttt/intro_res.txt'):
            importationFile2('./ttt/doc_ttt/intro_res.txt', encodage="Utf-8")
    except FileNotFoundError as no_file:
        print("+ File intro_res not found !")
        messagebox.showinfo('INFO', 'File intro_res not found !')

    # Lbl for VP
    self.x18, self.y18 = 60, 800
    self.paramlab = tk.Label(self.can, text="Vitals Parameters : ", width=20, font=12,
        fg='white', bg='DodgerBlue2', anchor='e')
    self.wparamlab_window = self.can.create_window(self.x18, self.y18, window=self.paramlab)

    #Textbox for param
    self.x19, self.y19 = 250, 920
    self.t19 = tk.Text(self.can, height=10, width=50, font=18, relief=SUNKEN)
    self.wt19_window = self.can.create_window(self.x19, self.y19, window=self.t19)

    # Display text in textbox from param files
    try:
        with open('./param/paramdata1.txt', 'r') as fileparam:
            linesparam = fileparam.readlines()
            for i in range(0, len(linesparam)):
                for line in linesparam:
                    line.replace('{', '')
                    line.replace('}', '')
                    line = linesparam[i]
                    self.t19.insert(tk.INSERT, linesparam[i])
                    self.t19.insert(tk.INSERT, linesparam[i+1])
                    self.t19.insert(tk.INSERT, linesparam[i+2])
                    self.t19.insert(tk.INSERT, linesparam[i+3])
                    self.t19.insert(tk.INSERT, linesparam[i+4])
                    self.t19.insert(tk.INSERT, linesparam[i+5])
                    self.t19.insert(tk.INSERT, linesparam[i+6])
                    break
                self.t19.insert(tk.INSERT,
                    "All vitals parameters done...")
                break
    except FileNotFoundError as infofileout:
        print("File 3 has not been found", infofileout)
    except IndexError as inforange:
        self.t19.insert(tk.INSERT, "All vitals parameters done...")
        print("List 3 got less than 6 lines", inforange)
    else:
        ("Error unknow 3 (for param)")

    # Lbl for BMI
    self.x18, self.y18 = 40, 1040
    self.paramlab = tk.Label(self.can, text="Weight and BMI : ", width=20, font=12,
        fg='white', bg='DodgerBlue2', anchor='e')
    self.wparamlab_window = self.can.create_window(self.x18, self.y18, window=self.paramlab)

    #Textbox for bmi
    self.x19, self.y19 = 250, 1160
    self.t19 = tk.Text(self.can, height=10, width=50, font=18, relief=SUNKEN)
    self.wt19_window = self.can.create_window(self.x19, self.y19, window=self.t19)

    # Display text in textbox from bmi files
    try:
        with open('./calBmi/bmi.txt', 'r') as filebmi:
            linesbmi = filebmi.readlines()
            for i in range(0, len(linesbmi)):
                for line in linesbmi:
                    line.replace('{', '')
                    line.replace('}', '')
                    line = linesbmi[i]
                    self.t19.insert(tk.INSERT, linesbmi[i])
                    self.t19.insert(tk.INSERT, linesbmi[i+1])
                    self.t19.insert(tk.INSERT, linesbmi[i+2])
                    self.t19.insert(tk.INSERT, linesbmi[i+3])
                    self.t19.insert(tk.INSERT, linesbmi[i+4])
                    self.t19.insert(tk.INSERT, linesbmi[i+5])
                    self.t19.insert(tk.INSERT, linesbmi[i+6])
                    break
                self.t19.insert(tk.INSERT,
                    "All bmi done...")
                break
    except FileNotFoundError as infofileout:
        print("File 4 has not been found", infofileout)
    except IndexError as inforange:
        self.t19.insert(tk.INSERT, "All bmi done...")
        print("List 4 got less than 6 lines", inforange)
    else:
        ("Error unknow 4 (for BMI)")

    self.x58, self.y58 = 250, 1290 
    self.lbl_need = tk.Label(self.can, text='--- 14 needs and depedencies ---',
        font="Times 14 bold", width=60,
        height=1, bg='RoyalBlue3', fg='white')
    self.wlbl_need = self.can.create_window(self.x58, self.y58,
        window = self.lbl_need)

    """
    Boire et manger
    Respirer
    Dormir, se reposer
    Etre propre, protéger ses téguments
    Elimination
    Se recréer
    Apprendre
    Température
    S'occuper en vue de se réaliser
    Agir selon ses valeurs et croyances
    Se vêtir et se dévêtir
    Eviter les dangers
    Se mouvoir, maintenir une bonne posture
    Communiquer avec ses semblables
    """

    def recordata():
        print("Date : " + time.strftime("%d/%m/%Y"))
        print("Nom du patient : ", ent_name.get())
        with open('./medidoc/rslt_dmst1.txt', 'a+') as file:
            file.write("----------------------------------------------------------\n")
            file.write("Date : ")
            file.write(time.strftime("%d.%m.%Y") + '\n')
            file.write("Hour : ")
            file.write(time.strftime("%H:%M:%S") + '\n')
            file.write("Patient name : ")
            file.write(ent_name.get() + '\n')
            file.write("Birthday : ")
            file.write(nt_birth.get() + '\n')
            file.write("Allergy : ")
            file.write(allertxt.get() + '\n')
            file.write("Transmissible disease : ")
            file.write(transdis.get() + '\n')
            file.write("----------------------------------------------------------\n")

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
            print("Error from dmst to way out", p_out)

    # Button save and quit
    self.x64, self.y64 = 780, 2000
    self.buttonsave = tk.Button(self.can, text="Save", width=10, bd=3,
        fg='yellow', bg='RoyalBlue3', activebackground='pale turquoise',
        highlightbackground='cyan', command = record_alldata)
    self.buttonsave = self.can.create_window(self.x64, self.y64,
        window = self.buttonsave)

    self.x65, self.y65 = 1050, 2000
    self.buttonquit = tk.Button(self.can, text='Return to main menu', width=20, bd=3,
        fg='white', bg='RoyalBlue3', activebackground='pale turquoise',
        highlightbackground='cyan', command = way_back)
    self.buttonquit = self.can.create_window(self.x65, self.y65,
        window = self.buttonquit)

    self.can.configure(scrollregion=self.can.bbox(ALL))
