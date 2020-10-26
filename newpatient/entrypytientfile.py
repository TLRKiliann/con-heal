#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
from tkinter import messagebox
import os
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError as err_report:
    print("+ An error occured about pymysql !", err_report)
    pass


gui=Tk()
gui.title("Enter new patient")
gui.configure(bg='cyan')
#gui.geometry('300x200')

def get(IDpatient, Patient_num, Patientname, Patient_entree, Surname, Sur_pat,
    Allergia, Patient_allergy, Birthvalue, Birth_entree, Diagnostic, Diagnos_pat):
    """
        Entry at first time a patient
        (when program is open for the
        first time) and when entry button
        is pressed.
    """
    MsgBox = messagebox.askyesno('Save data', 'Do you want to save ?')
    if MsgBox == 1:
        IDpatient = Patient_num.get()
        Patientname = Patient_entree.get()
        Surname = Sur_pat.get()
        Allergia = Patient_allergy.get()
        Birthvalue = Birth_entree.get()
        Diagnostic = Diagnos_pat.get()
        print(Patientname)
        print(Birthvalue)
        try:
            if os.path.getsize('./newpatient/entryfile.txt'):
                print("+ File 'entryfile.txt' exist !")
            if Patient_num.get() == "" or Birth_entree.get() == "":
                messagebox.showerror("MySQL Connection", "Enter Correct Details.")
        except FileNotFoundError as outcom5:
            print("+ Sorry, file 'entryfile.txt' not exist !")
            print(str(outcom5))
            print("+ File 'entryfile.txt' created !")
            with open('./newpatient/entryfile.txt', 'w') as namefile:
                namefile.write(Patientname + '\n')
                namefile.write(Birthvalue + '\n')
            sqlCon = pymysql.connect(host='127.0.0.1', user='root', password='Ko@l@tr3379', database='timetrackconn')
            cur = sqlCon.cursor()
            cur.execute("INSERT into timetrackconn values (%s, %s, %s, %s, %s, %s)",(
            Patient_num.get(),
            Patient_entree.get(),
            Sur_pat.get(),
            Patient_allergy.get(),
            Birth_entree.get(),
            Diagnos_pat.get(),
            ))
            sqlCon.commit()
            sqlCon.close()
            messagebox.showinfo("MySQL connection", "Record Entered Successfully !")

    gui.destroy()

labelName = Label(gui)
labelName = Label(text='Enter NAME : ',
    font="Times 14 bold",
    fg='RoyalBlue3', bg='cyan')
labelName.pack(pady=10)

IDpatient = StringVar()
IDpatient.set('ID of patient')
Patient_num = Entry(gui, textvariable=IDpatient,
    highlightbackground='light sky blue',
    bd=4)
Patient_num.pack()

Patientname = StringVar()
Patientname.set('Firstname + Lastname')
Patient_entree = Entry(gui, textvariable=Patientname,
    highlightbackground='light sky blue',
    bd=4)
Patient_entree.pack()

Surname = StringVar()
Surname.set("Nom de famile")
Sur_pat = Entry(gui, textvariable=Surname,
    highlightbackground='light sky blue',
    bd=4)
Sur_pat.pack()

Allergia=StringVar()
Allergia.set('Allergy')
Patient_allergy = Entry(gui, textvariable=Allergia,
    highlightbackground='light sky blue',
    bd=4)
Patient_allergy.pack()

labelBirth = Label(gui)
labelBirth = Label(text='Birth Date : ', font="Times 14 bold",
    fg='RoyalBlue4', bg='cyan')
labelBirth.pack(pady=10)

Birthvalue=StringVar()
Birthvalue.set('Format: 00/00/0000')
Birth_entree = Entry(gui, textvariable=Birthvalue,
    highlightbackground='light sky blue', bd=4)
Birth_entree.pack()

Diagnosis = StringVar()
Diagnosis.set('Diagnostic')
Diagnos_pat = Entry(gui, textvariable=Diagnosis,
    highlightbackground='light sky blue',
    bd=4)
Diagnos_pat.pack()

bouton1 = Button(gui, text="Enter", width=8, bd=3,
    fg='yellow', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='dark turquoise',
    command = lambda: get(IDpatient, Patient_num,
        Patientname, Patient_entree,
        Surname, Sur_pat,
        Allergia, Patient_allergy,
        Birthvalue, Birth_entree, Diagnosis, Diagnos_pat))
bouton1.pack(side=LEFT, padx=10, pady=20)

buttQuit=Button(gui, text="Quit", width=8, bd=3,
    fg='cyan', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='dark turquoise', command=quit)
buttQuit.pack(side=LEFT, padx=10, pady=20)

gui.mainloop()
