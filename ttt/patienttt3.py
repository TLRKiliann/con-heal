#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
import os
import json
import subprocess


def callTreatment3(self):
    self.can.delete(ALL)
    self.can.configure(bg='DodgerBlue2')

    self.x1, self.y1 = 625, 40
    self.textLab = Label(self.can, text="Introduction of treatement (ttt)",
        font=('Times', 22, 'bold'), fg='aquamarine', bg='DodgerBlue2')
    self.textLab = self.can.create_window(self.x1, self.y1, window=self.textLab)

    self.x2, self.y2 = 370, 80
    self.labelallergy = Label(self.can, text="Allergy : ",
        font=('Arial', 18, 'bold'), fg='coral', bg='DodgerBlue2')
    self.labelallergy = self.can.create_window(self.x2, self.y2, window=self.labelallergy)

    # To read allergy for entry widget
    with open('./newpatient/entryfile3.txt', 'r') as filename2:
        line1 = filename2.readline()
        line2 = filename2.readline()
        line3 = filename2.readline()

    self.x3, self.y3 = 680, 80
    entrytext = StringVar()
    self.entryName = Entry(self.can, textvariable=entrytext, width=60)
    entrytext.set(line3)
    self.entryName = self.can.create_window(self.x3, self.y3, window=self.entryName)

    def callbackDay(event):
        print(self.comboDay.get())

    def callbackMonth(event):
        print(self.comboMonth.get())

    def callbackYear(event):
        print(self.comboYear.get())

    def callbackFinishDay(event):
        print(comboFinishDay.get())

    def callbackFinishMonth(event):
        print(comboFinishMonth.get())

    def callbackFinishYear(event):
        print(comboFinishYear.get())
    """
    def showTreat():
            #To display tabs of ttt, convdose.json 
            #file must be existing.
        try:
            if os.path.getsize('./ttt/doc_ttt3/convdose.json'):
                subprocess.call('./ttt/doc_ttt3/tabs.py')
        except FileNotFoundError as no_tabs:
            print("+ Sorry, it's not possible to show tab of ttt, \
                convdose.json file missing !")
            tttTabs()

    def tttTabs():
        messagebox.showinfo("Info", "No ttt recorded for \
            this patient, convdose.json file missing !") 

    def showReserve():
            #To display tabs of reserve, convres.json 
            #file must be existing.
        try:
            if os.path.getsize('./ttt/doc_ttt3/convres.json'):
                subprocess.call('./ttt/doc_ttt3/tabres.py')
        except FileNotFoundError as no_tabs:
            print("+ Sorry, it's not possible to show tab of reserve, \
                convres.json file missing !")
            reserveTabs()

    def reserveTabs():
        messagebox.showinfo("Info", "No reserve recorded for \
            this patient, convres.json file missing !")

    def deleteTreatment():
            #To earase one line in array
            #for one treatment
        MSB = messagebox.askyesno('Delete ttt', 'Are you sure ?')
        if MSB == 1:
            print("+ Ok, ttt has been ejected !")
            messagebox.showinfo('info BOX', 'Treatment is away !')
            try:
                if os.path.getsize('./ttt/doc_ttt3/convdose.json'):
                    print("+ File 'convdose' exist !")
                    with open('./ttt/doc_ttt3/convdose.json', 'r') as datafile:
                        datastore = json.load(datafile)
                    
                    dataDose = datastore
                    for key, value in dataDose.items():
                        if deleteTreat.get() == value[0]['Treatment']:
                            del value[0]
                            print("+ TTT earased !")

                        elif deleteTreat.get() == value[1]['Treatment']:
                            del value[1]
                            print("+ TTT earased !")

                        elif deleteTreat.get() == value[2]['Treatment']:
                            del value[2]
                            print("+ TTT earased !")
                            
                        elif deleteTreat.get() == value[3]['Treatment']:
                            del value[3]
                            print("+ TTT earased !")

                        elif deleteTreat.get() == value[4]['Treatment']:
                            del value[4]
                            print("+ TTT earased !")

                        elif deleteTreat.get() == value[5]['Treatment']:
                            del value[5]
                            print("+ TTT earased !")

                        elif deleteTreat.get() == value[6]['Treatment']:
                            del value[6]
                            print("+ TTT earased !")

                        elif deleteTreat.get() == value[7]['Treatment']:
                            del value[7]
                            print("+ TTT earased !")

                        elif deleteTreat.get() == value[8]['Treatment']:
                            del value[8]
                            print("+ TTT earased !")

                        elif deleteTreat.get() == value[9]['Treatment']:
                            del value[9]
                            print("+ TTT earased !")

                        elif deleteTreat.get() == value[10]['Treatment']:
                            del value[10]
                            print("+ TTT earased !")

                        elif deleteTreat.get() == value[11]['Treatment']:
                            del value[11]
                            print("+ TTT earased !")

                        elif deleteTreat.get() == value[12]['Treatment']:
                            del value[12]
                            print("+ TTT earased !")

                        elif deleteTreat.get() == value[13]['Treatment']:
                            del value[13]
                            print("+ TTT earased !")

                        elif deleteTreat.get() == value[14]['Treatment']:
                            del value[14]
                            print("+ TTT earased !")
                        else:
                            print("Treatment is not present into medication")

                        if deleteTreat.get() == '':
                            print("None treatment checked")
                        else:
                            print("---Ok VALUE 'Treatment' earased---")
                            with open('./ttt/doc_ttt3/convdose.json', 'w') as datafile2:
                                json.dump(dataDose, datafile2, indent=4)
            except FileNotFoundError as outcom:
                print('+ Sorry, file convdose.json not exist !', outcom)
        else:           
            messagebox.showinfo('Return', 'Treatment not earased')

    def deleteReserve():
            #To earase one line in array
            #for one Reserve
        MSB2 = messagebox.askyesno('Delete Reserve', 'Are you sure ?')
        if MSB2 == 1:
            print("Ok, Reserve has been ejected !")
            messagebox.showinfo('info BOX', 'Reserve is away !')
            try:
                if os.path.getsize('./ttt/doc_ttt3/convres.json'):
                    print("+ File 'convres' exist !")
                    with open('./ttt/doc_ttt3/convres.json', 'r') as datafile:
                        datastore = json.load(datafile)
                    
                    dataRes = datastore
                    for key, value in dataRes.items():
                        if deleteRes.get() == value[0]['Treatment']:
                            del value[0]
                            print("+ Reserve earased !")

                        elif deleteRes.get() == value[1]['Treatment']:
                            del value[1]
                            print("+ Reserve earased !")

                        elif deleteRes.get() == value[2]['Treatment']:
                            del value[2]
                            print("+ Reserve earased !")
                            
                        elif deleteRes.get() == value[3]['Treatment']:
                            del value[3]
                            print("+ Reserve earased !")

                        elif deleteRes.get() == value[4]['Treatment']:
                            del value[4]
                            print("+ Reserve earased !")

                        elif deleteRes.get() == value[5]['Treatment']:
                            del value[5]
                            print("+ Reserve earased !")

                        elif deleteRes.get() == value[6]['Treatment']:
                            del value[6]
                            print("+ Reserve earased !")

                        elif deleteRes.get() == value[7]['Treatment']:
                            del value[7]
                            print("+ Reserve earased !")

                        elif deleteRes.get() == value[8]['Treatment']:
                            del value[8]
                            print("+ Reserve earased !")

                        elif deleteRes.get() == value[9]['Treatment']:
                            del value[9]
                            print("+ Reserve earased !")

                        elif deleteRes.get() == value[10]['Treatment']:
                            del value[10]
                            print("+ Reserve earased !")

                        elif deleteRes.get() == value[11]['Treatment']:
                            del value[11]
                            print("+ Reserve earased !")

                        elif deleteRes.get() == value[12]['Treatment']:
                            del value[12]
                            print("+ Reserve earased !")

                        elif deleteRes.get() == value[13]['Treatment']:
                            del value[13]
                            print("+ Reserve earased !")

                        elif deleteRes.get() == value[14]['Treatment']:
                            del value[14]
                            print("+ Reserve earased !")
                        else:
                            print("Reserve is not present into medication")

                        if deleteRes.get() == '':
                            print("None Reserve checked")
                        else:
                            print("---Ok VALUE 'Reserve' earased---")
                            with open('./ttt/doc_ttt3/convres.json', 'w') as datafile2:
                                json.dump(dataRes, datafile2, indent=4)
            except FileNotFoundError as outinfo:
                print('+ Sorry, file convres.json not exist !', outinfo)
        else:           
            messagebox.showinfo('Return', 'Reserve not earased')

    def copyTttMess():
            #MessageBox to ensure if it's well done.
        messagebox.askyesno('Record', 'Do you want to save ?')
        if MsgBox == 1:
            print("Ok to save")
            copyToFile()
            #app.destroy()
        else:
            messagebox.showinfo('Return', 'You will return to the application')

    def copyToFile():
            #To write all data to intro_ttt.json
            #to reuse them after.
        with open('./ttt/doc_ttt3/intro_ttt.txt', '+a') as file:
            file.write(str("Date : "))
            file.write(textDate.get() + '\n')
            file.write(str("Heure : "))
            file.write(textHour.get() + '\n')
            file.write(str("Name : "))
            file.write(textName.get() + '\n')
            file.write(str("Date of introduction : "))
            file.write(comboDay.get())
            file.write(comboMonth.get())
            file.write(comboYear.get())
            file.write(str('\n'))
            file.write(str("Nom du ttt : "))
            file.write(textTreat.get() + '\n')
            file.write(str("Dosage du ttt : "))
            file.write(textDosage.get() + '\n')
            if CheckVarMatin.get()==1:
                file.write(str("Matin : "))
            file.write(Entmatin.get() + '\n')
            if CheckVarMidi.get()==1:
                file.write(str("Midi : "))
            file.write(Entmidi.get() + '\n')
            if CheckVarSoir.get()==1:
                file.write(str("Soir : "))
            file.write(Entsoir.get() + '\n')
            if CheckVarNuit.get()==1:
                file.write(str("Nuit : "))
            file.write(Entnuit.get() + '\n')
            file.write(str("Date of end : "))
            file.write(comboFinishDay.get())
            file.write('/' + comboFinishMonth.get() + '/')
            file.write(comboFinishYear.get())
            file.write(str('\n'))
            file.write(str("Signature : "))
            file.write(textSign.get())
            file.write(str('\n\n'))
        try:
            if os.path.getsize('./ttt/doc_ttt3/convdose.json'):
                print("+ File 'convdose' exist !")
                with open('./ttt/doc_ttt3/convdose.json', 'r') as datafile:
                    datastore = json.load(datafile)
                    print(datastore)
                dataDose = datastore
                dataDose['data'].append({'Date' : textDate.get(), \
                    'Date of introduction' : comboDay.get() + comboMonth.get() + \
                    comboYear.get(), 'Date of end' : comboFinishDay.get() + \
                    '/' + comboFinishMonth.get() + '/' + comboFinishYear.get(), \
                    'Treatment' : textTreat.get(), 'Dosage' : textDosage.get(), \
                    'Matin' : Entmatin.get(), 'Midi' : Entmidi.get(), \
                    'Soir' : Entsoir.get(), 'Nuit' : Entnuit.get()})
                if textTreat.get() == "":
                    print("---No value 'Treatment' introduced---")
                else:
                    print("---Ok value 'Treatment' introduced---")
                    with open('./ttt/doc_ttt3/convdose.json', 'w') as datafile2:
                        json.dump(dataDose, datafile2, indent=4)
        except FileNotFoundError as outcom:
            print('+ Sorry, file convdose.json not exist !')
            print(str(outcom))
            print("+ File convdose.json created !")
            dataDose = {}
            dataDose['data'] = []
            dataDose['data'].append({'Date' : textDate.get(), \
                'Date of introduction' : comboDay.get() + comboMonth.get() + \
                comboYear.get(), 'Date of end' : comboFinishDay.get() + \
                '/' + comboFinishMonth.get() + '/' + comboFinishYear.get(), \
                'Treatment' : textTreat.get(), 'Dosage' : textDosage.get(), \
                'Matin' : Entmatin.get(), 'Midi' : Entmidi.get(), \
                'Soir' : Entsoir.get(), 'Nuit' : Entnuit.get()})
            if textTreat.get() == "":
                print("---No value 'Treatment' introduced---")
            else:
                print("---Ok value 'Treatment' introduced---")
                with open('./ttt/doc_ttt3/convdose.json', 'w') as datafile:
                    json.dump(dataDose, datafile, indent=4)

    def copyResMess():
        #MessageBox to ensure if it's well done.
        MsgBox = messagebox.askyesno('Record', 'Do you want to save ?')
        if MsgBox == 1:
            print("Ok to save")
            copyToReserve()
            #app.destroy()
        else:
            messagebox.showinfo('Return', 'You will return to the application')

    def copyToReserve():
        #To write all data to intro_res.txt
        #to reuse them after.
        with open('./ttt/doc_ttt3/intro_res.txt', '+a') as file:
            file.write(str("Date : "))
            file.write(textDate.get() + '\n')
            file.write(str("Heure : "))
            file.write(textHour.get() + '\n')
            file.write(str("Name : "))
            file.write(textName.get() + '\n')
            file.write(str("Date of introduction : "))
            file.write(comboDay.get())
            file.write(comboMonth.get())
            file.write(comboYear.get())
            file.write(str('\n'))
            file.write(str("Nom du ttt : "))
            file.write(textTreat.get() + '\n')
            file.write(str("Dosage du ttt : "))
            file.write(textDosage.get() + '\n')
            if CheckVar1.get()==1:
                file.write(str("Réserve : "))
                file.write(str("Oui\n"))
            if CheckVar2.get()==1:
                file.write(str("1ère intention : "))
                file.write(str("Oui\n"))
            if CheckVar3.get()==1:
                file.write(str("2ème intention : "))
                file.write(str("Oui\n"))
            if Rnbre.get()=='':
                print("Pas de réserves!")
                file.write(Rnbre.get() + '\n')
            file.write(str("Date of end : "))
            file.write(comboFinishDay.get())
            file.write('/' + comboFinishMonth.get() + '/')
            file.write(comboFinishYear.get())
            file.write(str('\n'))
            file.write(str("Signature : "))
            file.write(textSign.get())
            file.write(str('\n\n'))
        try:
            if os.path.getsize('./ttt/doc_ttt3/convres.json'):
                print("+ File 'convres' exist !")
                with open('./ttt/doc_ttt3/convres.json', 'r') as datafile:
                    datastore = json.load(datafile)
                    print(datastore)
                dataDose = datastore
                dataDose['data'].append({'Date' : textDate.get(), \
                    'Date of introduction' : comboDay.get() + comboMonth.get() + \
                    comboYear.get(), 'Date of end' : comboFinishDay.get() + \
                    '/' + comboFinishMonth.get() + '/' + comboFinishYear.get(), \
                    'Treatment' : textTreat.get(), 'Dosage' : textDosage.get(), \
                    'Reserve' : CheckVar1.get(), 'First-line' : CheckVar2.get(), \
                    'Second-line' : CheckVar3.get(), 'Number/24h' : Rnbre.get()})
                if textTreat.get() == "":
                    print("---No value 'Treatment' introduced---")
                else:
                    print("---Ok value 'Treatment' introduced---")
                    with open('./ttt/doc_ttt3/convres.json', 'w') as datafile2:
                        json.dump(dataDose, datafile2, indent=4)
        except FileNotFoundError as outcom:
            print('+ Sorry, file convres.json not exist !')
            print(str(outcom))
            print("+ File convres.json created !")
            dataDose = {}
            dataDose['data'] = []
            dataDose['data'].append({'Date' : textDate.get(), \
                'Date of introduction' : comboDay.get() + comboMonth.get() + \
                comboYear.get(), 'Date of end' : comboFinishDay.get() + \
                '/' + comboFinishMonth.get() + '/' + comboFinishYear.get(), \
                'Treatment' : textTreat.get(), 'Dosage' : textDosage.get(), \
                'Reserve' : CheckVar1.get(), 'First-line' : CheckVar2.get(), \
                'Second-line' : CheckVar3.get(), 'Number/24h' : Rnbre.get()})
            if textTreat.get() == "":
                print("+ No value 'Treatment' introduced---")
            elif CheckVar2.get() == 0:
                print("+ There is not First-line reserve marked---")
            elif CheckVar2.get() != 0:
                print("+ There is First-line reserve marked---")
            elif CheckVar3.get() == 0:
                print("+ There is not Second-line reserve marked---")
            elif CheckVar3.get() != 0:
                print("+ There is Second-line reserve marked---")
            else:
                print("Problem with reserve registration")
            print("+ Ok, value 'Treatment' introduced---")
            with open('./ttt/doc_ttt3/convres.json', 'w') as datafile:
                json.dump(dataDose, datafile, indent=4)

    def readFileStory():
        try:
            if os.path.getsize("./ttt/doc_ttt3/intro_ttt.txt"):
                subprocess.call("./ttt/doc_ttt3/readstory.py")
        except FileNotFoundError as no_storyfile:
            print("+ Sorry, it's not possible to show tab of ttt, \
                no ttt has been introduced !", no_storyfile)
            noStory()

    def noStory():
        messagebox.showinfo("Info", "None historic of ttt is available, \
            no ttt has been introduced !") 
    """
    self.x4, self.y4 = 120, 140
    self.LabDate = Label(self.can, text="Date : ", width=15, font=12,
        fg='cyan', bg='RoyalBlue4', anchor='e')
    self.LabDate = self.can.create_window(self.x4, self.y4, window=self.LabDate)

    self.x5, self.y5 = 120, 170
    self.LabHour = Label(self.can, text="Hour : ", width=15, font=12,
        fg='cyan', bg='RoyalBlue4', anchor='e')
    self.LabHour = self.can.create_window(self.x5, self.y5, window=self.LabHour)

    self.x6, self.y6 = 120, 200
    self.LabName = Label(self.can, text="Patient's name : ", width=15, font=12,
        fg='cyan', bg='RoyalBlue4', anchor='e')
    self.LabName = self.can.create_window(self.x6, self.y6, window=self.LabName)

    self.x7, self.y7 = 120, 230
    self.LabTreat = Label(self.can, text='Name of drug : ', width=15, 
        font=12, fg='cyan', bg='RoyalBlue4', anchor='e')
    self.LabTreat = self.can.create_window(self.x7, self.y7, window=self.LabTreat)

    self.x8, self.y8 = 120, 260
    self.LabDose = Label(self.can, text="Dose : ", width=15, font=12,
        fg='cyan', bg='RoyalBlue4', anchor='e')
    self.LabDose = self.can.create_window(self.x8, self.y8, window=self.LabDose)

    self.x9, self.y9 = 300, 140
    time_string = IntVar()
    self.textDate = Entry(self.can, textvariable=time_string,
        highlightbackground='grey', bd=4)
    time_string.set(time.strftime("%d/%m/%Y"))
    self.textDate = self.can.create_window(self.x9, self.y9, window=self.textDate)

    self.x10, self.y10 = 300, 170
    time_Htring = IntVar()
    self.textHour = Entry(self.can, textvariable=time_Htring,
        highlightbackground='grey', bd=4)
    time_Htring.set(time.strftime("%H:%M:%S"))
    self.textHour = self.can.create_window(self.x10, self.y10, window=self.textHour)

    # To read name of patient for entry widget
    with open('./newpatient/entryfile3.txt', 'r') as filename:
        line1=filename.readline()

    self.x11, self.y11 = 300, 200
    name_text = StringVar()
    self.textName = Entry(self.can, textvariable=name_text,
        highlightbackground='grey', bd=4)
    name_text.set(line1)
    self.textName = self.can.create_window(self.x11, self.y11, window=self.textName)

    self.x12, self.y12 = 300, 230
    ttt_name = StringVar()
    self.textTreat = Entry(self.can, textvariable=ttt_name,
        highlightbackground='grey', bd=4)
    ttt_name.set("Drug")
    self.textTreat = self.can.create_window(self.x12, self.y12, window=self.textTreat)

    self.x13, self.y13 = 300, 260
    tttDosage = StringVar()
    self.textDosage = Entry(self.can, textvariable=tttDosage,
        highlightbackground='grey', bd=4)
    tttDosage.set("mcg/ml/mg/UI/gttes")
    self.textDosage = self.can.create_window(self.x13, self.y13, window=self.textDosage)

    """
    self.x14, self.y14 = 200, 260
    delete_text = StringVar()
    self.deleteTreat = Entry(self.can, textvariable=delete_text,
        highlightbackground='red', bd=4)
    delete_text.set("Enter ttt to stop")
    self.deleteTreat = self.can.create_window(self.x14, self.y14, window=self.deleteTreat)

    # Button to stop ttt and R
    buttStopttt = Button(self.can, text="Stop ttt", width=10, fg='yellow',
        bg='red', bd=3, highlightbackground='RoyalBlue4',
        activebackground='coral', command=deleteTreatment)
    buttStopttt.grid(row=3, column=3, padx=10)

    deleteRes = Entry(self.can)
    delete_res = StringVar()
    delete_res.set("Enter R to stop")
    deleteRes = Entry(textvariable=delete_res,
        highlightbackground='red', bd=4)
    deleteRes.grid(row=5, column=2)

    # Buttons with functions
    buttStopttt = Button(self.can, text="Stop R", width=10, fg='yellow',
        bg='red', bd=3, highlightbackground='RoyalBlue4',
        activebackground='coral', command=deleteReserve, padx=10)
    buttStopttt.grid(row=5, column=3)

    buttShowttt = Button(self.can, text="Show ttt", width=10, fg='cyan',
        bg='RoyalBlue3', bd=3, highlightbackground='RoyalBlue4', 
        activebackground='dark turquoise', command=showTreat)
    buttShowttt.grid(row=7, column=2)

    buttShowttt = Button(self.can, text="Show R", width=10, fg='cyan',
        bg='RoyalBlue3', bd=3, highlightbackground='RoyalBlue4', 
        activebackground='dark turquoise', command=showReserve)
    buttShowttt.grid(row=7, column=3)
    """
    self.x20, self.y20 = 650, 140
    self.textDateS = Label(self.can, text="Processing start date :", 
        font=('Arial 14 bold'), fg='aquamarine', bg='RoyalBlue4', width=40, anchor='w')
    self.textDateS = self.can.create_window(self.x20, self.y20, window=self.textDateS)

    def changeDay():
        self.comboDay["values"] = ['01', '02', '03', '04',
                              '05', '06', '07', '08',
                              '09', '10', '11', '12',
                              '13', '14', '15', '16',
                              '17', '18', '19', '20',
                              '21', '22', '23', '24',
                              '25', '26', '27', '28',
                              '29', '30', '31']
    self.x21, self.y21 = 600, 180
    self.labelDay = Label(self.can,
        text = "Choose the day :", font=12, fg='cyan', bg='RoyalBlue4')
    self.labelDay = self.can.create_window(self.x21, self.y21, window=self.labelDay)

    self.x22, self.y22 = 600, 220
    self.comboDay = ttk.Combobox(self.can,
        values=['01', '02', '03', '04',
                '05', '06', '07', '08',
                '09', '10', '11', '12',
                '13', '14', '15', '16',
                '17', '18', '19', '20',
                '21', '22', '23', '24',
                '25', '26', '27', '28',
                '29', '30', '31'], postcommand=changeDay)
    self.comboDay.bind("<<ComboboxSelected>>", callbackDay)
    self.comboDay = self.can.create_window(self.x22, self.y22, window=self.comboDay)

    def changeMonth():
        self.comboMonth["values"] = [' January',
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

    self.x23, self.y23 = 800, 180
    self.labelMonth = Label(self.can,
        text = "Choose the month :", font=12, fg='cyan', bg='RoyalBlue4')
    self.labelMonth = self.can.create_window(self.x23, self.y23, window=self.labelMonth)

    self.x24, self.y24 = 800, 220
    self.comboMonth = ttk.Combobox(self.can,
        values=[' January',
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
    self.comboMonth = self.can.create_window(self.x24, self.y24, window=self.comboMonth)

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

    self.x25, self.y25 = 1000, 180
    self.labelYear = Label(self.can,
        text = "Choose the year :", font=12, fg='cyan', bg='RoyalBlue4')
    self.labelYear = self.can.create_window(self.x25, self.y25, window=self.labelYear)

    self.x26, self.y26 = 1000, 220
    self.comboYear = ttk.Combobox(self.can,
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
    self.comboYear = self.can.create_window(self.x26, self.y26, window=self.comboYear)


    # Date of finish
    self.x27, self.y27 = 650, 260
    self.txtfinishdate = Label(self.can, text="Processing end date :", 
        font=('Arial 14 bold'), fg='aquamarine', bg='RoyalBlue4', width=40, anchor='w')
    self.txtfinishdate = self.can.create_window(self.x27, self.y27, window=self.txtfinishdate)


    def finishDay():
        self.comboFinishDay["values"] = ['01', '02', '03', '04',
                                    '05', '06', '07', '08',
                                    '09', '10', '11', '12',
                                    '13', '14', '15', '16',
                                    '17', '18', '19', '20',
                                    '21', '22', '23', '24',
                                    '25', '26', '27', '28',
                                    '29', '30', '31']
    self.x28, self.y28 = 600, 300
    self.labelFinishDay = Label(self.can,
        text = "Choose the day :", font=12, fg='cyan', bg='RoyalBlue4')
    self.labelFinishDay = self.can.create_window(self.x28, self.y28, window=self.labelFinishDay)

    self.x29, self.y29 = 600, 340
    self.comboFinishDay = ttk.Combobox(self.can,
        values=['01', '02', '03', '04',
                '05', '06', '07', '08',
                '09', '10', '11', '12',
                '13', '14', '15', '16',
                '17', '18', '19', '20',
                '21', '22', '23', '24',
                '25', '26', '27', '28',
                '29', '30', '31'], postcommand=finishDay)
    self.comboFinishDay.bind("<<ComboboxSelected>>", callbackFinishDay)
    self.comboFinishDay = self.can.create_window(self.x29, self.y29, window=self.comboFinishDay)

    def finishMonth():
        self.comboFinishMonth["values"] = ['01',
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
                                    '12']
    
    self.x30, self.y30 = 800, 300
    self.labelMonth = Label(self.can,
        text = "Choose the month :", font=12, fg='cyan', bg='RoyalBlue4')
    self.labelMonth = self.can.create_window(self.x30, self.y30, window=self.labelMonth)

    self.comboFinishMonth = ttk.Combobox(self.can,
        values=['01',  
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

    self.x31, self.y31 = 800, 340
    self.comboFinishMonth.bind("<<ComboboxSelected>>", callbackFinishMonth)
    self.comboFinishMonth = self.can.create_window(self.x31, self.y31, window=self.comboFinishMonth)

    def finishYear():
        self.comboFinishYear["values"] = ['', '2020', '2021', '2022', '2023',
                                     '2024', '2025', '2026', '2027',
                                     '2028', '2029', '2030', '2031',
                                     '2032', '2033', '2034', '2035']

    self.x32, self.y32 = 1000, 300
    self.labelFinishYear = Label(self.can,
        text = "Choose the year :", font=12, fg='cyan', bg='RoyalBlue4')
    self.labelFinishYear = self.can.create_window(self.x32, self.y32, window=self.labelFinishYear)

    self.x33, self.y33 = 1000, 340
    self.comboFinishYear = ttk.Combobox(self.can,
        values=['', '2020', '2021', '2022', '2023',
                '2024', '2025', '2026', '2027',
                '2028', '2029', '2030', '2031',
                '2032', '2033', '2034', '2035'], postcommand=finishYear)
    self.comboFinishYear.bind("<<ComboboxSelected>>", callbackFinishYear)
    self.comboFinishYear.current(0)
    self.comboFinishYear = self.can.create_window(self.x33, self.y33, window=self.comboFinishYear)

    """
    self.x34, self.y34 = 800, 600
    self.buttStory = Button(self.can, text="Historic", width=10, fg='cyan',
        bg='RoyalBlue3', bd=3, highlightbackground='RoyalBlue4', 
        activebackground='dark turquoise', command=readFileStory)
    self.buttStory = self.can.create_window(self.x34, self.y34, window=self.buttStory)
    """

    self.x34, self.y34 = 100, 400
    self.checkLab = Label(self.can, text="Doses :", font=('Arial 14 bold'), 
        fg='aquamarine', bg='RoyalBlue4')
    self.checkLab = self.can.create_window(self.x34, self.y34, window=self.checkLab)

    # CheckBox
    self.x35, self.y35 = 100, 440
    CheckVarMatin = IntVar()
    self.Cma = Checkbutton(self.can, text="Morning --->", fg='navy', 
        bg='cyan', variable=CheckVarMatin, 
        onvalue=1, offvalue=0, height=1, 
        width=15, anchor='w')
    self.Cma = self.can.create_window(self.x35, self.y35, window=self.Cma)

    self.x36, self.y36 = 300, 440
    self.LabDose = Label(self.can, text='Morning take : ', font=12,
        width=20, fg='cyan', bg='RoyalBlue4')
    self.LabDose = self.can.create_window(self.x36, self.y36, window=self.LabDose)

    self.x37, self.y37 = 500, 400
    self.DosaLab = Label(self.can, text="Unity :", font=('Arial 14 bold'), 
        fg='aquamarine', bg='RoyalBlue4')
    self.DosaLab = self.can.create_window(self.x37, self.y37, window=self.DosaLab)

    self.x38, self.y38 = 500, 440
    self.Entmatin = Entry(self.can, highlightbackground='grey', bd=4)
    self.Entmatin = self.can.create_window(self.x38, self.y38, window=self.Entmatin)

    self.x39, self.y39 = 100, 480
    CheckVarMidi = IntVar()
    self.Cmi = Checkbutton(self.can, text="Noon --->", fg='navy', 
        bg='cyan', variable=CheckVarMidi, 
        onvalue=1, offvalue=0, height=1, 
        width=15, anchor='w')
    self.Cmi = self.can.create_window(self.x39, self.y39, window=self.Cmi)

    self.x40, self.y40 = 300, 480
    self.Lunchtime = Label(self.can, text='Lunchtime take : ', font=12, 
        width=20, fg='cyan', bg='RoyalBlue4')
    self.Lunchtime = self.can.create_window(self.x40, self.y40, window=self.Lunchtime)

    self.x41, self.y41 = 500, 480
    self.Entmidi = Entry(self.can, highlightbackground='grey', bd=4)
    self.Entmidi = self.can.create_window(self.x41, self.y41, window=self.Entmidi)

    self.x42, self.y42 = 100, 520
    CheckVarSoir = IntVar()
    self.Csoir = Checkbutton(self.can, text="Evening --->", fg='navy', 
        bg='cyan', variable=CheckVarSoir, 
        onvalue=1, offvalue=0, height=1, 
        width=15, anchor='w')
    self.Csoir = self.can.create_window(self.x42, self.y42, window=self.Csoir)

    self.x43, self.y43 = 300, 520
    self.Evetake = Label(self.can, text='Evening take : ', font=12,
        width=20, fg='cyan', bg='RoyalBlue4')
    self.Evetake = self.can.create_window(self.x43, self.y43, window=self.Evetake)

    self.x44, self.y44 = 500, 520
    self.Entsoir = Entry(self.can, highlightbackground='grey', bd=4)
    self.Entsoir = self.can.create_window(self.x44, self.y44, window=self.Entsoir)

    self.x45, self.y45 = 100, 560
    CheckVarNuit = IntVar()
    self.Cnuit = Checkbutton(self.can, text="Night --->", fg='navy', 
        bg='cyan', variable=CheckVarNuit, 
        onvalue=1, offvalue=0, height=1, 
        width=15, anchor='w')
    self.Cnuit = self.can.create_window(self.x45, self.y45, window=self.Cnuit)

    self.x46, self.y46 = 300, 560
    self.Nightlab = Label(self.can, text='Night-time take : ', font=12,
        width=20, fg='cyan', bg='RoyalBlue4')
    self.Nightlab = self.can.create_window(self.x46, self.y46, window=self.Nightlab)

    self.x47, self.y47 = 500, 560
    self.Entnuit = Entry(self.can, highlightbackground='grey', bd=4)
    self.Entnuit = self.can.create_window(self.x47, self.y47, window=self.Entnuit)


    """
    CheckVar1 = IntVar()
    C1 = tk.Checkbutton(self.can, text="Reserve", fg='navy', 
        bg='pale green', variable=CheckVar1, 
        onvalue=1, offvalue=0, height=1, 
        width=20, anchor='w')
    C1.grid(row=20, column=0, pady=10)

    CheckVar2 = IntVar()
    C2 = tk.Checkbutton(self.can, text="First-line", fg='navy', 
        bg='pale green', variable=CheckVar2, 
        onvalue=1, offvalue=0, height=1, 
        width=20, anchor='w')
    C2.grid(row=20, column=1, pady=10)

    CheckVar3 = IntVar()
    C3 = tk.Checkbutton(self.can, text="Second-line", fg='navy', 
        bg='pale green', variable=CheckVar3, 
        onvalue=1, offvalue=0, height=1, 
        width=20, anchor='w')
    C3.grid(row=20, column=2, pady=10)

    LabelR = Label(self.can, text='Number of R/24h : ', font=12, 
        width=20, fg='cyan', bg='RoyalBlue4')
    LabelR.grid(row=21, column=0)

    Rnbre = Entry(self.can)
    Rnbre = Entry(highlightbackground='grey', bd=4)
    Rnbre.grid(row=21, column=1)

    LabSign = Label(self.can, text='Signature :', font=12, 
        width=15, fg='red', bg='pale green')
    LabSign.grid(row=22, column=0, pady=10)

    textSign = Entry(self.can)
    textSign = Entry(highlightbackground='grey', bd=4)
    textSign.grid(row=22, column=1, pady=10)

    buttCopy = Button(self.can, text="Save ttt", width=10, fg='yellow',
        bg='RoyalBlue3', bd=3, highlightbackground='RoyalBlue4',
        activebackground='dark turquoise', command=copyTttMess)
    buttCopy.grid(row=21, column=2)

    buttCopy = Button(self.can, text="Save R", width=10, fg='yellow',
        bg='RoyalBlue3', bd=3, highlightbackground='RoyalBlue4',
        activebackground='dark turquoise', command=copyResMess)
    buttCopy.grid(row=22, column=2)

    buttQuit = Button(self.can, text="Quit", width=10, fg='white',
        bg='RoyalBlue3', bd=3, highlightbackground='RoyalBlue4',
        activebackground='dark turquoise', command=quit)
    buttQuit.grid(row=22, column=3)
    """
    self.can.configure(scrollregion=self.can.bbox(ALL))
