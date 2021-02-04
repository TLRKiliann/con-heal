#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
import tkinter as tk
#from tkinter import ttk
from tkinter import messagebox
import time
import subprocess
from boxapp import callBox
from patcaps import callResident
from backapp import *
from Backup.backupfile import dataBackToSave
from param.backup_month import paramBackToSave
from calBmi.bmi_backup import bmiBackToSave
from contact.conpact.pat_contact1 import Window
from contact.conpact.doc_contact1 import doctorWind
from contact.conpact.family_contact1 import famWind
from contact.conpact.hcs_contact1 import homecsWind
from contact.conpact2.pat_contact2 import Window2
from contact.conpact2.doc_contact2 import doctorWind2
from contact.conpact2.family_contact2 import famWind2
from contact.conpact2.hcs_contact2 import homecsWind2
from contact.conpact3.pat_contact3 import Window3
from contact.conpact3.doc_contact3 import doctorWind3
from contact.conpact3.family_contact3 import famWind3
from contact.conpact3.hcs_contact3 import homecsWind3
from contact.conpact4.pat_contact4 import Window4
from contact.conpact4.doc_contact4 import doctorWind4
from contact.conpact4.family_contact4 import famWind4
from contact.conpact4.hcs_contact4 import homecsWind4
from contact.conpact5.pat_contact5 import Window5
from contact.conpact5.doc_contact5 import doctorWind5
from contact.conpact5.family_contact5 import famWind5
from contact.conpact5.hcs_contact5 import homecsWind5
from contact.conpact6.pat_contact6 import Window6
from contact.conpact6.doc_contact6 import doctorWind6
from contact.conpact6.family_contact6 import famWind6
from contact.conpact6.hcs_contact6 import homecsWind6
from contact.conpact7.pat_contact7 import Window7
from contact.conpact7.doc_contact7 import doctorWind7
from contact.conpact7.family_contact7 import famWind7
from contact.conpact7.hcs_contact7 import homecsWind7
from contact.conpact8.pat_contact8 import Window8
from contact.conpact8.doc_contact8 import doctorWind8
from contact.conpact8.family_contact8 import famWind8
from contact.conpact8.hcs_contact8 import homecsWind8
from contact.conpact9.pat_contact9 import Window9
from contact.conpact9.doc_contact9 import doctorWind9
from contact.conpact9.family_contact9 import famWind9
from contact.conpact9.hcs_contact9 import homecsWind9
from contact.conpact10.pat_contact10 import Window10
from contact.conpact10.doc_contact10 import doctorWind10
from contact.conpact10.family_contact10 import famWind10
from contact.conpact10.hcs_contact10 import homecsWind10
from contact.conpact11.pat_contact11 import Window11
from contact.conpact11.doc_contact11 import doctorWind11
from contact.conpact11.family_contact11 import famWind11
from contact.conpact11.hcs_contact11 import homecsWind11
from contact.conpact12.pat_contact12 import Window12
from contact.conpact12.doc_contact12 import doctorWind12
from contact.conpact12.family_contact12 import famWind12
from contact.conpact12.hcs_contact12 import homecsWind12
from contact.conpact13.pat_contact13 import Window13
from contact.conpact13.doc_contact13 import doctorWind13
from contact.conpact13.family_contact13 import famWind13
from contact.conpact13.hcs_contact13 import homecsWind13
from contact.conpact14.pat_contact14 import Window14
from contact.conpact14.doc_contact14 import doctorWind14
from contact.conpact14.family_contact14 import famWind14
from contact.conpact14.hcs_contact14 import homecsWind14
from contact.conpact15.pat_contact15 import Window15
from contact.conpact15.doc_contact15 import doctorWind15
from contact.conpact15.family_contact15 import famWind15
from contact.conpact15.hcs_contact15 import homecsWind15
from contact.conpact16.pat_contact16 import Window16
from contact.conpact16.doc_contact16 import doctorWind16
from contact.conpact16.family_contact16 import famWind16
from contact.conpact16.hcs_contact16 import homecsWind16
from contact.conpact17.pat_contact17 import Window17
from contact.conpact17.doc_contact17 import doctorWind17
from contact.conpact17.family_contact17 import famWind17
from contact.conpact17.hcs_contact17 import homecsWind17
from contact.conpact18.pat_contact18 import Window18
from contact.conpact18.doc_contact18 import doctorWind18
from contact.conpact18.family_contact18 import famWind18
from contact.conpact18.hcs_contact18 import homecsWind18
from contact.conpact19.pat_contact19 import Window19
from contact.conpact19.doc_contact19 import doctorWind19
from contact.conpact19.family_contact19 import famWind19
from contact.conpact19.hcs_contact19 import homecsWind19
from contact.conpact20.pat_contact20 import Window20
from contact.conpact20.doc_contact20 import doctorWind20
from contact.conpact20.family_contact20 import famWind20
from contact.conpact20.hcs_contact20 import homecsWind20
from contact.conpact21.pat_contact21 import Window21
from contact.conpact21.doc_contact21 import doctorWind21
from contact.conpact21.family_contact21 import famWind21
from contact.conpact21.hcs_contact21 import homecsWind21
from contact.conpact22.pat_contact22 import Window22
from contact.conpact22.doc_contact22 import doctorWind22
from contact.conpact22.family_contact22 import famWind22
from contact.conpact22.hcs_contact22 import homecsWind22
from contact.conpact23.pat_contact23 import Window23
from contact.conpact23.doc_contact23 import doctorWind23
from contact.conpact23.family_contact23 import famWind23
from contact.conpact23.hcs_contact23 import homecsWind23
from contact.conpact24.pat_contact24 import Window24
from contact.conpact24.doc_contact24 import doctorWind24
from contact.conpact24.family_contact24 import famWind24
from contact.conpact24.hcs_contact24 import homecsWind24
from vmed.medload import *
from need.needownload.download import *
from diag.diagdownload import *
from ttt.tttdownload import *
from ttt.patienttt1 import callTreatment1
from ttt.patienttt2 import callTreatment2
from ttt.patienttt3 import callTreatment3
from ttt.patienttt4 import callTreatment4
from ttt.patienttt5 import callTreatment5
from ttt.patienttt6 import callTreatment6
from ttt.patienttt7 import callTreatment7
from ttt.patienttt8 import callTreatment8
from ttt.patienttt9 import callTreatment9
from ttt.patienttt10 import callTreatment10
from ttt.patienttt11 import callTreatment11
from ttt.patienttt12 import callTreatment12
from ttt.patienttt13 import callTreatment13
from ttt.patienttt14 import callTreatment14
from ttt.patienttt15 import callTreatment15
from ttt.patienttt16 import callTreatment16
from ttt.patienttt17 import callTreatment17
from ttt.patienttt18 import callTreatment18
from ttt.patienttt19 import callTreatment19
from ttt.patienttt20 import callTreatment20
from ttt.patienttt21 import callTreatment21
from ttt.patienttt22 import callTreatment22
from ttt.patienttt23 import callTreatment23
from ttt.patienttt24 import callTreatment24
from labo.labodownload import *
from labo.resultlabo1 import callLabo1
from labo.resultlabo2 import callLabo2
from labo.resultlabo3 import callLabo3
from labo.resultlabo4 import callLabo4
from labo.resultlabo5 import callLabo5
from labo.resultlabo6 import callLabo6
from labo.resultlabo7 import callLabo7
from labo.resultlabo8 import callLabo8
from labo.resultlabo9 import callLabo9
from labo.resultlabo10 import callLabo10
from labo.resultlabo11 import callLabo11
from labo.resultlabo12 import callLabo12
from labo.resultlabo13 import callLabo13
from labo.resultlabo14 import callLabo14
from labo.resultlabo15 import callLabo15
from labo.resultlabo16 import callLabo16
from labo.resultlabo17 import callLabo17
from labo.resultlabo18 import callLabo18
from labo.resultlabo19 import callLabo19
from labo.resultlabo20 import callLabo20
from labo.resultlabo21 import callLabo21
from labo.resultlabo22 import callLabo22
from labo.resultlabo23 import callLabo23
from labo.resultlabo24 import callLabo24
import passw
from shootransfert import loaderfile


def tocopyfiles():
    loaderfile()
tocopyfiles()

class ScrollCanvas(tk.Frame):
    """
        To prepare ScrollBar for main application.
    """
    def __init__(self, boss=None):
        tk.Frame.__init__(self, borderwidth=borderwidth, relief=relief)
        self.can = tk.Canvas(self, width=width, height=height, bd=bd,
            bg=bg, relief=relief)
        self.frame = tk.Frame(self.can)
        self.vsb = tk.Scrollbar(self, orient=VERTICAL, command=self.can.yview)
        self.can.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side=tk.RIGHT, fill=Y)
        self.can.pack(side=tk.LEFT, fill=BOTH, expand=YES)
        self.can.create_window((4,4), window=self.frame, anchor=NW,
                                  tags="self.frame")
        self.frame.bind("<Configure>", self.onFrameConfigure)

class MenuBar(tk.Frame):
    """
        Wrapp down
    """
    def __init__(self, boss=None):
        tk.Frame.__init__(self, borderwidth=5, bg='RoyalBlue3', padx=0)
        # 1st menu
        fileMenu = tk.Menubutton(self, text='Menu', fg='white',
            font=("Times 14"), bg='grey30', relief=GROOVE)
        new_text = StringVar()
        new_text2 = StringVar()
        new_text3 = StringVar()
        new_text4 = StringVar()
        new_text5 = StringVar()
        new_text6 = StringVar()
        new_text7 = StringVar()
        new_text8 = StringVar()
        new_text9 = StringVar()
        new_text10 = StringVar()
        new_text11 = StringVar()
        new_text12 = StringVar()
        new_text13 = StringVar()
        new_text14 = StringVar()
        new_text15 = StringVar()
        new_text16 = StringVar()
        new_text17 = StringVar()
        new_text18 = StringVar()
        new_text19 = StringVar()
        new_text20 = StringVar()
        new_text21 = StringVar()
        new_text22 = StringVar()
        new_text23 = StringVar()
        new_text24 = StringVar()

        # For label below (in me2.add_command)
        try:
            with open('./newpatient/entryfile.txt', 'r') as namefile:
                line1 = namefile.readline()
                new_text = line1
                if new_text == '-':
                    new_text = new_text
                else:
                    new_text = new_text[:-1]
        except FileNotFoundError as fileout:
            print("No file entryfile.txt exist", fileout)

        try:
            with open('./newpatient/entryfile2.txt', 'r') as namefile2:
                line2 = namefile2.readline()
                new_text2 = line2
                if new_text2 == '-':
                    new_text2 = new_text2
                else:
                    new_text2 = new_text2[:-1]
        except FileNotFoundError as fileout2:
            print("No file entryfile2.txt exist", fileout2)

        try:
            with open('./newpatient/entryfile3.txt', 'r') as namefile3:
                line3 = namefile3.readline()
                new_text3 = line3
                if new_text3 == '-':
                    new_text3 = new_text3
                else:
                    new_text3 = new_text3[:-1]
        except FileNotFoundError as fileout3:
            print("No file entryfile3.txt exist", fileout3)

        try:
            with open('./newpatient/entryfile4.txt', 'r') as namefile4:
                line4 = namefile4.readline()
                new_text4 = line4
                if new_text4 == '-':
                    new_text4 = new_text4
                else:
                    new_text4 = new_text4[:-1]
        except FileNotFoundError as fileout4:
            print("No file entryfile4.txt exist", fileout4)

        try:
            with open('./newpatient/entryfile5.txt', 'r') as namefile5:
                line5 = namefile5.readline()
                new_text5 = line5
                if new_text5 == '-':
                    new_text5 = new_text5
                else:
                    new_text5 = new_text5[:-1]
        except FileNotFoundError as fileout5:
            print("No file entryfile5.txt exist", fileout5)

        try:
            with open('./newpatient/entryfile6.txt', 'r') as namefile6:
                line6 = namefile6.readline()
                new_text6 = line6
                if new_text6 == '-':
                    new_text6 = new_text6
                else:
                    new_text6 = new_text6[:-1]
        except FileNotFoundError as fileout6:
            print("No file entryfile6.txt exist", fileout6)

        try:
            with open('./newpatient/entryfile7.txt', 'r') as namefile7:
                line7 = namefile7.readline()
                new_text7 = line7
                if new_text7 == '-':
                    new_text7 = new_text7
                else:
                    new_text7 = new_text7[:-1]
        except FileNotFoundError as fileout7:
            print("No file entryfile7.txt exist", fileout7)

        try:
            with open('./newpatient/entryfile8.txt', 'r') as namefile8:
                line8 = namefile8.readline()
                new_text8 = line8
                if new_text8 == '-':
                    new_text8 = new_text8
                else:
                    new_text8 = new_text8[:-1]
        except FileNotFoundError as fileout8:
            print("No file entryfile8.txt exist", fileout8)

        try:
            with open('./newpatient/entryfile9.txt', 'r') as namefile9:
                line9 = namefile9.readline()
                new_text9 = line9
                if new_text9 == '-':
                    new_text9 = new_text9
                else:
                    new_text9 = new_text9[:-1]
        except FileNotFoundError as fileout9:
            print("No file entryfile9.txt exist", fileout9)

        try:
            with open('./newpatient/entryfile10.txt', 'r') as namefile10:
                line10 = namefile10.readline()
                new_text10 = line10
                if new_text10 == '-':
                    new_text10 = new_text10
                else:
                    new_text10 = new_text10[:-1]
        except FileNotFoundError as fileout10:
            print("No file entryfile10.txt exist", fileout10)

        try:
            with open('./newpatient/entryfile11.txt', 'r') as namefile11:
                line11 = namefile11.readline()
                new_text11 = line11
                if new_text11 == '-':
                    new_text11 = new_text11
                else:
                    new_text11 = new_text11[:-1]
        except FileNotFoundError as fileout11:
            print("No file entryfile11.txt exist", fileout11)

        try:
            with open('./newpatient/entryfile12.txt', 'r') as namefile12:
                line12 = namefile12.readline()
                new_text12 = line12
                if new_text12 == '-':
                    new_text12 = new_text12
                else:
                    new_text12 = new_text12[:-1]
        except FileNotFoundError as fileout12:
            print("No file entryfile12.txt exist", fileout12)

        try:
            with open('./newpatient/entryfile13.txt', 'r') as namefile13:
                line13 = namefile13.readline()
                new_text13 = line13
                if new_text13 == '-':
                    new_text13 = new_text13
                else:
                    new_text13 = new_text13[:-1]
        except FileNotFoundError as fileout13:
            print("No file entryfile13.txt exist", fileout13)

        try:
            with open('./newpatient/entryfile14.txt', 'r') as namefile14:
                line14 = namefile14.readline()
                new_text14 = line14
                if new_text14 == '-':
                    new_text14 = new_text14
                else:
                    new_text14 = new_text14[:-1]
        except FileNotFoundError as fileout14:
            print("No file entryfile14.txt exist", fileout14)

        try:
            with open('./newpatient/entryfile15.txt', 'r') as namefile15:
                line15 = namefile15.readline()
                new_text15 = line15
                if new_text15 == '-':
                    new_text15 = new_text15
                else:
                    new_text15 = new_text15[:-1]
        except FileNotFoundError as fileout15:
            print("No file entryfile15.txt exist", fileout15)

        try:
            with open('./newpatient/entryfile16.txt', 'r') as namefile16:
                line16 = namefile16.readline()
                new_text16 = line16
                if new_text16 == '-':
                    new_text16 = new_text16
                else:
                    new_text16 = new_text16[:-1]
        except FileNotFoundError as fileout16:
            print("No file entryfile16.txt exist", fileout16)

        try:
            with open('./newpatient/entryfile17.txt', 'r') as namefile17:
                line17 = namefile17.readline()
                new_text17 = line17
                if new_text17 == '-':
                    new_text17 = new_text17
                else:
                    new_text17 = new_text17[:-1]
        except FileNotFoundError as fileout17:
            print("No file entryfile17.txt exist", fileout17)

        try:
            with open('./newpatient/entryfile18.txt', 'r') as namefile18:
                line18 = namefile18.readline()
                new_text18 = line18
                if new_text18 == '-':
                    new_text18 = new_text18
                else:
                    new_text18 = new_text18[:-1]
        except FileNotFoundError as fileout18:
            print("No file entryfile18.txt exist", fileout18)

        try:
            with open('./newpatient/entryfile19.txt', 'r') as namefile19:
                line19 = namefile19.readline()
                new_text19 = line19
                if new_text19 == '-':
                    new_text19 = new_text19
                else:
                    new_text19 = new_text19[:-1]
        except FileNotFoundError as fileout19:
            print("No file entryfile19.txt exist", fileout19)

        try:
            with open('./newpatient/entryfile20.txt', 'r') as namefile20:
                line20 = namefile20.readline()
                new_text20 = line20
                if new_text20 == '-':
                    new_text20 = new_text20
                else:
                    new_text20 = new_text20[:-1]
        except FileNotFoundError as fileout20:
            print("No file entryfile20.txt exist", fileout20)

        try:
            with open('./newpatient/entryfile21.txt', 'r') as namefile21:
                line21 = namefile21.readline()
                new_text21 = line21
                if new_text21 == '-':
                    new_text21 = new_text21
                else:
                    new_text21 = new_text21[:-1]
        except FileNotFoundError as fileout21:
            print("No file entryfile21.txt exist", fileout21)

        try:
            with open('./newpatient/entryfile22.txt', 'r') as namefile22:
                line22 = namefile22.readline()
                new_text22 = line22
                if new_text22 == '-':
                    new_text22 = new_text22
                else:
                    new_text22 = new_text22[:-1]
        except FileNotFoundError as fileout22:
            print("No file entryfile22.txt exist", fileout22)

        try:
            with open('./newpatient/entryfile23.txt', 'r') as namefile23:
                line23 = namefile23.readline()
                new_text23 = line23
                if new_text23 == '-':
                    new_text23 = new_text23
                else:
                    new_text23 = new_text23[:-1]
        except FileNotFoundError as fileout23:
            print("No file entryfile23.txt exist", fileout23)

        try:
            with open('./newpatient/entryfile24.txt', 'r') as namefile24:
                line24 = namefile24.readline()
                new_text24 = line24
                if new_text24 == '-':
                    new_text24 = new_text24
                else:
                    new_text24 = new_text24[:-1]
        except FileNotFoundError as fileout24:
            print("No file entryfile24.txt exist", fileout24)

        fileMenu.pack(side=LEFT, padx=3)
        # Partie déroulante du menu 1st
        me1 = tk.Menu(fileMenu, tearoff=0)
        me1.add_command(label='Start Page', underline=0, font=("Times 14 bold"),
            background='black',activebackground='aquamarine',
            foreground='aquamarine', activeforeground='black',
            command=boss.framShow)
        me1.add_command(label="Textbox", underline=0, font=("Times 14 bold"),
            background='black', activebackground='cyan',
            foreground='aquamarine', activeforeground='black',
            command=boss.showSynopsis)
        me1.add_command(label="Residents", underline=0, font=("Times 14 bold"),
            background='black', activebackground='cyan',
            foreground='aquamarine', activeforeground='black',
            command=boss.showPatients)
        me1.add_command(label='DataBase', underline=0, font=("Times 14 bold"),
            background='black', activebackground='aquamarine',
            foreground='white', activeforeground='black',
            command=boss.funcPyCon)
        me1.add_command(label='MapApp', font=("Times 14 bold"),
            background='black', activebackground='aquamarine',
            foreground='yellow', activeforeground='black',
            command=boss.instalpy)
        me1.add_command(label='Quit', font=("Times 14 bold"),
            background='black', activebackground='red',
            foreground='coral', activeforeground='white',
            command=boss.msgExit)
        # Integration of 1st menu
        fileMenu.configure(activeforeground='black', activebackground='cyan',
            menu=me1)

        # Agenda menu
        cmd_agenda = tk.Menubutton(self, text='Agenda', font=("Times 14"),
            fg='cyan', bg='grey30', relief=GROOVE)
        cmd_agenda.pack(side=LEFT, padx=3)
        me3 = Menu(cmd_agenda)
        # Partie déroulante du menu agenda
        me3.add_command(label=new_text, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda)
        me3.add_command(label=new_text2, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda2)
        me3.add_command(label=new_text3, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda3)
        me3.add_command(label=new_text4, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda4)
        me3.add_command(label=new_text5, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda5)
        me3.add_command(label=new_text6, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda6)
        me3.add_command(label=new_text7, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda7)
        me3.add_command(label=new_text8, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda8)
        me3.add_command(label=new_text9, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda9)
        me3.add_command(label=new_text10, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda10)
        me3.add_command(label=new_text11, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda11)
        me3.add_command(label=new_text12, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda12)
        me3.add_command(label=new_text13, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda13)
        me3.add_command(label=new_text14, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda14)
        me3.add_command(label=new_text15, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda15)
        me3.add_command(label=new_text16, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda16)
        me3.add_command(label=new_text17, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda17)
        me3.add_command(label=new_text18, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda18)
        me3.add_command(label=new_text19, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda19)
        me3.add_command(label=new_text20, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda20)
        me3.add_command(label=new_text21, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda21)
        me3.add_command(label=new_text22, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda22)
        me3.add_command(label=new_text23, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda23)
        me3.add_command(label=new_text24, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda24)
        # Integration of agenda menu
        cmd_agenda.configure(activeforeground='black', activebackground='cyan',
            menu=me3)

        # Contact menu
        contact = tk.Menubutton(self, text='Contacts', font=("Times 14"),
            fg='cyan', bg='grey30', relief=GROOVE)
        contact.pack(side=LEFT, padx=3)
        contchck = tk.Menu(contact)
        me1 = Menu(contchck)
        me1.add_command(label='Patient Data', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num1)
        me1.add_command(label='Relation - Family', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_1)
        me1.add_command(label="Doctors' Data", font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_1)
        me1.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_1)
        contchck.add_cascade(label=new_text, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me1)
        me2 = Menu(contchck)
        me2.add_command(label='Patient Data', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num2)
        me2.add_command(label='Relation - Family', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_2)
        me2.add_command(label="Doctors' Data", font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_2)
        me2.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_2)
        contchck.add_cascade(label=new_text2, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me2)
        me3 = Menu(contchck)
        me3.add_command(label='Patient Data', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num3)
        me3.add_command(label='Relation - Family', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_3)
        me3.add_command(label="Doctors' Data", font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_3)
        me3.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_3)
        contchck.add_cascade(label=new_text3, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me3)
        me4 = Menu(contchck)
        me4.add_command(label='Patient Data', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num4)
        me4.add_command(label='Relation - Family', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_4)
        me4.add_command(label="Doctors' Data", font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_4)
        me4.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_4)
        contchck.add_cascade(label=new_text4, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me4)
        me5 = Menu(contchck)
        me5.add_command(label='Patient Data', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num5)
        me5.add_command(label='Relation - Family', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_5)
        me5.add_command(label="Doctors' Data", font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_5)
        me5.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_5)
        contchck.add_cascade(label=new_text5, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me5)
        me6 = Menu(contchck)
        me6.add_command(label='Patient Data', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num6)
        me6.add_command(label='Relation - Family', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_6)
        me6.add_command(label="Doctors' Data", font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_6)
        me6.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_6)
        contchck.add_cascade(label=new_text6, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me6)
        me7 = Menu(contchck)
        me7.add_command(label='Patient Data', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num7)
        me7.add_command(label='Relation - Family', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_7)
        me7.add_command(label="Doctors' Data", font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_7)
        me7.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_7)
        contchck.add_cascade(label=new_text7, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me7)
        me8 = Menu(contchck)
        me8.add_command(label='Patient Data', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num8)
        me8.add_command(label='Relation - Family', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_8)
        me8.add_command(label="Doctors' Data", font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_8)
        me8.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_8)
        contchck.add_cascade(label=new_text8, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me8)
        me9 = Menu(contchck)
        me9.add_command(label='Patient Data', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num9)
        me9.add_command(label='Relation - Family', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_9)
        me9.add_command(label="Doctors' Data", font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_9)
        me9.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_9)
        contchck.add_cascade(label=new_text9, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me9)
        me10 = Menu(contchck)
        me10.add_command(label='Patient Data', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num10)
        me10.add_command(label='Relation - Family', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_10)
        me10.add_command(label="Doctors' Data", font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_10)
        me10.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_10)
        contchck.add_cascade(label=new_text10, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me10)
        me11 = Menu(contchck)
        me11.add_command(label='Patient Data', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num11)
        me11.add_command(label='Relation - Family', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_11)
        me11.add_command(label="Doctors' Data", font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_11)
        me11.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_11)
        contchck.add_cascade(label=new_text11, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me11)
        me12 = Menu(contchck)
        me12.add_command(label='Patient Data', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num12)
        me12.add_command(label='Relation - Family', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_12)
        me12.add_command(label="Doctors' Data", font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_12)
        me12.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_12)
        contchck.add_cascade(label=new_text12, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me12)
        me13 = Menu(contchck)
        me13.add_command(label='Patient Data', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num13)
        me13.add_command(label='Relation - Family', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_13)
        me13.add_command(label="Doctors' Data", font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_13)
        me13.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_13)
        contchck.add_cascade(label=new_text13, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me13)
        me14 = Menu(contchck)
        me14.add_command(label='Patient Data', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num14)
        me14.add_command(label='Relation - Family', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_14)
        me14.add_command(label="Doctors' Data", font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_14)
        me14.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_14)
        contchck.add_cascade(label=new_text14, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me14)
        me15 = Menu(contchck)
        me15.add_command(label='Patient Data', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num15)
        me15.add_command(label='Relation - Family', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_15)
        me15.add_command(label="Doctors' Data", font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_15)
        me15.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_15)
        contchck.add_cascade(label=new_text15, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me15)
        me16 = Menu(contchck)
        me16.add_command(label='Patient Data', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num16)
        me16.add_command(label='Relation - Family', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_16)
        me16.add_command(label="Doctors' Data", font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_16)
        me16.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_16)
        contchck.add_cascade(label=new_text16, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me16)
        me17 = Menu(contchck)
        me17.add_command(label='Patient Data', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num17)
        me17.add_command(label='Relation - Family', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_17)
        me17.add_command(label="Doctors' Data", font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_17)
        me17.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_17)
        contchck.add_cascade(label=new_text17, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me17)
        me18 = Menu(contchck)
        me18.add_command(label='Patient Data', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num18)
        me18.add_command(label='Relation - Family', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_18)
        me18.add_command(label="Doctors' Data", font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_18)
        me18.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_18)
        contchck.add_cascade(label=new_text18, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me18)
        me19 = Menu(contchck)
        me19.add_command(label='Patient Data', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num19)
        me19.add_command(label='Relation - Family', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_19)
        me19.add_command(label="Doctors' Data", font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_19)
        me19.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_19)
        contchck.add_cascade(label=new_text19, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me19)
        me20 = Menu(contchck)
        me20.add_command(label='Patient Data', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num20)
        me20.add_command(label='Relation - Family', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_20)
        me20.add_command(label="Doctors' Data", font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_20)
        me20.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_20)
        contchck.add_cascade(label=new_text20, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me20)
        me21 = Menu(contchck)
        me21.add_command(label='Patient Data', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num21)
        me21.add_command(label='Relation - Family', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_21)
        me21.add_command(label="Doctors' Data", font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_21)
        me21.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_21)
        contchck.add_cascade(label=new_text21, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me21)
        me22 = Menu(contchck)
        me22.add_command(label='Patient Data', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num22)
        me22.add_command(label='Relation - Family', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_22)
        me22.add_command(label="Doctors' Data", font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_22)
        me22.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_22)
        contchck.add_cascade(label=new_text22, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me22)
        me23 = Menu(contchck)
        me23.add_command(label='Patient Data', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num23)
        me23.add_command(label='Relation - Family', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_23)
        me23.add_command(label="Doctors' Data", font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_23)
        me23.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_23)
        contchck.add_cascade(label=new_text23, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me23)
        me24 = Menu(contchck)
        me24.add_command(label='Patient Data', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num24)
        me24.add_command(label='Relation - Family', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_24)
        me24.add_command(label="Doctors' Data", font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_24)
        me24.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_24)
        contchck.add_cascade(label=new_text24, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me24)
        contact.configure(activeforeground='black', activebackground='cyan', menu=contchck)

        # 14 besoins menu
        cmd_Besoins = tk.Menubutton(self, text='14 Needs', font=("Times 14"),
            fg='cyan', bg='grey30', relief=GROOVE)
        cmd_Besoins.pack(side=LEFT, padx=3)
        # Partie déroulante du menu 14b
        me4 = Menu(cmd_Besoins)
        me4.add_command(label=new_text, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoinsCoche)
        #me4.add_separator()
        me4.add_command(label=new_text2, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins2Coche)
        #me4.add_separator()
        me4.add_command(label=new_text3, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins3Coche)
        #me4.add_separator()
        me4.add_command(label=new_text4, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins4Coche)
        #me4.add_separator()
        me4.add_command(label=new_text5, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins5Coche)
        #me4.add_separator()
        me4.add_command(label=new_text6, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins6Coche)
        #me4.add_separator()
        me4.add_command(label=new_text7, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins7Coche)
        #me4.add_separator()
        me4.add_command(label=new_text8, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins8Coche)
        #me4.add_separator()
        me4.add_command(label=new_text9, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins9Coche)
        #me4.add_separator()
        me4.add_command(label=new_text10, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins10Coche)
        #me4.add_separator()
        me4.add_command(label=new_text11, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins11Coche)
        #me4.add_separator()
        me4.add_command(label=new_text12, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins12Coche)
        #me4.add_separator()
        me4.add_command(label=new_text13, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins13Coche)
        #me4.add_separator()
        me4.add_command(label=new_text14, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins14Coche)
        #me4.add_separator()
        me4.add_command(label=new_text15, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins15Coche)
        #me4.add_separator()
        me4.add_command(label=new_text16, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins16Coche)
        #me4.add_separator()
        me4.add_command(label=new_text17, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins17Coche)
        #me4.add_separator()
        me4.add_command(label=new_text18, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins18Coche)
        #me4.add_separator()
        me4.add_command(label=new_text19, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins19Coche)
        #me4.add_separator()
        me4.add_command(label=new_text20, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins20Coche)
        #me4.add_separator()
        me4.add_command(label=new_text21, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins21Coche)
        #me4.add_separator()
        me4.add_command(label=new_text22, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins22Coche)
        #me4.add_separator()
        me4.add_command(label=new_text23, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins23Coche)
        #me4.add_separator()
        me4.add_command(label=new_text24, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins24Coche)
        # Integration of 14b menu
        cmd_Besoins.configure(activeforeground='black', activebackground='cyan',
            menu=me4)

        # Helth and care menu
        cmd_Soins = tk.Menubutton(self, text='Care and monitoring', font=("Times 14"),
            fg='cyan', bg='grey30', relief=GROOVE)
        cmd_Soins.pack(side=LEFT, padx=3)
        # Partie déroulante du menu health and care
        meSoins = Menu(cmd_Soins)
        meSoins.add_command(label=new_text, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins1)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text2, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins2)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text3, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins3)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text4, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins4)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text5, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins5)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text6, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins6)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text7, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins7)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text8, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins8)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text9, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins9)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text10, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins10)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text11, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins11)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text12, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins12)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text13, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins13)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text14, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins14)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text15, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins15)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text16, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins16)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text17, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins17)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text18, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins18)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text19, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins19)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text20, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins20)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text21, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins21)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text22, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins22)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text23, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins23)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text24, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins24)
        # Integration of health and care menu
        cmd_Soins.configure(activeforeground='black', activebackground='cyan',
            menu=meSoins)

        # Treatments
        cmd_ttt = tk.Menubutton(self, text='Treatments', font=("Times 14"),
            fg='cyan', bg='grey30', relief=GROOVE)
        cmd_ttt.pack(side=LEFT, padx=3)
        # Partie déroulante du menu health and care
        meTtt = Menu(cmd_ttt)
        meTtt.add_command(label=new_text, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed1)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text2, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed2)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text3, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed3)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text4, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed4)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text5, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed5)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text6, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed6)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text7, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed7)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text8, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed8)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text9, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed9)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text10, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed10)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text11, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed11)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text12, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed12)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text13, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed13)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text14, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed14)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text15, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed15)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text16, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed16)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text17, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed17)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text18, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed18)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text19, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed19)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text20, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed20)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text21, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed21)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text22, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed22)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text23, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed23)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text24, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed24)
        # Integration of health and care menu
        cmd_ttt.configure(activeforeground='black', activebackground='cyan',
            menu=meTtt)

        # Vital parameters menu
        self.cmd_Param = tk.Menubutton(self, text='Vital Parameters', font=("Times 14"),
            fg='cyan', bg='grey30', relief=GROOVE)
        self.cmd_Param.pack(side=LEFT, padx=3)
        # Partie déroulante du menu param
        menuParam = Menu(self.cmd_Param)
        menuParam.add_command(label=new_text, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.showParam1)
        #menuParam.add_separator()
        menuParam.add_command(label=new_text2, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.showParam2)
        #menuParam.add_separator()
        menuParam.add_command(label=new_text3, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.showParam3)
        #menuParam.add_separator()
        menuParam.add_command(label=new_text4, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.showParam4)
        #menuParam.add_separator()
        menuParam.add_command(label=new_text5, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.showParam5)
        #menuParam.add_separator()
        menuParam.add_command(label=new_text6, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.showParam6)
        #menuParam.add_separator()
        menuParam.add_command(label=new_text7, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.showParam7)
        #menuParam.add_separator()
        menuParam.add_command(label=new_text8, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.showParam8)
        #menuParam.add_separator()
        menuParam.add_command(label=new_text9, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.showParam9)
        #menuParam.add_separator()
        menuParam.add_command(label=new_text10, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.showParam10)
        #menuParam.add_separator()
        menuParam.add_command(label=new_text11, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.showParam11)
        #menuParam.add_separator()
        menuParam.add_command(label=new_text12, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.showParam12)
        #menuParam.add_separator()
        menuParam.add_command(label=new_text13, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.showParam13)
        #menuParam.add_separator()
        menuParam.add_command(label=new_text14, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.showParam14)
        #menuParam.add_separator()
        menuParam.add_command(label=new_text15, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.showParam15)
        #menuParam.add_separator()
        menuParam.add_command(label=new_text16, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.showParam16)
        #menuParam.add_separator()
        menuParam.add_command(label=new_text17, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.showParam17)
        #menuParam.add_separator()
        menuParam.add_command(label=new_text18, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.showParam18)
        #menuParam.add_separator()
        menuParam.add_command(label=new_text19, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.showParam19)
        #menuParam.add_separator()
        menuParam.add_command(label=new_text20, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.showParam20)
        #menuParam.add_separator()
        menuParam.add_command(label=new_text21, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.showParam21)
        #menuParam.add_separator()
        menuParam.add_command(label=new_text22, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.showParam22)
        #menuParam.add_separator()
        menuParam.add_command(label=new_text23, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.showParam23)
        #menuParam.add_separator()
        menuParam.add_command(label=new_text24, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.showParam24)
        # Integration of Vital parameters menu
        self.cmd_Param.configure(activeforeground='black', activebackground='cyan',
            menu=menuParam)

        # BMI menu
        cmd_BMI = tk.Menubutton(self, text='Body Mass Indice', font=("Times 14"),
            fg='cyan', bg='grey30', relief=GROOVE)
        cmd_BMI.pack(side=LEFT, padx=3)
        # drop-down portion of BMI menu
        meBmi = Menu(cmd_BMI)
        meBmi.add_command(label=new_text, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB)
        meBmi.add_command(label=new_text2, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB2)
        meBmi.add_command(label=new_text3, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB3)
        meBmi.add_command(label=new_text4, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB4)
        meBmi.add_command(label=new_text5, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB5)
        meBmi.add_command(label=new_text6, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB6)
        meBmi.add_command(label=new_text7, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB7)
        meBmi.add_command(label=new_text8, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB8)
        meBmi.add_command(label=new_text9, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB9)
        meBmi.add_command(label=new_text10, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB10)
        meBmi.add_command(label=new_text11, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB11)
        meBmi.add_command(label=new_text12, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB12)
        meBmi.add_command(label=new_text13, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB13)
        meBmi.add_command(label=new_text14, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB14)
        meBmi.add_command(label=new_text15, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB15)
        meBmi.add_command(label=new_text16, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB16)
        meBmi.add_command(label=new_text17, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB17)
        meBmi.add_command(label=new_text18, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB18)
        meBmi.add_command(label=new_text19, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB19)
        meBmi.add_command(label=new_text20, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB20)
        meBmi.add_command(label=new_text21, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB21)
        meBmi.add_command(label=new_text22, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB22)
        meBmi.add_command(label=new_text23, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB23)
        meBmi.add_command(label=new_text24, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB24)
        # Integration of 3rd menu
        cmd_BMI.configure(activeforeground='black', activebackground='cyan',
            menu=meBmi)

        # Medical Visite
        cmd_Vmed = tk.Menubutton(self, text='Medical Visit', font=("Times 14"),
            fg='cyan', bg='grey30', relief=GROOVE)
        cmd_Vmed.pack(side=LEFT, padx=3)
        # drop-down portion of vmed
        meVmed = Menu(cmd_Vmed)
        meVmed.add_command(label=new_text, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed)
        meVmed.add_command(label=new_text2, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed2)
        meVmed.add_command(label=new_text3, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed3)
        meVmed.add_command(label=new_text4, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed4)
        meVmed.add_command(label=new_text5, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed5)
        meVmed.add_command(label=new_text6, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed6)
        meVmed.add_command(label=new_text7, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed7)
        meVmed.add_command(label=new_text8, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed8)
        meVmed.add_command(label=new_text9, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed9)
        meVmed.add_command(label=new_text10, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed10)
        meVmed.add_command(label=new_text11, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed11)
        meVmed.add_command(label=new_text12, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed12)
        meVmed.add_command(label=new_text13, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed13)
        meVmed.add_command(label=new_text14, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed14)
        meVmed.add_command(label=new_text15, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed15)
        meVmed.add_command(label=new_text16, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed16)
        meVmed.add_command(label=new_text17, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed17)
        meVmed.add_command(label=new_text18, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed18)
        meVmed.add_command(label=new_text19, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed19)
        meVmed.add_command(label=new_text20, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed20)
        meVmed.add_command(label=new_text21, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed21)
        meVmed.add_command(label=new_text22, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed22)
        meVmed.add_command(label=new_text23, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed23)
        meVmed.add_command(label=new_text24, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed24)
        # Integration of 3rd menu
        cmd_Vmed.configure(activeforeground='black', activebackground='cyan',
            menu=meVmed)

        # Nutrition menu for intolerance and hate meals
        cmd_Print = tk.Menubutton(self, text='Intolerance All.', font=("Times 14"),
            fg='cyan', bg='grey30', relief=GROOVE)
        cmd_Print.pack(side=LEFT, padx=3)
        # drop-down portion of nutrition
        mePrint = Menu(cmd_Print)
        mePrint.add_command(label=new_text, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu)
        mePrint.add_command(label=new_text2, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu2)
        mePrint.add_command(label=new_text3, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu3)
        mePrint.add_command(label=new_text4, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu4)
        mePrint.add_command(label=new_text5, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu5)
        mePrint.add_command(label=new_text6, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu6)
        mePrint.add_command(label=new_text7, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu7)
        mePrint.add_command(label=new_text8, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu8)
        mePrint.add_command(label=new_text9, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu9)
        mePrint.add_command(label=new_text10, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu10)
        mePrint.add_command(label=new_text11, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu11)
        mePrint.add_command(label=new_text12, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu12)
        mePrint.add_command(label=new_text13, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu13)
        mePrint.add_command(label=new_text14, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu14)
        mePrint.add_command(label=new_text15, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu15)
        mePrint.add_command(label=new_text16, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu16)
        mePrint.add_command(label=new_text17, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu17)
        mePrint.add_command(label=new_text18, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu18)
        mePrint.add_command(label=new_text19, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu19)
        mePrint.add_command(label=new_text20, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu20)
        mePrint.add_command(label=new_text21, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu21)
        mePrint.add_command(label=new_text22, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu22)
        mePrint.add_command(label=new_text23, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu23)
        mePrint.add_command(label=new_text24, font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu24)
        # Integration of nutrition menu
        cmd_Print.configure(activeforeground='black', activebackground='cyan',
            menu=mePrint)

        # Menu for showing all Graphs togather per patient
        cmd_backup = tk.Menubutton(self, text='Global', font=("Times 14"), fg='cyan',
            bg='grey30', relief=GROOVE)
        cmd_backup.pack(side=LEFT, padx=3)
        # drop-down portion of Graphics menu
        me1 = Menu(cmd_backup)
        me2 = Menu(me1)
        me2.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup)
        me1.add_cascade(label=new_text, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me2)
        me3=Menu(me1)
        me3.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup2)
        me1.add_cascade(label=new_text2, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me3)
        me4=Menu(me1)
        me4.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup3)
        me1.add_cascade(label=new_text3, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me4)
        me5=Menu(me1)
        me5.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup4)
        me1.add_cascade(label=new_text4, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me5)
        me6=Menu(me1)
        me6.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup5)
        me1.add_cascade(label=new_text5, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me6)
        me7=Menu(me1)
        me7.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup6)
        me1.add_cascade(label=new_text6, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me7)
        me8=Menu(me1)
        me8.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup7)
        # Integration of sub-menu
        me1.add_cascade(label=new_text7, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me8)
        me9=Menu(me1)
        me9.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup8)
        # Integration of sub-menu
        me1.add_cascade(label=new_text8, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me9)
        me10=Menu(me1)
        me10.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup9)
        # Integration of sub-menu
        me1.add_cascade(label=new_text9, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me10)
        me11=Menu(me1)
        me11.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup10)
        # Integration of sub-menu
        me1.add_cascade(label=new_text10, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me11)
        me12=Menu(me1)
        me12.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup11)
        # Integration of sub-menu
        me1.add_cascade(label=new_text11, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me12)
        me13=Menu(me1)
        me13.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup12)
        # Integration of sub-menu
        me1.add_cascade(label=new_text12, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me13)
        me14=Menu(me1)
        me14.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup13)
        # Integration of sub-menu
        me1.add_cascade(label=new_text13, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me14)
        me15=Menu(me1)
        me15.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup14)
        # Integration of sub-menu
        me1.add_cascade(label=new_text14, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me15)
        me16=Menu(me1)
        me16.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup15)
        # Integration of sub-menu
        me1.add_cascade(label=new_text15, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me16)
        me17=Menu(me1)
        me17.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup16)
        # Integration of sub-menu
        me1.add_cascade(label=new_text16, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me17)
        me18=Menu(me1)
        me18.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup17)
        # Integration of sub-menu
        me1.add_cascade(label=new_text17, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me18)
        me19=Menu(me1)
        me19.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup18)
        # Integration of sub-menu
        me1.add_cascade(label=new_text18, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me19)
        me20=Menu(me1)
        me20.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup19)
        # Integration of sub-menu
        me1.add_cascade(label=new_text19, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me20)
        me21=Menu(me1)
        me21.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup20)
        # Integration of sub-menu
        me1.add_cascade(label=new_text20, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me21)
        me22=Menu(me1)
        me22.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup21)
        # Integration of sub-menu
        me1.add_cascade(label=new_text21, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me22)
        me23=Menu(me1)
        me23.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup22)
        # Integration of sub-menu
        me1.add_cascade(label=new_text22, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me23)
        me24=Menu(me1)
        me24.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup23)
        # Integration of sub-menu
        me1.add_cascade(label=new_text23, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me24)
        me25=Menu(me1)
        me25.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup24)
        # Integration of sub-menu
        me1.add_cascade(label=new_text24, underline=0, font=('Times 12'),
            background='black', foreground='cyan',
            activeforeground='black', activebackground='cyan', menu=me25)
        # Integration of Graph menu
        cmd_backup.configure(activeforeground='black', activebackground='cyan', menu=me1)

# Application principale (Main app)
class Application(tk.Frame):
    """
        Main app to display first page.
    """
    def __init__(self, boss=None):
        tk.Frame.__init__(self, borderwidth=5, bg='RoyalBlue4', padx=20, pady=20, relief=GROOVE)
        self.master.title('Time-Track Developed by ko@l@tr33 - 2020')
        self.master.withdraw()
        self.master.update_idletasks()  # Update "requested size" from geometry manager
        x = (self.master.winfo_screenwidth() / 3 - self.master.winfo_reqwidth()) / 2
        y = (self.master.winfo_screenheight() / 3 - self.master.winfo_reqheight()) / 2
        self.master.geometry("+%d+%d" % (x, y))
        self.master.deiconify()
        self.master.protocol("WM_DELETE_WINDOW", lambda arg=self.master: self.msgQuitapp(arg))

        self.mBar = MenuBar(self)
        self.mBar.pack(side=TOP, fill=X, expand=YES)

        self.can = tk.Canvas(self, width=1250, height=700, bg='black')
        self.frame = tk.Frame(self.can)
        # ScrollCanvas limite de la zone à parcourir avec la barre 1250 - 700
        self.vsb = tk.Scrollbar(self, orient=VERTICAL, command=self.can.yview)
        self.can.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side=tk.RIGHT, fill=Y)
        self.can.create_window((4,4), window=self.frame, anchor=NW, tags="self.frame")

        self.clock_label = tk.Label(self, text="", fg="white", bg="RoyalBlue3",
            font=("helvetica", 18, 'bold'))
        self.clock_label.pack(side=tk.TOP, fill=X, expand=YES)
        self.clock_label.after(200, self.tick)

        # Insertion of picture
        self.photo = tk.PhotoImage(file='./syno_gif/fondcolorbg4.png')
        self.item = self.can.create_image(625, 350, image=self.photo)
        # Insertion of text
        self.can.create_text(625, 350, anchor=CENTER,
            text="Python 3.6 - Tkinter 8.6 - GIMP 2.8",
            font=('Times New Roman', 18, 'bold'), fill='turquoise')
        self.can.create_text(1240, 670, anchor=NE, text="ko@l@tr33",
            font=('Times', 12), fill='turquoise')
        # Configuration de la Scrollbar sur le Frame
        self.frame.bind("<Configure>", self.onFrameConfigure)
        self.can.pack(side=LEFT, fill=BOTH, expand=YES)
        # 3 buttons on welcome page.
        self.button1 = tk.Button(self, text="Info", font=('Times 14 bold'),
            bg='grey17', fg='cyan', command = self.frameInfo)
        self.button1.configure(width=10, bd=3, highlightbackground='grey10',
            activebackground='pale turquoise')
        self.button1_window = self.can.create_window(75, 30, anchor=CENTER,
            window=self.button1)
        # Pycon button
        self.button2 = tk.Button(self, text="DATABASE", font=('Times 18 bold'),
            bg='RoyalBlue3', fg='white', command = self.funcPyCon)
        self.button2.configure(width=15, bd=3, highlightbackground='RoyalBlue4',
            activebackground='pale turquoise')
        self.button2_window = self.can.create_window(300, 450, anchor=CENTER,
            window=self.button2)
        # Synopsis button
        self.button3 = tk.Button(self, text="TEXTBOX", font=('Times 18 bold'),
            bg='RoyalBlue3', fg='white', command = self.showSynopsis)
        self.button3.configure(width=15, bd=3, highlightbackground='RoyalBlue4',
            activebackground='pale turquoise')
        self.button3_window = self.can.create_window(625, 450, anchor=CENTER,
            window=self.button3)
        # Psychotabs button
        self.button4 = tk.Button(self, text="RESIDENTS", font=('Times 18 bold'),
            bg='RoyalBlue3', fg='white', command = self.showPatients)
        self.button4.configure(width=15, bd=3, highlightbackground='RoyalBlue4',
            activebackground='pale turquoise')
        self.button4_window = self.can.create_window(950, 450, anchor=CENTER,
            window=self.button4)
        self.pack()

    def tick(self):
        """ Updates the display clock every 200 milliseconds """
        self.new_time = time.strftime("%H:%M:%S %p")
        try:
            if self.new_time == self.new_time:
                self.time = self.new_time
                self.display_time = self.time
                self.clock_label.configure(text=self.display_time)
                self._job = self.clock_label.after(200, self.tick)
        except (ValueError, OSError) as val_err:
            print("Error time --> ", val_err)

    # Method to reconfigure scrollbar every time.
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.can.configure(scrollregion=self.can.bbox(ALL))

    def effacer(self):
        '''Reinitialize canvas when we pass through another'''
        self.can.delete(ALL)

    def framShow(self):
        """
            To update without
            re-enter id and passwd
        """
        try:
            if self._job is not None:
                self.clock_label.after_cancel(self._job)
                self._job = None
                self.master.destroy()
                Application()
                #Application.__init__(self)
        except (OSError, ValueError) as two_err:
            print("OS or Val error", two_err)

    def msgQuitapp(self, arg):
        """
            If usr want to quit, a question
            into a msgbox appear.
        """
        try:
            MsgBox = messagebox.askyesno('Quit system', 'Do you want to quit ?')
            if MsgBox == 1:
                self.master.destroy()
        except OSError as quitwind:
            print("Error 2 : time to quit !!!", quitwind)

    def msgExit(self):
        """
            If usr want to quit, a question
            into a msgbox appear.
        """
        try:
            MsgBoxapp = messagebox.askyesno('Quit system', 'Do you want to quit ?')
            if MsgBoxapp == 1:
                self.master.destroy()
        except OSError as quitapp:
            print("Error 3 : time to quit !!!", quitapp)

    def frameInfo(self):
        """
            Info for button on first page
        """
        self.lab = tk.Tk()
        self.lab.title("ATCD")
        self.lab.configure(bg="grey22")

        self.labFra = tk.LabelFrame(self.lab, text="\nWelcome !",
            font=("Arial 12"),fg='cyan', bg='grey22')
        self.labFra.pack(padx=5, pady=5)
        self.separator = tk.Frame(self.labFra, height=2, bd=1,
            relief=SUNKEN)

        self.lab4 = tk.Label(self.labFra, text="\nInfo",
            font=('Times 16 bold'), fg='cyan', bg='grey22').pack()
        self.separator = tk.Frame(self.labFra, height=2, bd=1, relief=SUNKEN)
        self.separator.pack(fill=X, padx=100, pady=3)

        self.lab5 = tk.Label(self.labFra, justify=LEFT, fg='cyan',
            bg='grey22', font=('Times', 14),
            text="\nMenu Bar, DB, Textbox and Residents are the most usefull skills\n"
            "to perform onto this app ! If you need help, you can go to MapApp to\n"
            "access map of this app and understand how the app is used ;)\n\n"
            "Enjoy it !\n").pack(padx=10)
        self.separator = tk.Frame(self.labFra, height=2, bd=1, relief=SUNKEN)
        self.separator.pack(fill=X, padx=30, pady=3)
        self.lab6 = tk.Label(self.labFra, justify=LEFT, fg='cyan',
            bg='grey22', font=('Times', 14),
            text="Path : Menu Bar --> Menu --> MapApp").pack(padx=10, pady=10)

    def instalpy(self):
        """
            Explanation about skills
            and how to use app
        """
        self.can.delete(ALL)
        self.can.configure(background='black')
        self.photo = tk.PhotoImage(file='./syno_gif/pyt2.gif')
        self.item=self.can.create_image(625, 350, image=self.photo)
        self.can.create_text(400, 20, anchor=NW,
            text="- MAPAPP -\n\n"

            "Usefull functionalities :\n"
            "----------------------------\n"
            "---> Backup is scheduled every 5 days and each month for Vital Parameters and BMI\n"
            "---> Display if a treatment or reserve ends the next day and print a stop into tabs\n"
            "---> Agenda is verified every day and a reminder appear to show you" \
            " if an appointment is fixed for tomorrow\n\n"

            "How to use heal-track :\n\n"

            "To make a patient entry : \n"

            "Entry or Add patient (read below) ---> Allergy + Intolerance --->" \
            " 14 Needs ---> Care and Monitoring :\n"
            "-----------------------------------------------------------------"
            "---------------------------------------------------------\n"
            "Use 'Entry' button to enter for first time new patient. Use 'Add " \
            "patient' once time all patients were enter \n"
            "(button to replace a patient who's left with delete button).\n"
            "Once time, patient had added use 'Update' button to enter an allergy " \
            "if none, write 'none' and press enter !\n"
            "You can also use 'Intolerance' in the Menu Bar to complete 'allergy'.\n"
            "After it, Care and Monitoring is available only if you have entered one " \
            "or more needs of patient.\n"
            "1 ---> Press 'add patient' (button)\n"
            "2 ---> Write data of patient and press 'enter'\n"
            "3 ---> Use Refresh (button)\n"
            "4 ---> Click on 'Intolerances' (in menubar) and press enter.\n"
            "5 ---> Use 'Update' button to write allergia into DB\n"
            "6 ---> Click on 14 Needs ()\n"
            "7 ---> Care and monitoring\n\n"

            "Care and monitoring retrieve all data from :\n"
            "----------------------------------------------------\n"
            "+ 14 Needs (V. Henderson)\n"
            "+ Labo (dosage of neuroleptic)\n"
            "+ Stix (button into Labo)\n"

            "!!! WARNING !!! : don't enter allergia before intolerance," \
            "otherwise it will be erased...\n"

            "\nDevelopped on Linux Xubuntu (xfce4) Voyager 18.04 by ko@l@tr33\n",
            font=('Times', 13), fill='aquamarine')
        self.can.configure(scrollregion=self.can.bbox(ALL))

    def showSynopsis(self):
        """
            To call func in boxapp.py
        """
        callBox(self)

    def funcPyCon(self):
        """
            To display data from database
        """
        self.master.withdraw()
        subprocess.run('./accessDB.py', check=True)
        self.master.deiconify()

    def showPatients(self):
        """
            To call func in patcaps.py
        """
        callResident(self)

    def callPatient1(self):
        """
            To enter a new patient.
        """
        subprocess.Popen('./newpatient/entrypytientfile.py', shell=True)

    def delEverPat(self):
        """
            To delete patient
        """
        subprocess.Popen('./deletepatient/deleverything.py', shell=True)

    def addPatientAfter(self):
        """
            To add new patient after delete one of them
        """
        subprocess.Popen('./newpatient/torecord.py', shell=True)

    def patientAgenda(self):
        """
            Multiples possibilities with next cmd :
            self.master.withdraw()
            self.master.overrideredirect(True)
            self.master.deiconify()
            self.master.lift()
            self.master.focus_force()
        """
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda.py', check=True)
        self.master.deiconify()

    def patientAgenda2(self):
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda2.py', check=True)
        self.master.deiconify()

    def patientAgenda3(self):
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda3.py', check=True)
        self.master.deiconify()

    def patientAgenda4(self):
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda4.py', check=True)
        self.master.deiconify()

    def patientAgenda5(self):
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda5.py', check=True)
        self.master.deiconify()

    def patientAgenda6(self):
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda6.py', check=True)
        self.master.deiconify()

    def patientAgenda7(self):
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda7.py', check=True)
        self.master.deiconify()

    def patientAgenda8(self):
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda8.py', check=True)
        self.master.deiconify()

    def patientAgenda9(self):
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda9.py', check=True)
        self.master.deiconify()

    def patientAgenda10(self):
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda10.py', check=True)
        self.master.deiconify()

    def patientAgenda11(self):
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda11.py', check=True)
        self.master.deiconify()

    def patientAgenda12(self):
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda12.py', check=True)
        self.master.deiconify()

    def patientAgenda13(self):
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda13.py', check=True)
        self.master.deiconify()

    def patientAgenda14(self):
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda14.py', check=True)
        self.master.deiconify()

    def patientAgenda15(self):
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda15.py', check=True)
        self.master.deiconify()

    def patientAgenda16(self):
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda16.py', check=True)
        self.master.deiconify()

    def patientAgenda17(self):
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda17.py', check=True)
        self.master.deiconify()

    def patientAgenda18(self):
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda18.py', check=True)
        self.master.deiconify()

    def patientAgenda19(self):
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda19.py', check=True)
        self.master.deiconify()

    def patientAgenda20(self):
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda20.py', check=True)
        self.master.deiconify()

    def patientAgenda21(self):
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda21.py', check=True)
        self.master.deiconify()

    def patientAgenda22(self):
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda22.py', check=True)
        self.master.deiconify()

    def patientAgenda23(self):
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda23.py', check=True)
        self.master.deiconify()

    def patientAgenda24(self):
        self.master.withdraw()
        subprocess.run('./patient_agenda/origin_agenda24.py', check=True)
        self.master.deiconify()

    # Contact patient 1
    def contact_num1(self):
        Window(self)

    def contactfamily_1(self):
        famWind(self)

    def contactdoctor_1(self):
        doctorWind(self)

    def contacthcsystem_1(self):
        homecsWind(self)

    # Contact patient 2
    def contact_num2(self):
        Window2(self)

    def contactfamily_2(self):
        famWind2(self)

    def contactdoctor_2(self):
        doctorWind2(self)

    def contacthcsystem_2(self):
        homecsWind2(self)

    # Contact patient 3
    def contact_num3(self):
        Window3(self)

    def contactfamily_3(self):
        famWind3(self)

    def contactdoctor_3(self):
        doctorWind3(self)

    def contacthcsystem_3(self):
        homecsWind3(self)

    # Contact patient 4
    def contact_num4(self):
        Window4(self)

    def contactfamily_4(self):
        famWind4(self)

    def contactdoctor_4(self):
        doctorWind4(self)

    def contacthcsystem_4(self):
        homecsWind4(self)

    # Contact patient 5
    def contact_num5(self):
        Window5(self)

    def contactfamily_5(self):
        famWind5(self)

    def contactdoctor_5(self):
        doctorWind5(self)

    def contacthcsystem_5(self):
        homecsWind5(self)

    # Contact patient 6
    def contact_num6(self):
        Window6(self)

    def contactfamily_6(self):
        famWind6(self)

    def contactdoctor_6(self):
        doctorWind6(self)

    def contacthcsystem_6(self):
        homecsWind6(self)

    # Contact patient 7
    def contact_num7(self):
        Window7(self)

    def contactfamily_7(self):
        famWind7(self)

    def contactdoctor_7(self):
        doctorWind7(self)

    def contacthcsystem_7(self):
        homecsWind7(self)

    # Contact patient 8
    def contact_num8(self):
        Window8(self)

    def contactfamily_8(self):
        famWind8(self)

    def contactdoctor_8(self):
        doctorWind8(self)

    def contacthcsystem_8(self):
        homecsWind8(self)

    # Contact patient 9
    def contact_num9(self):
        Window9(self)

    def contactfamily_9(self):
        famWind9(self)

    def contactdoctor_9(self):
        doctorWind9(self)

    def contacthcsystem_9(self):
        homecsWind9(self)

    # Contact patient 10
    def contact_num10(self):
        Window10(self)

    def contactfamily_10(self):
        famWind10(self)

    def contactdoctor_10(self):
        doctorWind10(self)

    def contacthcsystem_10(self):
        homecsWind10(self)

    # Contact patient 11
    def contact_num11(self):
        Window11(self)

    def contactfamily_11(self):
        famWind11(self)

    def contactdoctor_11(self):
        doctorWind11(self)

    def contacthcsystem_11(self):
        homecsWind11(self)

    # Contact patient 12
    def contact_num12(self):
        Window12(self)

    def contactfamily_12(self):
        famWind12(self)

    def contactdoctor_12(self):
        doctorWind12(self)

    def contacthcsystem_12(self):
        homecsWind12(self)

    # Contact patient 13
    def contact_num13(self):
        Window13(self)

    def contactfamily_13(self):
        famWind13(self)

    def contactdoctor_13(self):
        doctorWind13(self)

    def contacthcsystem_13(self):
        homecsWind13(self)

    # Contact patient 14
    def contact_num14(self):
        Window14(self)

    def contactfamily_14(self):
        famWind14(self)

    def contactdoctor_14(self):
        doctorWind14(self)

    def contacthcsystem_14(self):
        homecsWind14(self)

    # Contact patient 15
    def contact_num15(self):
        Window15(self)

    def contactfamily_15(self):
        famWind15(self)

    def contactdoctor_15(self):
        doctorWind15(self)

    def contacthcsystem_15(self):
        homecsWind15(self)

    # Contact patient 16
    def contact_num16(self):
        Window16(self)

    def contactfamily_16(self):
        famWind16(self)

    def contactdoctor_16(self):
        doctorWind16(self)

    def contacthcsystem_16(self):
        homecsWind16(self)

    # Contact patient 17
    def contact_num17(self):
        Window17(self)

    def contactfamily_17(self):
        famWind17(self)

    def contactdoctor_17(self):
        doctorWind17(self)

    def contacthcsystem_17(self):
        homecsWind17(self)

    # Contact patient 18
    def contact_num18(self):
        Window18(self)

    def contactfamily_18(self):
        famWind18(self)

    def contactdoctor_18(self):
        doctorWind18(self)

    def contacthcsystem_18(self):
        homecsWind18(self)

    # Contact patient 19
    def contact_num19(self):
        Window19(self)

    def contactfamily_19(self):
        famWind19(self)

    def contactdoctor_19(self):
        doctorWind19(self)

    def contacthcsystem_19(self):
        homecsWind19(self)

    # Contact patient 20
    def contact_num20(self):
        Window20(self)

    def contactfamily_20(self):
        famWind20(self)

    def contactdoctor_20(self):
        doctorWind20(self)

    def contacthcsystem_20(self):
        homecsWind20(self)

    # Contact patient 21
    def contact_num21(self):
        Window21(self)

    def contactfamily_21(self):
        famWind21(self)

    def contactdoctor_21(self):
        doctorWind21(self)

    def contacthcsystem_21(self):
        homecsWind21(self)

    # Contact patient 22
    def contact_num22(self):
        Window22(self)

    def contactfamily_22(self):
        famWind22(self)

    def contactdoctor_22(self):
        doctorWind22(self)

    def contacthcsystem_22(self):
        homecsWind22(self)

    # Contact patient 23
    def contact_num23(self):
        Window23(self)

    def contactfamily_23(self):
        famWind23(self)

    def contactdoctor_23(self):
        doctorWind23(self)

    def contacthcsystem_23(self):
        homecsWind23(self)

    # Contact patient 24
    def contact_num24(self):
        Window24(self)

    def contactfamily_24(self):
        famWind24(self)

    def contactdoctor_24(self):
        doctorWind24(self)

    def contacthcsystem_24(self):
        homecsWind24(self)

    # CheckBox 14 needs OK
    def besoinsCoche(self):
        subprocess.Popen('./need/checkb.py', shell=True)

    def besoins2Coche(self):
        subprocess.Popen('./need/checkb2.py', shell=True)

    def besoins3Coche(self):
        subprocess.Popen('./need/checkb3.py', shell=True)

    def besoins4Coche(self):
        subprocess.Popen('./need/checkb4.py', shell=True)

    def besoins5Coche(self):
        subprocess.Popen('./need/checkb5.py', shell=True)

    def besoins6Coche(self):
        subprocess.Popen('./need/checkb6.py', shell=True)

    def besoins7Coche(self):
        subprocess.Popen('./need/checkb7.py', shell=True)

    def besoins8Coche(self):
        subprocess.Popen('./need/checkb8.py', shell=True)

    def besoins9Coche(self):
        subprocess.Popen('./need/checkb9.py', shell=True)

    def besoins10Coche(self):
        subprocess.Popen('./need/checkb10.py', shell=True)

    def besoins11Coche(self):
        subprocess.Popen('./need/checkb11.py', shell=True)

    def besoins12Coche(self):
        subprocess.Popen('./need/checkb12.py', shell=True)

    def besoins13Coche(self):
        subprocess.Popen('./need/checkb13.py', shell=True)

    def besoins14Coche(self):
        subprocess.Popen('./need/checkb14.py', shell=True)

    def besoins15Coche(self):
        subprocess.Popen('./need/checkb15.py', shell=True)

    def besoins16Coche(self):
        subprocess.Popen('./need/checkb16.py', shell=True)

    def besoins17Coche(self):
        subprocess.Popen('./need/checkb17.py', shell=True)

    def besoins18Coche(self):
        subprocess.Popen('./need/checkb18.py', shell=True)

    def besoins19Coche(self):
        subprocess.Popen('./need/checkb19.py', shell=True)

    def besoins20Coche(self):
        subprocess.Popen('./need/checkb20.py', shell=True)

    def besoins21Coche(self):
        subprocess.Popen('./need/checkb21.py', shell=True)

    def besoins22Coche(self):
        subprocess.Popen('./need/checkb22.py', shell=True)

    def besoins23Coche(self):
        subprocess.Popen('./need/checkb23.py', shell=True)

    def besoins24Coche(self):
        subprocess.Popen('./need/checkb24.py', shell=True)

    # Func 14 needs suivi OK
    def suiviSoins1(self):
        needload1()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_1.py", check=True)
        self.master.deiconify()

    def suiviSoins2(self):
        needload2()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_2.py", check=True)
        self.master.deiconify()

    def suiviSoins3(self):
        needload3()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_3.py", check=True)
        self.master.deiconify()

    def suiviSoins4(self):
        needload4()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_4.py", check=True)
        self.master.deiconify()

    def suiviSoins5(self):
        needload5()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_5.py", check=True)
        self.master.deiconify()

    def suiviSoins6(self):
        needload6()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_6.py", check=True)
        self.master.deiconify()

    def suiviSoins7(self):
        needload7()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_7.py", check=True)
        self.master.deiconify()

    def suiviSoins8(self):
        needload8()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_8.py", check=True)
        self.master.deiconify()

    def suiviSoins9(self):
        needload9()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_9.py", check=True)
        self.master.deiconify()

    def suiviSoins10(self):
        needload10()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_10.py", check=True)
        self.master.deiconify()

    def suiviSoins11(self):
        needload11()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_11.py", check=True)
        self.master.deiconify()

    def suiviSoins12(self):
        needload12()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_12.py", check=True)
        self.master.deiconify()

    def suiviSoins13(self):
        needload13()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_13.py", check=True)
        self.master.deiconify()

    def suiviSoins14(self):
        needload14()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_14.py", check=True)
        self.master.deiconify()

    def suiviSoins15(self):
        needload15()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_15.py", check=True)
        self.master.deiconify()

    def suiviSoins16(self):
        needload16()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_16.py", check=True)
        self.master.deiconify()

    def suiviSoins17(self):
        needload17()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_17.py", check=True)
        self.master.deiconify()

    def suiviSoins18(self):
        needload18()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_18.py", check=True)
        self.master.deiconify()

    def suiviSoins19(self):
        needload19()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_19.py", check=True)
        self.master.deiconify()

    def suiviSoins20(self):
        needload20()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_20.py", check=True)
        self.master.deiconify()

    def suiviSoins21(self):
        needload21()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_21.py", check=True)
        self.master.deiconify()

    def suiviSoins22(self):
        needload22()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_22.py", check=True)
        self.master.deiconify()

    def suiviSoins23(self):
        needload23()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_23.py", check=True)
        self.master.deiconify()

    def suiviSoins24(self):
        needload24()
        self.master.withdraw()
        subprocess.run("./need/suivi_patient_24.py", check=True)
        self.master.deiconify()

    # Func Diagnostic
    def diag1(self):
        diagloading1()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient1.py", check=True)
        self.master.deiconify()

    def diag2(self):
        diagloading2()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient2.py", check=True)
        self.master.deiconify()

    def diag3(self):
        diagloading3()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient3.py", check=True)
        self.master.deiconify()

    def diag4(self):
        diagloading4()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient4.py", check=True)
        self.master.deiconify()

    def diag5(self):
        diagloading5()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient5.py", check=True)
        self.master.deiconify()

    def diag6(self):
        diagloading6()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient6.py", check=True)
        self.master.deiconify()

    def diag7(self):
        diagloading7()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient7.py", check=True)
        self.master.deiconify()

    def diag8(self):
        diagloading8()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient8.py", check=True)
        self.master.deiconify()

    def diag9(self):
        diagloading9()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient9.py", check=True)
        self.master.deiconify()

    def diag10(self):
        diagloading10()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient10.py", check=True)
        self.master.deiconify()

    def diag11(self):
        diagloading11()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient11.py", check=True)
        self.master.deiconify()

    def diag12(self):
        diagloading12()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient12.py", check=True)
        self.master.deiconify()

    def diag13(self):
        diagloading13()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient13.py", check=True)
        self.master.deiconify()

    def diag14(self):
        diagloading14()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient14.py", check=True)
        self.master.deiconify()

    def diag15(self):
        diagloading15()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient15.py", check=True)
        self.master.deiconify()

    def diag16(self):
        diagloading16()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient16.py", check=True)
        self.master.deiconify()

    def diag17(self):
        diagloading17()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient17.py", check=True)
        self.master.deiconify()

    def diag18(self):
        diagloading18()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient18.py", check=True)
        self.master.deiconify()

    def diag19(self):
        diagloading19()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient19.py", check=True)
        self.master.deiconify()

    def diag20(self):
        diagloading20()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient20.py", check=True)
        self.master.deiconify()

    def diag21(self):
        diagloading21()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient21.py", check=True)
        self.master.deiconify()

    def diag22(self):
        diagloading22()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient22.py", check=True)
        self.master.deiconify()

    def diag23(self):
        diagloading23()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient23.py", check=True)
        self.master.deiconify()

    def diag24(self):
        diagloading24()
        self.master.withdraw()
        subprocess.run("./diag/diag_patient24.py", check=True)
        self.master.deiconify()

    # treatments
    def tttMed1(self):
        downloadttt1()
        callTreatment1(self)

    def tttMed2(self):
        downloadttt2()
        callTreatment2(self)

    def tttMed3(self):
        downloadttt3()
        callTreatment3(self)

    def tttMed4(self):
        downloadttt4()
        callTreatment4(self)

    def tttMed5(self):
        downloadttt5()
        callTreatment5(self)

    def tttMed6(self):
        downloadttt6()
        callTreatment6(self)

    def tttMed7(self):
        downloadttt7()
        callTreatment7(self)

    def tttMed8(self):
        downloadttt8()
        callTreatment8(self)

    def tttMed9(self):
        downloadttt9()
        callTreatment9(self)

    def tttMed10(self):
        downloadttt10()
        callTreatment10(self)

    def tttMed11(self):
        downloadttt11()
        callTreatment11(self)

    def tttMed12(self):
        downloadttt12()
        callTreatment12(self)

    def tttMed13(self):
        downloadttt13()
        callTreatment13(self)

    def tttMed14(self):
        downloadttt14()
        callTreatment14(self)

    def tttMed15(self):
        downloadttt15()
        callTreatment15(self)

    def tttMed16(self):
        downloadttt16()
        callTreatment16(self)

    def tttMed17(self):
        downloadttt17()
        callTreatment17(self)

    def tttMed18(self):
        downloadttt18()
        callTreatment18(self)

    def tttMed19(self):
        downloadttt19()
        callTreatment19(self)

    def tttMed20(self):
        downloadttt20()
        callTreatment20(self)

    def tttMed21(self):
        downloadttt21()
        callTreatment21(self)

    def tttMed22(self):
        downloadttt22()
        callTreatment22(self)

    def tttMed23(self):
        downloadttt23()
        callTreatment23(self)

    def tttMed24(self):
        downloadttt24()
        callTreatment24(self)

    # Func labo
    def laboResult(self):
        labodownload1()
        callLabo1(self)

    def laboResult2(self):
        labodownload2()
        callLabo2(self)

    def laboResult3(self):
        labodownload3()
        callLabo3(self)

    def laboResult4(self):
        labodownload4()
        callLabo4(self)

    def laboResult5(self):
        labodownload5()
        callLabo5(self)

    def laboResult6(self):
        labodownload6()
        callLabo6(self)

    def laboResult7(self):
        labodownload7()
        callLabo7(self)

    def laboResult8(self):
        labodownload8()
        callLabo8(self)

    def laboResult9(self):
        labodownload9()
        callLabo9(self)

    def laboResult10(self):
        labodownload10()
        callLabo10(self)

    def laboResult11(self):
        labodownload11()
        callLabo11(self)

    def laboResult12(self):
        labodownload12()
        callLabo12(self)

    def laboResult13(self):
        labodownload13()
        callLabo13(self)

    def laboResult14(self):
        labodownload14()
        callLabo14(self)

    def laboResult15(self):
        labodownload15()
        callLabo15(self)

    def laboResult16(self):
        labodownload16()
        callLabo16(self)

    def laboResult17(self):
        labodownload17()
        callLabo17(self)

    def laboResult18(self):
        labodownload18()
        callLabo18(self)

    def laboResult19(self):
        labodownload19()
        callLabo19(self)

    def laboResult20(self):
        labodownload20()
        callLabo20(self)

    def laboResult21(self):
        labodownload21()
        callLabo21(self)

    def laboResult22(self):
        labodownload22()
        callLabo22(self)

    def laboResult23(self):
        labodownload23()
        callLabo23(self)

    def laboResult24(self):
        labodownload24()
        callLabo24(self)

    # Func Vital Parameters
    def showParam1(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.call("./param/fencap.py")
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def showParam2(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.call("./param/fencap2.py")
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def showParam3(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.call("./param/fencap3.py")
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def showParam4(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.call("./param/fencap4.py")
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def showParam5(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.call("./param/fencap5.py")
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def showParam6(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.call("./param/fencap6.py")
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def showParam7(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.call("./param/fencap7.py")
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def showParam8(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.call("./param/fencap8.py")
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def showParam9(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.call("./param/fencap9.py")
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def showParam10(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.call("./param/fencap10.py")
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def showParam11(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.call("./param/fencap11.py")
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def showParam12(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.call("./param/fencap12.py")
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def showParam13(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.call("./param/fencap13.py")
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def showParam14(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.call("./param/fencap14.py")
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def showParam15(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.call("./param/fencap15.py")
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def showParam16(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.call("./param/fencap16.py")
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def showParam17(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.call("./param/fencap17.py")
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def showParam18(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.call("./param/fencap18.py")
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def showParam19(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.call("./param/fencap19.py")
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def showParam20(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.call("./param/fencap20.py")
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def showParam21(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.call("./param/fencap21.py")
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def showParam22(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.call("./param/fencap22.py")
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def showParam23(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.call("./param/fencap23.py")
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def showParam24(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.call("./param/fencap24.py")
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    # Func BMI
    def calculB(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.run("./calBmi/CalculBmi.py", check=True)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def calculB2(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.run("./calBmi/CalculBmi2.py", check=True)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def calculB3(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.run("./calBmi/CalculBmi3.py", check=True)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def calculB4(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.run("./calBmi/CalculBmi4.py", check=True)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def calculB5(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.run("./calBmi/CalculBmi5.py", check=True)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def calculB6(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.run("./calBmi/CalculBmi6.py", check=True)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def calculB7(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.run("./calBmi/CalculBmi7.py", check=True)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def calculB8(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.run("./calBmi/CalculBmi8.py", check=True)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def calculB9(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.run("./calBmi/CalculBmi9.py", check=True)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def calculB10(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.run("./calBmi/CalculBmi10.py", check=True)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def calculB11(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.run("./calBmi/CalculBmi11.py", check=True)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def calculB12(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.run("./calBmi/CalculBmi12.py", check=True)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def calculB13(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.run("./calBmi/CalculBmi13.py", check=True)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def calculB14(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.run("./calBmi/CalculBmi14.py", check=True)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def calculB15(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.run("./calBmi/CalculBmi15.py", check=True)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def calculB16(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.run("./calBmi/CalculBmi16.py", check=True)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def calculB17(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.run("./calBmi/CalculBmi17.py", check=True)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def calculB18(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.run("./calBmi/CalculBmi18.py", check=True)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def calculB19(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.run("./calBmi/CalculBmi19.py", check=True)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def calculB20(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.run("./calBmi/CalculBmi20.py", check=True)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def calculB21(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.run("./calBmi/CalculBmi21.py", check=True)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def calculB22(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.run("./calBmi/CalculBmi22.py", check=True)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def calculB23(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.run("./calBmi/CalculBmi23.py", check=True)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def calculB24(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.run("./calBmi/CalculBmi24.py", check=True)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    # Func Visit MED
    def visitMed(self):
        medownload1()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient1.py", check=True)
        self.master.deiconify()

    def visitMed2(self):
        medownload2()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient2.py", check=True)
        self.master.deiconify()

    def visitMed3(self):
        medownload3()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient3.py", check=True)
        self.master.deiconify()

    def visitMed4(self):
        medownload4()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient4.py", check=True)
        self.master.deiconify()

    def visitMed5(self):
        medownload5()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient5.py", check=True)
        self.master.deiconify()

    def visitMed6(self):
        medownload6()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient6.py", check=True)
        self.master.deiconify()

    def visitMed7(self):
        medownload7()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient7.py", check=True)
        self.master.deiconify()

    def visitMed8(self):
        medownload8()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient8.py", check=True)
        self.master.deiconify()

    def visitMed9(self):
        medownload9()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient9.py", check=True)
        self.master.deiconify()

    def visitMed10(self):
        medownload10()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient10.py", check=True)
        self.master.deiconify()

    def visitMed11(self):
        medownload11()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient11.py", check=True)
        self.master.deiconify()

    def visitMed12(self):
        medownload12()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient12.py", check=True)
        self.master.deiconify()

    def visitMed13(self):
        medownload13()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient13.py", check=True)
        self.master.deiconify()

    def visitMed14(self):
        medownload14()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient14.py", check=True)
        self.master.deiconify()

    def visitMed15(self):
        medownload15()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient15.py", check=True)
        self.master.deiconify()

    def visitMed16(self):
        medownload16()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient16.py", check=True)
        self.master.deiconify()

    def visitMed17(self):
        medownload17()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient17.py", check=True)
        self.master.deiconify()

    def visitMed18(self):
        medownload18()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient18.py", check=True)
        self.master.deiconify()

    def visitMed19(self):
        medownload19()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient19.py", check=True)
        self.master.deiconify()

    def visitMed20(self):
        medownload20()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient20.py", check=True)
        self.master.deiconify()

    def visitMed21(self):
        medownload21()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient21.py", check=True)
        self.master.deiconify()

    def visitMed22(self):
        medownload22()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient22.py", check=True)
        self.master.deiconify()

    def visitMed23(self):
        medownload23()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient23.py", check=True)
        self.master.deiconify()

    def visitMed24(self):
        medownload24()
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient24.py", check=True)
        self.master.deiconify()

    def updateLink(self):
        """
            To update data for patient
            in txt entryfile and for DB.
        """
        subprocess.Popen('./update/updatepatient1.py', shell=True)

    def updateLink2(self):
        subprocess.Popen('./update/updatepatient2.py', shell=True)

    def updateLink3(self):
        subprocess.Popen('./update/updatepatient3.py', shell=True)

    def updateLink4(self):
        subprocess.Popen('./update/updatepatient4.py', shell=True)

    def updateLink5(self):
        subprocess.Popen('./update/updatepatient5.py', shell=True)

    def updateLink6(self):
        subprocess.Popen('./update/updatepatient6.py', shell=True)

    def updateLink7(self):
        subprocess.Popen('./update/updatepatient7.py', shell=True)

    def updateLink8(self):
        subprocess.Popen('./update/updatepatient8.py', shell=True)

    def updateLink9(self):
        subprocess.Popen('./update/updatepatient9.py', shell=True)

    def updateLink10(self):
        subprocess.Popen('./update/updatepatient10.py', shell=True)

    def updateLink11(self):
        subprocess.Popen('./update/updatepatient11.py', shell=True)

    def updateLink12(self):
        subprocess.Popen('./update/updatepatient12.py', shell=True)

    def updateLink13(self):
        subprocess.Popen('./update/updatepatient13.py', shell=True)

    def updateLink14(self):
        subprocess.Popen('./update/updatepatient14.py', shell=True)

    def updateLink15(self):
        subprocess.Popen('./update/updatepatient15.py', shell=True)

    def updateLink16(self):
        subprocess.Popen('./update/updatepatient16.py', shell=True)

    def updateLink17(self):
        subprocess.Popen('./update/updatepatient17.py', shell=True)

    def updateLink18(self):
        subprocess.Popen('./update/updatepatient18.py', shell=True)

    def updateLink19(self):
        subprocess.Popen('./update/updatepatient19.py', shell=True)

    def updateLink20(self):
        subprocess.Popen('./update/updatepatient20.py', shell=True)

    def updateLink21(self):
        subprocess.Popen('./update/updatepatient21.py', shell=True)

    def updateLink22(self):
        subprocess.Popen('./update/updatepatient22.py', shell=True)

    def updateLink23(self):
        subprocess.Popen('./update/updatepatient23.py', shell=True)

    def updateLink24(self):
        subprocess.Popen('./update/updatepatient24.py', shell=True)

    # Menu print
    def nutritionMenu(self):
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient1.py', check=True)
        self.master.deiconify()

    def nutritionMenu2(self):
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient2.py', check=True)
        self.master.deiconify()

    def nutritionMenu3(self):
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient3.py', check=True)
        self.master.deiconify()

    def nutritionMenu4(self):
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient4.py', check=True)
        self.master.deiconify()

    def nutritionMenu5(self):
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient5.py', check=True)
        self.master.deiconify()

    def nutritionMenu6(self):
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient6.py', check=True)
        self.master.deiconify()

    def nutritionMenu7(self):
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient7.py', check=True)
        self.master.deiconify()

    def nutritionMenu8(self):
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient8.py', check=True)
        self.master.deiconify()

    def nutritionMenu9(self):
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient9.py', check=True)
        self.master.deiconify()

    def nutritionMenu10(self):
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient10.py', check=True)
        self.master.deiconify()

    def nutritionMenu11(self):
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient11.py', check=True)
        self.master.deiconify()

    def nutritionMenu12(self):
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient12.py', check=True)
        self.master.deiconify()

    def nutritionMenu13(self):
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient13.py', check=True)
        self.master.deiconify()

    def nutritionMenu14(self):
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient14.py', check=True)
        self.master.deiconify()

    def nutritionMenu15(self):
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient15.py', check=True)
        self.master.deiconify()

    def nutritionMenu16(self):
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient16.py', check=True)
        self.master.deiconify()

    def nutritionMenu17(self):
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient17.py', check=True)
        self.master.deiconify()

    def nutritionMenu18(self):
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient18.py', check=True)
        self.master.deiconify()

    def nutritionMenu19(self):
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient19.py', check=True)
        self.master.deiconify()

    def nutritionMenu20(self):
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient20.py', check=True)
        self.master.deiconify()

    def nutritionMenu21(self):
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient21.py', check=True)
        self.master.deiconify()

    def nutritionMenu22(self):
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient22.py', check=True)
        self.master.deiconify()

    def nutritionMenu23(self):
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient23.py', check=True)
        self.master.deiconify()

    def nutritionMenu24(self):
        self.master.withdraw()
        subprocess.run('./nutrition/nutrit_patient24.py', check=True)
        self.master.deiconify()

    # To acces files into Backup folder
    def allFilesBackup(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        backupFuncPatient(self)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def allFilesBackup2(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        backupFuncPatient2(self)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def allFilesBackup3(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        backupFuncPatient3(self)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def allFilesBackup4(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        backupFuncPatient4(self)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def allFilesBackup5(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        backupFuncPatient5(self)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def allFilesBackup6(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        backupFuncPatient6(self)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def allFilesBackup7(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        backupFuncPatient7(self)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def allFilesBackup8(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        backupFuncPatient8(self)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def allFilesBackup9(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        backupFuncPatient9(self)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def allFilesBackup10(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        backupFuncPatient10(self)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def allFilesBackup11(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        backupFuncPatient11(self)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def allFilesBackup12(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        backupFuncPatient12(self)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def allFilesBackup13(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        backupFuncPatient13(self)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def allFilesBackup14(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        backupFuncPatient14(self)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def allFilesBackup15(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        backupFuncPatient15(self)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def allFilesBackup16(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        backupFuncPatient16(self)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def allFilesBackup17(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        backupFuncPatient17(self)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def allFilesBackup18(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        backupFuncPatient18(self)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def allFilesBackup19(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        backupFuncPatient19(self)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def allFilesBackup20(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        backupFuncPatient20(self)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def allFilesBackup21(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        backupFuncPatient21(self)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def allFilesBackup22(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        backupFuncPatient22(self)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def allFilesBackup23(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        backupFuncPatient23(self)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def allFilesBackup24(self):
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        backupFuncPatient24(self)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def updateFiletxt(self):
        """
            It's time to backup !
        """
        dataBackToSave(self)
        paramBackToSave(self)
        bmiBackToSave(self)

    def upDateAll(self):
        """
            To reset app by pressing
            refresh button. Close,
            open directly and update
            data from patcaps.py !
        """
        try:
            if self._job is not None:
                self.clock_label.after_cancel(self._job)
                self._job = None
                self.master.destroy()
                Application.__init__(self)
                self.showPatients()
        except (OSError, ValueError) as p_out:
            print("Error with refresh...", p_out)

if __name__=='__main__':
    app = Application()
    app.mainloop()
