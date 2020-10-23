#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
# from tkinter import ttk
import tkinter.messagebox
import os
import time
import datetime
import pymysql


#------------------

StudentID = StringVar()
Firstname = StringVar()
Surname = StringVar()
Address = StringVar()
Gender = StringVar()
Mobile = StringVar()

#------------------

def iExit():
    iExit = tkinter.messagebox.askyesno('MySQL Connection', 'Confirm if you want to exit ?')
    if iExit > 0:
        root.destroy()
        return

def Reset():
    self.entStudentID.delete(0, END)
    self.entFirstname.delete(0, END)
    self.entSurname.delete(0, END)
    self.entAddress.delete(0, END)
    Gender.set("")
    self.entMobile.delete(0, END)

# Interact with database to add
def addData():
    if StudentID.get() == "" or Firstname.get() == "" or Surname.get() == "":
        tkinter.messagebox.showerror("MySQL Connection", "Enter Correct Details.")
    else:
        sqlCon = pymysql.connect(host='127.0.0.1', user='root', password='Ko@l@tr3379', database='pydatabase')
        cur = sqlCon.cursor()
        cur.execute("INSERT into pydatabase values (%s,%s,%s,%s,%s,%s)",(

        StudentID.get(),
        Firstname.get(),
        Surname.get(),
        Address.get(),
        Gender.get(),
        Mobile.get(),
        ))
        sqlCon.commit()
        sqlCon.close()
        tkinter.messagebox.showinfo("MySQL connection", "Record Entered Successfully !")

# Interact with database to display
def DisplayData():
    sqlCon = pymysql.connect(host='127.0.0.1', user='root', password='Ko@l@tr3379', database='pydatabase')
    cur = sqlCon.cursor()
    cur.execute("SELECT * from pydatabase")
    result = cur.fetchall()
    if len(result) != 0:
        self.student_records.delete(*self.student_records.get_children())
        for row in result:
            self.student_records.insert('',END,values =row)
        sqlCon.commit()
    sqlCon.close()

# Interact with database to diplay database in frame
def PyDataBaseInfo(ev):
    viewInfo = self.student_records.focus()
    learnerData = self.student_records.item(viewInfo)
    row = learnerData['values']
    StudentID.set(row[0])
    Firstname.set(row[1])
    Surname.set(row[2])
    Address.set(row[3])
    Gender.set(row[4])
    Mobile.set(row[5])

# Interact with database to update
def update():
    sqlCon = pymysql.connect(host='127.0.0.1', user='root', password='Ko@l@tr3379', database='pydatabase')
    cur = sqlCon.cursor()
    cur.execute("UPDATE pydatabase set firstname=%s, surname=%s, address=%s, gender=%s, mobile=%s where stdid=%s",(
    Firstname.get(),
    Surname.get(),
    Address.get(),
    Gender.get(),
    Mobile.get(),
    StudentID.get()
    ))
    sqlCon.commit()
    DisplayData()
    sqlCon.close()
    tkinter.messagebox.showinfo("Data Entry Form", "Record Updated Successfully !")

# Interact with database to delete
def deleteDB():
    sqlCon = pymysql.connect(host='127.0.0.1', user='root', password='Ko@l@tr3379', database='pydatabase')
    cur = sqlCon.cursor()
    cur.execute("DELETE from pydatabase where stdid=%s", StudentID.get())
    sqlCon.commit()
    DisplayData()
    sqlCon.close()
    tkinter.messagebox.showinfo("Data Entry Form", "Record Successfully Deleted !")
    Reset()

# Interact with database to search
def searchDB():
    try:
        sqlCon = pymysql.connect(host='127.0.0.1', user='root', password='Ko@l@tr3379', database='pydatabase')
        cur = sqlCon.cursor()
        cur.execute("SELECT * from pydatabase where stdid=%s", StudentID.get())
        row = cur.fetchone()

        StudentID.set(row[0])
        Firstname.set(row[1])
        Surname.set(row[2])
        Address.set(row[3])
        Gender.set(row[4])
        Mobile.set(row[5])

        sqlCon.commit()
    except:
        tkinter.messagebox.showinfo("Data Entry Form", "No Such Record Found !")
        Reset()

    sqlCon.close()














# Main page
def callResident(self):
    self.can.delete(ALL)
    self.can.configure(background='cyan')
    self.photo=PhotoImage(file='./syno_gif/title_tt.png')
    self.item=self.can.create_image(625, 85, image=self.photo)

    """
    # To backup (main file)
    self.updateFiletxt()
    dispAgBox()
    dispTttBox()
    dispResFunc()
    """

    # Display date
    self.x1, self.y1 = 1065, 70
    self.Date_write=Entry(self.can)
    self.data_time=StringVar()
    self.Date_write=Entry(self.can, textvariable=self.data_time, width=10,
        highlightbackground='grey', bd=4)
    self.data_time.set(time.strftime("%d/%m/%Y"))
    self.Date_write=self.can.create_window(self.x1, self.y1,
        window=self.Date_write)

    # Static time
    self.x2, self.y2 = 1165, 70
    self.Date_write2 = Entry(self.can)
    self.data_time2 = StringVar()
    self.Date_write2 = Entry(self.can, width=10, textvariable=self.data_time2,
        highlightbackground='grey', bd=4)
    self.data_time2.set(time.strftime("%H:%M:%S %p"))
    self.Date_write2=self.can.create_window(self.x2, self.y2,
        window=self.Date_write2)

    # To display time dynamically à revoir (new_file.py)
    # To introduce a new pytient
    self.x3, self.y3 = 200, 160
    self.b3=Button(self.can, width=10, font=16, bd=3, highlightbackground='blue',
        bg='RoyalBlue3', fg='white', activebackground='dark turquoise',
        activeforeground='white', text="New Entry", command=self.callPatient1)
    self.fb3=self.can.create_window(self.x3, self.y3, window=self.b3)

    # To add one patient and files
    self.x4, self.y4 = 400, 160
    self.b4=Button(self.can, width=10, font=16, bd=3, highlightbackground='blue',
        bg='RoyalBlue3', fg='cyan', activebackground='dark turquoise',
        activeforeground='white', text="Add patient", command=self.addPatientAfter)
    self.fb4=self.can.create_window(self.x4, self.y4, window=self.b4)
    
    # To refresh canvas + menu bar
    self.x5, self.y5 = 600, 160
    self.b5=Button(self.can, width=10, font=16, bd=3, bg='RoyalBlue3',
        fg='SpringGreen2', highlightbackground='blue',
        activebackground='yellow', activeforeground='SpringGreen2',
        text="Refresh", command=self.upDateAll)
    self.fb5=self.can.create_window(self.x5, self.y5, window=self.b5)

    # To delete one patient and all files
    self.x6, self.y6 = 800, 160
    self.b6=Button(self.can, width=10, font=16, bd=3, highlightbackground='blue',
        bg='RoyalBlue3', fg='coral', activebackground='red', 
        activeforeground='white', text="Delete patient", command=self.delEverPat)
    self.fb6=self.can.create_window(self.x6, self.y6, window=self.b6)


    # Patient 1
    try:
        with open('./newpatient/entryfile.txt', 'r') as namefile:
            line1=namefile.readline()
    except FileNotFoundError as callfile:
        print("File entryfile.txt doesn't exist !", callfile)

    self.data_time=line1
    self.x10, self.y10 = 129, 230
    self.Data_write=Entry(self.can)
    self.new_data1=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data1,
        highlightbackground='grey', bd=4)
    self.new_data1.set(line1)
    self.Data_write=self.can.create_window(self.x10, self.y10,
        window=self.Data_write)

    self.x11, self.y11 = 271, 230
    self.b11=Button(self.can, width=8, font=16, bg='blue violet', fg='cyan',
        activebackground='aquamarine', text="Allergy",
        command=self.allergyLink)
    self.fb11=self.can.create_window(self.x11, self.y11, window=self.b11)

    self.x12, self.y12 = 429, 230
    self.b12=Button(self.can, width=18, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Diagnostic + ATCD",
        command=self.diag1)
    self.fb12=self.can.create_window(self.x12, self.y12, window=self.b12)

    self.x13, self.y13 = 597, 230
    self.b13=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Treatments",
        command=self.tttMed1)
    self.fb13=self.can.create_window(self.x13, self.y13, window=self.b13)

    self.x14, self.y14 = 725, 230
    self.b14=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Laboratory",
        command=self.laboResult)
    self.fb14=self.can.create_window(self.x14, self.y14, window=self.b14)

    self.x15, self.y15 = 853, 230
    self.b15=Button(self.can, width=10, font=15, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Medical Visit",
        command=self.visitMed)
    self.fb15=self.can.create_window(self.x15, self.y15, window=self.b15)

    self.x16, self.y16 = 981, 230
    self.b16=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Intolerance",
        command=self.nutritionMenu)
    self.fb16=self.can.create_window(self.x16, self.y16, window=self.b16)

    self.x17, self.y17 = 1109, 230
    self.b17=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="BMI",
        command=self.calculB)
    self.fb17=self.can.create_window(self.x17, self.y17, window=self.b17)

    self.can.configure(scrollregion=self.can.bbox(ALL))
