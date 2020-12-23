#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
import os
import json
import subprocess


def callTreatment4(self):
    self.can.delete(ALL)
    self.can.configure(bg='DodgerBlue2')

    self.x1, self.y1 = 625, 30
    self.textLab = Label(self.can, text="Introduction of treatement (ttt)",
        font=('Times', 22, 'bold'), fg='white', bg='DodgerBlue2')
    self.textLab_window = self.can.create_window(self.x1, self.y1, window=self.textLab)

    self.x2, self.y2 = 410, 80
    self.labelallergy = Label(self.can, text="Allergy : ",
        font=('Arial', 18, 'bold'), fg='coral', bg='DodgerBlue2')
    self.labelallergy_window = self.can.create_window(self.x2, self.y2, window=self.labelallergy)

    # To read allergy for entry widget
    with open('./newpatient/entryfile4.txt', 'r') as filename2:
        line1 = filename2.readline()
        line2 = filename2.readline()
        line3 = filename2.readline()

    self.x3, self.y3 = 670, 80
    self.entrytext = StringVar()
    self.entryName = Entry(self.can, textvariable=self.entrytext, width=50)
    self.entrytext.set(line3[:-1])
    self.entryName_window = self.can.create_window(self.x3, self.y3, window=self.entryName)

    self.x4, self.y4 = 120, 180
    self.LabDate = Label(self.can, text="Date : ", width=15, font=12,
        fg='white', bg='DodgerBlue2', anchor='e')
    self.LabDate_window = self.can.create_window(self.x4, self.y4, window=self.LabDate)

    self.x5, self.y5 = 120, 210
    self.LabHour = Label(self.can, text="Hour : ", width=15, font=12,
        fg='white', bg='DodgerBlue2', anchor='e')
    self.LabHour_window = self.can.create_window(self.x5, self.y5, window=self.LabHour)

    self.x6, self.y6 = 120, 240
    self.LabName = Label(self.can, text="Patient name : ", width=15, font=12,
        fg='white', bg='DodgerBlue2', anchor='e')
    self.LabName_window = self.can.create_window(self.x6, self.y6, window=self.LabName)

    self.x7, self.y7 = 120, 270
    self.LabTreat = Label(self.can, text='Name of drug : ', width=15, 
        font=12, fg='white', bg='DodgerBlue2', anchor='e')
    self.LabTreat_window = self.can.create_window(self.x7, self.y7, window=self.LabTreat)

    self.x8, self.y8 = 120, 300
    self.LabDose = Label(self.can, text="Dose : ", width=15, font=12,
        fg='white', bg='DodgerBlue2', anchor='e')
    self.LabDose_window = self.can.create_window(self.x8, self.y8, window=self.LabDose)

    self.x9, self.y9 = 300, 180
    self.time_string = IntVar()
    self.textDate = Entry(self.can, textvariable=self.time_string,
        highlightbackground='grey', bd=4)
    self.time_string.set(time.strftime("%d/%m/%Y"))
    self.textDate_window = self.can.create_window(self.x9, self.y9, window=self.textDate)

    self.x10, self.y10 = 300, 210
    self.time_Htring = IntVar()
    self.textHour = Entry(self.can, textvariable=self.time_Htring,
        highlightbackground='grey', bd=4)
    self.time_Htring.set(time.strftime("%H:%M:%S"))
    self.textHour_window = self.can.create_window(self.x10, self.y10, window=self.textHour)

    # To read name of patient for entry widget
    with open('./newpatient/entryfile4.txt', 'r') as filename:
        line1=filename.readline()

    self.x11, self.y11 = 300, 240
    self.name_text = StringVar()
    self.textName = Entry(self.can, textvariable=self.name_text,
        highlightbackground='grey', bd=4)
    self.name_text.set(line1[:-1])
    self.textName_window = self.can.create_window(self.x11, self.y11, window=self.textName)

    self.x12, self.y12 = 300, 270
    self.ttt_name = StringVar()
    self.textTreat = Entry(self.can, textvariable=self.ttt_name,
        highlightbackground='grey', bd=4)
    self.ttt_name.set("Drug")
    self.textTreat_window = self.can.create_window(self.x12, self.y12, window=self.textTreat)

    self.x13, self.y13 = 300, 300
    self.tttDosage = StringVar()
    self.textDosage = Entry(self.can, textvariable=self.tttDosage,
        highlightbackground='grey', bd=4)
    self.tttDosage.set("mcg/ml/mg/UI/gttes")
    self.textDosage_window = self.can.create_window(self.x13, self.y13, window=self.textDosage)

    def callbackDay(event):
        print(self.comboDay.get())

    def callbackMonth(event):
        print(self.comboMonth.get())

    def callbackYear(event):
        print(self.comboYear.get())

    def callbackFinishDay(event):
        print(self.comboFinishDay.get())

    def callbackFinishMonth(event):
        print(self.comboFinishMonth.get())

    def callbackFinishYear(event):
        print(self.comboFinishYear.get())

    def showTreat():
            #To display tabs of ttt, convdose.json 
            #file must be existing.
        try:
            if os.path.getsize('./ttt/doc_ttt4/convdose.json'):
                subprocess.call('./ttt/doc_ttt4/tabs.py')
        except FileNotFoundError as no_tabtreat:
            print("+ Sorry, it's not possible to show tab of ttt, " \
                "convdose.json file missing !", no_tabtreat)
            tttTabs()

    def tttTabs():
        messagebox.showinfo("Info", "No ttt recorded for " \
            "this patient, convdose.json file missing !") 

    def showReserve():
            #To display tabs of reserve, convres.json 
            #file must be existing.
        try:
            if os.path.getsize('./ttt/doc_ttt4/convres.json'):
                subprocess.call('./ttt/doc_ttt4/tabres.py')
        except FileNotFoundError as no_tabres:
            print("+ Sorry, it's not possible to show tab of reserve, " \
                "convres.json file missing !", no_tabres)
            reserveTabs()

    def reserveTabs():
        messagebox.showinfo("Info", "No reserve recorded for " \
            "this patient, convres.json file missing !")

    def deleteTreatment():
            #To earase one line in array
            #for one treatment
        MSBask = messagebox.askyesno('Delete ttt', 'Are you sure ?')
        if MSBask == 1:
            print("+ Ok, ttt has been ejected !")
            messagebox.showinfo('info BOX', 'Treatment is away !')
            try:
                if os.path.getsize('./ttt/doc_ttt4/convdose.json'):
                    print("+ File 'convdose' exist !")
                    with open('./ttt/doc_ttt4/convdose.json', 'r') as datafile:
                        datastore = json.load(datafile)
                    
                    dataDose = datastore
                    for key, value in dataDose.items():
                        if self.deleteTreat.get() == value[0]['Treatment']:
                            del value[0]
                            print("+ TTT earased !")

                        elif self.deleteTreat.get() == value[1]['Treatment']:
                            del value[1]
                            print("+ TTT earased !")

                        elif self.deleteTreat.get() == value[2]['Treatment']:
                            del value[2]
                            print("+ TTT earased !")
                            
                        elif self.deleteTreat.get() == value[3]['Treatment']:
                            del value[3]
                            print("+ TTT earased !")

                        elif self.deleteTreat.get() == value[4]['Treatment']:
                            del value[4]
                            print("+ TTT earased !")

                        elif self.deleteTreat.get() == value[5]['Treatment']:
                            del value[5]
                            print("+ TTT earased !")

                        elif self.deleteTreat.get() == value[6]['Treatment']:
                            del value[6]
                            print("+ TTT earased !")

                        elif self.deleteTreat.get() == value[7]['Treatment']:
                            del value[7]
                            print("+ TTT earased !")

                        elif self.deleteTreat.get() == value[8]['Treatment']:
                            del value[8]
                            print("+ TTT earased !")

                        elif self.deleteTreat.get() == value[9]['Treatment']:
                            del value[9]
                            print("+ TTT earased !")

                        elif self.deleteTreat.get() == value[10]['Treatment']:
                            del value[10]
                            print("+ TTT earased !")

                        elif self.deleteTreat.get() == value[11]['Treatment']:
                            del value[11]
                            print("+ TTT earased !")

                        elif self.deleteTreat.get() == value[12]['Treatment']:
                            del value[12]
                            print("+ TTT earased !")

                        elif self.deleteTreat.get() == value[13]['Treatment']:
                            del value[13]
                            print("+ TTT earased !")

                        elif self.deleteTreat.get() == value[14]['Treatment']:
                            del value[14]
                            print("+ TTT earased !")
                        else:
                            print("Treatment is not present into medication")

                        if self.deleteTreat.get() == '':
                            print("None treatment checked")
                        else:
                            print("---Ok VALUE 'Treatment' earased---")
                            with open('./ttt/doc_ttt4/convdose.json', 'w') as datafile2:
                                json.dump(dataDose, datafile2, indent=4)
            except FileNotFoundError as fnfe:
                print('+ Sorry, file convdose.json not exist !', fnfe)
        else:           
            messagebox.showinfo('Return', 'Treatment not earased')

    def deleteReserve():
            #To earase one line in array
            #for one Reserve
        MSB2asno = messagebox.askyesno('Delete Reserve', 'Are you sure ?')
        if MSB2asno == 1:
            print("Ok, Reserve has been ejected !")
            messagebox.showinfo('info BOX', 'Reserve is away !')
            try:
                if os.path.getsize('./ttt/doc_ttt4/convres.json'):
                    print("+ File 'convres' exist !")
                    with open('./ttt/doc_ttt4/convres.json', 'r') as datafile:
                        datastore = json.load(datafile)
                    
                    dataRes = datastore
                    for key, value in dataRes.items():
                        if self.deleteRes.get() == value[0]['Treatment']:
                            del value[0]
                            print("+ Reserve earased !")

                        elif self.deleteRes.get() == value[1]['Treatment']:
                            del value[1]
                            print("+ Reserve earased !")

                        elif self.deleteRes.get() == value[2]['Treatment']:
                            del value[2]
                            print("+ Reserve earased !")
                            
                        elif self.deleteRes.get() == value[3]['Treatment']:
                            del value[3]
                            print("+ Reserve earased !")

                        elif self.deleteRes.get() == value[4]['Treatment']:
                            del value[4]
                            print("+ Reserve earased !")

                        elif self.deleteRes.get() == value[5]['Treatment']:
                            del value[5]
                            print("+ Reserve earased !")

                        elif self.deleteRes.get() == value[6]['Treatment']:
                            del value[6]
                            print("+ Reserve earased !")

                        elif self.deleteRes.get() == value[7]['Treatment']:
                            del value[7]
                            print("+ Reserve earased !")

                        elif self.deleteRes.get() == value[8]['Treatment']:
                            del value[8]
                            print("+ Reserve earased !")

                        elif self.deleteRes.get() == value[9]['Treatment']:
                            del value[9]
                            print("+ Reserve earased !")

                        elif self.deleteRes.get() == value[10]['Treatment']:
                            del value[10]
                            print("+ Reserve earased !")

                        elif self.deleteRes.get() == value[11]['Treatment']:
                            del value[11]
                            print("+ Reserve earased !")

                        elif self.deleteRes.get() == value[12]['Treatment']:
                            del value[12]
                            print("+ Reserve earased !")

                        elif self.deleteRes.get() == value[13]['Treatment']:
                            del value[13]
                            print("+ Reserve earased !")

                        elif self.deleteRes.get() == value[14]['Treatment']:
                            del value[14]
                            print("+ Reserve earased !")
                        else:
                            print("Reserve is not present into medication")

                        if self.deleteRes.get() == '':
                            print("None Reserve checked")
                        else:
                            print("---Ok VALUE 'Reserve' earased---")
                            with open('./ttt/doc_ttt4/convres.json', 'w') as datafile2:
                                json.dump(dataRes, datafile2, indent=4)
            except FileNotFoundError as outinfo:
                print('+ Sorry, file convres.json not exist !', outinfo)
        else:           
            messagebox.showinfo('Return', 'Reserve not earased')

    def copyTttMess():
            #MessageBox to ensure if it's well done.
        MsgBoxayes = messagebox.askyesno('Record', 'Do you want to save ?')
        if MsgBoxayes == 1:
            print("Ok to save")
            copyToFile()
            #app.destroy()
        else:
            messagebox.showinfo('Return', 'You will return to the application')

    def copyToFile():
            #To write all data to intro_ttt.json
            #to reuse them after.
        with open('./ttt/doc_ttt4/intro_ttt.txt', '+a') as file:
            file.write(str("Date : "))
            file.write(self.textDate.get() + '\n')
            file.write(str("Heure : "))
            file.write(self.textHour.get() + '\n')
            file.write(str("Name : "))
            file.write(self.textName.get() + '\n')
            file.write(str("Date of introduction : "))
            file.write(self.comboDay.get())
            file.write(self.comboMonth.get())
            file.write(self.comboYear.get())
            file.write(str('\n'))
            file.write(str("Nom du ttt : "))
            file.write(self.textTreat.get() + '\n')
            file.write(str("Dosage du ttt : "))
            file.write(self.textDosage.get() + '\n')
            if self.CheckVarMatin.get()==1:
                file.write(str("Matin : "))
            file.write(self.Entmatin.get() + '\n')
            if self.CheckVarMidi.get()==1:
                file.write(str("Midi : "))
            file.write(self.Entmidi.get() + '\n')
            if self.CheckVarSoir.get()==1:
                file.write(str("Soir : "))
            file.write(self.Entsoir.get() + '\n')
            if self.CheckVarNuit.get()==1:
                file.write(str("Nuit : "))
            file.write(self.Entnuit.get() + '\n')
            file.write(str("Date of end : "))
            file.write(self.comboFinishDay.get())
            file.write('/' + self.comboFinishMonth.get() + '/')
            file.write(self.comboFinishYear.get())
            file.write(str('\n'))
            file.write(str("Signature : "))
            file.write(self.textSign.get())
            file.write(str('\n\n'))
        try:
            if os.path.getsize('./ttt/doc_ttt4/convdose.json'):
                print("+ File 'convdose' exist !")
                with open('./ttt/doc_ttt4/convdose.json', 'r') as datafile:
                    datastore = json.load(datafile)
                    print(datastore)
                dataDose = datastore
                dataDose['data'].append({'Date' : self.textDate.get(), \
                    'Date of introduction' : self.comboDay.get() + self.comboMonth.get() + \
                    self.comboYear.get(), 'Date of end' : self.comboFinishDay.get() + \
                    '/' + self.comboFinishMonth.get() + '/' + self.comboFinishYear.get(), \
                    'Treatment' : self.textTreat.get(), 'Dosage' : self.textDosage.get(), \
                    'Matin' : self.Entmatin.get(), 'Midi' : self.Entmidi.get(), \
                    'Soir' : self.Entsoir.get(), 'Nuit' : self.Entnuit.get()})
                if self.textTreat.get() == "":
                    print("---No value 'Treatment' introduced---")
                else:
                    print("---Ok value 'Treatment' introduced---")
                    with open('./ttt/doc_ttt4/convdose.json', 'w') as datafile2:
                        json.dump(dataDose, datafile2, indent=4)
        except FileNotFoundError as fnf:
            print('+ Sorry, file convdose.json not exist !', fnf)
            print("+ File convdose.json created !")
            dataDose = {}
            dataDose['data'] = []
            dataDose['data'].append({'Date' : self.textDate.get(), \
                'Date of introduction' : self.comboDay.get() + self.comboMonth.get() + \
                self.comboYear.get(), 'Date of end' : self.comboFinishDay.get() + \
                '/' + self.comboFinishMonth.get() + '/' + self.comboFinishYear.get(), \
                'Treatment' : self.textTreat.get(), 'Dosage' : self.textDosage.get(), \
                'Matin' : self.Entmatin.get(), 'Midi' : self.Entmidi.get(), \
                'Soir' : self.Entsoir.get(), 'Nuit' : self.Entnuit.get()})
            if self.textTreat.get() == "":
                print("---No value 'Treatment' introduced---")
            else:
                print("---Ok value 'Treatment' introduced---")
                with open('./ttt/doc_ttt4/convdose.json', 'w') as datafile:
                    json.dump(dataDose, datafile, indent=4)

    def copyResMess():
        #MessageBox to ensure if it's well done.
        MsgBoxayn = messagebox.askyesno('Record', 'Do you want to save ?')
        if MsgBoxayn == 1:
            print("Ok to save")
            copyToReserve()
            #app.destroy()
        else:
            messagebox.showinfo('Return', 'You will return to the application')

    def copyToReserve():
        #To write all data to intro_res.txt
        #to reuse them after.
        with open('./ttt/doc_ttt4/intro_res.txt', '+a') as file:
            file.write(str("Date : "))
            file.write(self.textDate.get() + '\n')
            file.write(str("Heure : "))
            file.write(self.textHour.get() + '\n')
            file.write(str("Name : "))
            file.write(self.textName.get() + '\n')
            file.write(str("Date of introduction : "))
            file.write(self.comboDay.get())
            file.write(self.comboMonth.get())
            file.write(self.comboYear.get())
            file.write(str('\n'))
            file.write(str("Nom du ttt : "))
            file.write(self.textTreat.get() + '\n')
            file.write(str("Dosage du ttt : "))
            file.write(self.textDosage.get() + '\n')
            if self.CheckVar1.get()==1:
                file.write(str("Réserve : "))
                file.write(str("Oui\n"))
            if self.CheckVar2.get()==1:
                file.write(str("1ère intention : "))
                file.write(str("Oui\n"))
            if self.CheckVar3.get()==1:
                file.write(str("2ème intention : "))
                file.write(str("Oui\n"))
            if self.Rnbre.get()=='':
                print("Pas de réserves!")
                file.write(self.Rnbre.get() + '\n')
            file.write(str("Date of end : "))
            file.write(self.comboFinishDay.get())
            file.write('/' + self.comboFinishMonth.get() + '/')
            file.write(self.comboFinishYear.get())
            file.write(str('\n'))
            file.write(str("Signature : "))
            file.write(self.textSign.get())
            file.write(str('\n\n'))
        try:
            if os.path.getsize('./ttt/doc_ttt4/convres.json'):
                print("+ File 'convres' exist !")
                with open('./ttt/doc_ttt4/convres.json', 'r') as datafile:
                    datastore = json.load(datafile)
                    print(datastore)
                dataDose = datastore
                dataDose['data'].append({'Date' : self.textDate.get(), \
                    'Date of introduction' : self.comboDay.get() + self.comboMonth.get() + \
                    self.comboYear.get(), 'Date of end' : self.comboFinishDay.get() + \
                    '/' + self.comboFinishMonth.get() + '/' + self.comboFinishYear.get(), \
                    'Treatment' : self.textTreat.get(), 'Dosage' : self.textDosage.get(), \
                    'Reserve' : self.CheckVar1.get(), 'First-line' : self.CheckVar2.get(), \
                    'Second-line' : self.CheckVar3.get(), 'Number/24h' : self.Rnbre.get()})
                if self.textTreat.get() == "":
                    print("---No value 'Treatment' introduced---")
                else:
                    print("---Ok value 'Treatment' introduced---")
                    with open('./ttt/doc_ttt4/convres.json', 'w') as datafile2:
                        json.dump(dataDose, datafile2, indent=4)
        except FileNotFoundError as outcom:
            print('+ Sorry, file convres.json not exist !', outcom)
            print("+ File convres.json created !")
            dataDose = {}
            dataDose['data'] = []
            dataDose['data'].append({'Date' : self.textDate.get(), \
                'Date of introduction' : self.comboDay.get() + self.comboMonth.get() + \
                self.comboYear.get(), 'Date of end' : self.comboFinishDay.get() + \
                '/' + self.comboFinishMonth.get() + '/' + self.comboFinishYear.get(), \
                'Treatment' : self.textTreat.get(), 'Dosage' : self.textDosage.get(), \
                'Reserve' : self.CheckVar1.get(), 'First-line' : self.CheckVar2.get(), \
                'Second-line' : self.CheckVar3.get(), 'Number/24h' : self.Rnbre.get()})
            if self.textTreat.get() == "":
                print("+ No value 'Treatment' introduced---")
            elif self.CheckVar2.get() == 0:
                print("+ There is not First-line reserve marked---")
            elif self.CheckVar2.get() != 0:
                print("+ There is First-line reserve marked---")
            elif self.CheckVar3.get() == 0:
                print("+ There is not Second-line reserve marked---")
            elif self.CheckVar3.get() != 0:
                print("+ There is Second-line reserve marked---")
            else:
                print("Problem with reserve registration")
            print("+ Ok, value 'Treatment' introduced---")
            with open('./ttt/doc_ttt4/convres.json', 'w') as datafile:
                json.dump(dataDose, datafile, indent=4)

    def readFileStory():
        try:
            if os.path.getsize("./ttt/doc_ttt4/intro_ttt.txt"):
                subprocess.call("./ttt/doc_ttt4/readstory.py")
        except FileNotFoundError as no_storyfile:
            print("+ Sorry, it's not possible to show tab of ttt, " \
                "no ttt has been introduced !", no_storyfile)
            noStory()

    def noStory():
        messagebox.showinfo("Info", "None historic of ttt is available, " \
            "no ttt has been introduced !") 

    self.x14, self.y14 = 500, 180
    self.buttShowttt = Button(self.can, text="Show ttt", width=10, fg='white',
        bg='RoyalBlue3', bd=3, highlightbackground='cyan', 
        activebackground='pale turquoise', command=showTreat)
    self.buttShowttt_window = self.can.create_window(self.x14, self.y14, window=self.buttShowttt)

    self.x15, self.y15 = 500, 240
    self.buttShowres = Button(self.can, text="Show R", width=10, fg='white',
        bg='RoyalBlue3', bd=3, highlightbackground='cyan', 
        activebackground='pale turquoise', command=showReserve)
    self.buttShowres_window = self.can.create_window(self.x15, self.y15, window=self.buttShowres)

    self.x16, self.y16 = 500, 300
    self.buttStory = Button(self.can, text="Historic", width=10, fg='white',
        bg='RoyalBlue3', bd=3, highlightbackground='cyan', 
        activebackground='pale turquoise', command=readFileStory)
    self.buttStory_window = self.can.create_window(self.x16, self.y16, window=self.buttStory)

    self.x20, self.y20 = 800, 140
    self.textProcess = Label(self.can, text="Processing start date :", 
        font=('Arial 14 bold'), fg='aquamarine', bg='DodgerBlue2', width=40, anchor='w')
    self.textProcess_window = self.can.create_window(self.x20, self.y20, window=self.textProcess)

    def changeDay():
        self.comboDay['values']=['', '01', '02', '03', '04',
                                '05', '06', '07', '08',
                                '09', '10', '11', '12',
                                '13', '14', '15', '16',
                                '17', '18', '19', '20',
                                '21', '22', '23', '24',
                                '25', '26', '27', '28',
                                '29', '30', '31']

    self.labelDay = Label(self.can,
        text = "Choose the day :", font=12, fg='white', bg='DodgerBlue2')
    self.labelDay_window = self.can.create_window(700, 180, window=self.labelDay)

    self.mystring = tk.StringVar()
    self.comboDay = ttk.Combobox(self.can, textvariable=self.mystring,
        values=['', '01', '02', '03', '04',
                '05', '06', '07', '08',
                '09', '10', '11', '12',
                '13', '14', '15', '16',
                '17', '18', '19', '20',
                '21', '22', '23', '24',
                '25', '26', '27', '28',
                '29', '30', '31'], postcommand=changeDay)

    self.comboDay.bind("<<ComboboxSelected>>", callbackDay)
    self.comboDay.current(0)
    self.comboDay_window = self.can.create_window(700, 220, window=self.comboDay)

    def changeMonth():
        self.comboMonth["values"] = ['',
                                    ' January',
                                    ' February',
                                    ' March',
                                    ' April',
                                    ' May',
                                    ' June',
                                    ' July',
                                    ' August',
                                    ' September',
                                    ' October',
                                    ' November',
                                    ' December']

    self.x23, self.y23 = 900, 180
    self.labelMonth = Label(self.can,
        text = "Choose the month :", font=12, fg='white', bg='DodgerBlue2')
    self.labelMonth_window = self.can.create_window(self.x23, self.y23, window=self.labelMonth)

    self.x24, self.y24 = 900, 220
    self.mystring2 = tk.StringVar()
    self.comboMonth = ttk.Combobox(self.can, textvariable=self.mystring2,
        values=['',
                ' January',
                ' February',
                ' March',
                ' April',
                ' May',
                ' June',
                ' July',
                ' August',
                ' September',
                ' October',
                ' November',
                ' December'], postcommand=changeMonth)

    self.comboMonth.bind("<<ComboboxSelected>>", callbackMonth)
    self.comboMonth.current(0)
    self.comboMonth_window = self.can.create_window(self.x24, self.y24, window=self.comboMonth)

    def changeYear():
        self.comboYear["values"] = ['', ' 2000', ' 2001', ' 2002', ' 2003',
                                    ' 2004', ' 2005', ' 2006', ' 2007',
                                    ' 2008', ' 2009', ' 2010', ' 2011',
                                    ' 2012', ' 2013', ' 2014', ' 2015',
                                    ' 2016', ' 2017', ' 2018', ' 2019',
                                    ' 2020', ' 2021', ' 2022', ' 2023',
                                    ' 2024', ' 2025', ' 2026', ' 2027',
                                    ' 2028', ' 2029', ' 2030', ' 2031',
                                    ' 2032', ' 2033', ' 2034', ' 2035']

    self.x25, self.y25 = 1100, 180
    self.labelYear = Label(self.can,
        text = "Choose the year :", font=12, fg='white', bg='DodgerBlue2')
    self.labelYear_window = self.can.create_window(self.x25, self.y25, window=self.labelYear)

    self.x26, self.y26 = 1100, 220
    self.mystring3 = tk.StringVar()
    self.comboYear = ttk.Combobox(self.can, textvariable=self.mystring3,
        values=['', ' 2000', ' 2001', ' 2002', ' 2003',
                ' 2004', ' 2005', ' 2006', ' 2007',
                ' 2008', ' 2009', ' 2010', ' 2011',
                ' 2012', ' 2013', ' 2014', ' 2015',
                ' 2016', ' 2017', ' 2018', ' 2019',
                ' 2020', ' 2021', ' 2022', ' 2023',
                ' 2024', ' 2025', ' 2026', ' 2027',
                ' 2028', ' 2029', ' 2030', ' 2031',
                ' 2032', ' 2033', ' 2034', ' 2035'], postcommand=changeYear)

    self.comboYear.bind("<<ComboboxSelected>>", callbackYear)
    self.comboYear.current(0)
    self.comboYear_window = self.can.create_window(self.x26, self.y26, window=self.comboYear)

    # Date of finish
    self.x27, self.y27 = 800, 270
    self.txtfinishdate = Label(self.can, text="Processing end date :", 
        font=('Arial 14 bold'), fg='aquamarine', bg='DodgerBlue2', width=40, anchor='w')
    self.txtfinishdate_window = self.can.create_window(self.x27, self.y27, window=self.txtfinishdate)

    def finishDay():
        self.comboFinishDay["values"] = ['', '01', '02', '03', '04',
                                        '05', '06', '07', '08',
                                        '09', '10', '11', '12',
                                        '13', '14', '15', '16',
                                        '17', '18', '19', '20',
                                        '21', '22', '23', '24',
                                        '25', '26', '27', '28',
                                        '29', '30', '31']

    self.x28, self.y28 = 700, 310
    self.labelFinishDay = Label(self.can,
        text = "Choose the day :", font=12, fg='white', bg='DodgerBlue2')
    self.labelFinishDay_window = self.can.create_window(self.x28, self.y28, window=self.labelFinishDay)

    self.x29, self.y29 = 700, 350
    self.mystring4 = tk.StringVar()
    self.comboFinishDay = ttk.Combobox(self.can, textvariable=self.mystring4,
        values=['', '01', '02', '03', '04',
                '05', '06', '07', '08',
                '09', '10', '11', '12',
                '13', '14', '15', '16',
                '17', '18', '19', '20',
                '21', '22', '23', '24',
                '25', '26', '27', '28',
                '29', '30', '31'], postcommand=finishDay)

    self.comboFinishDay.bind("<<ComboboxSelected>>", callbackFinishDay)
    self.comboFinishDay.current(0)
    self.comboFinishDay_window = self.can.create_window(self.x29, self.y29, window=self.comboFinishDay)

    def finishMonth():
        self.comboFinishMonth["values"] = ['', '01', '02', '03', '04',
                                            '05', '06', '07', '08',
                                            '09', '10', '11', '12']
    
    self.x30, self.y30 = 900, 310
    self.labelMonth = Label(self.can,
        text = "Choose the month :", font=12, fg='white', bg='DodgerBlue2')
    self.labelMonth_window = self.can.create_window(self.x30, self.y30, window=self.labelMonth)

    self.x31, self.y31 = 900, 350
    self.mystring5 = tk.StringVar()
    self.comboFinishMonth = ttk.Combobox(self.can, textvariable=self.mystring5,
        values=['',
                '01',  
                '02', 
                '03', 
                '04', 
                '05', 
                '06', 
                '07', 
                '08', 
                '09', 
                '10', 
                '11', 
                '12'], postcommand=finishMonth)

    self.comboFinishMonth.bind("<<ComboboxSelected>>", callbackFinishMonth)
    self.comboFinishMonth.current(0)
    self.comboFinishMonth_window = self.can.create_window(self.x31, self.y31, window=self.comboFinishMonth)

    def finishYear():
        self.comboFinishYear["values"] = ['', '2020', '2021', '2022', '2023',
                                        '2024', '2025', '2026', '2027',
                                        '2028', '2029', '2030', '2031',
                                        '2032', '2033', '2034', '2035']

    self.x32, self.y32 = 1100, 310
    self.labelFinishYear = Label(self.can,
        text = "Choose the year :", font=12, fg='white', bg='DodgerBlue2')
    self.labelFinishYear_window = self.can.create_window(self.x32, self.y32, window=self.labelFinishYear)

    self.x33, self.y33 = 1100, 350
    self.mystring6 = tk.StringVar()
    self.comboFinishYear = ttk.Combobox(self.can, textvariable=self.mystring6,
        values=['', '2020', '2021', '2022', '2023',
                '2024', '2025', '2026', '2027',
                '2028', '2029', '2030', '2031',
                '2032', '2033', '2034', '2035'], postcommand=finishYear)

    self.comboFinishYear.bind("<<ComboboxSelected>>", callbackFinishYear)
    self.comboFinishYear.current(0)
    self.comboFinishYear_window = self.can.create_window(self.x33, self.y33, window=self.comboFinishYear)

    self.x34, self.y34 = 100, 380
    self.checkLab = Label(self.can, text="Doses :", font=('Arial 14 bold'), 
        fg='aquamarine', bg='DodgerBlue2')
    self.checkLab_window = self.can.create_window(self.x34, self.y34, window=self.checkLab)

    self.x35, self.y35 = 100, 420
    self.CheckVarMatin = IntVar()
    self.Cma = Checkbutton(self.can, text="Morning --->", fg='navy', 
        bg='cyan', variable=self.CheckVarMatin, 
        onvalue=1, offvalue=0, height=1, 
        width=15, anchor='w')
    self.Cma_window = self.can.create_window(self.x35, self.y35, window=self.Cma)

    self.x36, self.y36 = 300, 420
    self.LabDose = Label(self.can, text='Morning take : ', font=12,
        width=20, fg='white', bg='DodgerBlue2')
    self.LabDose_window = self.can.create_window(self.x36, self.y36, window=self.LabDose)

    self.x37, self.y37 = 500, 380
    self.DosaLab = Label(self.can, text="Unity :", font=('Arial 14 bold'), 
        fg='aquamarine', bg='DodgerBlue2')
    self.DosaLab_window = self.can.create_window(self.x37, self.y37, window=self.DosaLab)

    self.x38, self.y38 = 500, 420
    self.Entmatin = Entry(self.can, highlightbackground='grey', bd=4)
    self.Entmatin_window = self.can.create_window(self.x38, self.y38, window=self.Entmatin)

    self.x39, self.y39 = 100, 460
    self.CheckVarMidi = IntVar()
    self.Cmi = Checkbutton(self.can, text="Noon --->", fg='navy', 
        bg='cyan', variable=self.CheckVarMidi, 
        onvalue=1, offvalue=0, height=1, 
        width=15, anchor='w')
    self.Cmi_window = self.can.create_window(self.x39, self.y39, window=self.Cmi)

    self.x40, self.y40 = 300, 460
    self.Lunchtime = Label(self.can, text='Lunchtime take : ', font=12, 
        width=20, fg='white', bg='DodgerBlue2')
    self.Lunchtime_window = self.can.create_window(self.x40, self.y40, window=self.Lunchtime)

    self.x41, self.y41 = 500, 460
    self.Entmidi = Entry(self.can, highlightbackground='grey', bd=4)
    self.Entmidi_window = self.can.create_window(self.x41, self.y41, window=self.Entmidi)

    self.x42, self.y42 = 100, 500
    self.CheckVarSoir = IntVar()
    self.Csoir = Checkbutton(self.can, text="Evening --->", fg='navy', 
        bg='cyan', variable=self.CheckVarSoir, 
        onvalue=1, offvalue=0, height=1, 
        width=15, anchor='w')
    self.Csoir_window = self.can.create_window(self.x42, self.y42, window=self.Csoir)

    self.x43, self.y43 = 300, 500
    self.Evetake = Label(self.can, text='Evening take : ', font=12,
        width=20, fg='white', bg='DodgerBlue2')
    self.Evetake_window = self.can.create_window(self.x43, self.y43, window=self.Evetake)

    self.x44, self.y44 = 500, 500
    self.Entsoir = Entry(self.can, highlightbackground='grey', bd=4)
    self.Entsoir_window = self.can.create_window(self.x44, self.y44, window=self.Entsoir)

    self.x45, self.y45 = 100, 540
    self.CheckVarNuit = IntVar()
    self.Cnuit = Checkbutton(self.can, text="Night --->", fg='navy', 
        bg='cyan', variable=self.CheckVarNuit, 
        onvalue=1, offvalue=0, height=1, 
        width=15, anchor='w')
    self.Cnuit_window = self.can.create_window(self.x45, self.y45, window=self.Cnuit)

    self.x46, self.y46 = 300, 540
    self.Nightlab = Label(self.can, text='Night-time take : ', font=12,
        width=20, fg='white', bg='DodgerBlue2')
    self.Nightlab_window = self.can.create_window(self.x46, self.y46, window=self.Nightlab)

    self.x47, self.y47 = 500, 540
    self.Entnuit = Entry(self.can, highlightbackground='grey', bd=4)
    self.Entnuit_window = self.can.create_window(self.x47, self.y47, window=self.Entnuit)

    self.x48, self.y48 = 500, 640
    self.buttsavettt = Button(self.can, text="Save as ttt", width=10, fg='yellow',
        bg='RoyalBlue3', bd=3, highlightbackground='cyan',
        activebackground='pale turquoise', command=copyTttMess)
    self.buttsavettt_window = self.can.create_window(self.x48, self.y48, window=self.buttsavettt)

    self.x50, self.y50 = 873, 420
    self.Labelifchoice = Label(self.can,
        text="If medication is a RESERVE make your choice below :",
        font=('Times', 16, 'bold'),fg='white', bg='DodgerBlue2')
    self.Labelifchoice_window = self.can.create_window(self.x50, self.y50, window=self.Labelifchoice)

    self.x51, self.y51 = 700, 460
    self.CheckVar1 = IntVar()
    self.C1 = Checkbutton(self.can, text="Reserve", fg='navy', 
        bg='pale green', variable=self.CheckVar1, 
        onvalue=1, offvalue=0, height=1, 
        width=16, anchor='w')
    self.C1_window = self.can.create_window(self.x51, self.y51, window=self.C1)

    self.x52, self.y52 = 700, 500
    self.CheckVar2 = IntVar()
    self.C2 = Checkbutton(self.can, text="First-line", fg='navy', 
        bg='pale green', variable=self.CheckVar2, 
        onvalue=1, offvalue=0, height=1, 
        width=16, anchor='w')
    self.C2_window = self.can.create_window(self.x52, self.y52, window=self.C2)

    self.x53, self.y53 = 700, 540
    self.CheckVar3 = IntVar()
    self.C3 = Checkbutton(self.can, text="Second-line", fg='navy', 
        bg='pale green', variable=self.CheckVar3, 
        onvalue=1, offvalue=0, height=1, 
        width=16, anchor='w')
    self.C3_window = self.can.create_window(self.x53, self.y53, window=self.C3)

    self.x54, self.y54 = 900, 540
    self.labelresd = Label(self.can, text='Number of R/24h : ', font=12, 
        width=15, fg='white', bg='DodgerBlue2')
    self.labelresd_window = self.can.create_window(self.x54, self.y54, window=self.labelresd)

    self.x55, self.y55 = 1100, 540
    self.Rnbre = Entry(self.can, bd=4, highlightbackground='grey')
    self.Rnbre_window = self.can.create_window(self.x55, self.y55, window=self.Rnbre)

    self.x56, self.y56 = 1100, 590
    self.buttsaveres = Button(self.can, text="Save as R", width=10, fg='yellow',
        bg='RoyalBlue3', bd=3, highlightbackground='cyan',
        activebackground='pale turquoise', command=copyResMess)
    self.buttsaveres_window = self.can.create_window(self.x56, self.y56, window=self.buttsaveres)

    self.x57, self.y57 = 110, 620
    self.delttt = StringVar()
    self.deleteTreat = Entry(self.can, bd=4, textvariable=self.delttt,
        highlightbackground='red')
    self.delttt.set("Enter ttt to stop")
    self.deleteTreat_window = self.can.create_window(self.x57, self.y57, window=self.deleteTreat)

    self.x58, self.y58 = 280, 620
    self.buttStopttt = Button(self.can, text="Stop ttt", width=10, fg='yellow',
        bg='red', bd=3, highlightbackground='cyan',
        activebackground='coral', command=deleteTreatment)
    self.buttStopttt_window = self.can.create_window(self.x58, self.y58, window=self.buttStopttt)

    self.x59, self.y59 = 110, 660
    self.deleteRes = Entry()
    self.delete_res = StringVar()
    self.delete_res.set("Enter R to stop")
    self.deleteRes = Entry(self.can, bd=4, textvariable=self.delete_res,
        highlightbackground='red')
    self.deleteRes_window = self.can.create_window(self.x59, self.y59, window=self.deleteRes)

    self.x60, self.y60 = 280, 660
    self.buttStopttt = Button(self.can, text="Stop R", width=10, fg='yellow',
        bg='red', bd=3, highlightbackground='cyan',
        activebackground='coral', command=deleteReserve, padx=10)
    self.buttStopttt_window = self.can.create_window(self.x60, self.y60, window=self.buttStopttt)

    self.x61, self.y61 = 500, 590
    self.LabSign = Label(self.can, text='Signature :', font=12, 
        width=15, fg='red', bg='pale green')
    self.LabSign_window = self.can.create_window(self.x61, self.y61, window=self.LabSign)

    self.x62, self.y62 = 700, 590
    self.textSign = Entry(self.can, highlightbackground='grey', bd=4)
    self.textSign_window = self.can.create_window(self.x62, self.y62, window=self.textSign)

    def awayOut():
        try:
            self.can.delete(ALL)
            self.showPatients()
        except (OSError, ValueError) as p_out:
            print("Error from labo to way out", p_out)

    self.x63, self.y63 = 1100, 660
    self.buttQuit = Button(self.can, text="Return to main menu", width=20, fg='white',
        bg='RoyalBlue3', bd=3, highlightbackground='cyan',
        activebackground='pale turquoise', command=awayOut)
    self.buttQuit_window = self.can.create_window(self.x63, self.y63, window=self.buttQuit)

    self.can.configure(scrollregion=self.can.bbox(ALL))
