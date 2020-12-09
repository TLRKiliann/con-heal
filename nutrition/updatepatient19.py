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
gui.configure(bg='DodgerBlue2')

# Interact with database to search data
def searchDB():
    """
        To search patient by ID
        and display data into 
        each GUI entree.
    """
    try:
        sqlCon = pymysql.connect(host='127.0.0.1', user='root', password='Ko@l@tr3379', database='timetrackconn')
        cur = sqlCon.cursor()
        cur.execute("SELECT * from timetrackconn where stdid=%s", patient_num.get())
        row = cur.fetchone()
        idpatient.set(row[0])
        firstpat.set(row[1])
        surname.set(row[2])
        birthvalue.set(row[3])
        #allergia.set(row[4]) 
        transdisval.set(row[5])
        diagnosis.set(row[6])
        sqlCon.commit()
    except:
        print("Error with search function in DB")
        messagebox.showinfo("Data Entry Form", "No Such Record Found !")
    sqlCon.close()

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
        patient_num.get(),
        ))
        sqlCon.commit()
        sqlCon.close()
        messagebox.showinfo("Data Entry Form", "Record Updated Successfully !")

    if idpatient == '19':
        if os.path.getsize('./newpatient/entryfile19.txt'):
            print("+ File 'entryfile19.txt' exist !")
            os.remove('./newpatient/entryfile19.txt')
            searchLineName19(firstpat, surname, birthvalue, allergia, transdisval, diagnosis)
    else:
        pass

    gui.destroy()

def searchLineName19(firstpat, surname, birthvalue, allergia, transdisval, diagnosis):
    """
        To save changing data for 
        entryfile.txt and display
        messagebox.
    """
    MsgBox2 = messagebox.askyesno('Save data', 'Do you want to save ?')
    if MsgBox2 == 1:
        with open('./newpatient/entryfile19.txt', 'w') as file2:
            file2.write(firstpat + " " + surname + '\n')
            file2.write(birthvalue + '\n')
            file2.write(allergia + '\n')
            file2.write(transdisval + '\n')
            file2.write(diagnosis + '\n')
    messagebox.showinfo("Info", "Data was updated for entryfile19.txt !")

with open('./allergy/allergyfile19.txt', 'r') as patfile:
    linea = patfile.readline()

labelID = Label(gui)
labelID = Label(text='ID : ',
    font="Times 14 bold",
    fg='RoyalBlue4', bg='DodgerBlue2')
labelID.pack(pady=10)

idpatient = StringVar()
idpatient.set('19')
patient_num = Entry(gui, textvariable=idpatient,
    highlightbackground='light sky blue',
    bd=4)
patient_num.pack()

labelname = Label(gui)
labelname = Label(text='Name : ',
    font="Times 14 bold",
    fg='RoyalBlue4', bg='DodgerBlue2')
labelname.pack(pady=10)

firstpat = StringVar()
#firstpat.set('Firstname')
firstname_pat = Entry(gui, textvariable=firstpat,
    highlightbackground='light sky blue',
    bd=4)
firstname_pat.pack()

surname = StringVar()
#surname.set("Lastname")
sur_pat = Entry(gui, textvariable=surname,
    highlightbackground='light sky blue',
    bd=4)
sur_pat.pack()

labelbirth = Label(gui)
labelbirth = Label(text='Birth Date : ', font="Times 14 bold",
    fg='RoyalBlue4', bg='DodgerBlue2')
labelbirth.pack(pady=10)

birthvalue=StringVar()
#birthvalue.set('Format: 00/00/0000')
birth_entree = Entry(gui, textvariable=birthvalue,
    highlightbackground='light sky blue', bd=4)
birth_entree.pack()

labelaller = Label(gui)
labelaller = Label(text='Allergy : ',
    font="Times 14 bold",
    fg='RoyalBlue4', bg='DodgerBlue2')
labelaller.pack(pady=10)

allergia = StringVar()
allergia.set(linea)
allergy_pat = Entry(gui, textvariable=allergia,
    highlightbackground='light sky blue',
    bd=4, width=40)
allergy_pat.pack()

labeltrans = Label(gui)
labeltrans = Label(text='Transmissible Disease : ',
    font="Times 14 bold",
    fg='RoyalBlue4', bg='DodgerBlue2')
labeltrans.pack(pady=10)

transdisval = StringVar()
#transdisval.set('None')
diseasetrans = Entry(gui, textvariable=transdisval,
    highlightbackground='light sky blue',
    bd=4)
diseasetrans.pack()

labeldiag = Label(gui)
labeldiag = Label(text='Diagnosis : ',
    font="Times 14 bold",
    fg='RoyalBlue4', bg='DodgerBlue2')
labeldiag.pack(pady=10)

diagnosis = StringVar()
#diagnosis.set('Diagnostic (main)')
diagnos_pat = Entry(gui, textvariable=diagnosis,
    highlightbackground='light sky blue',
    bd=4)
diagnos_pat.pack()

buttonsearch = Button(gui, text="Search ID", width=8, bd=3,
    fg='yellow', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise',
    command = searchDB)
buttonsearch.pack(side=LEFT, padx=10, pady=20)

buttonupdate = Button(gui, text="Enter", width=8, bd=3,
    fg='orange', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise',
    command = lambda: uptopat(idpatient, patient_num, firstpat, firstname_pat,
        surname, sur_pat, birthvalue, birth_entree, allergia, allergy_pat,
        transdisval, diseasetrans, diagnosis, diagnos_pat))
buttonupdate.pack(side=LEFT, padx=10, pady=20)

buttQuit=Button(gui, text="Quit", width=8, bd=3,
    fg='DodgerBlue2', bg='RoyalBlue3', highlightbackground='light sky blue',
    activebackground='pale turquoise', command=quit)
buttQuit.pack(side=LEFT, padx=10, pady=20)

gui.mainloop()

