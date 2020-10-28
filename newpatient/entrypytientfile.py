#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
from tkinter import messagebox
import os
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError as err_report2:
    print("+ An error occured about pymysql !", err_report2)
    pass


gui=Tk()
gui.title("Enter new patient")
gui.configure(bg='cyan')
#gui.geometry('300x200')

def get(IDpatient, Patient_num, Patientname, Firstname_pat, Surname, Sur_pat,
    Birthvalue, Birth_entree, Allergia, Patient_allergy, TransDisVal, TransDisease,
    Diagnostic, Diagnos_pat):
    """
        Entry at first time a patient
        (when program is open for the
        first time) and when entry button
        is pressed.
    """
    MsgBox = messagebox.askyesno('Save data', 'Do you want to save ?')
    if MsgBox == 1:
        IDpatient = Patient_num.get()
        Patientname = Firstname_pat.get()
        Surname = Sur_pat.get()
        Birthvalue = Birth_entree.get()
        Allergia = Patient_allergy.get()
        TransDisVal = TransDisease.get()
        Diagnostic = Diagnos_pat.get()

        if Patient_num.get() == "" or Firstname_pat.get() == "" or Sur_pat.get() == "":
            messagebox.showerror("MySQL Connection", "Enter Correct Details.")
        else:
            sqlCon = pymysql.connect(host='127.0.0.1', user='root', password='Ko@l@tr3379', database='timetrackconn')
            cur = sqlCon.cursor()
            cur.execute("INSERT into timetrackconn values (%s, %s, %s, %s, %s, %s, %s)",(
            Patient_num.get(),
            Firstname_pat.get(),
            Sur_pat.get(),
            Birth_entree.get(),
            Patient_allergy.get(),
            TransDisease.get(),
            Diagnos_pat.get(),
            ))
            sqlCon.commit()
            sqlCon.close()
            messagebox.showinfo("MySQL connection", "Record Entered Successfully !")

        try:
            if os.path.getsize('./newpatient/entryfile.txt'):
                print("+ File 'entryfile.txt' exist !")
        except FileNotFoundError as outcom1:
            print("+ Sorry, file 'entryfile.txt' not exist !")
            print(str(outcom1))
            print("+ File 'entryfile.txt' created !")
            with open('./newpatient/entryfile.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            if os.path.getsize('./newpatient/entryfile.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile2.txt'):
                print("+ File 'entryfile2.txt' exist !")
        except FileNotFoundError as outcom2:
            print("+ Sorry, file 'entryfile2.txt' not exist !")
            print(str(outcom2))
            print("+ File 'entryfile2.txt' created !")
            with open('./newpatient/entryfile2.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            if os.path.getsize('./newpatient/entryfile2.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile3.txt'):
                print("+ File 'entryfile3.txt' exist !")
        except FileNotFoundError as outcom3:
            print("+ Sorry, file 'entryfile3.txt' not exist !")
            print(str(outcom3))
            print("+ File 'entryfile3.txt' created !")
            with open('./newpatient/entryfile3.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            if os.path.getsize('./newpatient/entryfile3.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile4.txt'):
                print("+ File 'entryfile4.txt' exist !")
        except FileNotFoundError as outcom4:
            print("+ Sorry, file 'entryfile4.txt' not exist !")
            print(str(outcom4))
            print("+ File 'entryfile4.txt' created !")
            with open('./newpatient/entryfile4.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            if os.path.getsize('./newpatient/entryfile4.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile5.txt'):
                print("+ File 'entryfile5.txt' exist !")
        except FileNotFoundError as outcom5:
            print("+ Sorry, file 'entryfile5.txt' not exist !")
            print(str(outcom5))
            print("+ File 'entryfile5.txt' created !")
            with open('./newpatient/entryfile5.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            if os.path.getsize('./newpatient/entryfile5.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile6.txt'):
                print("+ File 'entryfile6.txt' exist !")
        except FileNotFoundError as outcom6:
            print("+ Sorry, file 'entryfile6.txt' not exist !")
            print(str(outcom6))
            print("+ File 'entryfile6.txt' created !")
            with open('./newpatient/entryfile6.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            if os.path.getsize('./newpatient/entryfile6.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile7.txt'):
                print("+ File 'entryfile7.txt' exist !")
        except FileNotFoundError as outcom7:
            print("+ Sorry, file 'entryfile7.txt' not exist !")
            print(str(outcom7))
            print("+ File 'entryfile7.txt' created !")
            with open('./newpatient/entryfile7.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            if os.path.getsize('./newpatient/entryfile7.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile8.txt'):
                print("+ File 'entryfile8.txt' exist !")
        except FileNotFoundError as outcom8:
            print("+ Sorry, file 'entryfile8.txt' not exist !")
            print(str(outcom8))
            print("+ File 'entryfile8.txt' created !")
            with open('./newpatient/entryfile8.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            if os.path.getsize('./newpatient/entryfile8.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile9.txt'):
                print("+ File 'entryfile9.txt' exist !")
        except FileNotFoundError as outcom9:
            print("+ Sorry, file 'entryfile9.txt' not exist !")
            print(str(outcom9))
            print("+ File 'entryfile9.txt' created !")
            with open('./newpatient/entryfile9.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            if os.path.getsize('./newpatient/entryfile9.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile10.txt'):
                print("+ File 'entryfile10.txt' exist !")
        except FileNotFoundError as outcom10:
            print("+ Sorry, file 'entryfile10.txt' not exist !")
            print(str(outcom10))
            print("+ File 'entryfile10.txt' created !")
            with open('./newpatient/entryfile10.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            if os.path.getsize('./newpatient/entryfile10.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile11.txt'):
                print("+ File 'entryfile11.txt' exist !")
        except FileNotFoundError as outcom11:
            print("+ Sorry, file 'entryfile11.txt' not exist !")
            print(str(outcom11))
            print("+ File 'entryfile11.txt' created !")
            with open('./newpatient/entryfile11.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            if os.path.getsize('./newpatient/entryfile11.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile12.txt'):
                print("+ File 'entryfile12.txt' exist !")
        except FileNotFoundError as outcom12:
            print("+ Sorry, file 'entryfile12.txt' not exist !")
            print(str(outcom12))
            print("+ File 'entryfile12.txt' created !")
            with open('./newpatient/entryfile12.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            if os.path.getsize('./newpatient/entryfile12.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile13.txt'):
                print("+ File 'entryfile13.txt' exist !")
        except FileNotFoundError as outcom13:
            print("+ Sorry, file 'entryfile13.txt' not exist !")
            print(str(outcom13))
            print("+ File 'entryfile13.txt' created !")
            with open('./newpatient/entryfile13.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            if os.path.getsize('./newpatient/entryfile13.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile14.txt'):
                print("+ File 'entryfile14.txt' exist !")
        except FileNotFoundError as outcom14:
            print("+ Sorry, file 'entryfile14.txt' not exist !")
            print(str(outcom14))
            print("+ File 'entryfile14.txt' created !")
            with open('./newpatient/entryfile14.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            if os.path.getsize('./newpatient/entryfile14.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile15.txt'):
                print("+ File 'entryfile15.txt' exist !")
        except FileNotFoundError as outcom15:
            print("+ Sorry, file 'entryfile15.txt' not exist !")
            print(str(outcom15))
            print("+ File 'entryfile15.txt' created !")
            with open('./newpatient/entryfile15.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            if os.path.getsize('./newpatient/entryfile15.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile16.txt'):
                print("+ File 'entryfile16.txt' exist !")
        except FileNotFoundError as outcom16:
            print("+ Sorry, file 'entryfile16.txt' not exist !")
            print(str(outcom16))
            print("+ File 'entryfile16.txt' created !")
            with open('./newpatient/entryfile16.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            if os.path.getsize('./newpatient/entryfile16.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile17.txt'):
                print("+ File 'entryfile17.txt' exist !")
        except FileNotFoundError as outcom17:
            print("+ Sorry, file 'entryfile17.txt' not exist !")
            print(str(outcom17))
            print("+ File 'entryfile17.txt' created !")
            with open('./newpatient/entryfile17.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            if os.path.getsize('./newpatient/entryfile17.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile18.txt'):
                print("+ File 'entryfile18.txt' exist !")
        except FileNotFoundError as outcom18:
            print("+ Sorry, file 'entryfile18.txt' not exist !")
            print(str(outcom18))
            print("+ File 'entryfile18.txt' created !")
            with open('./newpatient/entryfile18.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            if os.path.getsize('./newpatient/entryfile18.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile19.txt'):
                print("+ File 'entryfile19.txt' exist !")
        except FileNotFoundError as outcom19:
            print("+ Sorry, file 'entryfile19.txt' not exist !")
            print(str(outcom19))
            print("+ File 'entryfile19.txt' created !")
            with open('./newpatient/entryfile19.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            if os.path.getsize('./newpatient/entryfile19.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile20.txt'):
                print("+ File 'entryfile20.txt' exist !")
        except FileNotFoundError as outcom20:
            print("+ Sorry, file 'entryfile20.txt' not exist !")
            print(str(outcom20))
            print("+ File 'entryfile20.txt' created !")
            with open('./newpatient/entryfile20.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            if os.path.getsize('./newpatient/entryfile20.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile21.txt'):
                print("+ File 'entryfile21.txt' exist !")
        except FileNotFoundError as outcom21:
            print("+ Sorry, file 'entryfile21.txt' not exist !")
            print(str(outcom21))
            print("+ File 'entryfile21.txt' created !")
            with open('./newpatient/entryfile21.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            if os.path.getsize('./newpatient/entryfile21.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile22.txt'):
                print("+ File 'entryfile22.txt' exist !")
        except FileNotFoundError as outcom22:
            print("+ Sorry, file 'entryfile22.txt' not exist !")
            print(str(outcom22))
            print("+ File 'entryfile22.txt' created !")
            with open('./newpatient/entryfile22.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            if os.path.getsize('./newpatient/entryfile22.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile23.txt'):
                print("+ File 'entryfile23.txt' exist !")
        except FileNotFoundError as outcom23:
            print("+ Sorry, file 'entryfile23.txt' not exist !")
            print(str(outcom23))
            print("+ File 'entryfile23.txt' created !")
            with open('./newpatient/entryfile23.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            if os.path.getsize('./newpatient/entryfile23.txt'):
                return

        try:
            if os.path.getsize('./newpatient/entryfile24.txt'):
                print("+ File 'entryfile24.txt' exist !")
        except FileNotFoundError as outcom24:
            print("+ Sorry, file 'entryfile24.txt' not exist !")
            print(str(outcom24))
            print("+ File 'entryfile24.txt' created !")
            with open('./newpatient/entryfile24.txt', 'w') as namefile:
                namefile.write(Patientname + " " + Surname + '\n')
                namefile.write(Birthvalue + '\n')
                namefile.write(Allergia + '\n')
                namefile.write(TransDisVal + '\n')
                namefile.write(Diagnostic + '\n')
            if os.path.getsize('./newpatient/entryfile24.txt'):
                return

    #gui.destroy()

labelID = Label(gui)
labelID = Label(text='ID : ',
    font="Times 14 bold",
    fg='RoyalBlue4', bg='cyan')
labelID.pack(pady=10)

IDpatient = StringVar()
IDpatient.set('ID of patient')
Patient_num = Entry(gui, textvariable=IDpatient,
    highlightbackground='light sky blue',
    bd=4)
Patient_num.pack()

labelName = Label(gui)
labelName = Label(text='Name : ',
    font="Times 14 bold",
    fg='RoyalBlue4', bg='cyan')
labelName.pack(pady=10)

Patientname = StringVar()
Patientname.set('Firstname')
Firstname_pat = Entry(gui, textvariable=Patientname,
    highlightbackground='light sky blue',
    bd=4)
Firstname_pat.pack()

Surname = StringVar()
Surname.set("Lastname")
Sur_pat = Entry(gui, textvariable=Surname,
    highlightbackground='light sky blue',
    bd=4)
Sur_pat.pack()

labelBirth = Label(gui)
labelBirth = Label(text='Birth Date : ', font="Times 14 bold",
    fg='RoyalBlue4', bg='cyan')
labelBirth.pack(pady=10)

Birthvalue=StringVar()
Birthvalue.set('Format: 00/00/0000')
Birth_entree = Entry(gui, textvariable=Birthvalue,
    highlightbackground='light sky blue', bd=4)
Birth_entree.pack()

labelAller = Label(gui)
labelAller = Label(text='Allergy : ',
    font="Times 14 bold",
    fg='RoyalBlue4', bg='cyan')
labelAller.pack(pady=10)

Allergia = StringVar()
Allergia.set('None')
Patient_allergy = Entry(gui, textvariable=Allergia,
    highlightbackground='light sky blue',
    bd=4)
Patient_allergy.pack()

labelTrans = Label(gui)
labelTrans = Label(text='Transmissible Disease : ',
    font="Times 14 bold",
    fg='RoyalBlue4', bg='cyan')
labelTrans.pack(pady=10)

TransDisVal = StringVar()
TransDisVal.set('None')
TransDisease = Entry(gui, textvariable=TransDisVal,
    highlightbackground='light sky blue',
    bd=4)
TransDisease.pack()

labelDiag = Label(gui)
labelDiag = Label(text='Diagnosis : ',
    font="Times 14 bold",
    fg='RoyalBlue4', bg='cyan')
labelDiag.pack(pady=10)

Diagnosis = StringVar()
Diagnosis.set('Diagnostic (main)')
Diagnos_pat = Entry(gui, textvariable=Diagnosis,
    highlightbackground='light sky blue',
    bd=4)
Diagnos_pat.pack()

bouton1 = Button(gui, text="Enter", width=8, bd=3,
    fg='yellow', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='dark turquoise',
    command = lambda: get(IDpatient, Patient_num, Patientname, Firstname_pat,
        Surname, Sur_pat, Allergia, Patient_allergy, Birthvalue, Birth_entree, 
        TransDisVal, TransDisease, Diagnosis, Diagnos_pat))
bouton1.pack(side=LEFT, padx=10, pady=20)

buttQuit=Button(gui, text="Quit", width=8, bd=3,
    fg='cyan', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='dark turquoise', command=quit)
buttQuit.pack(side=LEFT, padx=10, pady=20)

gui.mainloop()
