#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
from tkinter import messagebox
import time
import datetime as dt
import subprocess
from contact.pat_contact1 import Window
from contact.doc_contact1 import doctorWind
from contact.family_contact1 import famWind
from contact.hcs_contact1 import homecsWind
from boxapp import callBox
from patcaps import callResident
from backapp import *
from Backup.backupfile import dataBackToSave
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
#import passw


class ScrollCanvas(Frame):
    """
        To prepare ScrollBar for main application.
    """
    def __init__(self, boss=None):
        Frame.__init__(self, borderwidth=borderwidth, relief=relief)
        self.can = Canvas(self, width=width, height=height, bd=bd,
            bg=bg, relief=relief)
        self.frame = Frame(self.can)
        self.vsb = Scrollbar(self, orient=VERTICAL, command=self.can.yview)
        self.can.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side=RIGHT, fill=Y)
        self.can.pack(side=LEFT, fill=BOTH, expand=YES)
        self.can.create_window((4,4), window=self.frame, anchor=NW,
                                  tags="self.frame")
        self.frame.bind("<Configure>", self.onFrameConfigure)

class MenuBar(Frame):
    """
        Wrapp down
    """
    def __init__(self, boss=None):
        Frame.__init__(self, borderwidth=5, bg='RoyalBlue3', padx=0)
        # 1st menu
        fileMenu = Menubutton(self, text='Menu', fg='white',
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
        except FileNotFoundError as fileout:
            print("No file entryfile.txt exist", fileout)

        try:
            with open('./newpatient/entryfile2.txt', 'r') as namefile2:
                line2 = namefile2.readline()
                new_text2 = line2
        except FileNotFoundError as fileout2:
            print("No file entryfile2.txt exist", fileout2)

        try:
            with open('./newpatient/entryfile3.txt', 'r') as namefile3:
                line3 = namefile3.readline()
                new_text3 = line3
        except FileNotFoundError as fileout3:
            print("No file entryfile3.txt exist", fileout3)

        try:
            with open('./newpatient/entryfile4.txt', 'r') as namefile4:
                line4 = namefile4.readline()
                new_text4 = line4
        except FileNotFoundError as fileout4:
            print("No file entryfile4.txt exist", fileout4)

        try:
            with open('./newpatient/entryfile5.txt', 'r') as namefile5:
                line5 = namefile5.readline()
                new_text5 = line5
        except FileNotFoundError as fileout5:
            print("No file entryfile5.txt exist", fileout5)

        try:
            with open('./newpatient/entryfile6.txt', 'r') as namefile6:
                line6 = namefile6.readline()
                new_text6 = line6
        except FileNotFoundError as fileout6:
            print("No file entryfile6.txt exist", fileout6)

        try:
            with open('./newpatient/entryfile7.txt', 'r') as namefile7:
                line7 = namefile7.readline()
                new_text7 = line7
        except FileNotFoundError as fileout7:
            print("No file entryfile7.txt exist", fileout7)

        try:
            with open('./newpatient/entryfile8.txt', 'r') as namefile8:
                line8 = namefile8.readline()
                new_text8 = line8
        except FileNotFoundError as fileout8:
            print("No file entryfile8.txt exist", fileout8)

        try:
            with open('./newpatient/entryfile9.txt', 'r') as namefile9:
                line9 = namefile9.readline()
                new_text9 = line9
        except FileNotFoundError as fileout9:
            print("No file entryfile9.txt exist", fileout9)

        try:
            with open('./newpatient/entryfile10.txt', 'r') as namefile10:
                line10 = namefile10.readline()
                new_text10 = line10
        except FileNotFoundError as fileout10:
            print("No file entryfile10.txt exist", fileout10)

        try:
            with open('./newpatient/entryfile11.txt', 'r') as namefile11:
                line11 = namefile11.readline()
                new_text11 = line11
        except FileNotFoundError as fileout11:
            print("No file entryfile11.txt exist", fileout11)

        try:
            with open('./newpatient/entryfile12.txt', 'r') as namefile12:
                line12 = namefile12.readline()
                new_text12 = line12
        except FileNotFoundError as fileout12:
            print("No file entryfile12.txt exist", fileout12)

        try:
            with open('./newpatient/entryfile13.txt', 'r') as namefile13:
                line13 = namefile13.readline()
                new_text13 = line13
        except FileNotFoundError as fileout13:
            print("No file entryfile13.txt exist", fileout13)

        try:
            with open('./newpatient/entryfile14.txt', 'r') as namefile14:
                line14 = namefile14.readline()
                new_text14 = line14
        except FileNotFoundError as fileout14:
            print("No file entryfile14.txt exist", fileout14)

        try:
            with open('./newpatient/entryfile15.txt', 'r') as namefile15:
                line15 = namefile15.readline()
                new_text15 = line15
        except FileNotFoundError as fileout15:
            print("No file entryfile15.txt exist", fileout15)

        try:
            with open('./newpatient/entryfile16.txt', 'r') as namefile16:
                line16 = namefile16.readline()
                new_text16 = line16
        except FileNotFoundError as fileout16:
            print("No file entryfile16.txt exist", fileout16)

        try:
            with open('./newpatient/entryfile17.txt', 'r') as namefile17:
                line17 = namefile17.readline()
                new_text17 = line17
        except FileNotFoundError as fileout17:
            print("No file entryfile17.txt exist", fileout17)

        try:
            with open('./newpatient/entryfile18.txt', 'r') as namefile18:
                line18 = namefile18.readline()
                new_text18 = line18
        except FileNotFoundError as fileout18:
            print("No file entryfile18.txt exist", fileout18)

        try:
            with open('./newpatient/entryfile19.txt', 'r') as namefile19:
                line19 = namefile19.readline()
                new_text19 = line19
        except FileNotFoundError as fileout19:
            print("No file entryfile19.txt exist", fileout19)

        try:
            with open('./newpatient/entryfile20.txt', 'r') as namefile20:
                line20 = namefile20.readline()
                new_text20 = line20
        except FileNotFoundError as fileout20:
            print("No file entryfile20.txt exist", fileout20)

        try:
            with open('./newpatient/entryfile21.txt', 'r') as namefile21:
                line21 = namefile21.readline()
                new_text21 = line21
        except FileNotFoundError as fileout21:
            print("No file entryfile21.txt exist", fileout21)

        try:
            with open('./newpatient/entryfile22.txt', 'r') as namefile22:
                line22 = namefile22.readline()
                new_text22 = line22
        except FileNotFoundError as fileout22:
            print("No file entryfile22.txt exist", fileout22)

        try:
            with open('./newpatient/entryfile23.txt', 'r') as namefile23:
                line23 = namefile23.readline()
                new_text23 = line23
        except FileNotFoundError as fileout23:
            print("No file entryfile23.txt exist", fileout23)

        try:
            with open('./newpatient/entryfile24.txt', 'r') as namefile24:
                line24 = namefile24.readline()
                new_text24 = line24
        except FileNotFoundError as fileout24:
            print("No file entryfile24.txt exist", fileout24)

        fileMenu.pack(side=LEFT, padx=3)
        # Partie déroulante du menu 1st
        me1 = Menu(fileMenu, tearoff=0)
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
            foreground='red', activeforeground='white',
            command=boss.msgExit)
        # Integration of 1st menu
        fileMenu.configure(activeforeground='black', activebackground='cyan',
            menu=me1)

        # Agenda menu
        cmd_agenda = Menubutton(self, text='Agenda', font=("Times 14"),
            fg='cyan', bg='grey30', relief=GROOVE)
        cmd_agenda.pack(side=LEFT, padx=3)
        me3 = Menu(cmd_agenda)
        # Partie déroulante du menu agenda
        me3.add_command(label=new_text[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda)
        me3.add_command(label=new_text2[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda2)
        me3.add_command(label=new_text3[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda3)
        me3.add_command(label=new_text4[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda4)
        me3.add_command(label=new_text5[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda5)
        me3.add_command(label=new_text6[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda6)
        me3.add_command(label=new_text7[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda7)
        me3.add_command(label=new_text8[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda8)
        me3.add_command(label=new_text9[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda9)
        me3.add_command(label=new_text10[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda10)
        me3.add_command(label=new_text11[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda11)
        me3.add_command(label=new_text12[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda12)
        me3.add_command(label=new_text13[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda13)
        me3.add_command(label=new_text14[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda14)
        me3.add_command(label=new_text15[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda15)
        me3.add_command(label=new_text16[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda16)
        me3.add_command(label=new_text17[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda17)
        me3.add_command(label=new_text18[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda18)
        me3.add_command(label=new_text19[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda19)
        me3.add_command(label=new_text20[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda20)
        me3.add_command(label=new_text21[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda21)
        me3.add_command(label=new_text22[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda22)
        me3.add_command(label=new_text23[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda23)
        me3.add_command(label=new_text24[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda24)
        # Integration of agenda menu
        cmd_agenda.configure(activeforeground='black', activebackground='cyan',
            menu=me3)

        # Contact menu
        contact = Menubutton(self, text='Contacts', font=("Times 14"),
            fg='cyan', bg='grey30', relief=GROOVE)
        contact.pack(side=LEFT, padx=3)
        contchck = Menu(contact)
        me1 = Menu(contchck)
        me1.add_command(label='Patient', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num1)
        me1.add_command(label='Familiy', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactfamily_1)
        me1.add_command(label='Doctor', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contactdoctor_1)
        me1.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contacthcsystem_1)
        contchck.add_cascade(label=new_text[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me1)
        me2 = Menu(contchck)
        me2.add_command(label='Patient', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num2)
        me2.add_command(label='Familiy', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num2)
        me2.add_command(label='Doctor', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num2)
        me2.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num2)
        contchck.add_cascade(label=new_text2[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me2)
        me3 = Menu(contchck)
        me3.add_command(label='Patient', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num3)
        me3.add_command(label='Familiy', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num3)
        me3.add_command(label='Doctor', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num3)
        me3.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num3)
        contchck.add_cascade(label=new_text3[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me3)
        me4 = Menu(contchck)
        me4.add_command(label='Patient', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num4)
        me4.add_command(label='Familiy', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num4)
        me4.add_command(label='Doctor', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num4)
        me4.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num4)
        contchck.add_cascade(label=new_text4[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me4)
        me5 = Menu(contchck)
        me5.add_command(label='Patient', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num5)
        me5.add_command(label='Familiy', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num5)
        me5.add_command(label='Doctor', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num5)
        me5.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num5)
        contchck.add_cascade(label=new_text5[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me5)
        me6 = Menu(contchck)
        me6.add_command(label='Patient', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num6)
        me6.add_command(label='Familiy', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num6)
        me6.add_command(label='Doctor', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num6)
        me6.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num6)
        contchck.add_cascade(label=new_text6[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me6)
        me7 = Menu(contchck)
        me7.add_command(label='Patient', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num7)
        me7.add_command(label='Familiy', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num7)
        me7.add_command(label='Doctor', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num7)
        me7.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num7)
        contchck.add_cascade(label=new_text7[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me7)
        me8 = Menu(contchck)
        me8.add_command(label='Patient', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num8)
        me8.add_command(label='Familiy', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num8)
        me8.add_command(label='Doctor', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num8)
        me8.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num8)
        contchck.add_cascade(label=new_text8[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me8)
        me9 = Menu(contchck)
        me9.add_command(label='Patient', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num9)
        me9.add_command(label='Familiy', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num9)
        me9.add_command(label='Doctor', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num9)
        me9.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num9)
        contchck.add_cascade(label=new_text9[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me9)
        me10 = Menu(contchck)
        me10.add_command(label='Patient', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num10)
        me10.add_command(label='Familiy', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num10)
        me10.add_command(label='Doctor', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num10)
        me10.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num10)
        contchck.add_cascade(label=new_text10[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me10)
        me11 = Menu(contchck)
        me11.add_command(label='Patient', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num11)
        me11.add_command(label='Familiy', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num11)
        me11.add_command(label='Doctor', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num11)
        me11.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num11)
        contchck.add_cascade(label=new_text11[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me11)
        me12 = Menu(contchck)
        me12.add_command(label='Patient', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num12)
        me12.add_command(label='Familiy', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num12)
        me12.add_command(label='Doctor', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num12)
        me12.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num12)
        contchck.add_cascade(label=new_text12[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me12)
        me13 = Menu(contchck)
        me13.add_command(label='Patient', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num13)
        me13.add_command(label='Familiy', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num13)
        me13.add_command(label='Doctor', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num13)
        me13.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num13)
        contchck.add_cascade(label=new_text13[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me13)
        me14 = Menu(contchck)
        me14.add_command(label='Patient', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num14)
        me14.add_command(label='Familiy', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num14)
        me14.add_command(label='Doctor', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num14)
        me14.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num14)
        contchck.add_cascade(label=new_text14[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me14)
        me15 = Menu(contchck)
        me15.add_command(label='Patient', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num15)
        me15.add_command(label='Familiy', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num15)
        me15.add_command(label='Doctor', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num15)
        me15.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num15)
        contchck.add_cascade(label=new_text15[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me15)
        me16 = Menu(contchck)
        me16.add_command(label='Patient', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num16)
        me16.add_command(label='Familiy', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num16)
        me16.add_command(label='Doctor', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num16)
        me16.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num16)
        contchck.add_cascade(label=new_text16[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me16)
        me17 = Menu(contchck)
        me17.add_command(label='Patient', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num17)
        me17.add_command(label='Familiy', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num17)
        me17.add_command(label='Doctor', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num17)
        me17.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num17)
        contchck.add_cascade(label=new_text17[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me17)
        me18 = Menu(contchck)
        me18.add_command(label='Patient', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num18)
        me18.add_command(label='Familiy', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num18)
        me18.add_command(label='Doctor', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num18)
        me18.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num18)
        contchck.add_cascade(label=new_text18[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me18)
        me19 = Menu(contchck)
        me19.add_command(label='Patient', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num19)
        me19.add_command(label='Familiy', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num19)
        me19.add_command(label='Doctor', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num19)
        me19.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num19)
        contchck.add_cascade(label=new_text19[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me19)
        me20 = Menu(contchck)
        me20.add_command(label='Patient', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num20)
        me20.add_command(label='Familiy', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num20)
        me20.add_command(label='Doctor', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num20)
        me20.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num20)
        contchck.add_cascade(label=new_text20[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me20)
        me21 = Menu(contchck)
        me21.add_command(label='Patient', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num21)
        me21.add_command(label='Familiy', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num21)
        me21.add_command(label='Doctor', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num21)
        me21.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num21)
        contchck.add_cascade(label=new_text21[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me21)
        me22 = Menu(contchck)
        me22.add_command(label='Patient', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num22)
        me22.add_command(label='Familiy', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num22)
        me22.add_command(label='Doctor', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num22)
        me22.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num22)
        contchck.add_cascade(label=new_text22[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me22)
        me23 = Menu(contchck)
        me23.add_command(label='Patient', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num23)
        me23.add_command(label='Familiy', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num23)
        me23.add_command(label='Doctor', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num23)
        me23.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num23)
        contchck.add_cascade(label=new_text23[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me23)
        me24 = Menu(contchck)
        me24.add_command(label='Patient', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num24)
        me24.add_command(label='Familiy', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num24)
        me24.add_command(label='Doctor', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num24)
        me24.add_command(label='Home care system', font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.contact_num24)
        contchck.add_cascade(label=new_text24[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me24)
        contact.configure(activeforeground='black', activebackground='cyan', menu=contchck)

        # 14 besoins menu
        cmd_Besoins = Menubutton(self, text='14 Needs', font=("Times 14"),
            fg='cyan', bg='grey30', relief=GROOVE)
        cmd_Besoins.pack(side=LEFT, padx=3)
        # Partie déroulante du menu 14b
        me4 = Menu(cmd_Besoins)
        me4.add_command(label=new_text[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoinsCoche)
        #me4.add_separator()
        me4.add_command(label=new_text2[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins2Coche)
        #me4.add_separator()
        me4.add_command(label=new_text3[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins3Coche)
        #me4.add_separator()
        me4.add_command(label=new_text4[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins4Coche)
        #me4.add_separator()
        me4.add_command(label=new_text5[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins5Coche)
        #me4.add_separator()
        me4.add_command(label=new_text6[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins6Coche)
        #me4.add_separator()
        me4.add_command(label=new_text7[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins7Coche)
        #me4.add_separator()
        me4.add_command(label=new_text8[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins8Coche)
        #me4.add_separator()
        me4.add_command(label=new_text9[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins9Coche)
        #me4.add_separator()
        me4.add_command(label=new_text10[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins10Coche)
        #me4.add_separator()
        me4.add_command(label=new_text11[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins11Coche)
        #me4.add_separator()
        me4.add_command(label=new_text12[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins12Coche)
        #me4.add_separator()
        me4.add_command(label=new_text13[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins13Coche)
        #me4.add_separator()
        me4.add_command(label=new_text14[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins14Coche)
        #me4.add_separator()
        me4.add_command(label=new_text15[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins15Coche)
        #me4.add_separator()
        me4.add_command(label=new_text16[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins16Coche)
        #me4.add_separator()
        me4.add_command(label=new_text17[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins17Coche)
        #me4.add_separator()
        me4.add_command(label=new_text18[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins18Coche)
        #me4.add_separator()
        me4.add_command(label=new_text19[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins19Coche)
        #me4.add_separator()
        me4.add_command(label=new_text20[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins20Coche)
        #me4.add_separator()
        me4.add_command(label=new_text21[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins21Coche)
        #me4.add_separator()
        me4.add_command(label=new_text22[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins22Coche)
        #me4.add_separator()
        me4.add_command(label=new_text23[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins23Coche)
        #me4.add_separator()
        me4.add_command(label=new_text24[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins24Coche)
        # Integration of 14b menu
        cmd_Besoins.configure(activeforeground='black', activebackground='cyan',
            menu=me4)

        # Helth and care menu
        cmd_Soins = Menubutton(self, text='Care and monitoring', font=("Times 14"),
            fg='cyan', bg='grey30', relief=GROOVE)
        cmd_Soins.pack(side=LEFT, padx=3)
        # Partie déroulante du menu health and care
        meSoins = Menu(cmd_Soins)
        meSoins.add_command(label=new_text[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins1)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text2[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins2)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text3[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins3)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text4[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins4)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text5[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins5)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text6[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins6)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text7[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins7)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text8[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins8)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text9[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins9)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text10[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins10)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text11[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins11)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text12[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins12)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text13[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins13)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text14[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins14)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text15[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins15)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text16[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins16)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text17[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins17)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text18[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins18)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text19[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins19)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text20[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins20)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text21[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins21)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text22[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins22)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text23[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins23)
        #meSoins.add_separator()
        meSoins.add_command(label=new_text24[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins24)
        # Integration of health and care menu
        cmd_Soins.configure(activeforeground='black', activebackground='cyan',
            menu=meSoins)

        # Treatments
        cmd_ttt = Menubutton(self, text='Treatments', font=("Times 14"),
            fg='cyan', bg='grey30', relief=GROOVE)
        cmd_ttt.pack(side=LEFT, padx=3)
        # Partie déroulante du menu health and care
        meTtt = Menu(cmd_ttt)
        meTtt.add_command(label=new_text[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed1)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text2[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed2)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text3[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed3)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text4[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed4)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text5[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed5)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text6[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed6)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text7[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed7)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text8[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed8)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text9[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed9)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text10[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed10)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text11[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed11)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text12[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed12)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text13[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed13)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text14[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed14)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text15[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed15)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text16[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed16)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text17[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed17)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text18[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed18)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text19[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed19)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text20[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed20)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text21[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed21)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text22[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed22)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text23[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed23)
        #meTtt.add_separator()
        meTtt.add_command(label=new_text24[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed24)
        # Integration of health and care menu
        cmd_ttt.configure(activeforeground='black', activebackground='cyan',
            menu=meTtt)

        # BMI menu
        cmd_BMI = Menubutton(self, text='Body Mass Indice', font=("Times 14"),
            fg='cyan', bg='grey30', relief=GROOVE)
        cmd_BMI.pack(side=LEFT, padx=3)
        # drop-down portion of BMI menu
        meBmi = Menu(cmd_BMI)
        meBmi.add_command(label=new_text[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB)
        meBmi.add_command(label=new_text2[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB2)
        meBmi.add_command(label=new_text3[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB3)
        meBmi.add_command(label=new_text4[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB4)
        meBmi.add_command(label=new_text5[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB5)
        meBmi.add_command(label=new_text6[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB6)
        meBmi.add_command(label=new_text7[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB7)
        meBmi.add_command(label=new_text8[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB8)
        meBmi.add_command(label=new_text9[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB9)
        meBmi.add_command(label=new_text10[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB10)
        meBmi.add_command(label=new_text11[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB11)
        meBmi.add_command(label=new_text12[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB12)
        meBmi.add_command(label=new_text13[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB13)
        meBmi.add_command(label=new_text14[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB14)
        meBmi.add_command(label=new_text15[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB15)
        meBmi.add_command(label=new_text16[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB16)
        meBmi.add_command(label=new_text17[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB17)
        meBmi.add_command(label=new_text18[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB18)
        meBmi.add_command(label=new_text19[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB19)
        meBmi.add_command(label=new_text20[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB20)
        meBmi.add_command(label=new_text21[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB21)
        meBmi.add_command(label=new_text22[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB22)
        meBmi.add_command(label=new_text23[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB23)
        meBmi.add_command(label=new_text24[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB24)
        # Integration of 3rd menu
        cmd_BMI.configure(activeforeground='black', activebackground='cyan',
            menu=meBmi)

        # Medical Visite
        cmd_Vmed = Menubutton(self, text='Medical Visit', font=("Times 14"),
            fg='cyan', bg='grey30', relief=GROOVE)
        cmd_Vmed.pack(side=LEFT, padx=3)
        # drop-down portion of vmed
        meVmed = Menu(cmd_Vmed)
        meVmed.add_command(label=new_text[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed)
        meVmed.add_command(label=new_text2[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed2)
        meVmed.add_command(label=new_text3[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed3)
        meVmed.add_command(label=new_text4[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed4)
        meVmed.add_command(label=new_text5[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed5)
        meVmed.add_command(label=new_text6[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed6)
        meVmed.add_command(label=new_text7[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed7)
        meVmed.add_command(label=new_text8[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed8)
        meVmed.add_command(label=new_text9[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed9)
        meVmed.add_command(label=new_text10[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed10)
        meVmed.add_command(label=new_text11[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed11)
        meVmed.add_command(label=new_text12[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed12)
        meVmed.add_command(label=new_text13[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed13)
        meVmed.add_command(label=new_text14[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed14)
        meVmed.add_command(label=new_text15[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed15)
        meVmed.add_command(label=new_text16[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed16)
        meVmed.add_command(label=new_text17[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed17)
        meVmed.add_command(label=new_text18[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed18)
        meVmed.add_command(label=new_text19[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed19)
        meVmed.add_command(label=new_text20[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed20)
        meVmed.add_command(label=new_text21[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed21)
        meVmed.add_command(label=new_text22[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed22)
        meVmed.add_command(label=new_text23[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed23)
        meVmed.add_command(label=new_text24[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed24)
        # Integration of 3rd menu
        cmd_Vmed.configure(activeforeground='black', activebackground='cyan',
            menu=meVmed)

        # Nutrition menu for intolerance and hate meals
        cmd_Print = Menubutton(self, text='Intolerance All.', font=("Times 14"),
            fg='cyan', bg='grey30', relief=GROOVE)
        cmd_Print.pack(side=LEFT, padx=3)
        # drop-down portion of nutrition
        mePrint = Menu(cmd_Print)
        mePrint.add_command(label=new_text[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu)
        mePrint.add_command(label=new_text2[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu2)
        mePrint.add_command(label=new_text3[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu3)
        mePrint.add_command(label=new_text4[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu4)
        mePrint.add_command(label=new_text5[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu5)
        mePrint.add_command(label=new_text6[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu6)
        mePrint.add_command(label=new_text7[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu7)
        mePrint.add_command(label=new_text8[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu8)
        mePrint.add_command(label=new_text9[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu9)
        mePrint.add_command(label=new_text10[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu10)
        mePrint.add_command(label=new_text11[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu11)
        mePrint.add_command(label=new_text12[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu12)
        mePrint.add_command(label=new_text13[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu13)
        mePrint.add_command(label=new_text14[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu14)
        mePrint.add_command(label=new_text15[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu15)
        mePrint.add_command(label=new_text16[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu16)
        mePrint.add_command(label=new_text17[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu17)
        mePrint.add_command(label=new_text18[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu18)
        mePrint.add_command(label=new_text19[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu19)
        mePrint.add_command(label=new_text20[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu20)
        mePrint.add_command(label=new_text21[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu21)
        mePrint.add_command(label=new_text22[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu22)
        mePrint.add_command(label=new_text23[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu23)
        mePrint.add_command(label=new_text24[:-1], font=('Times 12'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu24)
        # Integration of nutrition menu
        cmd_Print.configure(activeforeground='black', activebackground='cyan',
            menu=mePrint)

        # Menu for showing all Graphs togather per patient
        cmd_backup=Menubutton(self, text='Global', font=("Times 14"), fg='cyan',
            bg='grey30', relief=GROOVE)
        cmd_backup.pack(side=LEFT, padx=3)
        # drop-down portion of Graphics menu
        me1 = Menu(cmd_backup)
        me2 = Menu(me1)
        me2.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup)
        me1.add_cascade(label=new_text[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me2)
        me3=Menu(me1)
        me3.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup2)
        me1.add_cascade(label=new_text2[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me3)
        me4=Menu(me1)
        me4.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup3)
        me1.add_cascade(label=new_text3[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me4)
        me5=Menu(me1)
        me5.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup4)
        me1.add_cascade(label=new_text4[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me5)
        me6=Menu(me1)
        me6.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup5)
        me1.add_cascade(label=new_text5[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me6)
        me7=Menu(me1)
        me7.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup6)
        me1.add_cascade(label=new_text6[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me7)
        me8=Menu(me1)
        me8.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup7)
        # Integration of sub-menu
        me1.add_cascade(label=new_text7[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me8)
        me9=Menu(me1)
        me9.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup8)
        # Integration of sub-menu
        me1.add_cascade(label=new_text8[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me9)
        me10=Menu(me1)
        me10.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup9)
        # Integration of sub-menu
        me1.add_cascade(label=new_text9[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me10)
        me11=Menu(me1)
        me11.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup10)
        # Integration of sub-menu
        me1.add_cascade(label=new_text10[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me11)
        me12=Menu(me1)
        me12.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup11)
        # Integration of sub-menu
        me1.add_cascade(label=new_text11[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me12)
        me13=Menu(me1)
        me13.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup12)
        # Integration of sub-menu
        me1.add_cascade(label=new_text12[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me13)
        me14=Menu(me1)
        me14.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup13)
        # Integration of sub-menu
        me1.add_cascade(label=new_text13[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me14)
        me15=Menu(me1)
        me15.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup14)
        # Integration of sub-menu
        me1.add_cascade(label=new_text14[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me15)
        me16=Menu(me1)
        me16.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup15)
        # Integration of sub-menu
        me1.add_cascade(label=new_text15[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me16)
        me17=Menu(me1)
        me17.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup16)
        # Integration of sub-menu
        me1.add_cascade(label=new_text16[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me17)
        me18=Menu(me1)
        me18.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup17)
        # Integration of sub-menu
        me1.add_cascade(label=new_text17[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me18)
        me19=Menu(me1)
        me19.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup18)
        # Integration of sub-menu
        me1.add_cascade(label=new_text18[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me19)
        me20=Menu(me1)
        me20.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup19)
        # Integration of sub-menu
        me1.add_cascade(label=new_text19[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me20)
        me21=Menu(me1)
        me21.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup20)
        # Integration of sub-menu
        me1.add_cascade(label=new_text20[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me21)
        me22=Menu(me1)
        me22.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup21)
        # Integration of sub-menu
        me1.add_cascade(label=new_text21[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me22)
        me23=Menu(me1)
        me23.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup22)
        # Integration of sub-menu
        me1.add_cascade(label=new_text22[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me23)
        me24=Menu(me1)
        me24.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup23)
        # Integration of sub-menu
        me1.add_cascade(label=new_text23[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me24)
        me25=Menu(me1)
        me25.add_command(label='All Files.txt', underline=0, font=('Times 12'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup24)
        # Integration of sub-menu
        me1.add_cascade(label=new_text24[:-1], underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me25)
        # Integration of Graph menu
        cmd_backup.configure(activeforeground='black', activebackground='cyan', menu=me1)

# Application principale (Main app)
class Application(Frame):
    """
        Main app to display first page.
    """
    def __init__(self, boss=None):
        Frame.__init__(self, borderwidth=5, bg='RoyalBlue4', padx=20, pady=20, relief=GROOVE)
        self.master.title('Time-Track Developed by ko@l@tr33 - 2020')
        self.master.resizable(False, False)
        print(self.master.winfo_screenheight())
        print(self.master.winfo_screenwidth())
        #size_h=1050
        #size_w=1680
        self.window_height = 824
        self.window_width = 1310

        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()

        self.x_cordinate = int((self.screen_width/2) - (self.window_width/2))
        self.y_cordinate = int((self.screen_height/2) - (self.window_height/2))

        self.master.geometry("{}x{}+{}+{}".format(self.window_width, self.window_height,
            self.x_cordinate, self.y_cordinate))
        print(self.x_cordinate)
        print(self.y_cordinate)

        self.mBar = MenuBar(self)
        self.mBar.pack(side=TOP, fill=X, expand=YES)

        self.can = Canvas(self, width=1250, height=700, bg='black')
        self.frame = Frame(self.can)
        # ScrollCanvas limite de la zone à parcourir avec la barre 1250 - 700
        self.vsb = Scrollbar(self, orient=VERTICAL, command=self.can.yview)
        self.can.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side=RIGHT, fill=Y)
        self.can.create_window((4,4), window=self.frame, anchor=NW, tags="self.frame")
        self.clock_label = Label(self, text="",
            fg="white", bg="RoyalBlue3", font=("helvetica", 18, 'bold'))
        #self.clock_label = Label(self, text="", font=('Times New Roman', 18, 'bold'),
        #    fg='snow', bg='RoyalBlue3', padx=560)
        self.clock_label.after(200, self.tick)
        self.clock_label.pack(side=TOP, fill=X, expand=YES)
        # Read python - tkinter - self.master.Tk.call(func()) in effbot

        # Insertion of picture
        self.photo = PhotoImage(file='./syno_gif/fondcolorbg4.png')
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
        self.button1 = Button(self, text="Info", font=('Times 14 bold'),
            bg='grey17', fg='cyan', command = self.frameInfo)
        self.button1.configure(width=10, bd=3, highlightbackground='grey10',
            activebackground='pale turquoise')
        self.button1_window = self.can.create_window(75, 30, anchor=CENTER,
            window=self.button1)
        # Pycon button
        self.button2 = Button(self, text="DATABASE", font=('Times 18 bold'),
            bg='RoyalBlue3', fg='white', command = self.funcPyCon)
        self.button2.configure(width=15, bd=3, highlightbackground='RoyalBlue4',
            activebackground='pale turquoise')
        self.button2_window = self.can.create_window(300, 450, anchor=CENTER,
            window=self.button2)
        # Synopsis button
        self.button3 = Button(self, text="TEXTBOX", font=('Times 18 bold'),
            bg='RoyalBlue3', fg='white', command = self.showSynopsis)
        self.button3.configure(width=15, bd=3, highlightbackground='RoyalBlue4',
            activebackground='pale turquoise')
        self.button3_window = self.can.create_window(625, 450, anchor=CENTER,
            window=self.button3)
        # Psychotabs button
        self.button4 = Button(self, text="RESIDENTS", font=('Times 18 bold'),
            bg='RoyalBlue3', fg='white', command = self.showPatients)
        self.button4.configure(width=15, bd=3, highlightbackground='RoyalBlue4',
            activebackground='pale turquoise')
        self.button4_window = self.can.create_window(950, 450, anchor=CENTER,
            window=self.button4)

        self.pack()

    # Method to reconfigure scrollbar every time.
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.can.configure(scrollregion=self.can.bbox(ALL))

    def effacer(self):
        '''Reinitialize canvas when we pass through another'''
        self.can.delete(ALL)

    def tick(self):
        """ Updates the display clock every 200 milliseconds """
        new_time = time.strftime("%H:%M:%S %p")
        try:
            if new_time == new_time:
                self.time = new_time
                self.display_time = self.time
                self.clock_label.configure(text=self.display_time)
                self.clock_label.after(200, self.tick)
            else:
                print("FUCK every one !")
        except (ValueError, OSError) as val_err:
            print("Error time --> ", val_err)

    def framShow(self):
        """
            To update without
            re-enter id and passwd
        """
        try:
            self.clock_label.after(200 , self.clock_label.destroy())
            self.master.destroy()
            Application()
            #Application.__init__(self)
        except (OSError, ValueError) as two_err:
            print("OS or Val error", two_err)

    def msgExit(self):
        """
            If usr want to quit, a question
            into a msgbox appear.
        """
        try:
            MsgBox = messagebox.askyesno('Quit system', 'Do you want to quit ?')
            if MsgBox == 1:
                self.master.destroy()
        except OSError as fuckingtime:
            print("Error 2 : time to fucking time !!!", fuckingtime)

    def frameInfo(self):
        """
            Info for button on first page
        """
        self.lab=Tk()
        self.lab.title("ATCD")
        self.lab.configure(bg="grey22")

        self.labFra=LabelFrame(self.lab, text="\nWelcome !",
            font=("Arial 12"),fg='cyan', bg='grey22')
        self.labFra.pack(padx=5, pady=5)
        self.separator = Frame(self.labFra, height=2, bd=1,
            relief=SUNKEN)

        self.lab4=Label(self.labFra, text="\nInfo",
            font=('Times 16 bold'), fg='cyan', bg='grey22').pack()
        self.separator = Frame(self.labFra, height=2, bd=1, relief=SUNKEN)
        self.separator.pack(fill=X, padx=100, pady=3)

        self.lab5=Label(self.labFra, justify=LEFT, fg='cyan',
            bg='grey22', font=('Times', 14),
            text="\nMenu Bar, DB, Textbox and Residents are the most usefull skills\n"
            "to perform onto this app ! If you need help, you can go to MapApp to\n"
            "access map of this app and understand how the app is used ;)\n\n"
            "Enjoy it !\n").pack(padx=10)
        self.separator = Frame(self.labFra, height=2, bd=1, relief=SUNKEN)
        self.separator.pack(fill=X, padx=30, pady=3)
        self.lab6=Label(self.labFra, justify=LEFT, fg='cyan',
            bg='grey22', font=('Times', 14),
            text="Path : Menu Bar --> Menu --> MapApp").pack(padx=10, pady=10)

    def instalpy(self):
        """
            Explanation about skills
            and how to use app
        """
        self.can.delete(ALL)
        self.photo=PhotoImage(file='./syno_gif/pyt2.gif')
        self.item=self.can.create_image(625, 350, image=self.photo)
        self.can.create_text(500, 20, anchor=NW,
            text="- MAPAPP -\n\n"

            "Usefull functionalities :\n"
            "----------------------------\n"
            "---> A backup is preview for every first day of each month\n"
            "---> Display if a treatment or reserve ends the next day\n"
            "---> Agenda is verified every day and pop-up"
            "to show you if an appointment is fixed for tomorrow\n\n"

            "How to use heal-track :\n\n"

            "To make a patient entry : \n"

            "Entry or Add patient (read below) ---> Allergy + Intolerance --->"
            " 14 Needs ---> Care and Monitoring :\n"
            "-----------------------------------------------------------------"
            "---------------------------------------------------------\n"
            "Use 'Entry' button to enter for first time new patient. Use 'Add "
            "patient' once time all patients were enter \n"
            "(button to replace a patient who's left with delete button).\n"
            "Once time, patient had added use 'allergy' button to enter an allergy "
            "if none, write and enter 'none'!\n"
            "You can also use 'Intolerance' in the Menu Bar to complete 'allergy'.\n"
            "After it, Care and Monitoring is available only if you have entered one "
            "or more needs of patient.\n"
            "1 ---> Enter data of patient\n"
            "2 ---> Use Refresh (button)\n"
            "3 ---> Intolerances\n"
            "4 ---> 14 Needs\n"
            "5 ---> Care and monitoring\n\n"

            "Care and monitoring retrieve all data from :\n"
            "----------------------------------------------------\n"
            "+ 14 Needs (V. Henderson)\n"
            "+ Labo (dosage of neuroleptic)\n"

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
        subprocess.run('./newpatient/entrypytientfile.py', check=True)

    def delEverPat(self):
        """
            To delete patient
        """
        subprocess.run('./deletepatient/deleverything.py', check=True)

    def addPatientAfter(self):
        """
            To add new patient after delete one of them
        """
        subprocess.run('./newpatient/torecord.py', check=True)

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

    #def callDataPat(self):
    #    launchData(self)

    def contact_num2(self):
        subprocess.run('./contact/pat_contact2.py', check=True)

    def contact_num3(self):
        subprocess.run('./contact/pat_contact3.py', check=True)

    def contact_num4(self):
        subprocess.run('./contact/pat_contact4.py', check=True)

    def contact_num5(self):
        subprocess.run('./contact/pat_contact5.py', check=True)

    def contact_num6(self):
        subprocess.run('./contact/pat_contact6.py', check=True)

    def contact_num7(self):
        subprocess.run('./contact/pat_contact7.py', check=True)

    def contact_num8(self):
        subprocess.run('./contact/pat_contact8.py', check=True)

    def contact_num9(self):
        subprocess.run('./contact/pat_contact9.py', check=True)

    def contact_num10(self):
        subprocess.run('./contact/pat_contact10.py', check=True)

    def contact_num11(self):
        subprocess.run('./contact/pat_contact11.py', check=True)

    def contact_num12(self):
        subprocess.run('./contact/pat_contact12.py', check=True)

    def contact_num13(self):
        subprocess.run('./contact/pat_contact13.py', check=True)

    def contact_num14(self):
        subprocess.run('./contact/pat_contact14.py', check=True)

    def contact_num15(self):
        subprocess.run('./contact/pat_contact15.py', check=True)

    def contact_num16(self):
        subprocess.run('./contact/pat_contact16.py', check=True)

    def contact_num17(self):
        subprocess.run('./contact/pat_contact17.py', check=True)

    def contact_num18(self):
        subprocess.run('./contact/pat_contact18.py', check=True)

    def contact_num19(self):
        subprocess.run('./contact/pat_contact19.py', check=True)

    def contact_num20(self):
        subprocess.run('./contact/pat_contact20.py', check=True)

    def contact_num21(self):
        subprocess.run('./contact/pat_contact21.py', check=True)

    def contact_num22(self):
        subprocess.run('./contact/pat_contact22.py', check=True)

    def contact_num23(self):
        subprocess.run('./contact/pat_contact23.py', check=True)

    def contact_num24(self):
        subprocess.run('./contact/pat_contact24.py', check=True)

    # CheckBox 14 needs OK
    def besoinsCoche(self):
        self.master.withdraw()
        subprocess.run('./14besoins/checkb.py', check=True)
        self.master.deiconify()

    def besoins2Coche(self):
        self.master.withdraw()
        subprocess.run('./14besoins/checkb2.py', check=True)
        self.master.deiconify()

    def besoins3Coche(self):
        self.master.withdraw()
        subprocess.run('./14besoins/checkb3.py', check=True)
        self.master.deiconify()

    def besoins4Coche(self):
        self.master.withdraw()
        subprocess.run('./14besoins/checkb4.py', check=True)
        self.master.deiconify()

    def besoins5Coche(self):
        self.master.withdraw()
        subprocess.run('./14besoins/checkb5.py', check=True)
        self.master.deiconify()

    def besoins6Coche(self):
        self.master.withdraw()
        subprocess.run('./14besoins/checkb6.py', check=True)
        self.master.deiconify()

    def besoins7Coche(self):
        self.master.withdraw()
        subprocess.run('./14besoins/checkb7.py', check=True)
        self.master.deiconify()

    def besoins8Coche(self):
        self.master.withdraw()
        subprocess.run('./14besoins/checkb8.py', check=True)
        self.master.deiconify()

    def besoins9Coche(self):
        self.master.withdraw()
        subprocess.run('./14besoins/checkb9.py', check=True)
        self.master.deiconify()

    def besoins10Coche(self):
        self.master.withdraw()
        subprocess.run('./14besoins/checkb10.py', check=True)
        self.master.deiconify()

    def besoins11Coche(self):
        self.master.withdraw()
        subprocess.run('./14besoins/checkb11.py', check=True)
        self.master.deiconify()

    def besoins12Coche(self):
        self.master.withdraw()
        subprocess.run('./14besoins/checkb12.py', check=True)
        self.master.deiconify()

    def besoins13Coche(self):
        self.master.withdraw()
        subprocess.run('./14besoins/checkb13.py', check=True)
        self.master.deiconify()

    def besoins14Coche(self):
        self.master.withdraw()
        subprocess.run('./14besoins/checkb14.py', check=True)
        self.master.deiconify()

    def besoins15Coche(self):
        self.master.withdraw()
        subprocess.run('./14besoins/checkb15.py', check=True)
        self.master.deiconify()

    def besoins16Coche(self):
        self.master.withdraw()
        subprocess.run('./14besoins/checkb16.py', check=True)
        self.master.deiconify()

    def besoins17Coche(self):
        self.master.withdraw()
        subprocess.run('./14besoins/checkb17.py', check=True)
        self.master.deiconify()

    def besoins18Coche(self):
        self.master.withdraw()
        subprocess.run('./14besoins/checkb18.py', check=True)
        self.master.deiconify()

    def besoins19Coche(self):
        self.master.withdraw()
        subprocess.run('./14besoins/checkb19.py', check=True)
        self.master.deiconify()

    def besoins20Coche(self):
        self.master.withdraw()
        subprocess.run('./14besoins/checkb20.py', check=True)
        self.master.deiconify()

    def besoins21Coche(self):
        self.master.withdraw()
        subprocess.run('./14besoins/checkb21.py', check=True)
        self.master.deiconify()

    def besoins22Coche(self):
        self.master.withdraw()
        subprocess.run('./14besoins/checkb22.py', check=True)
        self.master.deiconify()

    def besoins23Coche(self):
        self.master.withdraw()
        subprocess.run('./14besoins/checkb23.py', check=True)
        self.master.deiconify()

    def besoins24Coche(self):
        self.master.withdraw()
        subprocess.run('./14besoins/checkb24.py', check=True)
        self.master.deiconify()

    # Func 14 needs suivi OK
    def suiviSoins1(self):
        self.master.withdraw()
        subprocess.run("./14besoins/suivi_patient_1.py", check=True)
        self.master.deiconify()

    def suiviSoins2(self):
        self.master.withdraw()
        subprocess.run("./14besoins/suivi_patient_2.py", check=True)
        self.master.deiconify()

    def suiviSoins3(self):
        self.master.withdraw()
        subprocess.run("./14besoins/suivi_patient_3.py", check=True)
        self.master.deiconify()

    def suiviSoins4(self):
        self.master.withdraw()
        subprocess.run("./14besoins/suivi_patient_4.py", check=True)
        self.master.deiconify()

    def suiviSoins5(self):
        self.master.withdraw()
        subprocess.run("./14besoins/suivi_patient_5.py", check=True)
        self.master.deiconify()

    def suiviSoins6(self):
        self.master.withdraw()
        subprocess.run("./14besoins/suivi_patient_6.py", check=True)
        self.master.deiconify()

    def suiviSoins7(self):
        self.master.withdraw()
        subprocess.run("./14besoins/suivi_patient_7.py", check=True)
        self.master.deiconify()

    def suiviSoins8(self):
        self.master.withdraw()
        subprocess.run("./14besoins/suivi_patient_8.py", check=True)
        self.master.deiconify()

    def suiviSoins9(self):
        self.master.withdraw()
        subprocess.run("./14besoins/suivi_patient_9.py", check=True)
        self.master.deiconify()

    def suiviSoins10(self):
        self.master.withdraw()
        subprocess.run("./14besoins/suivi_patient_10.py", check=True)
        self.master.deiconify()

    def suiviSoins11(self):
        self.master.withdraw()
        subprocess.run("./14besoins/suivi_patient_11.py", check=True)
        self.master.deiconify()

    def suiviSoins12(self):
        self.master.withdraw()
        subprocess.run("./14besoins/suivi_patient_12.py", check=True)
        self.master.deiconify()

    def suiviSoins13(self):
        self.master.withdraw()
        subprocess.run("./14besoins/suivi_patient_13.py", check=True)
        self.master.deiconify()

    def suiviSoins14(self):
        self.master.withdraw()
        subprocess.run("./14besoins/suivi_patient_14.py", check=True)
        self.master.deiconify()

    def suiviSoins15(self):
        self.master.withdraw()
        subprocess.run("./14besoins/suivi_patient_15.py", check=True)
        self.master.deiconify()

    def suiviSoins16(self):
        self.master.withdraw()
        subprocess.run("./14besoins/suivi_patient_16.py", check=True)
        self.master.deiconify()

    def suiviSoins17(self):
        self.master.withdraw()
        subprocess.run("./14besoins/suivi_patient_17.py", check=True)
        self.master.deiconify()

    def suiviSoins18(self):
        self.master.withdraw()
        subprocess.run("./14besoins/suivi_patient_18.py", check=True)
        self.master.deiconify()

    def suiviSoins19(self):
        self.master.withdraw()
        subprocess.run("./14besoins/suivi_patient_19.py", check=True)
        self.master.deiconify()

    def suiviSoins20(self):
        self.master.withdraw()
        subprocess.run("./14besoins/suivi_patient_20.py", check=True)
        self.master.deiconify()

    def suiviSoins21(self):
        self.master.withdraw()
        subprocess.run("./14besoins/suivi_patient_21.py", check=True)
        self.master.deiconify()

    def suiviSoins22(self):
        self.master.withdraw()
        subprocess.run("./14besoins/suivi_patient_22.py", check=True)
        self.master.deiconify()

    def suiviSoins23(self):
        self.master.withdraw()
        subprocess.run("./14besoins/suivi_patient_23.py", check=True)
        self.master.deiconify()

    def suiviSoins24(self):
        self.master.withdraw()
        subprocess.run("./14besoins/suivi_patient_24.py", check=True)
        self.master.deiconify()

    # treatments
    def tttMed1(self):
        callTreatment1(self)

    def tttMed2(self):
        callTreatment2(self)

    def tttMed3(self):
        callTreatment3(self)

    def tttMed4(self):
        callTreatment4(self)

    def tttMed5(self):
        callTreatment5(self)

    def tttMed6(self):
        callTreatment6(self)

    def tttMed7(self):
        callTreatment7(self)

    def tttMed8(self):
        callTreatment8(self)

    def tttMed9(self):
        callTreatment9(self)

    def tttMed10(self):
        callTreatment10(self)

    def tttMed11(self):
        callTreatment11(self)

    def tttMed12(self):
        callTreatment12(self)

    def tttMed13(self):
        callTreatment13(self)

    def tttMed14(self):
        callTreatment14(self)

    def tttMed15(self):
        callTreatment15(self)

    def tttMed16(self):
        callTreatment16(self)

    def tttMed17(self):
        callTreatment17(self)

    def tttMed18(self):
        callTreatment18(self)

    def tttMed19(self):
        callTreatment19(self)

    def tttMed20(self):
        callTreatment20(self)

    def tttMed21(self):
        callTreatment21(self)

    def tttMed22(self):
        callTreatment22(self)

    def tttMed23(self):
        callTreatment23(self)

    def tttMed24(self):
        callTreatment24(self)

    # Func BMI
    def calculB(self):
        self.master.withdraw()
        subprocess.run("./calBmi/CalculBmi.py", check=True)
        self.master.deiconify()

    def calculB2(self):
        self.master.withdraw()
        subprocess.run("./calBmi/CalculBmi2.py", check=True)
        self.master.deiconify()

    def calculB3(self):
        self.master.withdraw()
        subprocess.run("./calBmi/CalculBmi3.py", check=True)
        self.master.deiconify()

    def calculB4(self):
        self.master.withdraw()
        subprocess.run("./calBmi/CalculBmi4.py", check=True)
        self.master.deiconify()

    def calculB5(self):
        self.master.withdraw()
        subprocess.run("./calBmi/CalculBmi5.py", check=True)
        self.master.deiconify()

    def calculB6(self):
        self.master.withdraw()
        subprocess.run("./calBmi/CalculBmi6.py", check=True)
        self.master.deiconify()

    def calculB7(self):
        self.master.withdraw()
        subprocess.run("./calBmi/CalculBmi7.py", check=True)
        self.master.deiconify()

    def calculB8(self):
        self.master.withdraw()
        subprocess.run("./calBmi/CalculBmi8.py", check=True)
        self.master.deiconify()

    def calculB9(self):
        self.master.withdraw()
        subprocess.run("./calBmi/CalculBmi9.py", check=True)
        self.master.deiconify()

    def calculB10(self):
        self.master.withdraw()
        subprocess.run("./calBmi/CalculBmi10.py", check=True)
        self.master.deiconify()

    def calculB11(self):
        self.master.withdraw()
        subprocess.run("./calBmi/CalculBmi11.py", check=True)
        self.master.deiconify()

    def calculB12(self):
        self.master.withdraw()
        subprocess.run("./calBmi/CalculBmi12.py", check=True)
        self.master.deiconify()

    def calculB13(self):
        self.master.withdraw()
        subprocess.run("./calBmi/CalculBmi13.py", check=True)
        self.master.deiconify()

    def calculB14(self):
        self.master.withdraw()
        subprocess.run("./calBmi/CalculBmi14.py", check=True)
        self.master.deiconify()

    def calculB15(self):
        self.master.withdraw()
        subprocess.run("./calBmi/CalculBmi15.py", check=True)
        self.master.deiconify()

    def calculB16(self):
        self.master.withdraw()
        subprocess.run("./calBmi/CalculBmi16.py", check=True)
        self.master.deiconify()

    def calculB17(self):
        self.master.withdraw()
        subprocess.run("./calBmi/CalculBmi17.py", check=True)
        self.master.deiconify()

    def calculB18(self):
        self.master.withdraw()
        subprocess.run("./calBmi/CalculBmi18.py", check=True)
        self.master.deiconify()

    def calculB19(self):
        self.master.withdraw()
        subprocess.run("./calBmi/CalculBmi19.py", check=True)
        self.master.deiconify()

    def calculB20(self):
        self.master.withdraw()
        subprocess.run("./calBmi/CalculBmi20.py", check=True)
        self.master.deiconify()

    def calculB21(self):
        self.master.withdraw()
        subprocess.run("./calBmi/CalculBmi21.py", check=True)
        self.master.deiconify()

    def calculB22(self):
        self.master.withdraw()
        subprocess.run("./calBmi/CalculBmi22.py", check=True)
        self.master.deiconify()

    def calculB23(self):
        self.master.withdraw()
        subprocess.run("./calBmi/CalculBmi23.py", check=True)
        self.master.deiconify()

    def calculB24(self):
        self.master.withdraw()
        subprocess.run("./calBmi/CalculBmi24.py", check=True)
        self.master.deiconify()

    # Func Visit MED
    def visitMed(self):
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient1.py", check=True)
        self.master.deiconify()
        
    def visitMed2(self):
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient2.py", check=True)
        self.master.deiconify()
        
    def visitMed3(self):
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient3.py", check=True)
        self.master.deiconify()
        
    def visitMed4(self):
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient4.py", check=True)
        self.master.deiconify()
        
    def visitMed5(self):
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient5.py", check=True)
        self.master.deiconify()
        
    def visitMed6(self):
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient6.py", check=True)
        self.master.deiconify()
        
    def visitMed7(self):
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient7.py", check=True)
        self.master.deiconify()

    def visitMed8(self):
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient8.py", check=True)
        self.master.deiconify()

    def visitMed9(self):
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient9.py", check=True)
        self.master.deiconify()

    def visitMed10(self):
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient10.py", check=True)
        self.master.deiconify()

    def visitMed11(self):
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient11.py", check=True)
        self.master.deiconify()

    def visitMed12(self):
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient12.py", check=True)
        self.master.deiconify()

    def visitMed13(self):
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient13.py", check=True)
        self.master.deiconify()

    def visitMed14(self):
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient14.py", check=True)
        self.master.deiconify()

    def visitMed15(self):
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient15.py", check=True)
        self.master.deiconify()

    def visitMed16(self):
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient16.py", check=True)
        self.master.deiconify()

    def visitMed17(self):
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient17.py", check=True)
        self.master.deiconify()

    def visitMed18(self):
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient18.py", check=True)
        self.master.deiconify()

    def visitMed19(self):
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient19.py", check=True)
        self.master.deiconify()

    def visitMed20(self):
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient20.py", check=True)
        self.master.deiconify()

    def visitMed21(self):
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient21.py", check=True)
        self.master.deiconify()

    def visitMed22(self):
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient22.py", check=True)
        self.master.deiconify()

    def visitMed23(self):
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient23.py", check=True)
        self.master.deiconify()

    def visitMed24(self):
        self.master.withdraw()
        subprocess.run("./vmed/vm_patient24.py", check=True)
        self.master.deiconify()

    def updateLink(self):
        """
            To update data for patient
            in txt entryfile and for DB.
        """
        self.master.withdraw()
        subprocess.run('./update/updatepatient1.py', check=True)
        self.master.deiconify()

    def updateLink2(self):
        self.master.withdraw()
        subprocess.run('./update/updatepatient2.py', check=True)
        self.master.deiconify()

    def updateLink3(self):
        self.master.withdraw()
        subprocess.run('./update/updatepatient3.py', check=True)
        self.master.deiconify()

    def updateLink4(self):
        self.master.withdraw()
        subprocess.run('./update/updatepatient4.py', check=True)
        self.master.deiconify()

    def updateLink5(self):
        self.master.withdraw()
        subprocess.run('./update/updatepatient5.py', check=True)
        self.master.deiconify()

    def updateLink6(self):
        self.master.withdraw()
        subprocess.run('./update/updatepatient6.py', check=True)
        self.master.deiconify()

    def updateLink7(self):
        self.master.withdraw()
        subprocess.run('./update/updatepatient7.py', check=True)
        self.master.deiconify()

    def updateLink8(self):
        self.master.withdraw()
        subprocess.run('./update/updatepatient8.py', check=True)
        self.master.deiconify()

    def updateLink9(self):
        self.master.withdraw()
        subprocess.run('./update/updatepatient9.py', check=True)
        self.master.deiconify()

    def updateLink10(self):
        self.master.withdraw()
        subprocess.run('./update/updatepatient10.py', check=True)
        self.master.deiconify()

    def updateLink11(self):
        self.master.withdraw()
        subprocess.run('./update/updatepatient11.py', check=True)
        self.master.deiconify()

    def updateLink12(self):
        self.master.withdraw()
        subprocess.run('./update/updatepatient12.py', check=True)
        self.master.deiconify()

    def updateLink13(self):
        self.master.withdraw()
        subprocess.run('./update/updatepatient13.py', check=True)
        self.master.deiconify()

    def updateLink14(self):
        self.master.withdraw()
        subprocess.run('./update/updatepatient14.py', check=True)
        self.master.deiconify()

    def updateLink15(self):
        self.master.withdraw()
        subprocess.run('./update/updatepatient15.py', check=True)
        self.master.deiconify()

    def updateLink16(self):
        self.master.withdraw()
        subprocess.run('./update/updatepatient16.py', check=True)
        self.master.deiconify()

    def updateLink17(self):
        self.master.withdraw()
        subprocess.run('./update/updatepatient17.py', check=True)
        self.master.deiconify()

    def updateLink18(self):
        self.master.withdraw()
        subprocess.run('./update/updatepatient18.py', check=True)
        self.master.deiconify()

    def updateLink19(self):
        self.master.withdraw()
        subprocess.run('./update/updatepatient19.py', check=True)
        self.master.deiconify()

    def updateLink20(self):
        self.master.withdraw()
        subprocess.run('./update/updatepatient20.py', check=True)
        self.master.deiconify()

    def updateLink21(self):
        self.master.withdraw()
        subprocess.run('./update/updatepatient21.py', check=True)
        self.master.deiconify()

    def updateLink22(self):
        self.master.withdraw()
        subprocess.run('./update/updatepatient22.py', check=True)
        self.master.deiconify()

    def updateLink23(self):
        self.master.withdraw()
        subprocess.run('./update/updatepatient23.py', check=True)
        self.master.deiconify()

    def updateLink24(self):
        self.master.withdraw()
        subprocess.run('./update/updatepatient24.py', check=True)
        self.master.deiconify()

    # Func Diagnostic
    def diag1(self):
        self.master.withdraw()
        subprocess.run("./diag/diag_patient1.py", check=True)
        self.master.deiconify()

    def diag2(self):
        self.master.withdraw()
        subprocess.run("./diag/diag_patient2.py", check=True)
        self.master.deiconify()

    def diag3(self):
        self.master.withdraw()
        subprocess.run("./diag/diag_patient3.py", check=True)
        self.master.deiconify()

    def diag4(self):
        self.master.withdraw()
        subprocess.run("./diag/diag_patient4.py", check=True)
        self.master.deiconify()

    def diag5(self):
        self.master.withdraw()
        subprocess.run("./diag/diag_patient5.py", check=True)
        self.master.deiconify()

    def diag6(self):
        self.master.withdraw()
        subprocess.run("./diag/diag_patient6.py", check=True)
        self.master.deiconify()

    def diag7(self):
        self.master.withdraw()
        subprocess.run("./diag/diag_patient7.py", check=True)
        self.master.deiconify()

    def diag8(self):
        self.master.withdraw()
        subprocess.run("./diag/diag_patient8.py", check=True)
        self.master.deiconify()

    def diag9(self):
        self.master.withdraw()
        subprocess.run("./diag/diag_patient9.py", check=True)
        self.master.deiconify()

    def diag10(self):
        self.master.withdraw()
        subprocess.run("./diag/diag_patient10.py", check=True)
        self.master.deiconify()

    def diag11(self):
        self.master.withdraw()
        subprocess.run("./diag/diag_patient11.py", check=True)
        self.master.deiconify()

    def diag12(self):
        self.master.withdraw()
        subprocess.run("./diag/diag_patient12.py", check=True)
        self.master.deiconify()

    def diag13(self):
        self.master.withdraw()
        subprocess.run("./diag/diag_patient13.py", check=True)
        self.master.deiconify()

    def diag14(self):
        self.master.withdraw()
        subprocess.run("./diag/diag_patient14.py", check=True)
        self.master.deiconify()

    def diag15(self):
        self.master.withdraw()
        subprocess.run("./diag/diag_patient15.py", check=True)
        self.master.deiconify()

    def diag16(self):
        self.master.withdraw()
        subprocess.run("./diag/diag_patient16.py", check=True)
        self.master.deiconify()

    def diag17(self):
        self.master.withdraw()
        subprocess.run("./diag/diag_patient17.py", check=True)
        self.master.deiconify()

    def diag18(self):
        self.master.withdraw()
        subprocess.run("./diag/diag_patient18.py", check=True)
        self.master.deiconify()

    def diag19(self):
        self.master.withdraw()
        subprocess.run("./diag/diag_patient19.py", check=True)
        self.master.deiconify()

    def diag20(self):
        self.master.withdraw()
        subprocess.run("./diag/diag_patient20.py", check=True)
        self.master.deiconify()

    def diag21(self):
        self.master.withdraw()
        subprocess.run("./diag/diag_patient21.py", check=True)
        self.master.deiconify()

    def diag22(self):
        self.master.withdraw()
        subprocess.run("./diag/diag_patient22.py", check=True)
        self.master.deiconify()

    def diag23(self):
        self.master.withdraw()
        subprocess.run("./diag/diag_patient23.py", check=True)
        self.master.deiconify()

    def diag24(self):
        self.master.withdraw()
        subprocess.run("./diag/diag_patient24.py", check=True)
        self.master.deiconify()

    # Func labo
    def laboResult(self):
        callLabo1(self)

    def laboResult2(self):
        callLabo2(self)

    def laboResult3(self):
        callLabo3(self)

    def laboResult4(self):
        callLabo4(self)

    def laboResult5(self):
        callLabo5(self)

    def laboResult6(self):
        callLabo6(self)

    def laboResult7(self):
        callLabo7(self)

    def laboResult8(self):
        callLabo8(self)

    def laboResult9(self):
        callLabo9(self)

    def laboResult10(self):
        callLabo10(self)

    def laboResult11(self):
        callLabo11(self)

    def laboResult12(self):
        callLabo12(self)

    def laboResult13(self):
        callLabo13(self)

    def laboResult14(self):
        callLabo14(self)

    def laboResult15(self):
        callLabo15(self)

    def laboResult16(self):
        callLabo16(self)

    def laboResult17(self):
        callLabo17(self)

    def laboResult18(self):
        callLabo18(self)

    def laboResult19(self):
        callLabo19(self)

    def laboResult20(self):
        callLabo20(self)

    def laboResult21(self):
        callLabo21(self)

    def laboResult22(self):
        callLabo22(self)

    def laboResult23(self):
        callLabo23(self)

    def laboResult24(self):
        callLabo24(self)

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
        backupFuncPatient(self)

    def allFilesBackup2(self):
        backupFuncPatient2(self)

    def allFilesBackup3(self):
        backupFuncPatient3(self)

    def allFilesBackup4(self):
        backupFuncPatient4(self)

    def allFilesBackup5(self):
        backupFuncPatient5(self)

    def allFilesBackup6(self):
        backupFuncPatient6(self)

    def allFilesBackup7(self):
        backupFuncPatient7(self)

    def allFilesBackup8(self):
        backupFuncPatient8(self)

    def allFilesBackup9(self):
        backupFuncPatient9(self)

    def allFilesBackup10(self):
        backupFuncPatient10(self)

    def allFilesBackup11(self):
        backupFuncPatient11(self)

    def allFilesBackup12(self):
        backupFuncPatient12(self)

    def allFilesBackup13(self):
        backupFuncPatient13(self)

    def allFilesBackup14(self):
        backupFuncPatient14(self)

    def allFilesBackup15(self):
        backupFuncPatient15(self)

    def allFilesBackup16(self):
        backupFuncPatient16(self)

    def allFilesBackup17(self):
        backupFuncPatient17(self)

    def allFilesBackup18(self):
        backupFuncPatient18(self)

    def allFilesBackup19(self):
        backupFuncPatient19(self)

    def allFilesBackup20(self):
        backupFuncPatient20(self)

    def allFilesBackup21(self):
        backupFuncPatient21(self)

    def allFilesBackup22(self):
        backupFuncPatient22(self)

    def allFilesBackup23(self):
        backupFuncPatient23(self)

    def allFilesBackup24(self):
        backupFuncPatient24(self)

    def updateFiletxt(self):
        """
            To backup all files
            today !!!
        """
        dataBackToSave(self)

    def upDateAll(self):
        """
            To reset app by pressing 
            refresh button. Close,
            open directly and update
            data from patcaps.py !
        """
        try:
            self.master.destroy()
            Application.__init__(self)
            self.showPatients()
        except (OSError, ValueError) as p_out:
            print("Error --", p_out)

if __name__=='__main__':
    app = Application()
    app.mainloop()
