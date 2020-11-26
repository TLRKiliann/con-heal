#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    To calculate BMI if indice
    is too high or too low.
    The weight is recording too.
    It's possible to read results
    in txt file.
"""


from tkinter import *
import tkinter
from functools import partial
from tkinter import messagebox
import time
import os
import subprocess
import json


gui = Tk()
gui.title('Time-Track')
gui.configure(background='RoyalBlue4')

labelTitle = Label(gui, text="BMI calculator", font=('Times', 18, 'bold'),
    fg='aquamarine', bg='RoyalBlue4')
labelTitle.grid(row=0, column=1, columnspan=2, pady=10)

textDate = Label(gui, text="Date : ",
    font=18, width=20, fg='cyan', bg='RoyalBlue4', anchor='e')
textDate.grid(row=1, column=1)

textHour = Label(gui, text="Hour : ",
    font=18, width=20, fg='cyan', bg='RoyalBlue4', anchor='e')
textHour.grid(row=2, column=1)

textName = Label(gui, text="Patient Name : ",
    font=18, width=20, fg='cyan', bg='RoyalBlue4', anchor='e')
textName.grid(row=3, column=1)

labelNum1 = Label(gui, text="Enter Weight (Kg) : ",
    font=14, width=20, fg='white', bg='RoyalBlue4', anchor='e')
labelNum1.grid(row=4, column=1)

labelNum2 = Label(gui, text="Enter Height (M) : ",
    font=14, width=20, fg='white', bg='RoyalBlue4', anchor='e')
labelNum2.grid(row=5, column=1)

def call_result(textBox, number1, number2):
    number1 = entryNum1.get()
    number2 = entryNum2.get()
    try:
        textBox.delete("0.0", END)
        num1 = float(entryNum1.get())
        num2 = float(entryNum2.get())
        result = (num1)/(num2*num2)
        if result <= 18.5:
            textBox.insert(INSERT, "You are underweight !\n"
                                     "Your BMI (IMC) is : %d" % result)
            return
        elif result >= 18.5 and result <= 25:
            textBox.insert(INSERT, "Your BMI is in the standards.\n"
                                     "Your BMI (IMC) is : %d" % result)
            return
        elif result >= 18.5 and result <= 25:
            textBox.insert(INSERT, "Your BMI is in the standards.\n"
                                     "Your BMI (IMC) is : %d" % result)
            return
        else:
            textBox.insert(INSERT, "You are overweight !\n"
                                     "Your BMI (IMC) is : %d" % result)  
            return
    except ValueError as val_err:
        print("+ An error has occured !", val_err)
        messagebox.showwarning("Warning", "Please, enter a valid number !")

def buttRecord():
    """
        To enter BMI in an text zone entry
    """
    num1 = float((entryNum1.get()))
    num2 = float((entryNum2.get()))
    result = (num1)/(num2*num2)
    bypass = round(result, 3)

    with open('./calBmi/bmi8.txt', 'a+') as file:
        file.write(str("Date : "))
        file.write(textDate.get() + "\n")
        file.write(str("Heure : "))
        file.write(textHour.get() + "\n")
        file.write(str("Prenom et Nom : "))
        file.write(textName.get())
        file.write(str("Poids : "))
        file.write(entryNum1.get() + "\n")
        file.write(str("Taille : "))
        file.write(entryNum2.get() + "\n")
        file.write(str("BMI : "))
        file.write(str(bypass))
        file.write("\n\n")
        file.close()

    try:
        if os.path.getsize('./calBmi/doc_BMI8/file_bmi.json'):
            print("+ File 'BMI' exist !")
            with open('./calBmi/doc_BMI8/file_bmi.json', 'r') as datafile:
                datastore = json.load(datafile)
                print(datastore)
            dataBmi = datastore
            dataBmi['data'].append({'Date' : textDate.get(), 'BMI' : bypass})
            with open('./calBmi/doc_BMI8/file_bmi.json', 'w') as datafile2:
                json.dump(dataBmi, datafile2, indent=4)
    except FileNotFoundError as outcom:
        print('+ Sorry, file file_bmi.json not exist !')
        print(str(outcom))
        print("+ File file_bmi.json created !")
        dataBmi = {}
        dataBmi['data'] = []
        dataBmi['data'].append({'Date' : textDate.get(), 'BMI' : bypass})
        with open('./calBmi/doc_BMI8/file_bmi.json', 'w') as datafile:
            json.dump(dataBmi, datafile, indent=4)

    try:
        if os.path.getsize('./calBmi/doc_BMI8/file_kg.json'):
            print("+ File 'Kg' exist !")
            with open('./calBmi/doc_BMI8/file_kg.json', 'r') as datafile:
                datastore = json.load(datafile)
                print(datastore)
            dataBmi = datastore
            dataBmi['data'].append({'Date' : textDate.get(), 'Kg' : entryNum1.get()})
            with open('./calBmi/doc_BMI8/file_kg.json', 'w') as datafile2:
                json.dump(dataBmi, datafile2, indent=4)
    except FileNotFoundError as outcom:
        print('+ Sorry, file file_kg.json not exist !')
        print(str(outcom))
        print("+ File file_kg.json created !")
        dataBmi = {}
        dataBmi['data'] = []
        dataBmi['data'].append({'Date' : textDate.get(), 'Kg' : entryNum1.get()})
        with open('./calBmi/doc_BMI8/file_kg.json', 'w') as datafile:
            json.dump(dataBmi, datafile, indent=4)

    messagebox.showinfo('Record', 'Data saved')

def viewGraphicBmi():
    try:
        if os.path.getsize('./calBmi/doc_BMI8/file_bmi.json'):
            subprocess.run('./calBmi/doc_BMI8/convert_bmilist.py', check=True)
    except FileNotFoundError as no_file:
        print("No BMI file exist !", no_file)
        messagebox.showinfo('INFO', 'BMI file not found !')

def viewGraphicKilo():
    try:
        if os.path.getsize('./calBmi/doc_BMI8/file_kg.json'):
            subprocess.run('./calBmi/doc_BMI8/convert_kg.py', check=True)
    except FileNotFoundError as no_file:
        print("No kg file exist !", no_file)
        messagebox.showinfo('INFO', 'Kg file not found !')

def readBmi():
    subprocess.run('./calBmi/bmi_read3.py', check=True)

def buttdel():
    """
        To earase last data if the usr would to delete it.
    """
    messagebox.showwarning("Warning", "Are you sure to delete last record !")
    MSB_War = messagebox.askyesno('Warning', '!!! Warning !!! If you' \
        'continue, last result will be delete !!!')
    if MSB_War == 1:
        try:
            if os.path.getsize('./calBmi/doc_BMI8/file_bmi.json'):
                with open('./calBmi/doc_BMI8/file_bmi.json', 'r') as file:
                    data = json.load(file)
                for key, value in data.items():
                    print("Last value of bmi deleted")
                    print(value[-1])
                    del value[-1]
                with open('./calBmi/doc_BMI8/file_bmi.json', 'w') as file:
                    data = json.dump(data, file, indent=4)
                print("Last value of 'file_bmi.json' has been deleted !")
        except FileNotFoundError:
            print('+ Sorry, file asked not exist !')

        try:
            if os.path.getsize('./calBmi/doc_BMI8/file_kg.json'):
                with open('./calBmi/doc_BMI8/file_kg.json', 'r') as file:
                    data = json.load(file)
                for key, value in data.items():
                    print("Last value of weight deleted")
                    print(value[-1])
                    del value[-1]
                with open('./calBmi/doc_BMI8/file_kg.json', 'w') as file:
                    data = json.dump(data, file, indent=4)
                print("Last value of 'file_kg.json' has been deleted !")
        except FileNotFoundError:
            print('+ Sorry, file asked not exist !')
    else:
        messagebox.showinfo('Info', 'Ok, no data was deleted.')

time_string = IntVar() 
textDate = Entry(gui, textvariable=time_string, highlightbackground='gray', bd=4)
time_string.set(time.strftime("%d-%m-%Y"))
textDate.grid(row=1, column=2, padx=10)

time_Htring = IntVar()
textHour = Entry(gui, textvariable=time_Htring, highlightbackground='gray', bd=4)
time_Htring.set(time.strftime("%H:%M:%S"))
textHour.grid(row=2, column=2, padx=10)

# To read name of patient for entry widget
with open('./newpatient/entryfile8.txt', 'r') as filename:
    line1=filename.readline()

name_text = StringVar()
textName = Entry(gui, textvariable=name_text,
    highlightbackground='gray', bd=4)
name_text.set(line1)
textName.grid(row=3, column=2, padx=10)

number1 = StringVar()
entryNum1 = Entry(gui, textvariable=number1,
    width=6, bd=3, highlightbackground='gray')
number1.set('ex : 75')
entryNum1.grid(sticky='w', row=4, column=2, padx=10)

number2 = StringVar()
entryNum2 = Entry(gui, textvariable=number2,
    width=6, bd=3, highlightbackground='gray')
number2.set('1.00')
entryNum2.grid(sticky='w', row=5, column=2, padx=10)

textBox = Text(gui, height=2, width=25, font=12, relief=SUNKEN)
textBox.grid(row=6, column=1, columnspan=2, padx=10, pady=10)

call_result = partial(call_result, textBox, number1, number2)

buttonCal = Button(gui, text="Calculate", width=30, bd=3,
    fg='white', bg='RoyalBlue3', activeforeground='gray40',
    activebackground='turquoise2', highlightbackground='cyan',
    command=call_result)
buttonCal.grid(row=7, column=1, columnspan=2, padx=10)

buttonSave = Button(gui, text="Save", width=12, bd=3, 
    fg='yellow', bg='RoyalBlue3', activeforeground='gray40',
    activebackground='turquoise2', highlightbackground='RoyalBlue3',
    command=buttRecord)
buttonSave.grid(sticky='w', row=10, column=1, padx=10, pady=10)

buttonCancel = Button(gui, text="Cancel last check", width=12,
    bd=3, fg='coral', bg='RoyalBlue3', activeforeground='white',
    activebackground='red', highlightbackground='RoyalBlue3',
    command=buttdel)
buttonCancel.grid(sticky='w', row=11, column=1, padx=10)

buttonRead = Button(gui, text="Read", width=12, bd=3,
    fg='cyan', bg='RoyalBlue3',
    activebackground='dark turquoise',
    highlightbackground='RoyalBlue3', command=readBmi)
buttonRead.grid(sticky='w', row=12, column=1, padx=10, pady=10)

buttonBmi = Button(gui, text="Graph BMI", width=12, bd=3,
    fg='cyan', bg='RoyalBlue3', activeforeground='gray40',
    activebackground='turquoise', highlightbackground='RoyalBlue3',
    command=viewGraphicBmi)
buttonBmi.grid(sticky='e', row=10, column=2, padx=10, pady=10)

buttonWeight = Button(gui, text="Graph Weight", width=12, bd=3,
    fg='cyan', bg='RoyalBlue3', activeforeground='gray40',
    activebackground='turquoise', highlightbackground='RoyalBlue3',
    command=viewGraphicKilo)
buttonWeight.grid(sticky='e', row=11, column=2, padx=10)

buttonQuit = Button(gui, text="Quit", width=12, bd=3,
    fg='white', bg='RoyalBlue3', activebackground='turquoise',
    highlightbackground='RoyalBlue3', command=quit)
buttonQuit.grid(sticky='e', row=12, column=2, padx=10, pady=10)

gui.mainloop()
