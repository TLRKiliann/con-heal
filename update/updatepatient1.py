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

def uptopat(idpatient, patient_num, firstpat, firstname_pat,
    surname, sur_pat, birthvalue, birth_entree, allergia, allergy_pat,
    transdisval, diseasetrans, diagnosis, diagnos_pat):
    """
        Update data for patients
        in function of their id
    """

    idpatient = patient_num.get()
    firstpat = firstname_pat.get()
    surname = sur_pat.get()
    birthvalue = birth_entree.get()
    allergia = allergy_pat.get()
    transdisval = diseasetrans.get()
    diagnosis = diagnos_pat.get()

    # Interact with database to update
    if patient_num.get() == "" or firstname_pat.get() == "" or sur_pat.get() == "":
        messagebox.showerror("MySQL Connection", "Enter Correct Details.")
    else:
        sqlCon = pymysql.connect(host='127.0.0.1', user='root', password='Ko@l@tr3379', database='timetrackconn')
        cur = sqlCon.cursor()
        cur.execute("UPDATE timetrackconn set firstname=%s, surname=%s, birth=%s, allergia=%s, disease=%s, maindiagnostic=%s where stdid=%s",(
        firstname_pat.get(),
        sur_pat.get(),
        birth_entree.get(),
        allergy_pat.get(),
        diseasetrans.get(),
        diagnos_pat.get(),
        patient_num.get()
        ))
        sqlCon.commit()
        sqlCon.close()
        messagebox.showinfo("Data Entry Form", "Record Updated Successfully !")

    if idpatient == '1':
        if os.path.getsize('./newpatient/entryfile.txt'):
            print("+ File 'entryfile.txt' exist !")
            os.remove('./newpatient/entryfile.txt')
            searchLineName(firstpat, surname, birthvalue, allergia, transdisval, diagnosis)
    else:
        pass

    if idpatient == '2':
        if os.path.getsize('./newpatient/entryfile2.txt'):
            print("+ File 'entryfile2.txt' exist !")
            os.remove('./newpatient/entryfile2.txt')
            searchLineName2(firstpat, surname, birthvalue, allergia, transdisval, diagnosis)
    else:
        pass

    gui.destroy()

def searchLineName(firstpat, surname, birthvalue, allergia, transdisval, diagnosis):
    """
        To save changing data for 
        entryfile.txt and display
        messagebox.
    """
    MsgBox = messagebox.askyesno('Save data', 'Do you want to save ?')
    if MsgBox == 1:
        with open('./newpatient/entryfile.txt', 'w') as file:
            file.write(firstpat + " " + surname + '\n')
            file.write(birthvalue + '\n')
            file.write(allergia + '\n')
            file.write(transdisval + '\n')
            file.write(diagnosis + '\n')
            file.close()
    messagebox.showinfo("Info", "Data was updated for entryfile.txt !")

def searchLineName2(firstpat, surname, birthvalue, allergia, transdisval, diagnosis):
    MsgBox2 = messagebox.askyesno('Save data', 'Do you want to save ?')
    if MsgBox2 == 1:
        with open('./newpatient/entryfile2.txt', 'w') as file2:
            file2.write(firstpat + " " + surname + '\n')
            file2.write(birthvalue + '\n')
            file2.write(allergia + '\n')
            file2.write(transdisval + '\n')
            file2.write(diagnosis + '\n')
            file2.close()
    messagebox.showinfo("Info", "Data was updated for entryfile2.txt !")

labelID = Label(gui)
labelID = Label(text='ID : ',
    font="Times 14 bold",
    fg='RoyalBlue4', bg='cyan')
labelID.pack(pady=10)

idpatient = StringVar()
idpatient.set('ID of patient')
patient_num = Entry(gui, textvariable=idpatient,
    highlightbackground='light sky blue',
    bd=4)
patient_num.pack()

labelname = Label(gui)
labelname = Label(text='Name : ',
    font="Times 14 bold",
    fg='RoyalBlue4', bg='cyan')
labelname.pack(pady=10)

firstpat = StringVar()
firstpat.set('Firstname')
firstname_pat = Entry(gui, textvariable=firstpat,
    highlightbackground='light sky blue',
    bd=4)
firstname_pat.pack()

surname = StringVar()
surname.set("Lastname")
sur_pat = Entry(gui, textvariable=surname,
    highlightbackground='light sky blue',
    bd=4)
sur_pat.pack()

labelbirth = Label(gui)
labelbirth = Label(text='Birth Date : ', font="Times 14 bold",
    fg='RoyalBlue4', bg='cyan')
labelbirth.pack(pady=10)

birthvalue=StringVar()
birthvalue.set('Format: 00/00/0000')
birth_entree = Entry(gui, textvariable=birthvalue,
    highlightbackground='light sky blue', bd=4)
birth_entree.pack()

labelaller = Label(gui)
labelaller = Label(text='Allergy : ',
    font="Times 14 bold",
    fg='RoyalBlue4', bg='cyan')
labelaller.pack(pady=10)

allergia = StringVar()
allergia.set('None')
allergy_pat = Entry(gui, textvariable=allergia,
    highlightbackground='light sky blue',
    bd=4)
allergy_pat.pack()

labeltrans = Label(gui)
labeltrans = Label(text='Transmissible Disease : ',
    font="Times 14 bold",
    fg='RoyalBlue4', bg='cyan')
labeltrans.pack(pady=10)

transdisval = StringVar()
transdisval.set('None')
diseasetrans = Entry(gui, textvariable=transdisval,
    highlightbackground='light sky blue',
    bd=4)
diseasetrans.pack()

labeldiag = Label(gui)
labeldiag = Label(text='Diagnosis : ',
    font="Times 14 bold",
    fg='RoyalBlue4', bg='cyan')
labeldiag.pack(pady=10)

diagnosis = StringVar()
diagnosis.set('Diagnostic (main)')
diagnos_pat = Entry(gui, textvariable=diagnosis,
    highlightbackground='light sky blue',
    bd=4)
diagnos_pat.pack()

bouton1 = Button(gui, text="Enter", width=8, bd=3,
    fg='yellow', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='dark turquoise',
    command = lambda: uptopat(idpatient, patient_num, firstpat, firstname_pat,
        surname, sur_pat, birthvalue, birth_entree, allergia, allergy_pat,
        transdisval, diseasetrans, diagnosis, diagnos_pat))
bouton1.pack(side=LEFT, padx=10, pady=20)

buttQuit=Button(gui, text="Quit", width=8, bd=3,
    fg='cyan', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='dark turquoise', command=quit)
buttQuit.pack(side=LEFT, padx=10, pady=20)

gui.mainloop()
