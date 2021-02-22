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

    self.x4, self.y4 = 870, 100
    self.labl_title2 = tk.Label(self.can, text='--- Admin Data ---',
        font="Times 14 bold", width=60,
        height=1, bg='RoyalBlue3', fg='white')
    self.wlabl_title2 = self.can.create_window(self.x4, self.y4,
        window = self.labl_title2)

    self.x5, self.y5 = 90, 140
    self.LabDate = tk.Label(self.can, text="Date : ", width=15, font=12,
        fg='white', bg='DodgerBlue2', anchor='e')
    self.wLabDate_window = self.can.create_window(self.x5, self.y5, window=self.LabDate)

    # Admin from contact col 2
    self.x6, self.y6 = 870, 240
    self.t6 = tk.Text(self.can, height=11, width=50, font=18, relief=SUNKEN)
    self.wt6_window = self.can.create_window(self.x6, self.y6, window=self.t6)

    def importationAdmin(fichier, encodage="Utf-8"):
        filecontact = open(fichier, 'r', encoding=encodage)
        content = filecontact.readlines()
        filecontact.close()
        for li in content:
            self.t6.insert(END, li)

    try:
        if os.path.getsize('./contact/conpact/finalfile1.txt'):
            importationAdmin('./contact/conpact/finalfile1.txt', encodage="Utf-8")
    except FileNotFoundError as no_file:
        print("+ File finalfile1 not found !")
        messagebox.showinfo('INFO', 'File finalfile1 not found !')

    self.x7, self.y7 = 870, 380
    self.lbl_doc = tk.Label(self.can, text='--- Doctor Data ---',
        font="Times 14 bold", width=60,
        height=1, bg='RoyalBlue3', fg='white')
    self.wlbl_doc = self.can.create_window(self.x7, self.y7,
        window = self.lbl_doc)

    # Doctor from contact col 2
    self.x8, self.y8 = 870, 490
    self.t8 = tk.Text(self.can, height=8, width=50, font=18, relief=SUNKEN)
    self.wt8_window = self.can.create_window(self.x8, self.y8, window=self.t8)

    def importationDoc1(fichier, encodage="Utf-8"):
        filecontdoc = open(fichier, 'r', encoding=encodage)
        content = filecontdoc.readlines()
        filecontdoc.close()
        for li in content:
            self.t8.insert(END, li)

    try:
        if os.path.getsize('./contact/conpact/finaldoc1.txt'):
            importationDoc1('./contact/conpact/finaldoc1.txt', encodage="Utf-8")
    except FileNotFoundError as no_file:
        print("+ File finaldoc1 not found !")
        messagebox.showinfo('INFO', 'File finaldoc1 not found !')

    # Doctor2 from contact col 2
    self.x9, self.y9 = 870, 670
    self.t9 = tk.Text(self.can, height=8, width=50, font=18, relief=SUNKEN)
    self.wt9_window = self.can.create_window(self.x9, self.y9, window=self.t9)

    def importationDoc2(fichier, encodage="Utf-8"):
        filedoc2 = open(fichier, 'r', encoding=encodage)
        content = filedoc2.readlines()
        filedoc2.close()
        for li in content:
            self.t9.insert(END, li)

    try:
        if os.path.getsize('./contact/conpact/finaldoc2.txt'):
            importationDoc2('./contact/conpact/finaldoc2.txt', encodage="Utf-8")
    except FileNotFoundError as no_file:
        print("+ File finaldoc2 not found !")
        messagebox.showinfo('INFO', 'File finaldoc2 not found !')

    # Doctor2 from contact col 2
    self.x10, self.y10 = 870, 850
    self.t10 = tk.Text(self.can, height=8, width=50, font=18, relief=SUNKEN)
    self.wt10_window = self.can.create_window(self.x10, self.y10, window=self.t10)

    def importationDoc3(fichier, encodage="Utf-8"):
        filedoc3 = open(fichier, 'r', encoding=encodage)
        content = filedoc3.readlines()
        filedoc3.close()
        for li in content:
            self.t10.insert(END, li)

    try:
        if os.path.getsize('./contact/conpact/finaldoc3.txt'):
            importationDoc3('./contact/conpact/finaldoc3.txt', encodage="Utf-8")
    except FileNotFoundError as no_file:
        print("+ File finaldoc3.txt not found !")
        messagebox.showinfo('INFO', 'File finaldoc3.txt not found !')

    # Family contact from contact col 2
    self.x11, self.y11 = 870, 960
    self.lbl_fam = tk.Label(self.can, text='--- Family Data ---',
        font="Times 14 bold", width=60,
        height=1, bg='RoyalBlue3', fg='white')
    self.wlbl_fam = self.can.create_window(self.x11, self.y11,
        window = self.lbl_fam)

    self.x12, self.y12 = 870, 1050
    self.t12 = tk.Text(self.can, height=6, width=50, font=18, relief=SUNKEN)
    self.wt12_window = self.can.create_window(self.x12, self.y12, window=self.t12)

    def importationFam(fichier, encodage="Utf-8"):
        filedoc3 = open(fichier, 'r', encoding=encodage)
        content = filedoc3.readlines()
        filedoc3.close()
        for li in content:
            self.t12.insert(END, li)

    try:
        if os.path.getsize('./contact/conpact/finalfam1.txt'):
            importationFam('./contact/conpact/finalfam1.txt', encodage="Utf-8")
    except FileNotFoundError as no_file:
        print("+ File finalfam1.txt not found !")
        messagebox.showinfo('INFO', 'File finalfam1.txt not found !')

    # Home Care System contact from contact col 2
    self.x13, self.y13 = 870, 1140
    self.lbl_heal = tk.Label(self.can, text='--- Home Care System Data ---',
        font="Times 14 bold", width=60,
        height=1, bg='RoyalBlue3', fg='white')
    self.wlbl_heal = self.can.create_window(self.x13, self.y13,
        window = self.lbl_heal)

    self.x14, self.y14 = 870, 1230
    self.t14 = tk.Text(self.can, height=6, width=50, font=18, relief=SUNKEN)
    self.wt14_window = self.can.create_window(self.x14, self.y14, window=self.t14)

    def importationHealOne(fichier, encodage="Utf-8"):
        filehcs = open(fichier, 'r', encoding=encodage)
        content = filehcs.readlines()
        filehcs.close()
        for li in content:
            self.t14.insert(END, li)

    try:
        if os.path.getsize('./contact/conpact/finalhcs1.txt'):
            importationHealOne('./contact/conpact/finalhcs1.txt', encodage="Utf-8")
    except FileNotFoundError as no_file:
        print("+ File finalhcs1.txt not found !")
        messagebox.showinfo('INFO', 'File finalhcs1.txt not found !')

    self.x15, self.y15 = 870, 1370
    self.t15 = tk.Text(self.can, height=6, width=50, font=18, relief=SUNKEN)
    self.wt15_window = self.can.create_window(self.x15, self.y15, window=self.t15)

    def importationHealTwo(fichier, encodage="Utf-8"):
        filehcs2 = open(fichier, 'r', encoding=encodage)
        content = filehcs2.readlines()
        filehcs2.close()
        for li in content:
            self.t15.insert(END, li)

    try:
        if os.path.getsize('./contact/conpact/finalhcs2.txt'):
            importationHealTwo('./contact/conpact/finalhcs2.txt', encodage="Utf-8")
    except FileNotFoundError as no_file:
        print("+ File finalhcs2.txt not found !")
        messagebox.showinfo('INFO', 'File finalhcs2.txt not found !')

    self.x16, self.y16 = 870, 1510
    self.t16 = tk.Text(self.can, height=6, width=50, font=18, relief=SUNKEN)
    self.wt16_window = self.can.create_window(self.x16, self.y16, window=self.t16)

    def importationHealThree(fichier, encodage="Utf-8"):
        filehcs3 = open(fichier, 'r', encoding=encodage)
        content = filehcs3.readlines()
        filehcs3.close()
        for li in content:
            self.t16.insert(END, li)

    try:
        if os.path.getsize('./contact/conpact/finalhcs3.txt'):
            importationHealThree('./contact/conpact/finalhcs3.txt', encodage="Utf-8")
    except FileNotFoundError as no_file:
        print("+ File finalhcs3.txt not found !")
        messagebox.showinfo('INFO', 'File finalhcs3.txt not found !')

    self.x17, self.y17 = 90, 170
    self.LabHour = tk.Label(self.can, text="Hour : ", width=15, font=12,
        fg='white', bg='DodgerBlue2', anchor='e')
    self.wLabHour_window = self.can.create_window(self.x17, self.y17, window=self.LabHour)

    self.x18, self.y18 = 90, 200
    self.LabName = tk.Label(self.can, text="Patient name : ", width=15, font=12,
        fg='white', bg='DodgerBlue2', anchor='e')
    self.wLabName_window = self.can.create_window(self.x18, self.y18, window=self.LabName)

    self.x19, self.y19 = 90, 230
    self.birth_lab = tk.Label(self.can, text="Birthday : ", width=15, font=12,
        fg='white', bg='DodgerBlue2', anchor='e')
    self.wbirth_lab_window = self.can.create_window(self.x19, self.y19, window=self.birth_lab)

    self.x20, self.y20 = 90, 260
    self.allerlab = tk.Label(self.can, text="Allergy : ", width=15, font=12,
        fg='white', bg='DodgerBlue2', anchor='e')
    self.wallerlab_window = self.can.create_window(self.x20, self.y20, window=self.allerlab)

    self.x21, self.y21 = 65, 290
    self.tran_dis = tk.Label(self.can, text="Transmi. disease : ", width=20, font=12,
        fg='white', bg='DodgerBlue2', anchor='e')
    self.wtran_dis_window = self.can.create_window(self.x21, self.y21, window=self.tran_dis)

    self.x22, self.y22 = 30, 320 # +30
    self.diaglab = tk.Label(self.can, text="Diagnostics : ", width=15, font=12,
        fg='white', bg='DodgerBlue2', anchor='e')
    self.wdiaglab_window = self.can.create_window(self.x22, self.y22, window=self.diaglab)

    self.x23, self.y23 = 260, 140
    self.time_string = tk.IntVar()
    self.textDate = tk.Entry(self.can, textvariable=self.time_string,
        highlightbackground='grey', bd=3)
    self.time_string.set(time.strftime("%d:%m:%Y"))
    self.wtextDate_window = self.can.create_window(self.x23, self.y23, window=self.textDate)

    self.x24, self.y24 = 260, 170
    time_Htring = tk.IntVar()
    self.textHour = tk.Entry(self.can, textvariable=time_Htring,
        highlightbackground='grey', bd=3)
    time_Htring.set(time.strftime("%H:%M:%S"))
    self.wtextHour_window = self.can.create_window(self.x24, self.y24, window=self.textHour)

    self.x25, self.y25 = 260, 200
    ent_name = tk.StringVar()
    self.txt_name = tk.Entry(self.can, textvariable=ent_name,
        highlightbackground='grey', bd=3)
    ent_name.set(a_linedmst[:-1])
    self.wtxt_name_window = self.can.create_window(self.x25, self.y25, window=self.txt_name)

    self.x26, self.y26 = 260, 230
    nt_birth = tk.StringVar()
    self.s_birth = tk.Entry(self.can, textvariable=nt_birth,
        highlightbackground='grey', bd=3)
    nt_birth.set(b_linedmst[:-1])
    self.ws_birth_window = self.can.create_window(self.x26, self.y26, window=self.s_birth)

    self.x27, self.y27 = 260, 260
    allertxt = tk.StringVar()
    self.allername = tk.Entry(self.can, textvariable=allertxt,
        highlightbackground='grey', bd=3)
    allertxt.set(c_linedmst[:-1])
    self.wallername_window = self.can.create_window(self.x27, self.y27, window=self.allername)

    self.x28, self.y28 = 260, 290
    transdis = tk.StringVar()
    self.transmission = tk.Entry(self.can, textvariable=transdis,
        highlightbackground='grey', bd=3)
    transdis.set(d_linedmst[:-1])
    self.wtransmission_window = self.can.create_window(self.x28, self.y28, window=self.transmission)

    #Textbox for diag 1
    self.x29, self.y29 = 250, 440
    self.t29 = tk.Text(self.can, height=10, width=50, font=18, relief=SUNKEN)
    self.wt29_window = self.can.create_window(self.x29, self.y29, window=self.t29)

    # Display text in textbox from diag file
    try:
        with open('./diag/doc_diag/diagrecap1.txt', 'r') as filediag:
            linesdiag = filediag.readlines()
            for i in range(0, len(linesdiag)):
                for line in linesdiag:
                    line.replace('{', '')
                    line.replace('}', '')
                    line = linesdiag[i]
                    self.t29.insert(tk.INSERT, linesdiag[i])
                    self.t29.insert(tk.INSERT, linesdiag[i+1])
                    self.t29.insert(tk.INSERT, linesdiag[i+2])
                    self.t29.insert(tk.INSERT, linesdiag[i+3])
                    self.t29.insert(tk.INSERT, linesdiag[i+4])
                    self.t29.insert(tk.INSERT, linesdiag[i+5])
                    self.t29.insert(tk.INSERT, linesdiag[i+6])
                    break
                self.t29.insert(tk.INSERT,
                    "All diagnostics done...")
                break
    except FileNotFoundError as infofileout:
        print("File 1 has not been found", infofileout)
    except IndexError as inforange:
        self.t29.insert(tk.INSERT, "All diagnostics done...")
        print("List 1 got less than 6 lines", inforange)
    else:
        ("Error unknow 1 (for diag)")

    # Labl + Textbox + func to read in ttt files
    self.x30, self.y30 = 80, 560
    self.tttlab = tk.Label(self.can, text="Treatments + Reserves : ", width=25, font=12,
        fg='white', bg='DodgerBlue2', anchor='e')
    self.wtttlab_window = self.can.create_window(self.x30, self.y30, window=self.tttlab)

    self.x31, self.y31 = 250, 680
    self.t31 = tk.Text(self.can, height=10, width=50, font=18, relief=SUNKEN)
    self.wt31_window = self.can.create_window(self.x31, self.y31, window=self.t31)

    def importationFile(fichier, encodage="Utf-8"):
        file = open(fichier, 'r', encoding=encodage)
        content=file.readlines()
        file.close()
        for li in content:
            self.t31.insert(END, li)

    def importationFile2(fichier2, encodage="Utf-8"):
        file2 = open(fichier2, 'r', encoding=encodage)
        content=file2.readlines()
        file2.close()
        for li2 in content:
            self.t31.insert(END, li2)

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
    self.x32, self.y32 = 60, 800
    self.paramlab = tk.Label(self.can, text="Vitals Parameters : ", width=20, font=12,
        fg='white', bg='DodgerBlue2', anchor='e')
    self.wparamlab_window = self.can.create_window(self.x32, self.y32, window=self.paramlab)

    #Textbox for param
    self.x33, self.y33 = 250, 920
    self.t33 = tk.Text(self.can, height=10, width=50, font=18, relief=SUNKEN)
    self.wt33_window = self.can.create_window(self.x33, self.y33, window=self.t33)

    # Display text in textbox from param files
    def importationParam(fichier, encodage="Utf-8"):
        fileparam = open(fichier, 'r', encoding=encodage)
        content = fileparam.readlines()
        fileparam.close()
        for li in content:
            self.t33.insert(END, li)

    try:
        if os.path.getsize('./param/paramdata1.txt'):
            importationParam('./param/paramdata1.txt', encodage="Utf-8")
    except FileNotFoundError as no_file:
        print("+ File paramdata1.txt not found !")
        messagebox.showinfo('INFO', 'File paramdata1.txt not found !')

    # Lbl for BMI
    self.x34, self.y34 = 40, 1040
    self.paramlab = tk.Label(self.can, text="Weight and BMI : ", width=20, font=12,
        fg='white', bg='DodgerBlue2', anchor='e')
    self.wparamlab_window = self.can.create_window(self.x34, self.y34, window=self.paramlab)

    #Textbox for bmi
    self.x35, self.y35 = 250, 1160
    self.t35 = tk.Text(self.can, height=10, width=50, font=18, relief=SUNKEN)
    self.wt35_window = self.can.create_window(self.x35, self.y35, window=self.t35)

    # Display text in textbox from bmi files
    def importationBmi(fichier, encodage="Utf-8"):
        filebmi = open(fichier, 'r', encoding=encodage)
        content = filebmi.readlines()
        filebmi.close()
        for li in content:
            self.t35.insert(END, li)
    try:
        if os.path.getsize('./calBmi/bmi.txt'):
            importationBmi('./calBmi/bmi.txt', encodage="Utf-8")
    except FileNotFoundError as no_file:
        print("+ File bmi.txt not found !")
        messagebox.showinfo('INFO', 'File bmi.txt not found !')

    def recordata():
        """
            To record all data in GUI to txt file.
            I need a try here !!!
        """
        try:
            if os.path.getsize('./medidoc/rslt_dmst1.txt'):
                messagebox.showwarning('Warning',
                    '!!! Warning, saving new data will erased old file !!!')
                msgayn = messagebox.askyesno('ask', 'Would you like to continue')
                if msgayn == 1:
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

                    with open('./diag/doc_diag/diagrecap1.txt', 'r') as file_di:
                        with open('./medidoc/rslt_dmst1.txt', '+a') as file_dm:
                            diag_content = file_di.readlines()
                            for li in diag_content:
                                file_dm.writelines(diag_content)
                                break

                    with open('./ttt/doc_ttt/intro_ttt.txt', 'r') as file_ttt:
                        with open('./medidoc/rslt_dmst1.txt', '+a') as file_dm:
                            ttt_content = file_ttt.readlines()
                            for li in ttt_content:
                                file_dm.writelines(ttt_content)
                                break

                    with open('./ttt/doc_ttt/intro_res.txt', 'r') as file_res:
                        with open('./medidoc/rslt_dmst1.txt', '+a') as file_dm:
                            res_content = file_res.readlines()
                            for li in res_content:
                                file_dm.writelines(res_content)
                                break


./param/paramdata1.txt
./calBmi/bmi.txt


                    with open('./contact/conpact/finalfile1.txt', 'r') as file_contf1:
                        with open('./medidoc/rslt_dmst1.txt', '+a') as file_dm:
                            fcf1_content = file_contf1.readlines()
                            for li in fcf1_content:
                                file_dm.writelines(fcf1_content)
                                break

                    with open('./contact/conpact/finaldoc1.txt', 'r') as file_do1:
                        with open('./medidoc/rslt_dmst1.txt', '+a') as file_dm:
                            fcd1_content = file_do1.readlines()
                            for li in fcd1_content:
                                file_dm.writelines(fcd1_content)
                                break

                    with open('./contact/conpact/finaldoc2.txt', 'r') as file_do2:
                        with open('./medidoc/rslt_dmst1.txt', '+a') as file_dm:
                            fcd2_content = file_do2.readlines()
                            for li in fcd2_content:
                                file_dm.writelines(fcd2_content)
                                break

                    with open('./contact/conpact/finaldoc3.txt', 'r') as file_do3:
                        with open('./medidoc/rslt_dmst1.txt', '+a') as file_dm:
                            fcd3_content = file_do3.readlines()
                            for li in fcd3_content:
                                file_dm.writelines(fcd3_content)
                                break

                    with open('./contact/conpact/finalfam1.txt', 'r') as file_fam:
                        with open('./medidoc/rslt_dmst1.txt', '+a') as file_dm:
                            ff_content = file_fam.readlines()
                            for li in ff_content:
                                file_dm.writelines(ff_content)
                                break

                    with open('./contact/conpact/finalhcs1.txt', 'r') as file_hcs1:
                        with open('./medidoc/rslt_dmst1.txt', '+a') as file_dm:
                            hcs1_content = file_hcs1.readlines()
                            for li in hcs1_content:
                                file_dm.writelines(hcs1_content)
                                break

                    with open('./contact/conpact/finalhcs2.txt', 'r') as file_hcs2:
                        with open('./medidoc/rslt_dmst1.txt', '+a') as file_dm:
                            hcs2_content = file_hcs2.readlines()
                            for li in hcs2_content:
                                file_dm.writelines(hcs2_content)
                                break

                    with open('./contact/conpact/finalhcs3.txt', 'r') as file_hcs3:
                        with open('./medidoc/rslt_dmst1.txt', '+a') as file_dm:
                            hcs3_content = file_hcs3.readlines()
                            for li in hcs3_content:
                                file_dm.writelines(hcs3_content)
                                break

                    print(CheckVar1.get())
                    if CheckVar1.get() == 1:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file1:
                            file1.write("+ Orientation = 1\n")
                    elif CheckVar1.get() == 2:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file2:
                            file2.write("+ Orientation = 2\n")
                    elif CheckVar1.get() == 3:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file3:
                            file3.write("+ Orientation = 3\n")
                    elif CheckVar1.get() == 4:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file4:
                            file4.write("+ Orientation = 4\n")
                    else:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file0:
                            file0.write("+ Orientation = 0\n")

                    print(CheckVar2.get())
                    if CheckVar2.get() == 1:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file1:
                            file1.write("+ Cohérence = 1\n")
                    elif CheckVar2.get() == 2:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file2:
                            file2.write("+ Cohérence = 2\n")
                    elif CheckVar2.get() == 3:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file3:
                            file3.write("+ Cohérence = 3\n")
                    elif CheckVar2.get() == 4:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file4:
                            file4.write("+ Cohérence = 4\n")
                    else:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file0:
                            file0.write("+ Cohérence = 0\n")

                    print(CheckVar3.get())
                    if CheckVar3.get() == 1:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file1:
                            file1.write("+ Toilette = 1\n")
                    elif CheckVar3.get() == 2:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file2:
                            file2.write("+ Toilette = 2\n")
                    elif CheckVar3.get() == 3:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file3:
                            file3.write("+ Toilette = 3\n")
                    elif CheckVar3.get() == 4:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file4:
                            file4.write("+ Toilette = 4\n")
                    else:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file0:
                            file0.write("+ Toilette = 0\n")

                    print(CheckVar4.get())
                    if CheckVar4.get() == 1:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file1:
                            file1.write("+ Habillage = 1\n")
                    elif CheckVar4.get() == 2:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file2:
                            file2.write("+ Habillage = 2\n")
                    elif CheckVar4.get() == 3:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file3:
                            file3.write("+ Habillage = 3\n")
                    elif CheckVar4.get() == 4:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file4:
                            file4.write("+ Habillage = 4\n")
                    else:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file0:
                            file0.write("+ Habillage = 0\n")

                    print(CheckVar5.get())
                    if CheckVar5.get() == 1:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file1:
                            file1.write("+ Alimentation = 1\n")
                    elif CheckVar5.get() == 2:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file2:
                            file2.write("+ Alimentation = 2\n")
                    elif CheckVar5.get() == 3:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file3:
                            file3.write("+ Alimentation = 3\n")
                    elif CheckVar5.get() == 4:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file4:
                            file4.write("+ Alimentation = 4\n")
                    else:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file0:
                            file0.write("+ Alimentation = 0\n")

                    print(CheckVar6.get())
                    if CheckVar6.get() == 1:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file1:
                            file1.write("+ Elimination = 1\n")
                    elif CheckVar6.get() == 2:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file2:
                            file2.write("+ Elimination = 2\n")
                    elif CheckVar6.get() == 3:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file3:
                            file3.write("+ Elimination = 3\n")
                    elif CheckVar6.get() == 4:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file4:
                            file4.write("+ Elimination = 4\n")
                    else:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file0:
                            file0.write("+ Elimination = 0\n")

                    print(CheckVar7.get())
                    if CheckVar7.get() == 1:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file1:
                            file1.write("+ Déplacement = 1\n")
                    elif CheckVar7.get() == 2:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file2:
                            file2.write("+ Déplacement = 2\n")
                    elif CheckVar7.get() == 3:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file3:
                            file3.write("+ Déplacement = 3\n")
                    elif CheckVar7.get() == 4:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file4:
                            file4.write("+ Déplacement = 4\n")
                    else:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file0:
                            file0.write("+ Déplacement = 0\n")

                    print(CheckVar8.get())
                    if CheckVar8.get() == 1:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file1:
                            file1.write("+ Communication = 1\n")
                    elif CheckVar8.get() == 2:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file2:
                            file2.write("+ Communication = 2\n")
                    elif CheckVar8.get() == 3:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file3:
                            file3.write("+ Communication = 3\n")
                    elif CheckVar8.get() == 4:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file4:
                            file4.write("+ Communication = 4\n")
                    else:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file0:
                            file0.write("+ Communication = 0\n")

                    print(CheckVar9.get())
                    if CheckVar9.get() == 1:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file1:
                            file1.write("+ Directives anticipées = Oui\n")
                    else:
                        print("+ None (DA)")

                    print(CheckVar10.get())
                    if CheckVar10.get() == 1:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file1:
                            file1.write("+ Directives anticipées = Non\n")
                    else:
                        print("+ None (DA)")

                    print(CheckVar11.get())
                    if CheckVar11.get() == 1:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file1:
                            file1.write("+ PLAFA = Oui\n")
                    else:
                        print("+ None (PLAFA)")

                    print(CheckVar12.get())
                    if CheckVar12.get() == 1:
                        with open('./medidoc/rslt_dmst1.txt', 'a+') as file1:
                            file1.write("+ PLAFA = Non\n")
                    else:
                        print("+ None (PLAFA)")
                else:
                    messagebox.showinfo('Info', 'Nothing has changed !')
        except FileNotFoundError as fnf_totry:
            print("+ No file dmst1.txt exist !", fnf_totry)

    self.x36, self.y36 = 250, 1290 
    self.lbl_need = tk.Label(self.can, text='--- AGGIR (grid) and depedencies ---',
        font="Times 14 bold", width=60,
        height=1, bg='RoyalBlue3', fg='white')
    self.wlbl_need = self.can.create_window(self.x36, self.y36,
        window = self.lbl_need)

    self.x37, self.y37 = 250, 1320
    self.lbl_exneeds = tk.Label(self.can, text="0 = None / 1 = supervision only /"\
        " 2 = passive help / 3 = active help / 4 = show and tell",
        font="Times 11", width=80,
        height=1, bg='DodgerBlue2', fg='white')
    self.wlbl_exneeds = self.can.create_window(self.x37, self.y37,
        window = self.lbl_exneeds)

    self.x38, self.y38 = 80, 1360
    self.lbl_eat = tk.Label(self.can, text='- Orientation :',
        font="Times 14 bold", width=20, height=1,
        bg='DodgerBlue2', fg='white', anchor='w')
    self.wlbl_eat = self.can.create_window(self.x38, self.y38,
        window = self.lbl_eat)

    CheckVar1 = tk.IntVar()
    self.x39, self.y39 = 240, 1360
    self.C0 = tk.Radiobutton(self.can, text="0", highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=CheckVar1,
        value=0, height=1, width=3, anchor='w')
    self.wC0 = self.can.create_window(self.x39, self.y39,
        window = self.C0)

    self.x40, self.y40 = 295, 1360
    self.C1 = tk.Radiobutton(self.can, text="1", highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=CheckVar1,
        value=1, height=1, width=3, anchor='w')
    self.wC1 = self.can.create_window(self.x40, self.y40,
        window = self.C1)

    self.x41, self.y41 = 350, 1360
    self.C2 = tk.Radiobutton(self.can, text="2", highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=CheckVar1,
        value=2, height=1, width=3, anchor='w')
    self.wC2 = self.can.create_window(self.x41, self.y41,
        window = self.C2)

    self.x42, self.y42 = 405, 1360
    self.C3 = tk.Radiobutton(self.can, text="3", highlightbackground='cyan', fg='black', 
        bg='DodgerBlue2', variable=CheckVar1, 
        value=3, height=1, width=3, anchor='w')
    self.wC3 = self.can.create_window(self.x42, self.y42,
        window = self.C3)

    self.x43, self.y43 = 460, 1360
    self.C4 = tk.Radiobutton(self.can, text="4", highlightbackground='cyan', fg='black', 
        bg='DodgerBlue2', variable=CheckVar1, 
        value=4, height=1, width=3, anchor='w')
    self.wC4 = self.can.create_window(self.x43, self.y43,
        window = self.C4)

    # second need
    self.x44, self.y44 = 80, 1385
    self.lbl_sec = tk.Label(self.can, text='- Cohérence :',
        font="Times 14 bold", width=20, height=1,
        bg='DodgerBlue2', fg='white', anchor='w')
    self.wlbl_sec = self.can.create_window(self.x44, self.y44,
        window = self.lbl_sec)

    CheckVar2 = tk.IntVar()
    self.x45, self.y45 = 240, 1385
    self.C10 = tk.Radiobutton(self.can, text="0", highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=CheckVar2,
        value=0, height=1, width=3, anchor='w')
    self.wC10 = self.can.create_window(self.x45, self.y45,
        window = self.C10)

    self.x46, self.y46 = 295, 1385
    self.C11 = tk.Radiobutton(self.can, text="1", highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=CheckVar2,
        value=1, height=1, width=3, anchor='w')
    self.wC11 = self.can.create_window(self.x46, self.y46,
        window = self.C11)

    self.x47, self.y47 = 350, 1385
    self.C12 = tk.Radiobutton(self.can, text="2", highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=CheckVar2,
        value=2, height=1, width=3, anchor='w')
    self.wC12 = self.can.create_window(self.x47, self.y47,
        window = self.C12)

    self.x48, self.y48 = 405, 1385
    self.C13 = tk.Radiobutton(self.can, text="3", highlightbackground='cyan', fg='black', 
        bg='DodgerBlue2', variable=CheckVar2, 
        value=3, height=1, width=3, anchor='w')
    self.wC13 = self.can.create_window(self.x48, self.y48,
        window = self.C13)

    self.x49, self.y49 = 460, 1385
    self.C14 = tk.Radiobutton(self.can, text="4", highlightbackground='cyan', fg='black', 
        bg='DodgerBlue2', variable=CheckVar2, 
        value=4, height=1, width=3, anchor='w')
    self.wC14 = self.can.create_window(self.x49, self.y49,
        window = self.C14)

    # third need
    self.x50, self.y50 = 80, 1410
    self.lbl_third = tk.Label(self.can, text='- Toilette :',
        font="Times 14 bold", width=20, height=1,
        bg='DodgerBlue2', fg='white', anchor='w')
    self.wlbl_third = self.can.create_window(self.x50, self.y50,
        window = self.lbl_third)

    CheckVar3 = tk.IntVar()
    self.x51, self.y51 = 240, 1410
    self.C20 = tk.Radiobutton(self.can, text="0", highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=CheckVar3,
        value=0, height=1, width=3, anchor='w')
    self.wC20 = self.can.create_window(self.x51, self.y51,
        window = self.C20)

    self.x52, self.y52 = 295, 1410
    self.C21 = tk.Radiobutton(self.can, text="1", highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=CheckVar3,
        value=1, height=1, width=3, anchor='w')
    self.wC21 = self.can.create_window(self.x52, self.y52,
        window = self.C21)

    self.x53, self.y53 = 350, 1410
    self.C22 = tk.Radiobutton(self.can, text="2", highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=CheckVar3,
        value=2, height=1, width=3, anchor='w')
    self.wC22 = self.can.create_window(self.x53, self.y53,
        window = self.C22)

    self.x54, self.y54 = 405, 1410
    self.C23 = tk.Radiobutton(self.can, text="3", highlightbackground='cyan', fg='black', 
        bg='DodgerBlue2', variable=CheckVar3, 
        value=3, height=1, width=3, anchor='w')
    self.wC23 = self.can.create_window(self.x54, self.y54,
        window = self.C23)

    self.x55, self.y55 = 460, 1410
    self.C24 = tk.Radiobutton(self.can, text="4", highlightbackground='cyan', fg='black', 
        bg='DodgerBlue2', variable=CheckVar3, 
        value=4, height=1, width=3, anchor='w')
    self.wC24 = self.can.create_window(self.x55, self.y55,
        window = self.C24)

    # Forth need
    self.x56, self.y56 = 80, 1435
    self.lbl_forth = tk.Label(self.can, text='- Habillage :',
        font="Times 14 bold", width=20, height=1,
        bg='DodgerBlue2', fg='white', anchor='w')
    self.wlbl_forth = self.can.create_window(self.x56, self.y56,
        window = self.lbl_forth)

    CheckVar4 = tk.IntVar()
    self.x57, self.y57 = 240, 1435
    self.C30 = tk.Radiobutton(self.can, text="0", highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=CheckVar4,
        value=0, height=1, width=3, anchor='w')
    self.wC30 = self.can.create_window(self.x57, self.y57,
        window = self.C30)

    self.x58, self.y58 = 295, 1435
    self.C31 = tk.Radiobutton(self.can, text="1", highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=CheckVar4,
        value=1, height=1, width=3, anchor='w')
    self.wC31 = self.can.create_window(self.x58, self.y58,
        window = self.C31)

    self.x59, self.y59 = 350, 1435
    self.C32 = tk.Radiobutton(self.can, text="2", highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=CheckVar4,
        value=2, height=1, width=3, anchor='w')
    self.wC32 = self.can.create_window(self.x59, self.y59,
        window = self.C32)

    self.x60, self.y60 = 405, 1435
    self.C33 = tk.Radiobutton(self.can, text="3", highlightbackground='cyan', fg='black', 
        bg='DodgerBlue2', variable=CheckVar4, 
        value=3, height=1, width=3, anchor='w')
    self.wC33 = self.can.create_window(self.x60, self.y60,
        window = self.C33)

    self.x61, self.y61 = 460, 1435
    self.C34 = tk.Radiobutton(self.can, text="4", highlightbackground='cyan', fg='black', 
        bg='DodgerBlue2', variable=CheckVar4, 
        value=4, height=1, width=3, anchor='w')
    self.wC34 = self.can.create_window(self.x61, self.y61,
        window = self.C34)

    # fivth need
    self.x62, self.y62 = 80, 1460
    self.lbl_fivth = tk.Label(self.can, text='- Alimentation :',
        font="Times 14 bold", width=20, height=1,
        bg='DodgerBlue2', fg='white', anchor='w')
    self.wlbl_fivth = self.can.create_window(self.x62, self.y62,
        window = self.lbl_fivth)

    CheckVar5 = tk.IntVar()
    self.x63, self.y63 = 240, 1460
    self.C40 = tk.Radiobutton(self.can, text="0", highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=CheckVar5,
        value=0, height=1, width=3, anchor='w')
    self.wC40 = self.can.create_window(self.x63, self.y63,
        window = self.C40)

    self.x64, self.y64 = 295, 1460
    self.C41 = tk.Radiobutton(self.can, text="1", highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=CheckVar5,
        value=1, height=1, width=3, anchor='w')
    self.wC41 = self.can.create_window(self.x64, self.y64,
        window = self.C41)

    self.x65, self.y65 = 350, 1460
    self.C42 = tk.Radiobutton(self.can, text="2", highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=CheckVar5,
        value=2, height=1, width=3, anchor='w')
    self.wC42 = self.can.create_window(self.x65, self.y65,
        window = self.C42)

    self.x66, self.y66 = 405, 1460
    self.C43 = tk.Radiobutton(self.can, text="3", highlightbackground='cyan', fg='black', 
        bg='DodgerBlue2', variable=CheckVar5, 
        value=3, height=1, width=3, anchor='w')
    self.wC43 = self.can.create_window(self.x66, self.y66,
        window = self.C43)

    self.x67, self.y67 = 460, 1460
    self.C44 = tk.Radiobutton(self.can, text="4", highlightbackground='cyan', fg='black', 
        bg='DodgerBlue2', variable=CheckVar5, 
        value=4, height=1, width=3, anchor='w')
    self.wC44 = self.can.create_window(self.x67, self.y67,
        window = self.C44)

    # Sixth need
    self.x68, self.y68 = 80, 1485
    self.lbl_sixth = tk.Label(self.can, text='- Elimination :',
        font="Times 14 bold", width=20, height=1,
        bg='DodgerBlue2', fg='white', anchor='w')
    self.wlbl_sixth = self.can.create_window(self.x68, self.y68,
        window = self.lbl_sixth)

    CheckVar6 = tk.IntVar()
    self.x69, self.y69 = 240, 1485
    self.C50 = tk.Radiobutton(self.can, text="0", highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=CheckVar6,
        value=0, height=1, width=3, anchor='w')
    self.wC50 = self.can.create_window(self.x69, self.y69,
        window = self.C50)

    self.x70, self.y70 = 295, 1485
    self.C51 = tk.Radiobutton(self.can, text="1", highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=CheckVar6,
        value=1, height=1, width=3, anchor='w')
    self.wC51 = self.can.create_window(self.x70, self.y70,
        window = self.C51)

    self.x71, self.y71 = 350, 1485
    self.C52 = tk.Radiobutton(self.can, text="2", highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=CheckVar6,
        value=2, height=1, width=3, anchor='w')
    self.wC52 = self.can.create_window(self.x71, self.y71,
        window = self.C52)

    self.x72, self.y72 = 405, 1485
    self.C53 = tk.Radiobutton(self.can, text="3", highlightbackground='cyan', fg='black', 
        bg='DodgerBlue2', variable=CheckVar6, 
        value=3, height=1, width=3, anchor='w')
    self.wC53 = self.can.create_window(self.x72, self.y72,
        window = self.C53)

    self.x73, self.y73 = 460, 1485
    self.C54 = tk.Radiobutton(self.can, text="4", highlightbackground='cyan', fg='black', 
        bg='DodgerBlue2', variable=CheckVar6, 
        value=4, height=1, width=3, anchor='w')
    self.wC54 = self.can.create_window(self.x73, self.y73,
        window = self.C54)

    # Seventh need
    self.x74, self.y74 = 80, 1510
    self.lbl_seven = tk.Label(self.can, text='- Déplacement :',
        font="Times 14 bold", width=20, height=1,
        bg='DodgerBlue2', fg='white', anchor='w')
    self.wlbl_seven = self.can.create_window(self.x74, self.y74,
        window = self.lbl_seven)

    CheckVar7 = tk.IntVar()
    self.x75, self.y75 = 240, 1510
    self.C60 = tk.Radiobutton(self.can, text="0", highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=CheckVar7,
        value=0, height=1, width=3, anchor='w')
    self.wC60 = self.can.create_window(self.x75, self.y75,
        window = self.C60)

    self.x76, self.y76 = 295, 1510
    self.C61 = tk.Radiobutton(self.can, text="1", highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=CheckVar7,
        value=1, height=1, width=3, anchor='w')
    self.wC61 = self.can.create_window(self.x76, self.y76,
        window = self.C61)

    self.x77, self.y77 = 350, 1510
    self.C62 = tk.Radiobutton(self.can, text="2", highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=CheckVar7,
        value=2, height=1, width=3, anchor='w')
    self.wC62 = self.can.create_window(self.x77, self.y77,
        window = self.C62)

    self.x78, self.y78 = 405, 1510
    self.C63 = tk.Radiobutton(self.can, text="3", highlightbackground='cyan', fg='black', 
        bg='DodgerBlue2', variable=CheckVar7, 
        value=3, height=1, width=3, anchor='w')
    self.wC63 = self.can.create_window(self.x78, self.y78,
        window = self.C63)

    self.x79, self.y79 = 460, 1510
    self.C64 = tk.Radiobutton(self.can, text="4", highlightbackground='cyan', fg='black', 
        bg='DodgerBlue2', variable=CheckVar7, 
        value=4, height=1, width=3, anchor='w')
    self.wC64 = self.can.create_window(self.x79, self.y79,
        window = self.C64)

    # Heighth need
    self.x80, self.y80 = 80, 1535
    self.lbl_height = tk.Label(self.can, text='- Communication :',
        font="Times 14 bold", width=20, height=1,
        bg='DodgerBlue2', fg='white', anchor='w')
    self.wlbl_height = self.can.create_window(self.x80, self.y80,
        window = self.lbl_height)

    CheckVar8 = tk.IntVar()
    self.x81, self.y81 = 240, 1535
    self.C70 = tk.Radiobutton(self.can, text="0", highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=CheckVar8,
        value=0, height=1, width=3, anchor='w')
    self.wC70 = self.can.create_window(self.x81, self.y81,
        window = self.C70)

    self.x82, self.y82 = 295, 1535
    self.C71 = tk.Radiobutton(self.can, text="1", highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=CheckVar8,
        value=1, height=1, width=3, anchor='w')
    self.wC71 = self.can.create_window(self.x82, self.y82,
        window = self.C71)

    self.x83, self.y83 = 350, 1535
    self.C72 = tk.Radiobutton(self.can, text="2", highlightbackground='cyan', fg='black',
        bg='DodgerBlue2', variable=CheckVar8,
        value=2, height=1, width=3, anchor='w')
    self.wC72 = self.can.create_window(self.x83, self.y83,
        window = self.C72)

    self.x84, self.y84 = 405, 1535
    self.C73 = tk.Radiobutton(self.can, text="3", highlightbackground='cyan', fg='black', 
        bg='DodgerBlue2', variable=CheckVar8, 
        value=3, height=1, width=3, anchor='w')
    self.wC73 = self.can.create_window(self.x84, self.y84,
        window = self.C73)

    self.x85, self.y85 = 460, 1535
    self.C74 = tk.Radiobutton(self.can, text="4", highlightbackground='cyan', fg='black', 
        bg='DodgerBlue2', variable=CheckVar8, 
        value=4, height=1, width=3, anchor='w')
    self.wC74 = self.can.create_window(self.x85, self.y85,
        window = self.C74)

    # Auxiliary
    self.x86, self.y86 = 250, 1580
    self.lbl_aux = tk.Label(self.can, text='--- Auxiliary Equipement ---',
        font="Times 14 bold", width=60,
        height=1, bg='RoyalBlue3', fg='white')
    self.wlbl_aux = self.can.create_window(self.x86, self.y86,
        window = self.lbl_aux)

    self.x87, self.y87 = 250, 1670
    self.t87 = tk.Text(self.can, height=6, width=50, font=18, relief=SUNKEN)
    self.wt87_window = self.can.create_window(self.x87, self.y87, window=self.t87)

    def importationHealTwo(fichier, encodage="Utf-8"):
        filehcs2 = open(fichier, 'r', encoding=encodage)
        content = filehcs2.readlines()
        filehcs2.close()
        for li in content:
            self.t87.insert(END, li)

    try:
        if os.path.getsize('./auxequip/doc_equip/auxiliary1.txt'):
            importationHealTwo('./auxequip/doc_equip/auxiliary1.txt', encodage="Utf-8")
    except FileNotFoundError as no_file:
        print("+ File auxiliary1.txt not found !")
        messagebox.showinfo('INFO', 'File auxiliary1.txt not found !')

    # PLAFA
    self.x88, self.y88 = 80, 1800
    self.lbl_plafa = tk.Label(self.can, text='PLAFA :',
        font="Times 14 bold", width=20, height=1,
        bg='DodgerBlue2', fg='white', anchor='w')
    self.wlbl_plafa = self.can.create_window(self.x88, self.y88,
        window = self.lbl_plafa)

    CheckVar9 = tk.IntVar()
    self.x89, self.y89 = 250, 1800
    self.C75 = Checkbutton(self.can, text=" Oui", fg='black', 
        bg='DodgerBlue2', variable=CheckVar9, 
        onvalue=1, offvalue=0, height=1, 
        width=6, anchor="w")
    self.wC75 = self.can.create_window(self.x89, self.y89,
        window = self.C75)

    CheckVar10 = tk.IntVar()
    self.x90, self.y90 = 324, 1800
    self.C76 = Checkbutton(self.can, text=" Non", fg='black', 
        bg='DodgerBlue2', variable=CheckVar10, 
        onvalue=1, offvalue=0, height=1, 
        width=6, anchor="w")
    self.wC76 = self.can.create_window(self.x90, self.y90,
        window = self.C76)

    # DA
    self.x91, self.y91 = 80, 1825
    self.lbl_plafa = tk.Label(self.can, text='Directives anticipées :',
        font="Times 14 bold", width=20, height=1,
        bg='DodgerBlue2', fg='white', anchor='w')
    self.wlbl_plafa = self.can.create_window(self.x91, self.y91,
        window = self.lbl_plafa)

    CheckVar11 = tk.IntVar()
    self.x92, self.y92 = 250, 1825
    self.C77 = Checkbutton(self.can, text=" Oui", fg='black', 
        bg='DodgerBlue2', variable=CheckVar11, 
        onvalue=1, offvalue=0, height=1, 
        width=6, anchor="w")
    self.wC77 = self.can.create_window(self.x92, self.y92,
        window = self.C77)

    CheckVar12 = tk.IntVar()
    self.x93, self.y93 = 324, 1825
    self.C78 = Checkbutton(self.can, text=" Non", fg='black', 
        bg='DodgerBlue2', variable=CheckVar12, 
        onvalue=1, offvalue=0, height=1, 
        width=6, anchor="w")
    self.wC78 = self.can.create_window(self.x93, self.y93,
        window = self.C78)

    def uptoserv():
        """
            To upload data on server after creating files.
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
        """
            To display a msg to confirm that all data have been saved.
        """
        messagebox.showinfo("Confirmation", "Record confirmed and finished !")

    def record_alldata():
        """
            That the main function to save all data by calling other functions.
        """
        MsgBox = messagebox.askyesno('Record', 'Data will be saved, ok ?')
        if MsgBox == 1:
            uptoserv()
            recordata()
            msgvalidate()
            self.showPatients()
        else:
            messagebox.showinfo('Return', 'Ok, nothing has changed...')

    def way_back():
        """
            To return back to main page.
        """
        try:
            self.can.delete(ALL)
            self.showPatients()
        except (OSError, ValueError) as p_out:
            print("Error from dmst to way out", p_out)

    # Button save and quit
    self.x99, self.y99 = 800, 1700
    self.buttonsave = tk.Button(self.can, text="Save", width=10, bd=3,
        fg='yellow', bg='RoyalBlue3', activebackground='pale turquoise',
        highlightbackground='cyan', command = record_alldata)
    self.buttonsave = self.can.create_window(self.x99, self.y99,
        window = self.buttonsave)

    self.x100, self.y100 = 1000, 1700
    self.buttonquit = tk.Button(self.can, text='Return to main menu', width=20, bd=3,
        fg='white', bg='RoyalBlue3', activebackground='pale turquoise',
        highlightbackground='cyan', command = way_back)
    self.buttonquit = self.can.create_window(self.x100, self.y100,
        window = self.buttonquit)

    self.can.configure(scrollregion=self.can.bbox(ALL))
