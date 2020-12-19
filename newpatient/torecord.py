#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    To record a new patient
    in text zone (entree cap)
"""


from tkinter import *
from tkinter import messagebox
import os
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError as err_report4:
    print("+ An error occured about pymysql !", err_report4)
    pass


gui=Tk()
gui.title("Time-Track")
gui.configure(bg='DodgerBlue2')
#gui.geometry('300x200')

def get(PatientID, patientnum, Firstname, labelfirst, Surname, lblsurname, 
    Birthvalue, Birth_entree, Allergia, Patient_allergy, TransDisVal, TransDisease,
    Diagnosis, Diagnos_pat):
    """
        Add a patient with
        the add button
    """
    mot = "-"
    mot2 = "--"
    mot3 = "---"
    mot4 = "----"
    mot5 = "-----"
    mot6 = "------"
    mot7 = "-------"
    mot8 = "--------"
    mot9 = "---------"
    mot10 = "----------"
    mot11 = "-----------"
    mot12 = "------------"
    mot13 = "-------------"
    mot14 = "--------------"
    mot15 = "---------------"
    mot16 = "----------------"
    mot17 = "-----------------"
    mot18 = "------------------"
    mot19 = "-------------------"
    mot20 = "--------------------"
    mot21 = "---------------------"
    mot22 = "----------------------"
    mot23 = "-----------------------"
    mot24 = "------------------------"

    PatientID = patientnum.get()
    Firstname = labelfirst.get()
    Surname = lblsurname.get()
    Birthvalue = Birth_entree.get()
    Allergia = Patient_allergy.get()
    TransDisVal = TransDisease.get()
    Diagnosis = Diagnos_pat.get()

    if patientnum.get() == "" or labelfirst.get() == "" or lblsurname.get() == "":
        messagebox.showerror("MySQL Connection", "Enter Correct Details.")
    else:
        sqlCon = pymysql.connect(host='127.0.0.1', user='root', password='Ko@l@tr3379', database='timetrackconn')
        cur = sqlCon.cursor()
        cur.execute("INSERT into timetrackconn values (%s, %s, %s, %s, %s, %s, %s)",(
        patientnum.get(),
        labelfirst.get(),
        lblsurname.get(),
        Birth_entree.get(),
        Patient_allergy.get(),
        TransDisease.get(),
        Diagnos_pat.get(),
        ))
        sqlCon.commit()
        sqlCon.close()
        messagebox.showinfo("MySQL connection", "Record Entered Successfully !")

    if mot == '-':
        if os.path.getsize('./newpatient/entryfile.txt'):
            with open('./newpatient/entryfile.txt', 'r') as file1:
                lines = file1.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot in line:
                        searchLine1(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot2 == '--':
        if os.path.getsize('./newpatient/entryfile2.txt'):
            with open('./newpatient/entryfile2.txt', 'r') as file2:
                lines = file2.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot2 in line:
                        searchLine2(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot3 == '---':
        if os.path.getsize('./newpatient/entryfile3.txt'):
            with open('./newpatient/entryfile3.txt', 'r') as file3:
                lines = file3.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot3 in line:
                        searchLine3(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot4 == '----':
        if os.path.getsize('./newpatient/entryfile4.txt'):
            with open('./newpatient/entryfile4.txt', 'r') as file4:
                lines = file4.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot4 in line:
                        searchLine4(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot5 == '-----':
        if os.path.getsize('./newpatient/entryfile5.txt'):
            with open('./newpatient/entryfile5.txt', 'r') as file5:
                lines = file5.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot5 in line:
                        searchLine5(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot6 == '------':
        if os.path.getsize('./newpatient/entryfile6.txt'):
            with open('./newpatient/entryfile6.txt', 'r') as file6:
                lines = file6.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot6 in line:
                        searchLine6(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot7 == '-------':
        if os.path.getsize('./newpatient/entryfile7.txt'):
            with open('./newpatient/entryfile7.txt', 'r') as file7:
                lines = file7.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot7 in line:
                        searchLine7(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot8 == '--------':
        if os.path.getsize('./newpatient/entryfile8.txt'):
            with open('./newpatient/entryfile8.txt', 'r') as file8:
                lines = file8.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot8 in line:
                        searchLine8(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot9 == '---------':
        if os.path.getsize('./newpatient/entryfile9.txt'):
            with open('./newpatient/entryfile9.txt', 'r') as file9:
                lines = file9.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot9 in line:
                        searchLine9(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot10 == '----------':
        if os.path.getsize('./newpatient/entryfile10.txt'):
            with open('./newpatient/entryfile10.txt', 'r') as file10:
                lines = file10.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot10 in line:
                        searchLine10(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot11 == '-----------':
        if os.path.getsize('./newpatient/entryfile11.txt'):
            with open('./newpatient/entryfile11.txt', 'r') as file11:
                lines = file11.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot11 in line:
                        searchLine11(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot12 == '------------':
        if os.path.getsize('./newpatient/entryfile12.txt'):
            with open('./newpatient/entryfile12.txt', 'r') as file12:
                lines = file12.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot12 in line:
                        searchLine12(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot13 == '-------------':
        if os.path.getsize('./newpatient/entryfile13.txt'):
            with open('./newpatient/entryfile13.txt', 'r') as file13:
                lines = file13.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot13 in line:
                        searchLine13(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot14 == '--------------':
        if os.path.getsize('./newpatient/entryfile14.txt'):
            with open('./newpatient/entryfile14.txt', 'r') as file14:
                lines = file14.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot14 in line:
                        searchLine14(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot15 == '---------------':
        if os.path.getsize('./newpatient/entryfile15.txt'):
            with open('./newpatient/entryfile15.txt', 'r') as file15:
                lines = file15.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot15 in line:
                        searchLine15(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot16 == '----------------':
        if os.path.getsize('./newpatient/entryfile16.txt'):
            with open('./newpatient/entryfile16.txt', 'r') as file16:
                lines = file16.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot16 in line:
                        searchLine16(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot17 == '-----------------':
        if os.path.getsize('./newpatient/entryfile17.txt'):
            with open('./newpatient/entryfile17.txt', 'r') as file17:
                lines = file17.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot17 in line:
                        searchLine17(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot18 == '------------------':
        if os.path.getsize('./newpatient/entryfile18.txt'):
            with open('./newpatient/entryfile18.txt', 'r') as file18:
                lines = file18.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot18 in line:
                        searchLine18(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot19 == '-------------------':
        if os.path.getsize('./newpatient/entryfile19.txt'):
            with open('./newpatient/entryfile19.txt', 'r') as file19:
                lines = file19.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot19 in line:
                        searchLine19(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot20 == '--------------------':
        if os.path.getsize('./newpatient/entryfile20.txt'):
            with open('./newpatient/entryfile20.txt', 'r') as file20:
                lines = file20.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot20 in line:
                        searchLine20(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot21 == '---------------------':
        if os.path.getsize('./newpatient/entryfile21.txt'):
            with open('./newpatient/entryfile21.txt', 'r') as file21:
                lines = file21.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot21 in line:
                        searchLine21(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot22 == '----------------------':
        if os.path.getsize('./newpatient/entryfile22.txt'):
            with open('./newpatient/entryfile22.txt', 'r') as file22:
                lines = file22.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot22 in line:
                        searchLine22(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot23 == '-----------------------':
        if os.path.getsize('./newpatient/entryfile23.txt'):
            with open('./newpatient/entryfile23.txt', 'r') as file23:
                lines = file23.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot23 in line:
                        searchLine23(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        pass

    if mot24 == '------------------------':
        if os.path.getsize('./newpatient/entryfile24.txt'):
            with open('./newpatient/entryfile24.txt', 'r') as file24:
                lines = file24.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot24 in line:
                        searchLine24(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis)
    else:
        print("There is no file to edit as entryfile")

    gui.destroy()

def searchLine1(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    """
        To save new patient name
        by a msgbox and write the
        new name in an entryfile.txt
    """
    MsgBox = messagebox.askyesno('Save data', 'Do you want to save ?')
    if MsgBox == 1:
        file = open('./newpatient/entryfile.txt', 'w')
        file.write(Firstname + " " + Surname + '\n')
        file.write(Birthvalue + '\n')
        file.write(Allergia + '\n')
        file.write(TransDisVal + '\n')
        file.write(Diagnosis + '\n')
        file.close()

def searchLine2(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox = messagebox.askyesno('Save data', 'Do you want to save for patient 2 ?')
    if MsgBox == 1:
        with open('./newpatient/entryfile2.txt', 'w') as file2:
            file2.write(Firstname + " " + Surname + '\n')
            file2.write(Birthvalue + '\n')
            file2.write(Allergia + '\n')
            file2.write(TransDisVal + '\n')
            file2.write(Diagnosis + '\n')


def searchLine3(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox = messagebox.askyesno('Save data', 'Do you want to save for patient 3 ?')
    if MsgBox == 1:
        with open('./newpatient/entryfile3.txt', 'w') as file3:
            file3.write(Firstname + " " + Surname + '\n')
            file3.write(Birthvalue + '\n')
            file3.write(Allergia + '\n')
            file3.write(TransDisVal + '\n')
            file3.write(Diagnosis + '\n')

def searchLine4(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox = messagebox.askyesno('Save data', 'Do you want to save for patient 4 ?')
    if MsgBox == 1:
        with open('./newpatient/entryfile4.txt', 'w') as file4:
            file4.write(Firstname + " " + Surname + '\n')
            file4.write(Birthvalue + '\n')
            file4.write(Allergia + '\n')
            file4.write(TransDisVal + '\n')
            file4.write(Diagnosis + '\n')

def searchLine5(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox = messagebox.askyesno('Save data', 'Do you want to save for patient 5 ?')
    if MsgBox == 1:
        with open('./newpatient/entryfile5.txt', 'w') as file5:
            file5.write(Firstname + " " + Surname + '\n')
            file5.write(Birthvalue + '\n')
            file5.write(Allergia + '\n')
            file5.write(TransDisVal + '\n')
            file5.write(Diagnosis + '\n')

def searchLine6(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox = messagebox.askyesno('Save data', 'Do you want to save for patient 6 ?')
    if MsgBox == 1:
        with open('./newpatient/entryfile6.txt', 'w') as file6:
            file6.write(Firstname + " " + Surname + '\n')
            file6.write(Birthvalue + '\n')
            file6.write(Allergia + '\n')
            file6.write(TransDisVal + '\n')
            file6.write(Diagnosis + '\n')

def searchLine7(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox = messagebox.askyesno('Save data', 'Do you want to save for patient 7 ?')
    if MsgBox == 1:
        with open('./newpatient/entryfile7.txt', 'w') as file7:
            file7.write(Firstname + " " + Surname + '\n')
            file7.write(Birthvalue + '\n')
            file7.write(Allergia + '\n')
            file7.write(TransDisVal + '\n')
            file7.write(Diagnosis + '\n')

def searchLine8(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox = messagebox.askyesno('Save data', 'Do you want to save for patient 8 ?')
    if MsgBox == 1:
        with open('./newpatient/entryfile8.txt', 'w') as file8:
            file8.write(Firstname + " " + Surname + '\n')
            file8.write(Birthvalue + '\n')
            file8.write(Allergia + '\n')
            file8.write(TransDisVal + '\n')
            file8.write(Diagnosis + '\n')

def searchLine9(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox = messagebox.askyesno('Save data', 'Do you want to save for patient 9 ?')
    if MsgBox == 1:
        with open('./newpatient/entryfile9.txt', 'w') as file9:
            file9.write(Firstname + " " + Surname + '\n')
            file9.write(Birthvalue + '\n')
            file9.write(Allergia + '\n')
            file9.write(TransDisVal + '\n')
            file9.write(Diagnosis + '\n')

def searchLine10(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox = messagebox.askyesno('Save data', 'Do you want to save for patient 10 ?')
    if MsgBox == 1:
        with open('./newpatient/entryfile10.txt', 'w') as file10:
            file10.write(Firstname + " " + Surname + '\n')
            file10.write(Birthvalue + '\n')
            file10.write(Allergia + '\n')
            file10.write(TransDisVal + '\n')
            file10.write(Diagnosis + '\n')

def searchLine11(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox = messagebox.askyesno('Save data', 'Do you want to save for patient 11 ?')
    if MsgBox == 1:
        with open('./newpatient/entryfile11.txt', 'w') as file11:
            file11.write(Firstname + " " + Surname + '\n')
            file11.write(Birthvalue + '\n')
            file11.write(Allergia + '\n')
            file11.write(TransDisVal + '\n')
            file11.write(Diagnosis + '\n')

def searchLine12(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox = messagebox.askyesno('Save data', 'Do you want to save for patient 12 ?')
    if MsgBox == 1:
        with open('./newpatient/entryfile12.txt', 'w') as file12:
            file12.write(Firstname + " " + Surname + '\n')
            file12.write(Birthvalue + '\n')
            file12.write(Allergia + '\n')
            file12.write(TransDisVal + '\n')
            file12.write(Diagnosis + '\n')

def searchLine13(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox = messagebox.askyesno('Save data', 'Do you want to save for patient 13 ?')
    if MsgBox == 1:
        with open('./newpatient/entryfile13.txt', 'w') as file13:
            file13.write(Firstname + " " + Surname + '\n')
            file13.write(Birthvalue + '\n')
            file13.write(Allergia + '\n')
            file13.write(TransDisVal + '\n')
            file13.write(Diagnosis + '\n')

def searchLine14(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox = messagebox.askyesno('Save data', 'Do you want to save for patient 14 ?')
    if MsgBox == 1:
        with open('./newpatient/entryfile14.txt', 'w') as file14:
            file14.write(Firstname + " " + Surname + '\n')
            file14.write(Birthvalue + '\n')
            file14.write(Allergia + '\n')
            file14.write(TransDisVal + '\n')
            file14.write(Diagnosis + '\n')

def searchLine15(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox = messagebox.askyesno('Save data', 'Do you want to save for patient 15 ?')
    if MsgBox == 1:
        with open('./newpatient/entryfile15.txt', 'w') as file15:
            file15.write(Firstname + " " + Surname + '\n')
            file15.write(Birthvalue + '\n')
            file15.write(Allergia + '\n')
            file15.write(TransDisVal + '\n')
            file15.write(Diagnosis + '\n')

def searchLine16(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox = messagebox.askyesno('Save data', 'Do you want to save for patient 16 ?')
    if MsgBox == 1:
        with open('./newpatient/entryfile16.txt', 'w') as file16:
            file16.write(Firstname + " " + Surname + '\n')
            file16.write(Birthvalue + '\n')
            file16.write(Allergia + '\n')
            file16.write(TransDisVal + '\n')
            file16.write(Diagnosis + '\n')

def searchLine17(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox = messagebox.askyesno('Save data', 'Do you want to save for patient 17 ?')
    if MsgBox == 1:
        with open('./newpatient/entryfile17.txt', 'w') as file17:
            file17.write(Firstname + " " + Surname + '\n')
            file17.write(Birthvalue + '\n')
            file17.write(Allergia + '\n')
            file17.write(TransDisVal + '\n')
            file17.write(Diagnosis + '\n')

def searchLine18(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox = messagebox.askyesno('Save data', 'Do you want to save for patient 18 ?')
    if MsgBox == 1:
        with open('./newpatient/entryfile18.txt', 'w') as file18:
            file18.write(Firstname + " " + Surname + '\n')
            file18.write(Birthvalue + '\n')
            file18.write(Allergia + '\n')
            file18.write(TransDisVal + '\n')
            file18.write(Diagnosis + '\n')

def searchLine19(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox = messagebox.askyesno('Save data', 'Do you want to save for patient 19 ?')
    if MsgBox == 1:
        with open('./newpatient/entryfile19.txt', 'w') as file19:
            file19.write(Firstname + " " + Surname + '\n')
            file19.write(Birthvalue + '\n')
            file19.write(Allergia + '\n')
            file19.write(TransDisVal + '\n')
            file19.write(Diagnosis + '\n')

def searchLine20(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox = messagebox.askyesno('Save data', 'Do you want to save for patient 20 ?')
    if MsgBox == 1:
        with open('./newpatient/entryfile20.txt', 'w') as file20:
            file20.write(Firstname + " " + Surname + '\n')
            file20.write(Birthvalue + '\n')
            file20.write(Allergia + '\n')
            file20.write(TransDisVal + '\n')
            file20.write(Diagnosis + '\n')

def searchLine21(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox = messagebox.askyesno('Save data', 'Do you want to save for patient 21 ?')
    if MsgBox == 1:
        with open('./newpatient/entryfile21.txt', 'w') as file21:
            file21.write(Firstname + " " + Surname + '\n')
            file21.write(Birthvalue + '\n')
            file21.write(Allergia + '\n')
            file21.write(TransDisVal + '\n')
            file21.write(Diagnosis + '\n')

def searchLine22(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox = messagebox.askyesno('Save data', 'Do you want to save for patient 22 ?')
    if MsgBox == 1:
        with open('./newpatient/entryfile22.txt', 'w') as file22:
            file22.write(Firstname + " " + Surname + '\n')
            file22.write(Birthvalue + '\n')
            file22.write(Allergia + '\n')
            file22.write(TransDisVal + '\n')
            file22.write(Diagnosis + '\n')

def searchLine23(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox = messagebox.askyesno('Save data', 'Do you want to save for patient 23 ?')
    if MsgBox == 1:
        with open('./newpatient/entryfile23.txt', 'w') as file23:
            file23.write(Firstname + " " + Surname + '\n')
            file23.write(Birthvalue + '\n')
            file23.write(Allergia + '\n')
            file23.write(TransDisVal + '\n')
            file23.write(Diagnosis + '\n')

def searchLine24(Firstname, Surname, Birthvalue, Allergia, TransDisVal, Diagnosis):
    MsgBox = messagebox.askyesno('Save data', 'Do you want to save for patient 24 ?')
    if MsgBox == 1:
        with open('./newpatient/entryfile24.txt', 'w') as file24:
            file24.write(Firstname + " " + Surname + '\n')
            file24.write(Birthvalue + '\n')
            file24.write(Allergia + '\n')
            file24.write(TransDisVal + '\n')
            file24.write(Diagnosis + '\n')

labelID = Label(gui, text='ID Number: ',
    font="Times 14 bold",
    fg='white', bg='DodgerBlue2')
labelID.pack(pady=10)

PatientID=StringVar()
patientnum = Entry(gui, textvariable=PatientID,
    highlightbackground='SteelBlue', bd=4)
PatientID.set('Patient ID')
patientnum.pack()

labelName = Label(gui, text='Name : ',
    font="Times 14 bold",
    fg='white', bg='DodgerBlue2')
labelName.pack(pady=10)

Firstname=StringVar()
labelfirst = Entry(gui, textvariable=Firstname,
    highlightbackground='DodgerBlue2', bd=4)
Firstname.set('Firstname')
labelfirst.pack()

Surname=StringVar()
lblsurname = Entry(gui, textvariable=Surname,
    highlightbackground='SteelBlue', bd=4)
Surname.set('Lastname')
lblsurname.pack()

labelBirth = Label(gui, text='Birth Date : ', font="Times 14 bold",
    fg='white', bg='DodgerBlue2')
labelBirth.pack(pady=10)

Birthvalue=StringVar()
Birth_entree = Entry(gui, textvariable=Birthvalue,
    highlightbackground='SteelBlue', bd=4)
Birthvalue.set('Format: 00/00/0000')
Birth_entree.pack()

labelAller = Label(gui)
labelAller = Label(text='Allergy : ',
    font="Times 14 bold",
    fg='white', bg='DodgerBlue2')
labelAller.pack(pady=10)

Allergia=StringVar()
Patient_allergy = Entry(gui, textvariable=Allergia,
    highlightbackground='SteelBlue', bd=4)
Allergia.set('None')
Patient_allergy.pack()

labelTrans = Label(gui, text='Transmissible Disease : ',
    font="Times 14 bold",
    fg='white', bg='DodgerBlue2')
labelTrans.pack(pady=10)

TransDisVal = StringVar()
TransDisease = Entry(gui, textvariable=TransDisVal,
    highlightbackground='SteelBlue', bd=4)
TransDisVal.set('None')
TransDisease.pack()

labelDiag = Label(gui, text='Diagnosis : ',
    font="Times 14 bold",
    fg='white', bg='DodgerBlue2')
labelDiag.pack(pady=10)

Diagnosis = StringVar()
Diagnos_pat = Entry(gui, textvariable=Diagnosis,
    highlightbackground='SteelBlue', bd=4)
Diagnosis.set('Diagnostic (main)')
Diagnos_pat.pack()

bouton1 = Button(gui, text="Enter", width=8, bd=4,
    fg='yellow', bg='RoyalBlue3', highlightbackground='SteelBlue',
    activebackground='dark turquoise',
    command = lambda: get(PatientID, patientnum, Firstname, labelfirst,
        Surname, lblsurname, Birthvalue, Birth_entree, Allergia,
        Patient_allergy, TransDisVal, TransDisease, Diagnosis, Diagnos_pat))
bouton1.pack(side=LEFT, padx=10, pady=20)

buttQuit=Button(gui, text="Quit", width=8, bd=4,
    fg='cyan', bg='RoyalBlue3', highlightbackground='SteelBlue',
    activebackground='dark turquoise', command=quit)
buttQuit.pack(side=LEFT, padx=10, pady=20)

gui.mainloop()
