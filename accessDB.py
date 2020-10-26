#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    App for many doing severals interactions
    with a MySQL database in python code.
    My first one.
    Install python3-pymysql on your workstation
    not in your virtualenv (otherwise doesn't work)!
    > sudo apt install python3-pymysql
    then install pymysql into your virtualenv.
    > pip3 install pymysql or PyMySQL
"""


from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import os
import time
import datetime
from backapp import *
from agendapp import dispAgBox
from tttapp import dispTttBox
from resapp import dispResFunc
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError as err_report:
    print("+ An error occured about pymysql !", err_report)
    pass


def showDbPatient(self):
    """
        Open new window to display
        all data from database
    """
    self.can.delete(ALL)
    self.can.configure(background='cyan')
    self.photo=PhotoImage(file='./syno_gif/title_tt.png')
    self.item=self.can.create_image(625, 85, image=self.photo)


    PatientID = StringVar()
    Firstname = StringVar()
    Surname = StringVar()
    Allergy = StringVar()
    Born = StringVar()
    Diagnostic = StringVar()

    def searchDB():
        sqlCon = pymysql.connect(host='127.0.0.1', user='root', password='Ko@l@tr3379', database='timetrackconn')
        cur = sqlCon.cursor()
        cur.execute("SELECT * from timetrackconn")
        result = cur.fetchall()
        if len(result) != 0:
            self.student_records.delete(*self.student_records.get_children())
            for row in result:
                self.student_records.insert('', END, values = row)
            sqlCon.commit()
        sqlCon.close()

    self.student_records=ttk.Treeview(self.can, height=24, columns=("stdid", 
        "firstname", "surname", "allergy", "born", "maindiagnostic"))

    self.student_records.heading("stdid", text="PatientID")
    self.student_records.heading("firstname", text="Firstname")
    self.student_records.heading("surname", text="Surname")
    self.student_records.heading("allergy", text="Allergy")
    self.student_records.heading("born", text="Born")
    self.student_records.heading("maindiagnostic", text="Diagnostic")

    self.student_records['show']="headings"

    self.student_records.column("stdid", width=100)
    self.student_records.column("firstname", width=150)
    self.student_records.column("surname", width=150)
    self.student_records.column("allergy", width=200)
    self.student_records.column("born", width=100)
    self.student_records.column("maindiagnostic", width=200)

    self.student_records.pack(fill=BOTH, expand=YES)

    #self.student_records.bind("<ButtonRelease-1>", PyDataBaseInfo)
    self.btnSearch = Button(self.can, font=('arial', 12, 'bold'), text="Display", bd=4, 
        padx=8, pady=1, width=8, height=1, command=searchDB)
    self.btnSearch.pack()

    self.can.configure(scrollregion=self.can.bbox(ALL))
