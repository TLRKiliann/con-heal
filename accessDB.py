#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    App for many doing severals interactions
    with a MySQL database in python code.
    My first one 
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
import pymysql


def showDbPatient(self):
    """
        Open new window to display
        all data from database
    """
    self.can.delete(ALL)
    self.can.configure(background='cyan')
    #self.photo=PhotoImage(file='./syno_gif/title_tt.png')
    #self.item=self.can.create_image(625, 85, image=self.photo)


    PatientID = StringVar()
    Firstname = StringVar()
    Surname = StringVar()

    def searchDB():
        sqlCon = pymysql.connect(host='127.0.0.1', user='root', password='Ko@l@tr3379', database='timetrackconn')
        cur = sqlCon.cursor()
        cur.execute("SELECT * from timetrackconn where stdid=1")
        result = cur.fetchall()
        if len(result) != 0:
            self.student_records.delete(*self.student_records.get_children())
            for row in result:
                self.student_records.insert('', END, values = row)
            sqlCon.commit()
        sqlCon.close()

    self.student_records=ttk.Treeview(self, height=12, columns=("stdid", "firstname", "surname"))

    self.student_records.heading("stdid", text="PatientID")
    self.student_records.heading("firstname", text="Firstname")
    self.student_records.heading("surname", text="Surname")

    self.student_records['show']="headings"

    self.student_records.column("stdid", width=100)
    self.student_records.column("firstname", width=100)
    self.student_records.column("surname", width=100)

    self.student_records.pack()
    #self.student_records.bind("<ButtonRelease-1>", PyDataBaseInfo)
    self.btnSearch = Button(self, font=('arial', 12, 'bold'), text="Search", bd=4, 
        padx=8, pady=1, width=8, height=1, command=searchDB)
    self.btnSearch.pack()

    self.can.configure(scrollregion=self.can.bbox(ALL))
