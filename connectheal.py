#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
from tkinter import ttk
import tkinter.messagebox
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
