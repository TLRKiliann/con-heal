#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    This script was made to develop
    other butons with functions
"""


from tkinter import *
from tkinter import messagebox
import json
import os
import subprocess
import time
import sys


def writeData():
    """
        To export data in a json file
        and launching aspiFile9.py
    """
    try:
        if os.path.getsize('./param/paramdata9.txt'):
            print("+ File 'paramdata9.txt' exist !")
    except FileNotFoundError as info:
        print("The file : 'paramdata9.txt' doesn't exist !", info)
        print("File 'paramdata9.txt' created !")
    finally:
        with open('./param/paramdata9.txt', 'a+') as file:
            file.write(str("Date : "))
            file.write(textDate.get() + '\n')
            file.write(str("Hour : "))
            file.write(textHour.get() + '\n')
            file.write(str("Name and Surname : "))
            file.write(textName.get() + '\n')
            file.write(str("TA : "))
            file.write(textTa.get() + " mmHg\n")
            file.write(str("Puls : "))
            file.write(textPuls.get() + "/min\n")
            file.write(str("SaO2 : "))
            file.write(textSa.get() + "%\n")
            file.write(str("FR : "))
            file.write(textFr.get() + "/min\n")
            file.write(str("Temperature : "))
            file.write(textTemp.get() + "°C\n")
            file.write(str("Glycemie : "))
            file.write(textHgt.get() + " mmol/l\n")
            file.write(str("Douleurs (Pain) : "))
            file.write(textDlrs.get() +"/10\n\n")

    try:
        if os.path.getsize('./param/aspifile9/tensor.json'):
            print("+ File 'tensor' exist !")
            with open('./param/aspifile9/tensor.json', 'r') as datafile:
                datastore = json.load(datafile)
                print(datastore)
            dataTa = datastore
            dataTa['data'].append({'Date' : textDate.get(), 'Tension' : textTa.get()})
            if textTa.get() == "":
                print("---Pas de VALEUR 'Tension' entrée---")
            else:
                print("---Ok VALEUR 'Tension' entrée---")
                with open('./param/aspifile9/tensor.json', 'w') as datafile2:
                    json.dump(dataTa, datafile2, indent=4)
    except FileNotFoundError as outcom:
        print('+ Sorry, file tensor.json not exist !')
        print(str(outcom))
        print("+ File tensor.json created !")
        dataTa = {}
        dataTa['data'] = []
        dataTa['data'].append({'Date' : textDate.get(), 'Tension' : textTa.get()})
        if textTa.get() == "":
            print("---Pas de VALEUR 'Tension' entrée---")
        else:
            print("---Ok VALEUR 'Tension' entrée---")
            with open('./param/aspifile9/tensor.json', 'w') as datafile:
                json.dump(dataTa, datafile, indent=4)

    try:
        if os.path.getsize('./param/aspifile9/puls.json'):
            print("+ File 'puls' exist !")
            with open('./param/aspifile9/puls.json', 'r') as datapuls:
                datastore = json.load(datapuls)
                print(datastore)
            dataP = datastore
            dataP['data'].append({'Date' : textDate.get(), 'Puls' : textPuls.get()})
            if textPuls.get() == "":
                print("---Pas de VALEUR 'Puls' entrée---")
            else:
                print("---Ok VALEUR 'Puls' entrée---")
                with open('./param/aspifile9/puls.json', 'w') as datapuls2:
                    json.dump(dataP, datapuls2, indent=4)
    except FileNotFoundError as errorfile1:
        print('+ Sorry, file puls.json not exist !')
        print(str(errorfile1))
        print("+ File puls.json created !")
        dataP = {}
        dataP['data'] = []
        dataP['data'].append({'Date' : textDate.get(), 'Puls' : textPuls.get()})
        if textPuls.get() == "":
            print("---Pas de VALEUR 'Puls' entrée---")
        else:
            print("---Ok VALEUR 'Puls' entrée---")
            with open('./param/aspifile9/puls.json', 'w') as datapuls3:
                json.dump(dataP, datapuls3, indent=4)

    try:
        if os.path.getsize('./param/aspifile9/sat.json'):
            print("+ File 'sat' exist !")
            with open('./param/aspifile9/sat.json', 'r') as datasat:
                datastore = json.load(datasat)
                print(datastore)
            dataS = datastore
            dataS['data'].append({'Date' : textDate.get(), 'SaO2' : textSa.get()})
            if textSa.get() == "":
                print("---Pas de VALEUR 'SaO2' entrée---")
            else:
                print("---Ok VALEUR 'SaO2' entrée---")
                with open('./param/aspifile9/sat.json', 'w') as datasat2:
                    json.dump(dataS, datasat2, indent=4)
    except FileNotFoundError as errorfile2:
        print('+ Sorry, file sat.json not exist !')
        print(str(errorfile2))
        print("+ File sat.json created !")
        dataS = {}
        dataS['data'] = []
        dataS['data'].append({'Date' : textDate.get(), 'SaO2' : textSa.get()})
        if textSa.get() == "":
            print("---Pas de VALEUR 'SaO2' entrée---")
        else:
            print("---Ok VALEUR 'SaO2' entrée---")
            with open('./param/aspifile9/sat.json', 'w') as datasat3:
                json.dump(dataS, datasat3, indent=4)

    try:
        if os.path.getsize('./param/aspifile9/freq.json'):
            print("+ File 'freq' exist !")
            with open('./param/aspifile9/freq.json', 'r') as datafreq:
                datastore = json.load(datafreq)
                print(datastore)
            dataF = datastore
            dataF['data'].append({'Date' : textDate.get(), 'FR' : textFr.get()})
            if textFr.get() == "":
                print("---Pas de VALEUR 'FR' entrée---")
            else:
                print("---Ok VALEUR 'FR' entrée---")
                with open('./param/aspifile9/freq.json', 'w') as datafreq2:
                    json.dump(dataF, datafreq2, indent=4)
    except FileNotFoundError as errorfile3:
        print('+ Sorry, file freq.json not exist !')
        print(str(errorfile3))
        print("+ File freq.json created !")
        dataF = {}
        dataF['data'] = []
        dataF['data'].append({'Date' : textDate.get(), 'FR' : textFr.get()})
        if textFr.get() == "":
            print("---Pas de VALEUR 'FR' entrée---")
        else:
            print("---Ok VALEUR 'FR' entrée---")
            with open('./param/aspifile9/freq.json', 'w') as datafreq3:
                json.dump(dataF, datafreq3, indent=4)

    try:
        if os.path.getsize('./param/aspifile9/temp.json'):
            print("+ File 'temp' exist !")
            with open('./param/aspifile9/temp.json', 'r') as datatemp:
                datastore = json.load(datatemp)
                print(datastore)
            dataTe2 = datastore
            dataTe2['data'].append({'Date' : textDate.get(), 'Temperature' : textTemp.get()})
            if textTemp.get() == "":
                print("---Pas de VALEUR 'Temperature' entrée---")
            else:
                print("---Ok VALEUR 'Temperature' entrée---")
                with open('./param/aspifile9/temp.json', 'w') as datatemp2:
                    json.dump(dataTe2, datatemp2, indent=4)
    except FileNotFoundError as errorfile4:
        print('+ Sorry, file temp.json not exist !')
        print(str(errorfile4))
        print("+ File temp.json created !")
        dataTe2 = {}
        dataTe2['data'] = []
        dataTe2['data'].append({'Date' : textDate.get(), 'Temperature' : textTemp.get()})
        if textTemp.get() == "":
            print("---Pas de VALEUR 'Temperature' entrée---")
        else:
            print("---Ok VALEUR 'Temperature' entrée---")
            with open('./param/aspifile9/temp.json', 'w') as datatemp3:
                json.dump(dataTe2, datatemp3, indent=4)

    try:
        if os.path.getsize('./param/aspifile9/gly.json'):
            print("+ File 'gly' exist !")
            with open('./param/aspifile9/gly.json', 'r') as datagly:
                datastore = json.load(datagly)
                print(datastore)
            dataG = datastore
            dataG['data'].append({'Date' : textDate.get(), 'Glycemie' : textHgt.get()})
            if textHgt.get() == "":
                print("---Pas de VALEUR 'Glycemie' entrée---")
            else:
                print("---Ok VALEUR 'Glycemie' entrée---")
                with open('./param/aspifile9/gly.json', 'w') as datagly2:
                    json.dump(dataG, datagly2, indent=4)
    except FileNotFoundError as errorfile5:
        print('+ Sorry, file gly.json not exist !')
        print(str(errorfile5))
        print("+ File gly.json created !")
        dataG = {}
        dataG['data'] = []
        dataG['data'].append({'Date' : textDate.get(), 'Glycemie' : textHgt.get()})
        if textHgt.get() == "":
            print("---Pas de VALEUR 'Glycemie' entrée---")
        else:
            print("---Ok VALEUR 'Glycemie' entrée---")
            with open('./param/aspifile9/gly.json', 'w') as datagly3:
                json.dump(dataG, datagly3, indent=4)

    try:
        if os.path.getsize('./param/aspifile9/dlr.json'):
            print("+ File 'dlr' exist !")
            with open('./param/aspifile9/dlr.json', 'r') as datadlr:
                datastore = json.load(datadlr)
                print(datastore)
            dataD = datastore
            dataD['data'].append({'Date' : textDate.get(), 'Douleurs' : textDlrs.get()})
            if textDlrs.get() == "":
                print("---Pas de VALEUR 'Douleurs' entrée---")
            else:
                print("---Ok VALEUR 'Douleurs' entrée---")
                with open('./param/aspifile9/dlr.json', 'w') as datadlr2:
                    json.dump(dataD, datadlr2, indent=4)
    except FileNotFoundError as errorfile6:
        print('+ Sorry, file dlr.json not exist !')
        print(str(errorfile6))
        print("+ File dlr.json created !")
        dataD = {}
        dataD['data'] = []
        dataD['data'].append({'Date' : textDate.get(), 'Douleurs' : textDlrs.get()})
        if textDlrs.get() == "":
            print("---Pas de VALEUR 'Douleurs' entrée---")
        else:
            print("---Ok VALEUR 'Douleurs' entrée---")
            with open('./param/aspifile9/dlr.json', 'w') as datadlr3:
                json.dump(dataD, datadlr3, indent=4)

    label['text'] = ("Date: " + textDate.get() +
        "\nNom: " + textName.get() +
        "\nTension: " + textTa.get() +" -- " + "Puls: " + textPuls.get() +
        "\nSaO2: " + textSa.get() +" -- "+ "FR: " + textFr.get() +
        "\nTemperature: " + textTemp.get() +
        "\nGlycemie: " + textHgt.get() +
        "\nDouleurs: " + textDlrs.get() +
        "\nAll data have been added in json files !")

def mainRead():
    subprocess.run('./param/main_read9.py', check=True)

def appelTens():
    """
        to call aspidata.py for recapt data
        and launching matplotlib graph
    """
    try:
        if os.path.getsize('./param/aspifile9/tensor.json'):
            subprocess.run('./param/aspifile9/aspidata.py', check=True)
            label['text'] = ("Date: " + textDate.get() +
                "\nNom: " + textName.get() +
                "\nTension: " + textTa.get())
    except FileNotFoundError as errorgraph1:
        print('+ Sorry the TA plot doesn\'t work ! Data missing !', errorgraph1)
        label['text'] = "Sorry the TA plot doesn\'t work ! Data missing !"

def appelPuls():
    """
        to call aspidata.py for recapt data
        and launching matplotlib graph
    """
    try:
        if os.path.getsize('./param/aspifile9/puls.json'):
            subprocess.run('./param/aspifile9/aspipuls.py', check=True)
            label['text'] = ("Date: " + textDate.get() +" -- "+ "Nom: " + textName.get() +
                "\nPulsations: " + textPuls.get())
    except FileNotFoundError as errorgraph2:
        print('+ Sorry the Puls plot doesn\'t work ! Data missing !', errorgraph2)
        label['text'] = "Sorry the Puls plot doesn\'t work ! Data missing !"

def appelSat():
    """
        to call aspidata.py for recapt data
        and launching matplotlib graph
    """
    try:
        if os.path.getsize('./param/aspifile9/sat.json'):
            subprocess.run('./param/aspifile9/aspisat.py', check=True)
            label['text'] = ("Date: " + textDate.get() +" -- "+ "Nom: " + textName.get() +
                "\nSaO2: " + textSa.get())
    except FileNotFoundError as errorgraph3:
        print('+ Sorry the SaO2 plot doesn\'t work ! Data missing !', errorgraph3)
        label['text'] = "Sorry the SaO2 plot doesn\'t work ! Data missing !"

def appelFreq():
    """
        to call aspidata.py for recapt data
        and launching matplotlib graph
    """
    try:
        if os.path.getsize('./param/aspifile9/freq.json'):
            subprocess.run('./param/aspifile9/aspifreq.py', check=True)
            label['text'] = ("Date: " + textDate.get() +" -- "+ "Nom: " + textName.get() +
                "\nFrequ. resp.: " + textFr.get())
    except FileNotFoundError as errorgraph4:
        print('+ Sorry the FR plot doesn\'t work ! Data missing !', errorgraph4)
        label['text'] = "Sorry the FR plot doesn\'t work ! Data missing !"

def appelTemp():
    """
        to call aspidata.py for recapt data
        and launching matplotlib graph
    """
    try:
        if os.path.getsize('./param/aspifile9/temp.json'):
            subprocess.run('./param/aspifile9/aspitemp.py', check=True)
            label['text'] = ("Date: " + textDate.get() +" -- "+ "Nom: " + textName.get() +
                "\nTemperature: " + textTemp.get())
    except FileNotFoundError as errorgraph5:
        print('+ Sorry the Temp plot doesn\'t work ! Data missing !', errorgraph5)
        label['text'] = "Sorry the Temp plot doesn\'t work ! Data missing !"

def appelGly():
    """
        to call aspidata.py for recapt data
        and launching matplotlib graph
    """
    try:
        if os.path.getsize('./param/aspifile9/gly.json'):
            subprocess.run('./param/aspifile9/aspigly.py', check=True)
            label['text'] = ("Date: " + textDate.get() +" -- "+ "Nom: " + textName.get() +
                "\nGlycémie: " + textHgt.get())
    except FileNotFoundError as errorgraph6:
        print('+ Sorry the Hgt plot doesn\'t work ! Data missing !', errorgraph6)
        label['text'] = "Sorry the Hgt plot doesn\'t work ! Data missing !"

def appelDlr():
    """
        to call aspidata.py for recapt data
        and launching matplotlib graph
    """
    try:
        if os.path.getsize('./param/aspifile9/dlr.json'):
            subprocess.run('./param/aspifile9/aspidlr.py', check=True)
            label['text'] = ("Date: " + textDate.get() +" -- "+ "Nom: " + textName.get() +
                "\nDouleurs: " + textDlrs.get())
    except FileNotFoundError as errorgraph7:
        print('Sorry the Dlrs plot doesn\'t work ! Data missing !', errorgraph7)
        label['text'] = "Sorry the Dlrs plot doesn\'t work ! Data missing !"

def delMain():
    """
        To earase paramdata9.txt
    """
    Main_MsgBox = messagebox.askquestion("Confirm", "Are you sure ?\n"
        "It will delete paramdata9.txt with all data !!!")
    if Main_MsgBox == 'yes':
        try:
            if os.path.getsize('./param/paramdata9.txt'):
                os.remove('./param/paramdata9.txt')
                label['text'] = "File paramdata9.txt has been deleted !"
                print("+ File paramdata9.txt has been deleted !")
        except FileNotFoundError:
            label['text'] = "Sorry, file asked not exist !"
            print('+ Sorry, file asked not exist !')
    else:
        print("+ Nothing has changed !")
        label['text'] = "Nothing has changed !"

def delTA():
    """
        To earase last line
        of tensor.json
    """
    try:
        if os.path.getsize('./param/aspifile9/tensor.json'):
            with open('./param/aspifile9/tensor.json', 'r') as file:
                data = json.load(file)
            for key, value in data.items():
                print("Last value of TA deleted")
                print(value[-1])
                del value[-1]
            with open('./param/aspifile9/tensor.json', 'w') as file:
                data = json.dump(data, file, indent=4)
            label['text'] = "Last value of 'tensor.json' has been deleted !"
            print("Last value of 'tensor.json' has been deleted !")
    except (FileNotFoundError, IndexError) as out_ta:
        label['text'] = "Sorry, file asked not exist !"
        print('+ Sorry, file asked not exist !', out_ta)

def delPuls():
    """
        To earase last line
        of puls.json
    """
    try:
        if os.path.getsize('./param/aspifile9/puls.json'):
            with open('./param/aspifile9/puls.json', 'r') as file:
                data = json.load(file)
            for key, value in data.items():
                print("Last value of Puls deleted")
                print(value[-1])
                del value[-1]
            with open('./param/aspifile9/puls.json', 'w') as file:
                data = json.dump(data, file, indent=4)
            label['text'] = "Last value of 'puls.json' has been deleted !"
            print("Last value of 'puls.json' has been deleted !")
    except (FileNotFoundError, IndexError) as out_puls:
        label['text'] = "Sorry, file asked not exist !"
        print('+ Sorry, asked not exist !', out_puls)

def delSat():
    """
        To earase last line
        of sat.json
    """
    try:
        if os.path.getsize('./param/aspifile9/sat.json'):
            with open('./param/aspifile9/sat.json', 'r') as file:
                data = json.load(file)
            for key, value in data.items():
                print("Last value of SaO2 deleted")
                print(value[-1])
                del value[-1]
            with open('./param/aspifile9/sat.json', 'w') as file:
                data = json.dump(data, file, indent=4)
            label['text'] = "Last value of 'sat.json' has been deleted !"
            print("Last value of 'sat.json' has been deleted !")
    except (FileNotFoundError, IndexError) as out_sat:
        label['text'] = "Sorry, file asked not exist !"
        print('+ Sorry, file asked not exist !', out_sat)

def delFreq():
    """
        To earase last line
        of freq.json
    """
    try:
        if os.path.getsize('./param/aspifile9/freq.json'):
            with open('./param/aspifile9/freq.json', 'r') as file:
                data = json.load(file)
            for key, value in data.items():
                print("Last value of FR deleted")
                print(value[-1])
                del value[-1]
            with open('./param/aspifile9/freq.json', 'w') as file:
                data = json.dump(data, file, indent=4)
            label['text'] = "Last value of 'freq.json' has been deleted !"
            print("Last value of 'freq.json' has been deleted !")
    except (FileNotFoundError, IndexError) as out_freq:
        label['text'] = "Sorry, file asked not exist !"
        print('+ Sorry, file asked not exist !', out_freq)

def delTemp():
    """
        To earase last line
        of temp.json
    """
    try:
        if os.path.getsize('./param/aspifile9/temp.json'):
            with open('./param/aspifile9/temp.json', 'r') as file:
                data = json.load(file)
            for key, value in data.items():
                print("Last value of Temp deleted")
                print(value[-1])
                del value[-1]
            with open('./param/aspifile9/temp.json', 'w') as file:
                data = json.dump(data, file, indent=4)
            label['text'] = "Last value of 'temp.json' has been deleted !"
            print("Last value of 'temp.json' has been deleted !")
    except (FileNotFoundError, IndexError) as out_temp:
        label['text'] = "Sorry, file asked not exist !"
        print('+ Sorry, file asked not exist !', out_temp)

def delGly():
    """
        To earase last line
        of gly.json
    """
    try:
        if os.path.getsize('./param/aspifile9/gly.json'):
            with open('./param/aspifile9/gly.json', 'r') as file:
                data = json.load(file)
            for key, value in data.items():
                print("Last value of Gly deleted")
                print(value[-1])
                del value[-1]
            with open('./param/aspifile9/gly.json', 'w') as file:
                data = json.dump(data, file, indent=4)
            label['text'] = "Last value of 'gly.json' has been deleted !"
            print("Last value of 'gly.json' has been deleted !")
    except (FileNotFoundError, IndexError) as out_gly:
        label['text'] = "Sorry, file asked not exist !"
        print('+ Sorry, file asked not exist !', out_gly)

def delDlr():
    """
        To earase last line
        of dlr.json
    """
    try:
        if os.path.getsize('./param/aspifile9/dlr.json'):
            with open('./param/aspifile9/dlr.json', 'r') as file:
                data = json.load(file)
            for key, value in data.items():
                print("Last value of Pain deleted")
                print(value[-1])
                del value[-1]
            with open('./param/aspifile9/dlr.json', 'w') as file:
                data = json.dump(data, file, indent=4)
            label['text'] = "Last value of 'dlr.json' has been deleted !"
            print("Last value of 'dlr.json' has been deleted !")
    except (FileNotFoundError, IndexError) as out_dlr:
        label['text'] = "Sorry, file asked not exist !"
        print('+ Sorry, file asked not exist !', out_dlr)

def delEvery():
    """
        To delete all json files
    """
    MsgBox = messagebox.askquestion("Confirm","Are you sure ?\n"
        "It will delete all files with all data !!!")
    if MsgBox == 'yes':
        delTA()
        delPuls()
        delSat()
        delFreq()
        delTemp()
        delGly()
        delDlr()
        label['text'] = "All json files have been deleted !"
        print("All json files have been deleted !")
    else:
        label['text'] = "Nothing has been deleted !"
        print("+ Nothing has been deleted !")

# To read name of patient for entry widget
with open('./newpatient/entryfile9.txt', 'r') as filename:
    line1=filename.readline()

gui = Tk()
gui.title("Time-Track")
gui.configure(background='DodgerBlue2')
gui.geometry('650x600')

labelTitle = Label(gui, text="Vital Parameters",
    font=('Times 22 bold'), bg='DodgerBlue2', fg='white')
labelTitle.grid(row=0, column=1, columnspan=4, pady=10)

label = Label(gui, text='Date : ', font=('Times', 14),
    fg='white', bg='DodgerBlue2', width=15, anchor='e')
label.grid(row=1, column=1)

label = Label(gui, text='Hour : ', font=('Times', 14),
    fg='white', bg='DodgerBlue2', width=15, anchor='e')
label.grid(row=2, column=1)

label1 = Label(gui, text='Enter Name : ', font=('Times', 14),
    fg='white', bg='DodgerBlue2', width=15, anchor='e')
label1.grid(row=3, column=1)

label2 = Label(gui, text='Enter TA : ', font=('Times', 14),
    fg='white', bg='DodgerBlue2', width=15, anchor='e')
label2.grid(row=4, column=1)

label3 = Label(gui, text='Enter Puls : ', font=('Times', 14),
    fg='white', bg='DodgerBlue2', width=15, anchor='e')
label3.grid(row=5, column=1)

label4 = Label(gui, text='Enter SaO2 : ', font=('Times', 14),
    fg='white', bg='DodgerBlue2', width=15, anchor='e')
label4.grid(row=6, column=1)

label5 = Label(gui, text='Enter FR : ', font=('Times', 14),
    fg='white', bg='DodgerBlue2', width=15, anchor='e')
label5.grid(row=7, column=1)

label6 = Label(gui, text='Enter T°C : ', font=('Times', 14),
    fg='white', bg='DodgerBlue2', width=15, anchor='e')
label6.grid(row=8, column=1)

label7 = Label(gui, text='Enter Hgt : ', font=('Times', 14),
    fg='white', bg='DodgerBlue2', width=15, anchor='e')
label7.grid(row=9, column=1)

label8 = Label(gui, text='Eva dlrs/10 : ', font=('Times', 14),
    fg='white', bg='DodgerBlue2', width=15, anchor='e')
label8.grid(row=10, column=1)

time_string = IntVar()
textDate = Entry(gui, textvariable=time_string,
    highlightbackground='gray', bd=4)
time_string.set(time.strftime("%d/%m/%Y"))
textDate.grid(row=1, column=2)

time_Htring = IntVar()
textHour = Entry(gui, textvariable=time_Htring,
    highlightbackground='gray', bd=4)
time_Htring.set(time.strftime("%H:%M:%S"))
textHour.grid(row=2, column=2)

name_text = StringVar()
textName = Entry(gui, textvariable=name_text,
    highlightbackground='gray', bd=4)
name_text.set(line1[:-1])
textName.grid(row=3, column=2)

textTa = Entry(gui, highlightbackground='gray', bd=4)
textTa.grid(row=4, column=2)

textPuls = Entry(gui, highlightbackground='gray', bd=4)
textPuls.grid(row=5, column=2)

textSa = Entry(gui, highlightbackground='gray', bd=4)
textSa.grid(row=6, column=2)

textFr = Entry(gui, highlightbackground='gray', bd=4)
textFr.grid(row=7, column=2)

textTemp = Entry(gui, highlightbackground='gray', bd=4)
textTemp.grid(row=8, column=2)

textHgt = Entry(gui, highlightbackground='gray', bd=4)
textHgt.grid(row=9, column=2)

textDlrs = Entry(gui, highlightbackground='gray', bd=4)
textDlrs.grid(row=10, column=2)

button2Write = Button(gui)
button2Write.config(text='Quit', width=15,
    fg='navy', bg='lightblue',
    activebackground='pale turquoise',
    activeforeground='gray40',
    command=quit)
button2Write.grid(row=1, column=3)

buttonDel = Button(gui)
buttonDel.config(text='Reinitialize All Data', width=15,
    bg='coral', fg='yellow', activebackground='red',
    activeforeground='white', command=delEvery)
buttonDel.grid(row=1, column=4)

buttonWrite = Button(gui)
buttonWrite.config(text='CAPTURE DATA', width=33,
    fg='navy', bg='lightblue',
    activeforeground='gray40',
    activebackground='pale turquoise', command=writeData)
buttonWrite.grid(row=2, column=3, columnspan=4)

buttonMainlec = Button(gui)
buttonMainlec.config(text='Read All Data', width=15,
    bg='lightblue', fg='navy', activebackground='pale turquoise',
    activeforeground='gray40', command=mainRead)
buttonMainlec.grid(row=3, column=3)

buttonDel = Button(gui)
buttonDel.config(text='Delete File of Data', width=15,
    bg='coral', fg='yellow', activebackground='red',
    activeforeground='white', command=delMain)
buttonDel.grid(row=3, column=4)

button3Write = Button(gui)
button3Write.config(text='Graph TA', width=15,
    bg='lightblue', fg='navy', activebackground='pale turquoise',
    activeforeground='gray40', command=appelTens)
button3Write.grid(row=4, column=3)

button4Write = Button(gui)
button4Write.config(text='Graph Puls', width=15,
    bg='lightblue', fg='navy', activebackground='pale turquoise',
    activeforeground='gray40', command=appelPuls)
button4Write.grid(row=5, column=3)

button5Write = Button(gui)
button5Write.config(text='Graph SaO2', width=15,
    bg='lightblue', fg='navy', activebackground='pale turquoise',
    activeforeground='gray40', command=appelSat)
button5Write.grid(row=6, column=3)

button6Write = Button(gui)
button6Write.config(text='Graph FR', width=15,
    bg='lightblue', fg='navy', activebackground='pale turquoise',
    activeforeground='gray40', command=appelFreq)
button6Write.grid(row=7, column=3)

button7Write = Button(gui)
button7Write.config(text='Graph T°C', width=15,
    bg='lightblue', fg='navy',activebackground='pale turquoise',
    activeforeground='gray40', command=appelTemp)
button7Write.grid(row=8, column=3)

button8Write = Button(gui)
button8Write.config(text='Graph Hgt', width=15,
    bg='lightblue', fg='navy',activebackground='pale turquoise',
    activeforeground='gray40', command=appelGly)
button8Write.grid(row=9, column=3)

button9Write = Button(gui)
button9Write.config(text='Graph Dlrs', width=15,
    bg='lightblue', fg='navy',activebackground='pale turquoise',
    activeforeground='gray40', command=appelDlr)
button9Write.grid(row=10, column=3)

button1Del = Button(gui)
button1Del.config(text='Cancel last TA', width=15,
    bg='coral', fg='yellow', activeforeground='white',
    activebackground='red', command=delTA)
button1Del.grid(row=4, column=4)

button2Del = Button(gui)
button2Del.config(text='Cancel last Puls', width=15,
    bg='coral', fg='yellow', activeforeground='white',
    activebackground='red', command=delPuls)
button2Del.grid(row=5, column=4)

button3Del = Button(gui)
button3Del.config(text='Cancel last SaO2', width=15,
    bg='coral', fg='yellow', activeforeground='white',
    activebackground='red', command=delSat)
button3Del.grid(row=6, column=4)

button4Del = Button(gui)
button4Del.config(text='Cancel last FR', width=15,
    bg='coral', fg='yellow', activeforeground='white',
    activebackground='red', command=delFreq)
button4Del.grid(row=7, column=4)

button5Del = Button(gui)
button5Del.config(text='Cancel last T°C', width=15,
    bg='coral', fg='yellow', activeforeground='white',
    activebackground='red', command=delTemp)
button5Del.grid(row=8, column=4)

button6Del = Button(gui)
button6Del.config(text='Cancel last Hgt', width=15,
    bg='coral', fg='yellow', activeforeground='white',
    activebackground='red', command=delGly)
button6Del.grid(row=9, column=4)

button7Del = Button(gui)
button7Del.config(text='Cancel last Dlrs', width=15,
    bg='coral', fg='yellow', activeforeground='white',
    activebackground='red', command=delDlr)
button7Del.grid(row=10, column=4)

lower_frame = Frame(gui, bg='DodgerBlue2', bd=10, relief=GROOVE)
lower_frame.place(relx=0.5, rely=0.66, relwidth=0.9,
    relheight=0.3, anchor='n')

label = Label(lower_frame, text=" ", font=('Arial', 12),
    bg='white', anchor='nw', justify='left')
label.place(relwidth=1, relheight=1)

gui.mainloop()