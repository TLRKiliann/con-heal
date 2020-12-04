#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *


def Window(self):
    """
        Main function to define 
        design for contact interface.
    """
    self.can.delete(ALL)
    self.can.configure(background='DodgerBlue2')

    def allInData():
        """
            First page
        """
        try:
            with open('./newpatient/entryfile.txt', 'r') as namefile:
                line1 = namefile.readline()
                line2 = namefile.readline()
        except FileNotFoundError as fileout:
            print("No file entryfile.txt exist", fileout)

        try:
            with open('./contact/contact1.txt', 'r') as policyfile:
                native = policyfile.readline()
                phone = policyfile.readline()
                street = policyfile.readline()
                state = policyfile.readline()
                email = policyfile.readline()
                assu = policyfile.readline()
                polins = policyfile.readline()
        except FileNotFoundError as err_r:
            print("No file contact1.txt exist", err_r)

        self.x1, self.y1 = 950, 350
        self.txtBox = Text(self.can, height=25, width=40, font=18, relief=SUNKEN)
        self.txtBox.delete('1.0', END)
        self.txtBox.update()
        self.txtBox.insert(INSERT, "Patient Name : " + line1 + "\n\n")
        self.txtBox.insert(INSERT, "Birthdate : " + line2 + "\n\n")
        self.txtBox.insert(INSERT, "Native : " + native + "\n\n")
        self.txtBox.insert(INSERT, "Phone : " + phone + "\n\n")
        self.txtBox.insert(INSERT, "Street : " + street + "\n\n")
        self.txtBox.insert(INSERT, "City : " + state + "\n\n")
        self.txtBox.insert(INSERT, "e-mail : " + email + "\n\n")
        self.txtBox.insert(INSERT, "Insurance : " + assu + "\n\n")
        self.txtBox.insert(INSERT, "Policy : " + polins + "\n\n")
        self.ftxtBox_window = self.can.create_window(self.x1, self.y1, window=self.txtBox)

    def recorderData(native, nativaentry, txtphone, phonentry,
        addrtxt, entryaddr, citytxt, entrycity, mailtxt, entrymail,
        assurance, entryassu, policy, entrypolicy):
        """
            Display origin
        """
        try:
            with open('./newpatient/entryfile.txt', 'r') as namefile:
                line1 = namefile.readline()
                line2 = namefile.readline()
        except FileNotFoundError as fileout:
            print("No file entryfile.txt exist", fileout)

        self.x1, self.y1 = 950, 350
        self.txtBox = Text(self.can, height=25, width=40, font=18, relief=SUNKEN)
        self.txtBox.delete('1.0', END)
        #self.txtBox.insert(INSERT, "Patient Name : " + line1 + "\n\n")
        #self.txtBox.insert(INSERT, "Birthdate : " + line2 + "\n\n")
        self.txtBox.update()
        self.ftxtBox_window = self.can.create_window(self.x1, self.y1, window=self.txtBox)

        try:
            with open('./contact/contact1.txt', 'w') as iofile:
                iofile.write("Name : " + line1 + '\n')
                iofile.write("Birthdate : " + line2 + "\n")
                self.txtBox.insert('1.0', "Patient Name : " + line1 + "\n\n")
                self.txtBox.insert('2.0', "Birthdate : " + line2 + "\n\n")
                iofile.write("Native : " + nativentry.get() + '\n')
                self.txtBox.insert('4.0', "Native : " + nativentry.get() + "\n\n")
                iofile.write("Phone : " + phonentry.get() + '\n')
                self.txtBox.insert('6.0', "Phone : " + phonentry.get() + "\n\n")
                iofile.write("Address : " + entryaddr.get() + '\n')
                self.txtBox.insert('8.0', "Address : " + entryaddr.get() + "\n\n")
                iofile.write("City : " + entrycity.get() + '\n')
                self.txtBox.insert('9.0', "City : " + entrycity.get() + "\n\n")
                iofile.write("e-mail : " + entrymail.get() + '\n')
                self.txtBox.insert('11', "e-mail : " + entrymail.get() + "\n\n")
                iofile.write("Insurance : " + entryassu.get() + '\n')
                self.txtBox.insert('13', "Insurance : " + entryassu.get() + "\n\n")
                iofile.write("Policy : " + entrypolicy.get() + '\n')
                self.txtBox.insert('15', "Policy : " + entrypolicy.get() + "\n\n")
        except FileNotFoundError as err_w:
            print("No file contact1.txt exist", err_w)

    allInData()
    
    # Label title
    self.x11, self.y11 = 200, 100
    self.lbltitle = Label(self.can, text="Contact",
        font=('helvetica', 40, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.lbltitle_window = self.can.create_window(self.x11, self.y11,
        window = self.lbltitle)

    # Name
    self.x1, self.y1 = 200, 200
    self.labelname = Label(self.can, text="Patient Name :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.labelname_window = self.can.create_window(self.x1, self.y1,
        window = self.labelname)

    try:
        with open('./newpatient/entryfile.txt', 'r') as namefile:
            line1 = namefile.readline()
            txt_pat = line1
    except FileNotFoundError as callfile:
        print("File entryfile.txt doesn't exist !", callfile)

    try:
        self.txt_pat = line1
        self.x2, self.y2 = 400, 200
        self.txt_pat = StringVar()
        self.namentry = Entry(self.can, textvariable=self.txt_pat,
            highlightbackground='grey', bd=4)
        self.txt_pat.set(line1)
        self.namentry_window = self.can.create_window(self.x2, self.y2,
            window = self.namentry)
    except UnboundLocalError as ub_error1:
        print("+ File 1 not created !", ub_error1)

    # Native
    self.x15, self.y15 = 200, 250
    self.nativelab = Label(self.can, text="Native :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.nativelab_window = self.can.create_window(self.x15, self.y15,
        window = self.nativelab)

    self.x16, self.y16 = 400, 250
    self.native = StringVar()
    self.nativaentry = Entry(self.can, textvariable=self.native,
        highlightbackground='grey', bd=3)
    self.nativaentry_window = self.can.create_window(self.x16, self.y16,
        window = self.nativaentry)

    # Phone
    self.x20, self.y20 = 200, 300
    self.phonelabel = Label(self.can, text="Phone Number :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.phonelabel_window = self.can.create_window(self.x20, self.y20,
        window = self.phonelabel)

    self.x21, self.y21 = 400, 300
    self.txtphone = StringVar()
    self.phonentry = Entry(self.can, textvariable=self.txtphone,
        highlightbackground='grey', bd=3)
    self.phonentry_window = self.can.create_window(self.x21, self.y21,
        window = self.phonentry)

    # Address
    self.x30, self.y30 = 200, 350
    self.addrlabel = Label(self.can, text="Address :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.addrlabel_window = self.can.create_window(self.x30, self.y30,
        window = self.addrlabel)

    self.x31, self.y31 = 400, 350
    self.addrtxt = StringVar()
    self.addrentry = Entry(self.can, textvariable=self.addrtxt,
        highlightbackground='grey', bd=4)
    self.addrtxt.set("Street")
    self.addrentry_window = self.can.create_window(self.x31, self.y31,
        window = self.addrentry)

    self.x32, self.y32 = 400, 400
    self.citytxt = StringVar()
    self.cityentry = Entry(self.can, textvariable=self.citytxt,
        highlightbackground='grey', bd=4)
    self.citytxt.set("City")
    self.cityentry_window = self.can.create_window(self.x32, self.y32,
        window = self.cityentry)

    # e-mail
    self.x40, self.y40 = 200, 450
    self.mailabel = Label(self.can, text="e-mail :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.mailabel_window = self.can.create_window(self.x40, self.y40,
        window = self.mailabel)

    self.x41, self.y41 = 400, 450
    self.mailtxt = StringVar()
    self.entrymail = Entry(self.can, textvariable=self.mailtxt,
        highlightbackground='grey', bd=3)
    self.mailtxt.set("")
    self.entrymail_window = self.can.create_window(self.x41, self.y41,
        window = self.entrymail)

    # Assurance
    self.x50, self.y50 = 200, 500
    self.mailabel = Label(self.can, text="Insurance :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.mailabel_window = self.can.create_window(self.x50, self.y50,
        window = self.mailabel)

    self.x51, self.y51 = 400, 500
    self.assurance = StringVar()
    self.entryassu = Entry(self.can, textvariable=self.assurance,
        highlightbackground='grey', bd=3)
    self.entryassu_window = self.can.create_window(self.x51, self.y51,
        window = self.entryassu)

    # Police
    self.x50, self.y50 = 200, 550
    self.mailabel = Label(self.can, text="Policy Number :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.mailabel_window = self.can.create_window(self.x50, self.y50,
        window = self.mailabel)

    self.x51, self.y51 = 400, 550
    self.policy = StringVar()
    self.entrypolicy = Entry(self.can, textvariable=self.policy,
        highlightbackground='grey', bd=3)
    self.entrypolicy_window = self.can.create_window(self.x51, self.y51,
        window = self.entrypolicy)

    self.x52, self.y52 = 575, 550
    self.b52 = Button(self.can, text="Save", font=16,
        width=8, bd=3, bg='RoyalBlue3', fg='yellow',
        highlightbackground='RoyalBlue3',
        activebackground='pale turquoise',
        command = lambda: recorderData(self.native, self.nativaentry, self.txtphone, self.phonentry,
        self.addrtxt, self.entryaddr, self.citytxt, self.entrycity, self.mailtxt, self.entrymail,
        self.assurance, self.entryassu, self.policy, self.entrypolicy))
    self.fb52_window = self.can.create_window(self.x52, self.y52, window=self.b52)

    self.can.configure(scrollregion=self.can.bbox(ALL))
