#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *


def launchData(self):
    """
        Next page after enter patient 1
    """
    self.can.delete(ALL)
    self.can.configure(background='DodgerBlue2')
    
    txt_pat = StringVar()
    
    try:
        with open('./newpatient/entryfile.txt', 'r') as namefile:
            line1 = namefile.readline()
            txt_pat = line1
    except FileNotFoundError as fileout:
        print("No file entryfile.txt exist", fileout)

    self.x1, self.y1 = 625, 350
    self.t1 = Text(self.can, height=30, width=80, font=18, relief=SUNKEN)
    self.t1.insert(INSERT, "Patient Name : " + line1 + "\n\n")
    self.t1.insert(INSERT, "Phone : \n\n\n")
    self.t1.insert(INSERT, "Address : \n\n\n")
    self.t1.insert(INSERT, "e-mail : \n\n\n")
    self.t1.insert(INSERT, "Assurance : \n\n\n")
    self.t1.insert(INSERT, "Miscellanous : \n\n\n")
    self.ft1=self.can.create_window(self.x1, self.y1, window=self.t1)

    self.can.configure(scrollregion=self.can.bbox(ALL))
