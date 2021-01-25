#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
import tkinter as tk
from tkinter import ttk
import sys
import os
import time
import datetime as dt
from backapp import *
from agendapp import dispAgBox
from tttapp import dispTttBox
from resapp import dispResFunc


def callResident(self):
    """
        Main function called since main app
        heal_track.py for displaying patients
        with theirs names and more.
    """    
    self.can.delete(ALL)
    self.can.configure(background='DodgerBlue2')
    self.photo = tk.PhotoImage(file='./syno_gif/title_tt3.png')
    self.item_image = self.can.create_image(625, 85, image=self.photo)

    # Display date
    self.x1, self.y1 = 1140, 40
    self.data_time = tk.StringVar()
    self.datew = tk.Entry(self.can, textvariable=self.data_time, 
        width=9, bd=3, highlightbackground='grey')
    self.data_time.set(time.strftime("%d/%m/%Y"))
    self.fdatew_window = self.can.create_window(self.x1, self.y1,
        window=self.datew)

    # To introduce a new pytient
    self.x3, self.y3 = 125, 160
    self.b3 = tk.Button(self.can, text="New Entry", font=16,
        width=10, bd=3, bg='RoyalBlue3', fg='white',
        highlightbackground='pale turquoise',
        activebackground='pale turquoise',
        command=self.callPatient1)
    self.fb3_window = self.can.create_window(self.x3,
        self.y3, window=self.b3)

    # To add one patient and files
    self.x4, self.y4 = 325, 160
    self.b4 = tk.Button(self.can, text="Add patient", font=16,
        width=10, bd=3, bg='RoyalBlue3', fg='white',
        highlightbackground='pale turquoise',
        activebackground='pale turquoise',
        command=self.addPatientAfter)
    self.fb4_window = self.can.create_window(self.x4,
        self.y4, window=self.b4)
    
    # To refresh canvas + menu bar
    self.x5, self.y5 = 525, 160
    self.b5 = tk.Button(self.can, text="Refresh", font=16,
        width=10, bd=3, bg='RoyalBlue3', fg='SpringGreen2',
        highlightbackground='pale turquoise',
        activebackground='pale turquoise',
        command=self.upDateAll)
    self.fb5_window = self.can.create_window(self.x5,
        self.y5, window=self.b5)

    # To delete one patient and all files
    self.x6, self.y6 = 725, 160
    self.b6 = tk.Button(self.can, text="Delete patient", font=16,
        width=10, bd=3, bg='RoyalBlue3', fg='coral',
        highlightbackground='pale turquoise',
        activebackground='red',
        activeforeground='white', command=self.delEverPat)
    self.fb6_window = self.can.create_window(self.x6,
        self.y6, window=self.b6)

    # To go to resident page
    self.x6, self.y6 = 925, 160
    self.b6 = tk.Button(self.can, text="TextBox", font=16,
        width=10, bd=3, bg='RoyalBlue3', fg='white',
        highlightbackground='pale turquoise',
        activebackground='pale turquoise',
        command=self.showSynopsis)
    self.fb6_window = self.can.create_window(self.x6,
        self.y6, window=self.b6)

    # DB
    self.x7, self.y7 = 1125, 160
    self.b7 = tk.Button(self.can, text="DataBase", font=16,
        width=10, bd=3, bg='RoyalBlue3', fg='white',
        highlightbackground='pale turquoise',
        activebackground='pale turquoise',
        command=self.funcPyCon)
    self.fb7_window = self.can.create_window(self.x7,
        self.y7, window=self.b7)

    # Patient 1 +20
    try:
        with open('./newpatient/entryfile.txt', 'r') as namefile:
            line1 = namefile.readline()
    except FileNotFoundError as callfile:
        print("File entryfile.txt doesn't exist !", callfile)

    try:
        self.data_time = line1
        self.x10, self.y10 = 149, 230
        self.new_data1 = StringVar()
        self.d10 = Entry(self.can,
            textvariable=self.new_data1,
            highlightbackground='grey', bd=4)
        if line1 == '-':
            line1 = line1
        else:
            line1 = line1[:-1]
        self.new_data1.set(line1)
        self.fd10_window = self.can.create_window(self.x10,
            self.y10, window=self.d10)
    except UnboundLocalError as ub_error1:
        print("+ File 1 not created !", ub_error1)

    self.x11, self.y11 = 291, 230
    self.b11 = tk.Button(self.can, text="Update", font=16,
        width=8, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.updateLink)
    self.fb11_window = self.can.create_window(self.x11,
        self.y11, window=self.b11)

    self.x12, self.y12 = 449, 230
    self.b12 = tk.Button(self.can, text="Diagnostic + ATCD",
        font=16, width=18, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.diag1)
    self.fb12_window = self.can.create_window(self.x12,
        self.y12, window=self.b12)

    self.x13, self.y13 = 617, 230
    self.b13 = tk.Button(self.can, text="Treatments",
        font=16, width=10, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.tttMed1)
    self.fb13_window = self.can.create_window(self.x13,
        self.y13, window=self.b13)

    self.x14, self.y14 = 745, 230
    self.b14 = tk.Button(self.can, text="Laboratory",
        font=16, width=10, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.laboResult)
    self.fb14_window = self.can.create_window(self.x14,
        self.y14, window=self.b14)

    self.x15, self.y15 = 873, 230
    self.b15 = tk.Button(self.can, text="Medical Visit",
        font=16, width=10, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.visitMed)
    self.fb15_window = self.can.create_window(self.x15,
        self.y15, window=self.b15)

    self.x16, self.y16 = 1001, 230
    self.b16 = tk.Button(self.can, text="Intolerance",
        font=16, width=10, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.nutritionMenu)
    self.fb16_window = self.can.create_window(self.x16,
        self.y16, window=self.b16)

    self.x17, self.y17 = 1129, 230
    self.b17 = tk.Button(self.can, text="BMI",
        font=16, width=10, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.calculB)
    self.fb17_window = self.can.create_window(self.x17,
        self.y17, window=self.b17)

    # Patient 2
    try:
        with open('./newpatient/entryfile2.txt', 'r') as namefile:
            line2 = namefile.readline()
    except FileNotFoundError as callfile2:
        print("File entryfile2.txt doesn't exist !", callfile2)

    try:
        self.new_data2 = line2
        self.x20, self.y20 = 149, 262
        self.new_data2 = StringVar()
        self.d20 = Entry(self.can, textvariable=self.new_data2,
            highlightbackground='grey', bd=4)
        if line2 == '--':
            line2 = line2
        else:
            line2 = line2[:-1]
        self.new_data2.set(line2)
        self.fd20_window = self.can.create_window(self.x20,
            self.y20, window=self.d20)
    except UnboundLocalError as ub_error2:
        print("+ File 2 not created !", ub_error2)

    self.x21, self.y21 = 291, 262
    self.b21 = Button(self.can, text="Update", font=16,
        width=8, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.updateLink2)
    self.fb21_window = self.can.create_window(self.x21,
        self.y21, window=self.b21)

    self.x22, self.y22 = 449, 262
    self.b22 = Button(self.can, text="Diagnostic + ATCD",
        font=16, width=18, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.diag2)
    self.fb22_window = self.can.create_window(self.x22,
        self.y22, window=self.b22)

    self.x23, self.y23 = 617, 262
    self.b23 = Button(self.can, text="Treatments",
        font=16, width=10, fg='yellow', bg='RoyalBlue3', 
        activebackground='pale turquoise',
        command=self.tttMed2)
    self.fb23_window = self.can.create_window(self.x23,
        self.y23, window=self.b23)

    self.x24, self.y24 = 745, 262
    self.b24 = Button(self.can, text="Laboratory",
        font=16, width=10, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.laboResult2)
    self.fb24_window = self.can.create_window(self.x24,
        self.y24, window=self.b24)

    self.x25, self.y25 = 873, 262
    self.b25 = Button(self.can, text="Medical Visit",
        font=16, width=10, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.visitMed2)
    self.fb25_window = self.can.create_window(self.x25,
        self.y25, window=self.b25)

    self.x26, self.y26 = 1001, 262
    self.b26 = Button(self.can, text="Intolerance",
        font=16, width=10, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.nutritionMenu2)
    self.fb26_window = self.can.create_window(self.x26,
        self.y26, window=self.b26)

    self.x27, self.y27 = 1129, 262
    self.b27 = Button(self.can, text="BMI",
        font=16, width=10, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.calculB2)
    self.fb27_window = self.can.create_window(self.x27,
        self.y27, window=self.b27)

    # Patient 3
    try:
        with open('./newpatient/entryfile3.txt', 'r') as namefile:
            line3 = namefile.readline()
    except FileNotFoundError as callfile3:
        print("File entryfile3.txt doesn't exist !", callfile3)

    try:
        self.new_data3 = line3
        self.x30, self.y30 = 149, 294
        self.new_data3 = StringVar()
        self.d30 = Entry(self.can, textvariable=self.new_data3,
            highlightbackground='grey', bd=4)
        if line3 == '---':
            line3 = line3
        else:
            line3 = line3[:-1]
        self.new_data3.set(line3)
        self.fd30_window = self.can.create_window(self.x30,
            self.y30, window=self.d30)
    except UnboundLocalError as ub_error3:
        print("+ File 3 not created !", ub_error3)

    self.x31, self.y31 = 291, 294
    self.b31 = Button(self.can, text="Update", font=16,
        width=8, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.updateLink3)
    self.fb31_window = self.can.create_window(self.x31,
        self.y31, window=self.b31)

    self.x32, self.y32 = 449, 294
    self.b32 = Button(self.can, text="Diagnostic + ATCD",
        font=16, width=18, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.diag3)
    self.fb32_window = self.can.create_window(self.x32,
        self.y32, window=self.b32)

    self.x33, self.y33 = 617, 294
    self.b33 = Button(self.can, text="Treatments",
        font=16, width=10, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.tttMed3)
    self.fb33_window = self.can.create_window(self.x33,
        self.y33, window=self.b33)

    self.x34, self.y34 = 745, 294
    self.b34 = Button(self.can, text="Laboratory",
        font=16, width=10, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.laboResult3)
    self.fb34_window = self.can.create_window(self.x34,
        self.y34, window=self.b34)

    self.x35, self.y35 = 873, 294
    self.b35 = Button(self.can, text="Medical Visit",
        font=16, width=10, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.visitMed3)
    self.fb35_window = self.can.create_window(self.x35,
        self.y35, window=self.b35)

    self.x36, self.y36 = 1001, 294
    self.b36 = Button(self.can, text="Intolerance",
        font=16, width=10, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.nutritionMenu3)
    self.fb36_window = self.can.create_window(self.x36,
        self.y36, window=self.b36)

    self.x37, self.y37 = 1129, 294
    self.b37 = Button(self.can, text="BMI",
        font=16, width=10, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.calculB3)
    self.fb37_window = self.can.create_window(self.x37,
        self.y37, window=self.b37)

    # Patient 4
    try:
        with open('./newpatient/entryfile4.txt', 'r') as namefile:
            line4 = namefile.readline()
    except FileNotFoundError as callfile4:
        print("File entryfile4.txt doesn't exist !", callfile4)

    try:
        self.new_data4 = line4
        self.x40, self.y40 = 149, 326
        self.new_data4 = StringVar()
        self.d40 = Entry(self.can,
            textvariable=self.new_data4,
            highlightbackground='grey', bd=4)
        if line4 == '----':
            line4 = line4
        else:
            line4 = line4[:-1]
        self.new_data4.set(line4)
        self.fd40_window = self.can.create_window(self.x40,
            self.y40, window=self.d40)
    except UnboundLocalError as ub_error4:
        print("+ File 4 not created !", ub_error4)

    self.x41, self.y41 = 291, 326
    self.b41 = Button(self.can, text="Update",
        font=16, width=8, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.updateLink4)
    self.fb41_window = self.can.create_window(self.x41,
        self.y41, window=self.b41)

    self.x42, self.y42 = 449, 326
    self.b42 = Button(self.can, text="Diagnostic + ATCD",
        font=16, width=18, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.diag4)
    self.fb42_window = self.can.create_window(self.x42,
        self.y42, window=self.b42)

    self.x43, self.y43 = 617, 326
    self.b43 = Button(self.can, text="Treatments",
        font=16, width=10, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.tttMed4)
    self.fb43_window = self.can.create_window(self.x43,
        self.y43, window=self.b43)

    self.x44, self.y44 = 745, 326
    self.b44 = Button(self.can, text="Laboratory",
        font=16, width=10, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.laboResult4)
    self.fb44_window = self.can.create_window(self.x44,
        self.y44, window=self.b44)

    self.x45, self.y45 = 873, 326
    self.b45 = Button(self.can, text="Medical Visit",
        font=16, width=10, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.visitMed4)
    self.fb45_window = self.can.create_window(self.x45,
        self.y45, window=self.b45)

    self.x46, self.y46 = 1001, 326
    self.b46 = Button(self.can, text="Intolerance",
        font=16, width=10, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.nutritionMenu4)
    self.fb46_window = self.can.create_window(self.x46,
        self.y46, window=self.b46)

    self.x47, self.y47 = 1129, 326
    self.b47 = Button(self.can, text="BMI",
        font=16, width=10, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.calculB4)
    self.fb47_window = self.can.create_window(self.x47,
        self.y47, window=self.b47)

    # Patient 5
    try:
        with open('./newpatient/entryfile5.txt', 'r') as namefile:
            line5 = namefile.readline()
    except FileNotFoundError as callfile5:
        print("File entryfile5.txt doesn't exist !", callfile5)

    try:
        self.new_data5 = line5
        self.x50, self.y50 = 149, 358
        self.new_data5 = StringVar()
        self.d50 = Entry(self.can,
            textvariable=self.new_data5,
            highlightbackground='grey', bd=4)
        if line5 == '-----':
            line5 = line5
        else:
            line5 = line5[:-1]
        self.new_data5.set(line5)
        self.fd50_window = self.can.create_window(self.x50,
            self.y50, window=self.d50)
    except UnboundLocalError as ub_error5:
        print("+ File 5 not created !", ub_error5)

    self.x51, self.y51 = 291, 358
    self.b51 = Button(self.can, text="Update", font=16,
        width=8, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.updateLink5)
    self.fb51_window = self.can.create_window(self.x51,
        self.y51, window=self.b51)

    self.x52, self.y52 = 449, 358
    self.b52 = Button(self.can, text="Diagnostic + ATCD", font=16,
        width=18, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.diag5)
    self.fb52_window = self.can.create_window(self.x52,
        self.y52, window=self.b52)

    self.x53, self.y53 = 617, 358
    self.b53 = Button(self.can, text="Treatments", font=16,
        width=10, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.tttMed5)
    self.fb53_window = self.can.create_window(self.x53,
        self.y53, window=self.b53)

    self.x54, self.y54 = 745, 358
    self.b54 = Button(self.can, text="Laboratory", font=16,
        width=10, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.laboResult5)
    self.fb54_window = self.can.create_window(self.x54,
        self.y54, window=self.b54)

    self.x55, self.y55 = 873, 358
    self.b55 = Button(self.can, text="Medical Visit", font=16,
        width=10, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.visitMed5)
    self.fb55_window = self.can.create_window(self.x55,
        self.y55, window=self.b55)

    self.x56, self.y56 = 1001, 358
    self.b56 = Button(self.can, text="Intolerance", font=16,
        width=10, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.nutritionMenu5)
    self.fb56_window = self.can.create_window(self.x56,
        self.y56, window=self.b56)

    self.x57, self.y57 = 1129, 358
    self.b57 = Button(self.can, text="BMI", font=16,
        width=10, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.calculB5)
    self.fb57_window = self.can.create_window(self.x57,
        self.y57, window=self.b57)

    # Patient 6
    try:
        with open('./newpatient/entryfile6.txt', 'r') as namefile:
            line6 = namefile.readline()
    except FileNotFoundError as callfile6:
        print("File entryfile6.txt doesn't exist !", callfile6)

    try:
        self.new_data6 = line6
        self.x60, self.y60 = 149, 390
        self.new_data6 = StringVar()
        self.d60 = Entry(self.can, textvariable=self.new_data6,
            highlightbackground='grey', bd=4)
        if line6 == '------':
            line6 = line6
        else:
            line6 = line6[:-1]
        self.new_data6.set(line6)
        self.fd60_window = self.can.create_window(self.x60,
            self.y60, window=self.d60)
    except UnboundLocalError as ub_error6:
        print("+ File 6 not created !", ub_error6)

    self.x61, self.y61 = 291, 390
    self.b61 = Button(self.can, text="Update", font=16,
        width=8, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.updateLink6)
    self.fb61_window = self.can.create_window(self.x61,
        self.y61, window=self.b61)

    self.x62, self.y62 = 449, 390
    self.b62 = Button(self.can, text="Diagnostic + ATCD",
        font=16, width=18, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.diag6)
    self.fb62_window = self.can.create_window(self.x62,
        self.y62, window=self.b62)

    self.x64, self.y64 = 617, 390
    self.b64 = Button(self.can, text="Treatments", font=16,
        width=10, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.tttMed6)
    self.fb64_window = self.can.create_window(self.x64,
        self.y64, window=self.b64)

    self.x65, self.y65 = 745, 390
    self.b65 = Button(self.can, text="Laboratory", font=16,
        width=10, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.laboResult6)
    self.fb65_window = self.can.create_window(self.x65,
        self.y65, window=self.b65)

    self.x66, self.y66 = 873, 390
    self.b66 = Button(self.can, text="Medical Visit", font=16,
        width=10, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.visitMed6)
    self.fb66_window = self.can.create_window(self.x66,
        self.y66, window=self.b66)

    self.x67, self.y67 = 1001, 390
    self.b67 = Button(self.can, text="Intolerance", font=16,
        width=10, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.nutritionMenu6)
    self.fb67_window = self.can.create_window(self.x67,
        self.y67, window=self.b67)

    self.x68, self.y68 = 1129, 390
    self.b68 = Button(self.can, text="BMI", font=16,
        width=10, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.calculB6)
    self.fb68_window = self.can.create_window(self.x68,
        self.y68, window=self.b68)

    # Patient 7
    try:
        with open('./newpatient/entryfile7.txt', 'r') as namefile:
            line7 = namefile.readline()
    except FileNotFoundError as callfile7:
        print("File entryfile7.txt doesn't exist !", callfile7)

    try:
        self.new_data7 = line7
        self.x70, self.y70 = 149, 422
        self.new_data7 = StringVar()
        self.d70 = Entry(self.can, textvariable=self.new_data7,
            highlightbackground='grey', bd=4)
        if line7 == '-------':
            line7 = line7
        else:
            line7 = line7[:-1]
        self.new_data7.set(line7)
        self.fd70_window = self.can.create_window(self.x70,
            self.y70, window=self.d70)
    except UnboundLocalError as ub_error7:
        print("+ File 7 not created !", ub_error7)

    self.x71, self.y71 = 291, 422
    self.b71 = Button(self.can, text="Update", font=16,
        width=8, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.updateLink7)
    self.fb71_window = self.can.create_window(self.x71,
        self.y71, window=self.b71)

    self.x72, self.y72 = 449, 422
    self.b72 = Button(self.can, text="Diagnostic + ATCD",
        font=16, width=18, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.diag7)
    self.fb72_window = self.can.create_window(self.x72,
        self.y72, window=self.b72)

    self.x73, self.y73 = 617, 422
    self.b73 = Button(self.can, text="Treatments",
        font=16, width=10, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.tttMed7)
    self.fb73_window = self.can.create_window(self.x73,
        self.y73, window=self.b73)

    self.x74, self.y74 = 745, 422
    self.b74 = Button(self.can, text="Laboratory",
        font=16, width=10, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.laboResult7)
    self.fb74_window = self.can.create_window(self.x74,
        self.y74, window=self.b74)

    self.x75, self.y75 = 873, 422
    self.b75 = Button(self.can, text="Medical Visit",
        font=16, width=10, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.visitMed7)
    self.fb75_window = self.can.create_window(self.x75,
        self.y75, window=self.b75)

    self.x76, self.y76 = 1001, 422
    self.b76 = Button(self.can, text="Intolerance",
        font=16, width=10, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.nutritionMenu7)
    self.fb76_window = self.can.create_window(self.x76,
        self.y76, window=self.b76)

    self.x77, self.y77 = 1129, 422
    self.b77 = Button(self.can, text="BMI", font=16,
        width=10, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.calculB7)
    self.fb77_window = self.can.create_window(self.x77,
        self.y77, window=self.b77)

    # Patient 8
    try:
        with open('./newpatient/entryfile8.txt', 'r') as namefile:
            line8 = namefile.readline()
    except FileNotFoundError as callfile8:
        print("File entryfile8.txt doesn't exist !", callfile8)

    try:
        self.new_data8 = line8
        self.x80, self.y80 = 149, 454
        self.new_data8 = StringVar()
        self.d80 = Entry(self.can, textvariable=self.new_data8,
            highlightbackground='grey', bd=4)
        if line8 == '--------':
            line8 = line8
        else:
            line8 = line8[:-1]
        self.new_data8.set(line8)
        self.fd80_window = self.can.create_window(self.x80,
            self.y80, window=self.d80)
    except UnboundLocalError as ub_error8:
        print("+ File 8 not created !", ub_error8)

    self.x81, self.y81 = 291, 454
    self.b81 = Button(self.can, text="Update", font=16,
        width=8, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.updateLink8)
    self.fb81_window = self.can.create_window(self.x81,
        self.y81, window=self.b81)

    self.x82, self.y82 = 449, 454
    self.b82 = Button(self.can, text="Diagnostic + ATCD",
        font=16, width=18, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.diag8)
    self.fb82_window = self.can.create_window(self.x82,
        self.y82, window=self.b82)

    self.x83, self.y83 = 617, 454
    self.b83 = Button(self.can, text="Treatments", font=16,
        width=10, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.tttMed8)
    self.fb83_window = self.can.create_window(self.x83,
        self.y83, window=self.b83)

    self.x84, self.y84 = 745, 454
    self.b84 = Button(self.can, text="Laboratory", font=16,
        width=10, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.laboResult8)
    self.fb84_window = self.can.create_window(self.x84,
        self.y84, window=self.b84)

    self.x85, self.y85 = 873, 454
    self.b85 = Button(self.can, text="Medical Visit", font=16,
        width=10, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.visitMed8)
    self.fb85_window = self.can.create_window(self.x85,
        self.y85, window=self.b85)

    self.x86, self.y86 = 1001, 454
    self.b86 = Button(self.can, text="Intolerance", font=16,
        width=10, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.nutritionMenu8)
    self.fb86_window = self.can.create_window(self.x86,
        self.y86, window=self.b86)

    self.x87, self.y87 = 1129, 454
    self.b87 = Button(self.can, text="BMI", font=16,
        width=10, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.calculB8)
    self.fb87_window = self.can.create_window(self.x87,
        self.y87, window=self.b87)

    # Patient 9
    try:
        with open('./newpatient/entryfile9.txt', 'r') as namefile:
            line9 = namefile.readline()
    except FileNotFoundError as callfile9:
        print("File entryfile9.txt doesn't exist !", callfile9)

    try:
        self.new_data9 = line9
        self.x90, self.y90 = 149, 486
        self.new_data9 = StringVar()
        self.d90 = Entry(self.can, textvariable=self.new_data9,
            highlightbackground='grey', bd=4)
        if line9 == '---------':
            line9 = line9
        else:
            line9 = line9[:-1]
        self.new_data9.set(line9)
        self.fd90_window = self.can.create_window(self.x90,
            self.y90, window=self.d90)
    except UnboundLocalError as ub_error9:
        print("+ File 9 not created !", ub_error9)

    self.x91, self.y91 = 291, 486
    self.b91 = Button(self.can, text="Update",
        font=16, width=8, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.updateLink9)
    self.fb91_window = self.can.create_window(self.x91,
        self.y91, window=self.b91)

    self.x92, self.y92 = 449, 486
    self.b92 = Button(self.can, text="Diagnostic + ATCD",
        font=16, width=18, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.diag9)
    self.fb92_window = self.can.create_window(self.x92,
        self.y92, window=self.b92)

    self.x93, self.y93 = 617, 486
    self.b93 = Button(self.can, text="Treatments",
        font=16, width=10, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.tttMed9)
    self.fb93_window = self.can.create_window(self.x93,
        self.y93, window=self.b93)

    self.x94, self.y94 = 745, 486
    self.b94 = Button(self.can, text="Laboratory",
        font=16, width=10, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.laboResult9)
    self.fb94_window = self.can.create_window(self.x94,
        self.y94, window=self.b94)

    self.x95, self.y95 = 873, 486
    self.b95 = Button(self.can, text="Medical Visit",
        font=16, width=10, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.visitMed9)
    self.fb95_window = self.can.create_window(self.x95,
        self.y95, window=self.b95)

    self.x96, self.y96 = 1001, 486
    self.b96 = Button(self.can, text="Intolerance",
        font=16, width=10, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.nutritionMenu9)
    self.fb96_window = self.can.create_window(self.x96,
        self.y96, window=self.b96)

    self.x97, self.y97 = 1129, 486
    self.b97 = Button(self.can, text="BMI",
        font=16, width=10, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.calculB9)
    self.fb97_window = self.can.create_window(self.x97,
        self.y97, window=self.b97)

    # Patient 10
    try:
        with open('./newpatient/entryfile10.txt', 'r') as namefile:
            line10 = namefile.readline()
    except FileNotFoundError as callfile10:
        print("File entryfile10.txt doesn't exist !", callfile10)

    try:
        self.new_data10 = line10
        self.x100, self.y100 = 149, 518
        self.new_data10 = StringVar()
        self.d100 = Entry(self.can, textvariable=self.new_data10,
            highlightbackground='grey', bd=4)
        if line10 == '----------':
            line10 = line10
        else:
            line10 = line10[:-1]
        self.new_data10.set(line10)
        self.fd100_window = self.can.create_window(self.x100,
            self.y100, window=self.d100)
    except UnboundLocalError as ub_error10:
        print("+ File 10 not created !", ub_error10)

    self.x101, self.y101 = 291, 518
    self.b101 = Button(self.can, text="Update", font=16, width=8,
        fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.updateLink10)
    self.fb101_window = self.can.create_window(self.x101,
        self.y101, window=self.b101)

    self.x102, self.y102 = 449, 518
    self.b102 = Button(self.can, text="Diagnostic + ATCD",
        font=16, width=18, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.diag10)
    self.fb102_window = self.can.create_window(self.x102,
        self.y102, window=self.b102)

    self.x103, self.y103 = 617, 518
    self.b103 = Button(self.can, text="Treatments", font=16,
        width=10, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.tttMed10)
    self.fb103_window = self.can.create_window(self.x103,
        self.y103, window=self.b103)

    self.x104, self.y104 = 745, 518
    self.b104 = Button(self.can, text="Laboratory", font=16,
        width=10, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.laboResult10)
    self.fb104_window = self.can.create_window(self.x104,
        self.y104, window=self.b104)

    self.x105, self.y105 = 873, 518
    self.b105 = Button(self.can, text="Medical Visit",
        font=16, width=10, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.visitMed10)
    self.fb105_window = self.can.create_window(self.x105,
        self.y105, window=self.b105)

    self.x106, self.y106 = 1001, 518
    self.b106 = Button(self.can, text="Intolerance", font=16,
        width=10, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.nutritionMenu10)
    self.fb106_window = self.can.create_window(self.x106,
        self.y106, window=self.b106)

    self.x107, self.y107 = 1129, 518
    self.b107 = Button(self.can, text="BMI", font=16,
        width=10, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.calculB10)
    self.fb107_window = self.can.create_window(self.x107,
        self.y107, window=self.b107)

    # Patient 11
    try:
        with open('./newpatient/entryfile11.txt', 'r') as namefile:
            line11 = namefile.readline()
    except FileNotFoundError as callfile11:
        print("File entryfile11.txt doesn't exist !", callfile11)

    try:
        self.new_data11 = line11
        self.x110, self.y110 = 149, 550
        self.new_data11 = StringVar()
        self.d110 = Entry(self.can, textvariable=self.new_data11,
            highlightbackground='grey', bd=4)
        if line11 == '-----------':
            line11 = line11
        else:
            line11 = line11[:-1]
        self.new_data11.set(line11)
        self.fd110_window = self.can.create_window(self.x110,
            self.y110, window=self.d110)
    except UnboundLocalError as ub_error11:
        print("+ File 11 not created !", ub_error11)

    self.x111, self.y111 = 291, 550
    self.b111 = Button(self.can, text="Update", font=16,
        width=8, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.updateLink11)
    self.fb111_window = self.can.create_window(self.x111,
        self.y111, window=self.b111)

    self.x112, self.y112 = 449, 550
    self.b112 = Button(self.can, text="Diagnostic + ATCD",
        font=16, width=18, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.diag11)
    self.fb112_window = self.can.create_window(self.x112,
        self.y112, window=self.b112)

    self.x113, self.y113 = 617, 550
    self.b113 = Button(self.can, text="Treatments", font=16,
        width=10, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.tttMed11)
    self.fb113_window = self.can.create_window(self.x113,
        self.y113, window=self.b113)

    self.x114, self.y114 = 745, 550
    self.b114 = Button(self.can, text="Laboratory", font=16,
        width=10, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.laboResult11)
    self.fb114_window = self.can.create_window(self.x114,
        self.y114, window=self.b114)

    self.x115, self.y115 = 873, 550
    self.b115 = Button(self.can, text="Medical Visit",
        font=16, width=10, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.visitMed11)
    self.fb115_window = self.can.create_window(self.x115,
        self.y115, window=self.b115)

    self.x116, self.y116 = 1001, 550
    self.b116 = Button(self.can, text="Intolerance",
        font=16, width=10, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.nutritionMenu11)
    self.fb116_window = self.can.create_window(self.x116,
        self.y116, window=self.b116)

    self.x117, self.y117 = 1129, 550
    self.b117 = Button(self.can, text="BMI", font=16,
        width=10, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.calculB11)
    self.fb117_window = self.can.create_window(self.x117,
        self.y117, window=self.b117)

    # Patient 12
    try:
        with open('./newpatient/entryfile12.txt', 'r') as namefile:
            line12 = namefile.readline()
    except FileNotFoundError as callfile12:
        print("File entryfile12.txt doesn't exist !", callfile12)

    try:
        self.new_data12 = line12
        self.x120, self.y120 = 149, 582
        self.new_data12 = StringVar()
        self.d120 = Entry(self.can, textvariable=self.new_data12,
            highlightbackground='grey', bd=4)
        if line12 == '------------':
            line12 = line12
        else:
            line12 = line12[:-1]
        self.new_data12.set(line12)
        self.fd120_window = self.can.create_window(self.x120,
            self.y120, window=self.d120)
    except UnboundLocalError as ub_error12:
        print("+ File 12 not created !", ub_error12)

    self.x121, self.y121 = 291, 582
    self.b121 = Button(self.can, text="Update", font=16,
        width=8, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.updateLink12)
    self.fb121_window = self.can.create_window(self.x121,
        self.y121, window=self.b121)

    self.x122, self.y122 = 449, 582
    self.b122 = Button(self.can, text="Diagnostic + ATCD",
        font=16, width=18, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.diag12)
    self.fb122_window = self.can.create_window(self.x122,
        self.y122, window=self.b122)

    self.x123, self.y123 = 617, 582
    self.b123 = Button(self.can, text="Treatments",
        font=16, width=10, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.tttMed12)
    self.fb123_window = self.can.create_window(self.x123,
        self.y123, window=self.b123)

    self.x124, self.y124 = 745, 582
    self.b124 = Button(self.can, text="Laboratory", font=16,
        width=10, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.laboResult12)
    self.fb124_window = self.can.create_window(self.x124,
        self.y124, window=self.b124)

    self.x125, self.y125 = 873, 582
    self.b125 = Button(self.can, text="Medical Visit",
        font=16, width=10, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.visitMed12)
    self.fb125_window = self.can.create_window(self.x125,
        self.y125, window=self.b125)

    self.x126, self.y126 = 1001, 582
    self.b126 = Button(self.can, text="Intolerance", font=16,
        width=10, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.nutritionMenu12)
    self.fb126_window = self.can.create_window(self.x126,
        self.y126, window=self.b126)

    self.x127, self.y127 = 1129, 582
    self.b127 = Button(self.can, text="BMI", font=16,
        width=10, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.calculB12)
    self.fb127_window = self.can.create_window(self.x127,
        self.y127, window=self.b127)

    # Patient 13
    try:
        with open('./newpatient/entryfile13.txt', 'r') as namefile:
            line13 = namefile.readline()
    except FileNotFoundError as callfile13:
        print("File entryfile13.txt doesn't exist !", callfile13)

    try:
        self.new_data13 = line13
        self.x130, self.y130 = 149, 614
        self.new_data13 = StringVar()
        self.d130 = Entry(self.can, textvariable=self.new_data13,
            highlightbackground='grey', bd=4)
        if line13 == '-------------':
            line13 = line13
        else:
            line13 = line13[:-1]
        self.new_data13.set(line13)
        self.fd130_window = self.can.create_window(self.x130,
            self.y130, window=self.d130)
    except UnboundLocalError as ub_error13:
        print("+ File 13 not created !", ub_error13)

    self.x131, self.y131 = 291, 614
    self.b131 = Button(self.can, text="Update", font=16,
        width=8, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.updateLink13)
    self.fb131_window = self.can.create_window(self.x131,
        self.y131, window=self.b131)

    self.x132, self.y132 = 449, 614
    self.b132 = Button(self.can, text="Diagnostic + ATCD",
        font=16, width=18, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.diag13)
    self.fb132_window = self.can.create_window(self.x132,
        self.y132, window=self.b132)

    self.x133, self.y133 = 617, 614
    self.b133 = Button(self.can, text="Treatments",
        font=16, width=10, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.tttMed13)
    self.fb133_window = self.can.create_window(self.x133,
        self.y133, window=self.b133)

    self.x134, self.y134 = 745, 614
    self.b134 = Button(self.can, text="Laboratory",
        font=16, width=10, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.laboResult13)
    self.fb134_window = self.can.create_window(self.x134,
        self.y134, window=self.b134)

    self.x135, self.y135 = 873, 614
    self.b135 = Button(self.can, text="Medical Visit",
        font=16, width=10, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.visitMed13)
    self.fb135_window = self.can.create_window(self.x135,
        self.y135, window=self.b135)

    self.x136, self.y136 = 1001, 614
    self.b136 = Button(self.can, text="Intolerance",
        font=16, width=10, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.nutritionMenu13)
    self.fb136_window = self.can.create_window(self.x136,
        self.y136, window=self.b136)

    self.x137, self.y137 = 1129, 614
    self.b137 = Button(self.can, text="BMI", font=16,
        width=10, fg='white', bg='SteelBlue2',
        activebackground='pale turquoise',
        command=self.calculB13)
    self.fb137_window = self.can.create_window(self.x137,
        self.y137, window=self.b137)

    # Patient 14
    try:
        with open('./newpatient/entryfile14.txt', 'r') as namefile:
            line14 = namefile.readline()
    except FileNotFoundError as callfile14:
        print("File entryfile14.txt doesn't exist !", callfile14)

    try:
        self.new_data14 = line14
        self.x140, self.y140 = 149, 646
        self.new_data14 = StringVar()
        self.d140 = Entry(self.can, textvariable=self.new_data14,
            highlightbackground='grey', bd=4)
        if line14 == '--------------':
            line14 = line14
        else:
            line14 = line14[:-1]
        self.new_data14.set(line14)
        self.fd140_window = self.can.create_window(self.x140,
            self.y140, window=self.d140)
    except UnboundLocalError as ub_error14:
        print("+ File 14 not created !", ub_error14)

    self.x141, self.y141 = 291, 646
    self.b141 = Button(self.can, text="Update", font=16,
        width=8, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.updateLink14)
    self.fb141_window = self.can.create_window(self.x141,
        self.y141, window=self.b141)

    self.x142, self.y142 = 449, 646
    self.b142 = Button(self.can, text="Diagnostic + ATCD",
        font=16, width=18, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.diag14)
    self.fb142_window = self.can.create_window(self.x142,
        self.y142, window=self.b142)

    self.x143, self.y143 = 617, 646
    self.b143 = Button(self.can, text="Treatments", font=16,
        width=10, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.tttMed14)
    self.fb143_window = self.can.create_window(self.x143,
        self.y143, window=self.b143)

    self.x144, self.y144 = 745, 646
    self.b144 = Button(self.can, text="Laboratory", font=16,
        width=10, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.laboResult14)
    self.fb144_window = self.can.create_window(self.x144,
        self.y144, window=self.b144)

    self.x145, self.y145 = 873, 646
    self.b145 = Button(self.can, text="Medical Visit",
        font=16, width=10, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.visitMed14)
    self.fb145_window = self.can.create_window(self.x145,
        self.y145, window=self.b145)

    self.x146, self.y146 = 1001, 646
    self.b146 = Button(self.can, text="Intolerance", font=16,
        width=10, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.nutritionMenu14)
    self.fb146_window = self.can.create_window(self.x146,
        self.y146, window=self.b146)

    self.x147, self.y147 = 1129, 646
    self.b147 = Button(self.can, text="BMI", font=16,
        width=10, fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise',
        command=self.calculB14)
    self.fb147_window = self.can.create_window(self.x147,
        self.y147, window=self.b147)

    # Patient 15 --> to be continue (align)
    try:
        with open('./newpatient/entryfile15.txt', 'r') as namefile:
            line15 = namefile.readline()
    except FileNotFoundError as callfile15:
        print("File entryfile15.txt doesn't exist !", callfile15)
    
    try:
        self.new_data15 = line15
        self.x150, self.y150 = 149, 678
        self.new_data15 = StringVar()
        self.d150 = Entry(self.can, textvariable=self.new_data15,
            highlightbackground='grey', bd=4)
        if line15 == '---------------':
            line15 = line15
        else:
            line15 = line15[:-1]
        self.new_data15.set(line15)
        self.fd150_window = self.can.create_window(self.x150,
            self.y150, window=self.d150)
    except UnboundLocalError as ub_error15:
        print("+ File 15 not created !", ub_error15)

    self.x151, self.y151 = 291, 678
    self.b151 = Button(self.can, width=8, font=16,
    	fg='white', bg='SteelBlue2',
        activebackground='pale turquoise', text="Update",
        command=self.updateLink15)
    self.fb151_window = self.can.create_window(self.x151,
        self.y151, window=self.b151)

    self.x152, self.y152 = 449, 678
    self.b152 = Button(self.can, width=18, font=16,
    	fg='white', bg='SteelBlue2',
        activebackground='pale turquoise', text="Diagnostic + ATCD",
        command=self.diag15)
    self.fb152_window = self.can.create_window(self.x152,
        self.y152, window=self.b152)

    self.x153, self.y153 = 617, 678
    self.b153 = Button(self.can, width=10, font=16,
    	fg='white', bg='SteelBlue2',
        activebackground='pale turquoise', text="Treatments",
        command=self.tttMed15)
    self.fb153_window = self.can.create_window(self.x153,
        self.y153, window=self.b153)

    self.x154, self.y154 = 745, 678
    self.b154 = Button(self.can, width=10, font=16,
    	fg='white', bg='SteelBlue2',
        activebackground='pale turquoise', text="Laboratory",
        command=self.laboResult15)
    self.fb154_window = self.can.create_window(self.x154,
        self.y154, window=self.b154)

    self.x155, self.y155 = 873, 678
    self.b155 = Button(self.can, width=10, font=16,
    	fg='white', bg='SteelBlue2',
        activebackground='pale turquoise', text="Medical Visit",
        command=self.visitMed15)
    self.fb155_window = self.can.create_window(self.x155,
        self.y155, window=self.b155)

    self.x156, self.y156 = 1001, 678
    self.b156 = Button(self.can, width=10, font=16,
    	fg='white', bg='SteelBlue2',
        activebackground='pale turquoise', text="Intolerance",
        command=self.nutritionMenu15)
    self.fb156_window = self.can.create_window(self.x156,
        self.y156, window=self.b156)

    self.x157, self.y157 = 1129, 678
    self.b157 = Button(self.can, width=10, font=16,
    	fg='white', bg='SteelBlue2',
        activebackground='pale turquoise', text="BMI",
        command=self.calculB15)
    self.fb157_window = self.can.create_window(self.x157,
        self.y157, window=self.b157)

    # Patient 16
    try:
        with open('./newpatient/entryfile16.txt', 'r') as namefile:
            line16 = namefile.readline()
    except FileNotFoundError as callfile16:
        print("File entryfile16.txt doesn't exist !", callfile16)

    try:
        self.new_data16 = line16
        self.x160, self.y160 = 149, 710
        self.new_data16 = StringVar()
        self.d160 = Entry(self.can, textvariable=self.new_data16,
            highlightbackground='grey', bd=4)
        if line16 == '----------------':
            line16 = line16
        else:
            line16 = line16[:-1]
        self.new_data16.set(line16)
        self.fd160_window = self.can.create_window(self.x160,
            self.y160, window=self.d160)
    except UnboundLocalError as ub_error16:
        print("+ File 16 not created !", ub_error16)

    self.x161, self.y161 = 291, 710
    self.b161 = Button(self.can, width=8, font=16,
        fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Update",
        command=self.updateLink16)
    self.fb161_window = self.can.create_window(self.x161,
        self.y161, window=self.b161)

    self.x162, self.y162 = 449, 710
    self.b162 = Button(self.can, width=18, font=16,
        fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Diagnostic + ATCD",
        command=self.diag16)
    self.fb162_window = self.can.create_window(self.x162,
        self.y162, window=self.b162)

    self.x163, self.y163 = 617, 710
    self.b163 = Button(self.can, width=10, font=16,
        fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Treatments",
        command=self.tttMed16)
    self.fb163_window = self.can.create_window(self.x163,
        self.y163, window=self.b163)

    self.x164, self.y164 = 745, 710
    self.b164 = Button(self.can, width=10, font=16,
        fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Laboratory",
        command=self.laboResult16)
    self.fb164_window = self.can.create_window(self.x164,
        self.y164, window=self.b164)

    self.x165, self.y165 = 873, 710
    self.b165 = Button(self.can, width=10, font=16,
        fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Medical Visit",
        command=self.visitMed16)
    self.fb165_window = self.can.create_window(self.x165,
        self.y165, window=self.b165)

    self.x166, self.y166 = 1001, 710
    self.b166 = Button(self.can, width=10, font=16,
        fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Intolerance",
        command=self.nutritionMenu16)
    self.fb166_window = self.can.create_window(self.x166,
        self.y166, window=self.b166)

    self.x167, self.y167 = 1129, 710
    self.b167 = Button(self.can, width=10, font=16,
        fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise', text="BMI",
        command=self.calculB16)
    self.fb167_window = self.can.create_window(self.x167,
        self.y167, window=self.b167)

    # Patient 17
    try:
        with open('./newpatient/entryfile17.txt', 'r') as namefile:
            line17 = namefile.readline()
    except FileNotFoundError as callfile17:
        print("File entryfile17.txt doesn't exist !", callfile17)

    try:
        self.new_data17 = line17
        self.x170, self.y170 = 149, 742
        self.new_data17 = StringVar()
        self.d170 = Entry(self.can, textvariable=self.new_data17,
            highlightbackground='grey', bd=4)
        if line17 == '-----------------':
            line17 = line17
        else:
            line17 = line17[:-1]
        self.new_data17.set(line17)
        self.fd170_window = self.can.create_window(self.x170,
            self.y170, window=self.d170)
    except UnboundLocalError as ub_error17:
        print("+ File 17 not created !", ub_error17)

    self.x171, self.y171 = 291, 742
    self.b171 = Button(self.can, width=8, font=16,
    	fg='white', bg='SteelBlue2',
        activebackground='pale turquoise', text="Update",
        command=self.updateLink17)
    self.fb171_window = self.can.create_window(self.x171,
        self.y171, window=self.b171)

    self.x172, self.y172 = 449, 742
    self.b172 = Button(self.can, width=18, font=16,
    	fg='white', bg='SteelBlue2',
        activebackground='pale turquoise', text="Diagnostic + ATCD",
        command=self.diag17)
    self.fb172_window = self.can.create_window(self.x172,
        self.y172, window=self.b172)

    self.x173, self.y173 = 617, 742
    self.b173 = Button(self.can, width=10, font=16,
    	fg='white', bg='SteelBlue2',
        activebackground='pale turquoise', text="Treatments",
        command=self.tttMed17)
    self.fb173_window = self.can.create_window(self.x173,
        self.y173, window=self.b173)

    self.x174, self.y174 = 745, 742
    self.b174 = Button(self.can, width=10, font=16,
    	fg='white', bg='SteelBlue2',
        activebackground='pale turquoise', text="Laboratory",
        command=self.laboResult17)
    self.fb174_window = self.can.create_window(self.x174,
        self.y174, window=self.b174)

    self.x175, self.y175 = 873, 742
    self.b175 = Button(self.can, width=10, font=16,
    	fg='white', bg='SteelBlue2',
        activebackground='pale turquoise', text="Medical Visit",
        command=self.visitMed17)
    self.fb175_window = self.can.create_window(self.x175,
        self.y175, window=self.b175)

    self.x176, self.y176 = 1001, 742
    self.b176 = Button(self.can, width=10, font=16,
    	fg='white', bg='SteelBlue2',
        activebackground='pale turquoise', text="Intolerance",
        command=self.nutritionMenu17)
    self.fb176_window = self.can.create_window(self.x176,
        self.y176, window=self.b176)

    self.x177, self.y177 = 1129, 742
    self.b177 = Button(self.can, width=10, font=16,
    	fg='white', bg='SteelBlue2',
        activebackground='pale turquoise', text="BMI",
        command=self.calculB17)
    self.fb177_window = self.can.create_window(self.x177,
        self.y177, window=self.b177)

    # Patient 18
    try:
        with open('./newpatient/entryfile18.txt', 'r') as namefile:
            line18 = namefile.readline()
    except FileNotFoundError as callfile18:
        print("File entryfile18.txt doesn't exist !", callfile18)

    try:
        self.new_data18 = line18
        self.x180, self.y180 = 149, 774
        self.new_data18 = StringVar()
        self.d180 = Entry(self.can, textvariable=self.new_data18,
            highlightbackground='grey', bd=4)
        if line18 == '------------------':
            line18 = line18
        else:
            line18 = line18[:-1]
        self.new_data18.set(line18)
        self.fd180_window = self.can.create_window(self.x180,
            self.y180, window=self.d180)
    except UnboundLocalError as ub_error18:
        print("+ File 18 not created !", ub_error18)

    self.x181, self.y181 = 291, 774
    self.b181 = Button(self.can, width=8, font=16,
        fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Update",
        command=self.updateLink18)
    self.fb181_window = self.can.create_window(self.x181,
        self.y181, window=self.b181)

    self.x182, self.y182 = 449, 774
    self.b182 = Button(self.can, width=18, font=16,
        fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Diagnostic + ATCD",
        command=self.diag18)
    self.fb182_window = self.can.create_window(self.x182,
        self.y182, window=self.b182)

    self.x183, self.y183 = 617, 774
    self.b183 = Button(self.can, width=10, font=16,
        fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Treatments",
        command=self.tttMed18)
    self.fb183_window = self.can.create_window(self.x183,
        self.y183, window=self.b183)

    self.x184, self.y184 = 745, 774
    self.b184 = Button(self.can, width=10, font=16,
        fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Laboratory",
        command=self.laboResult18)
    self.fb184_window = self.can.create_window(self.x184,
        self.y184, window=self.b184)

    self.x185, self.y185 = 873, 774
    self.b185 = Button(self.can, width=10, font=16,
        fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Medical Visit",
        command=self.visitMed18)
    self.fb185_window = self.can.create_window(self.x185,
        self.y185, window=self.b185)

    self.x186, self.y186 = 1001, 774
    self.b186 = Button(self.can, width=10, font=16,
        fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Intolerance",
        command=self.nutritionMenu18)
    self.fb186_window = self.can.create_window(self.x186,
        self.y186, window=self.b186)

    self.x187, self.y187 = 1129, 774
    self.b187 = Button(self.can, width=10, font=16,
        fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise', text="BMI",
        command=self.calculB18)
    self.fb187_window = self.can.create_window(self.x187,
        self.y187, window=self.b187)

    # Patient 19
    try:
        with open('./newpatient/entryfile19.txt', 'r') as namefile:
            line19 = namefile.readline()
    except FileNotFoundError as callfile19:
        print("File entryfile19.txt doesn't exist !", callfile19)

    try:
        self.new_data19 = line19
        self.x190, self.y190 = 149, 806
        self.new_data19 = StringVar()
        self.d190 = Entry(self.can, textvariable=self.new_data19,
            highlightbackground='grey', bd=4)
        if line19 == '-------------------':
            line19 = line19
        else:
            line19 = line19[:-1]
        self.new_data19.set(line19)
        self.fd190_window = self.can.create_window(self.x190,
            self.y190, window=self.d190)
    except UnboundLocalError as ub_error19:
        print("+ File 19 not created !", ub_error19)

    self.x191, self.y191 = 291, 806
    self.b191 = Button(self.can, width=8, font=16,
    	fg='white', bg='SteelBlue2',
        activebackground='pale turquoise', text="Update",
        command=self.updateLink19)
    self.fb191_window = self.can.create_window(self.x191,
        self.y191, window=self.b191)

    self.x192, self.y192 = 449, 806
    self.b192 = Button(self.can, width=18, font=16,
    	fg='white', bg='SteelBlue2',
        activebackground='pale turquoise', text="Diagnostic + ATCD",
        command=self.diag19)
    self.fb192_window = self.can.create_window(self.x192,
        self.y192, window=self.b192)

    self.x193, self.y193 = 617, 806
    self.b193 = Button(self.can, width=10, font=16,
    	fg='white', bg='SteelBlue2',
        activebackground='pale turquoise', text="Treatments",
        command=self.tttMed19)
    self.fb193_window = self.can.create_window(self.x193,
        self.y193, window=self.b193)

    self.x194, self.y194 = 745, 806
    self.b194 = Button(self.can, width=10, font=16,
    	fg='white', bg='SteelBlue2',
        activebackground='pale turquoise', text="Laboratory",
        command=self.laboResult19)
    self.fb194_window = self.can.create_window(self.x194,
        self.y194, window=self.b194)

    self.x195, self.y195 = 873, 806
    self.b195 = Button(self.can, width=10, font=16,
    	fg='white', bg='SteelBlue2',
        activebackground='pale turquoise', text="Medical Visit",
        command=self.visitMed19)
    self.fb195_window = self.can.create_window(self.x195,
        self.y195, window=self.b195)

    self.x196, self.y196 = 1001, 806
    self.b196 = Button(self.can, width=10, font=16,
    	fg='white', bg='SteelBlue2',
        activebackground='pale turquoise', text="Intolerance",
        command=self.nutritionMenu19)
    self.fb196_window = self.can.create_window(self.x196,
        self.y196, window=self.b196)

    self.x197, self.y197 = 1129, 806
    self.b197 = Button(self.can, width=10, font=16,
    	fg='white', bg='SteelBlue2',
        activebackground='pale turquoise', text="BMI",
        command=self.calculB19)
    self.fb197_window = self.can.create_window(self.x197,
        self.y197, window=self.b197)

    # Patient 20
    try:
        with open('./newpatient/entryfile20.txt', 'r') as namefile:
            line20 = namefile.readline()
    except FileNotFoundError as callfile20:
        print("File entryfile20.txt doesn't exist !", callfile20)

    try:
        self.new_data20 = line20
        self.x200, self.y200 = 149, 838
        self.new_data20 = StringVar()
        self.d200 = Entry(self.can, textvariable=self.new_data20,
            highlightbackground='grey', bd=4)
        if line20 == '--------------------':
            line20 = line20
        else:
            line20 = line20[:-1]
        self.new_data20.set(line20)
        self.fd200_window = self.can.create_window(self.x200,
            self.y200, window=self.d200)
    except UnboundLocalError as ub_error20:
        print("+ File 20 not created !", ub_error20)

    self.x201, self.y201 = 291, 838
    self.b201 = Button(self.can, width=8, font=16,
        fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Update",
        command=self.updateLink20)
    self.fb201_window = self.can.create_window(self.x201,
        self.y201, window=self.b201)

    self.x202, self.y202 = 449, 838
    self.b202 = Button(self.can, width=18, font=16,
        fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Diagnostic + ATCD",
        command=self.diag20)
    self.fb202_window = self.can.create_window(self.x202,
        self.y202, window=self.b202)

    self.x203, self.y203 = 617, 838
    self.b203 = Button(self.can, width=10, font=16,
        fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Treatments",
        command=self.tttMed20)
    self.fb203_window = self.can.create_window(self.x203,
        self.y203, window=self.b203)

    self.x204, self.y204 = 745, 838
    self.b204 = Button(self.can, width=10, font=16,
        fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Laboratory",
        command=self.laboResult20)
    self.fb204_window = self.can.create_window(self.x204,
        self.y204, window=self.b204)

    self.x205, self.y205 = 873, 838
    self.b205 = Button(self.can, width=10, font=16,
        fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Medical Visit",
        command=self.visitMed20)
    self.fb205_window = self.can.create_window(self.x205,
        self.y205, window=self.b205)

    self.x206, self.y206 = 1001, 838
    self.b206 = Button(self.can, width=10, font=16,
        fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Intolerance",
        command=self.nutritionMenu20)
    self.fb206_window = self.can.create_window(self.x206,
        self.y206, window=self.b206)

    self.x207, self.y207 = 1129, 838
    self.b207 = Button(self.can, width=10, font=16,
        fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise', text="BMI",
        command=self.calculB20)
    self.fb207_window = self.can.create_window(self.x207,
        self.y207, window=self.b207)

    # Patient 21
    try:
        with open('./newpatient/entryfile21.txt', 'r') as namefile:
            line21 = namefile.readline()
    except FileNotFoundError as callfile21:
        print("File entryfile21.txt doesn't exist !", callfile21)

    try:
        self.new_data21 = line21
        self.x210, self.y210 = 149, 870
        self.new_data21 = StringVar()
        self.d210 = Entry(self.can, textvariable=self.new_data21,
            highlightbackground='grey', bd=4)
        if line21 == '---------------------':
            line21 = line21
        else:
            line21 = line21[:-1]
        self.new_data21.set(line21)
        self.fd210_window = self.can.create_window(self.x210,
            self.y210, window=self.d210)
    except UnboundLocalError as ub_error21:
        print("+ File 21 not created !", ub_error21)

    self.x211, self.y211 = 291, 870
    self.b211 = Button(self.can, width=8, font=16,
    	fg='white', bg='SteelBlue2',
        activebackground='pale turquoise', text="Update",
        command=self.updateLink21)
    self.fb211_window = self.can.create_window(self.x211,
        self.y211, window=self.b211)

    self.x212, self.y212 = 449, 870
    self.b212 = Button(self.can, width=18, font=16,
    	fg='white', bg='SteelBlue2',
        activebackground='pale turquoise', text="Diagnostic + ATCD",
        command=self.diag21)
    self.fb212_window = self.can.create_window(self.x212,
        self.y212, window=self.b212)

    self.x213, self.y213 = 617, 870
    self.b213 = Button(self.can, width=10, font=16,
    	fg='white', bg='SteelBlue2',
        activebackground='pale turquoise', text="Treatments",
        command=self.tttMed21)
    self.fb213_window = self.can.create_window(self.x213,
        self.y213, window=self.b213)

    self.x214, self.y214 = 745, 870
    self.b214 = Button(self.can, width=10, font=16,
    	fg='white', bg='SteelBlue2',
        activebackground='pale turquoise', text="Laboratory",
        command=self.laboResult21)
    self.fb214_window = self.can.create_window(self.x214,
        self.y214, window=self.b214)

    self.x215, self.y215 = 873, 870
    self.b215 = Button(self.can, width=10, font=16,
    	fg='white', bg='SteelBlue2',
        activebackground='pale turquoise', text="Medical Visit",
        command=self.visitMed21)
    self.fb215_window = self.can.create_window(self.x215,
        self.y215, window=self.b215)

    self.x216, self.y216 = 1001, 870
    self.b216 = Button(self.can, width=10, font=16,
    	fg='white', bg='SteelBlue2',
        activebackground='pale turquoise', text="Intolerance",
        command=self.nutritionMenu21)
    self.fb216_window = self.can.create_window(self.x216,
        self.y216, window=self.b216)

    self.x217, self.y217 = 1129, 870
    self.b217 = Button(self.can, width=10, font=16,
    	fg='white', bg='SteelBlue2',
        activebackground='pale turquoise', text="BMI",
        command=self.calculB21)
    self.fb217_window = self.can.create_window(self.x217,
        self.y217, window=self.b217)

    # Patient 22
    try:
        with open('./newpatient/entryfile22.txt', 'r') as namefile:
            line22 = namefile.readline()
    except FileNotFoundError as callfile22:
        print("File entryfile22.txt doesn't exist !", callfile22)
    
    try:
        self.new_data22 = line22
        self.x220, self.y220 = 149, 902
        self.new_data22 = StringVar()
        self.d220 = Entry(self.can, textvariable=self.new_data22,
            highlightbackground='grey', bd=4)
        if line22 == '----------------------':
            line22 = line22
        else:
            line22 = line22[:-1]
        self.new_data22.set(line22)
        self.fd220_window = self.can.create_window(self.x220,
            self.y220, window=self.d220)
    except UnboundLocalError as ub_error22:
        print("+ File 22 not created !", ub_error22)

    self.x221, self.y221 = 291, 902
    self.b221 = Button(self.can, width=8, font=16,
        fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Update",
        command=self.updateLink22)
    self.fb221_window = self.can.create_window(self.x221,
        self.y221, window=self.b221)

    self.x222, self.y222 = 449, 902
    self.b222 = Button(self.can, width=18, font=16,
        fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Diagnostic + ATCD",
        command=self.diag22)
    self.fb222_window = self.can.create_window(self.x222,
        self.y222, window=self.b222)

    self.x223, self.y223 = 617, 902
    self.b223 = Button(self.can, width=10, font=16,
        fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Treatments",
        command=self.tttMed22)
    self.fb223_window = self.can.create_window(self.x223,
        self.y223, window=self.b223)

    self.x224, self.y224 = 745, 902
    self.b224 = Button(self.can, width=10, font=16,
        fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Laboratory",
        command=self.laboResult22)
    self.fb224_window = self.can.create_window(self.x224,
        self.y224, window=self.b224)

    self.x225, self.y225 = 873, 902
    self.b225 = Button(self.can, width=10, font=16,
        fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Medical Visit",
        command=self.visitMed22)
    self.fb225_window = self.can.create_window(self.x225,
        self.y225, window=self.b225)

    self.x226, self.y226 = 1001, 902
    self.b226 = Button(self.can, width=10, font=16,
        fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Intolerance",
        command=self.nutritionMenu22)
    self.fb226_window = self.can.create_window(self.x226,
        self.y226, window=self.b226)

    self.x227, self.y227 = 1129, 902
    self.b227 = Button(self.can, width=10, font=16,
        fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise', text="BMI",
        command=self.calculB22)
    self.fb227_window = self.can.create_window(self.x227,
        self.y227, window=self.b227)

    # Patient 23
    try:
        with open('./newpatient/entryfile23.txt', 'r') as namefile:
            line23 = namefile.readline()
    except FileNotFoundError as callfile23:
        print("File entryfile23.txt doesn't exist !", callfile23)
    
    try:
        self.new_data23 = line23
        self.x230, self.y230 = 149, 934
        self.new_data23 = StringVar()
        self.d230 = Entry(self.can, textvariable=self.new_data23,
            highlightbackground='grey', bd=4)
        if line23 == '-----------------------':
            line23 = line23
        else:
            line23 = line23[:-1]
        self.new_data23.set(line23)
        self.fd230_window = self.can.create_window(self.x230,
            self.y230, window=self.d230)
    except UnboundLocalError as ub_error23:
        print("+ File 23 not created !", ub_error23)

    self.x231, self.y231 = 291, 934
    self.b231 = Button(self.can, width=8, font=16,
    	fg='white', bg='SteelBlue2',
        activebackground='pale turquoise', text="Update",
        command=self.updateLink23)
    self.fb231_window = self.can.create_window(self.x231,
        self.y231, window=self.b231)

    self.x232, self.y232 = 449, 934
    self.b232 = Button(self.can, width=18, font=16,
    	fg='white', bg='SteelBlue2',
        activebackground='pale turquoise', text="Diagnostic + ATCD",
        command=self.diag23)
    self.fb232_window = self.can.create_window(self.x232,
        self.y232, window=self.b232)

    self.x233, self.y233 = 617, 934
    self.b233 = Button(self.can, width=10, font=16,
    	fg='white', bg='SteelBlue2',
        activebackground='pale turquoise', text="Treatments",
        command=self.tttMed23)
    self.fb233_window = self.can.create_window(self.x233,
        self.y233, window=self.b233)

    self.x234, self.y234 = 745, 934
    self.b234 = Button(self.can, width=10, font=16,
    	fg='white', bg='SteelBlue2',
        activebackground='pale turquoise', text="Laboratory",
        command=self.laboResult23)
    self.fb234_window = self.can.create_window(self.x234,
        self.y234, window=self.b234)

    self.x235, self.y235 = 873, 934
    self.b235 = Button(self.can, width=10, font=16,
    	fg='white', bg='SteelBlue2',
        activebackground='pale turquoise', text="Medical Visit",
        command=self.visitMed23)
    self.fb235_window = self.can.create_window(self.x235,
        self.y235, window=self.b235)

    self.x236, self.y236 = 1001, 934
    self.b236 = Button(self.can, width=10, font=16,
    	fg='white', bg='SteelBlue2',
        activebackground='pale turquoise', text="Intolerance",
        command=self.nutritionMenu23)
    self.fb236_window = self.can.create_window(self.x236,
        self.y236, window=self.b236)

    self.x237, self.y237 = 1129, 934
    self.b237 = Button(self.can, width=10, font=16,
    	fg='white', bg='SteelBlue2',
        activebackground='pale turquoise', text="BMI",
        command=self.calculB23)
    self.fb237_window = self.can.create_window(self.x237,
        self.y237, window=self.b237)

    # Patient 24
    try:
        with open('./newpatient/entryfile24.txt', 'r') as namefile:
            line24 = namefile.readline()
    except FileNotFoundError as callfile24:
        print("File entryfile24.txt doesn't exist !", callfile24)

    try:
        self.new_data24 = line24
        self.x240, self.y240 = 149, 966
        self.new_data24 = StringVar()
        self.d240 = Entry(self.can, textvariable=self.new_data24,
          highlightbackground='grey', bd=4)
        if line24 == '------------------------':
            line24 = line24
        else:
            line24 = line24[:-1]
        self.new_data24.set(line24)
        self.fd240_window = self.can.create_window(self.x240,
            self.y240, window=self.d240)
    except UnboundLocalError as ub_error24:
        print("+ File 24 not created !", ub_error24)

    self.x241, self.y241 = 291, 966
    self.b241 = Button(self.can, width=8, font=16,
        fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Update",
        command=self.updateLink24)
    self.fb241_window = self.can.create_window(self.x241,
        self.y241, window=self.b241)

    self.x242, self.y242 = 449, 966
    self.b242 = Button(self.can, width=18, font=16,
        fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Diagnostic + ATCD",
        command=self.diag24)
    self.fb242_window = self.can.create_window(self.x242,
        self.y242, window=self.b242)

    self.x243, self.y243 = 617, 966
    self.b243 = Button(self.can, width=10, font=16,
        fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Treatments",
        command=self.tttMed24)
    self.fb243_window = self.can.create_window(self.x243,
        self.y243, window=self.b243)

    self.x244, self.y244 = 745, 966
    self.b244 = Button(self.can, width=10, font=16,
        fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Laboratory",
        command=self.laboResult24)
    self.fb244_window = self.can.create_window(self.x244,
        self.y244, window=self.b244)

    self.x245, self.y245 = 873, 966
    self.b245 = Button(self.can, width=10, font=16,
        fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Medical Visit",
        command=self.visitMed24)
    self.fb245_window = self.can.create_window(self.x245,
        self.y245, window=self.b245)

    self.x246, self.y246 = 1001, 966
    self.b246 = Button(self.can, width=10, font=16,
        fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise', text="Intolerance",
        command=self.nutritionMenu24)
    self.fb246_window = self.can.create_window(self.x246,
        self.y246, window=self.b246)

    self.x247, self.y247 = 1129, 966
    self.b247 = Button(self.can, width=10, font=16,
        fg='yellow', bg='RoyalBlue3',
        activebackground='pale turquoise', text="BMI",
        command=self.calculB24)
    self.fb247_window = self.can.create_window(self.x247,
        self.y247, window=self.b247)

    self.can.configure(scrollregion=self.can.bbox(ALL))
