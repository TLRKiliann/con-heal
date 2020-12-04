#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
import os


def doctorWind(self):
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
            print("+ No file entryfile.txt exist", fileout)

        try:
            if os.path.getsize('./contact/contact1.txt'):
                print("+ Ok, contact1.txt exist")
        except FileNotFoundError as errfnf:
            print("+ No file contact1.txt exist", errfnf)
            with open('./contact/contact1.txt', 'a+') as testf:
                print("+ File contact1.txt created !")

        try:
            if os.path.exists('./contact/contact1.txt'):
                with open('./contact/contact1.txt', 'r') as policyfile:
                    line1 = policyfile.readline()
                    line2 = policyfile.readline()
                    native = policyfile.readline()
                    phone = policyfile.readline()
                    street = policyfile.readline()
                    state = policyfile.readline()
                    email = policyfile.readline()
                    assu = policyfile.readline()
                    polins = policyfile.readline()
            else:
                pass
        except FileNotFoundError as err_r:
            print("+ No file contact1.txt exist", err_r)

        self.x1, self.y1 = 900, 350
        self.txtBox = Text(self.can, height=25, width=40, font=18, relief=SUNKEN)
        self.txtBox.delete('1.0', END)
        self.txtBox.update()
        self.txtBox.insert(INSERT, line1 + "\n\n")
        self.txtBox.insert('3.0', line2 + "\n\n")
        self.txtBox.insert('5.0', native + "\n\n")
        self.txtBox.insert('7.0', phone + "\n\n")
        self.txtBox.insert('9.0', street + "\n\n")
        self.txtBox.insert('10.0', state + "\n\n")
        self.txtBox.insert('12.0', email + "\n\n")
        self.txtBox.insert('14.0', assu + "\n\n")
        self.txtBox.insert('16.0', polins + "\n\n")
        self.ftxtBox_window = self.can.create_window(self.x1, self.y1, window=self.txtBox)

    def recorderData(namentry, birthentry, native, nativaentry, txtphone, phonentry,
        addrtxt, addrentry, citytxt, cityentry, mailtxt, entrymail,
        assurance, entryassu, policy, entrypolicy):
        """
            Display origin
        """
        try:
            if os.path.getsize('./contact/contact1.txt'):
                print("+ Ok, contact1.txt exist")
        except FileNotFoundError as errfnf:
            print("+ No file contact1.txt exist", errfnf)
            with open('./contact/contact1.txt', 'a+') as testf:
                print("+ File contact1.txt created !")

        self.x1, self.y1 = 900, 350
        self.txtBox = Text(self.can, height=25, width=40, font=18, relief=SUNKEN)
        self.txtBox.delete('1.0', END)
        self.txtBox.update()
        self.ftxtBox_window = self.can.create_window(self.x1, self.y1, window=self.txtBox)

        try:
            with open('./contact/contact1.txt', 'w') as iofile:
                iofile.write("Name : " + namentry.get())
                self.txtBox.insert(INSERT, "Patient Name : " + namentry.get() + "\n\n")
                iofile.write("Birthdate : " + line2)
                self.txtBox.insert('3.0', "Birthdate : " + line2 + "\n\n")
                iofile.write("Native : " + nativaentry.get() + "\n")
                self.txtBox.insert('5.0', "Native : " + nativaentry.get() + "\n\n")
                iofile.write("Phone : " + phonentry.get() + "\n")
                self.txtBox.insert('7.0', "Phone : " + phonentry.get() + "\n\n")
                iofile.write("Street : " + addrentry.get() + "\n")
                self.txtBox.insert('9.0', "Street : " + addrentry.get() + "\n\n")
                iofile.write("City : " + cityentry.get() + "\n")
                self.txtBox.insert('10.0', "City : " + cityentry.get() + "\n\n")
                iofile.write("e-mail : " + entrymail.get() + "\n")
                self.txtBox.insert('12.0', "e-mail : " + entrymail.get() + "\n\n")
                iofile.write("Insurance : " + entryassu.get() + "\n")
                self.txtBox.insert('14.0', "Insurance : " + entryassu.get() + "\n\n")
                iofile.write("Policy : " + entrypolicy.get() + "\n")
                self.txtBox.insert('16.0', "Policy : " + entrypolicy.get() + "\n\n")
        except FileNotFoundError as err_w:
            print("+ No file contact1.txt exist", err_w)

    allInData()

    # Label title
    self.x11, self.y11 = 250, 100
    self.lbltitle = Label(self.can, text="Contact",
        font=('helvetica', 40, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.lbltitle_window = self.can.create_window(self.x11, self.y11,
        window = self.lbltitle)

    # Name
    self.x1, self.y1 = 250, 200
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
        print("+ File entryfile.txt doesn't exist !", callfile)

    try:
        self.txt_pat = line1
        self.x2, self.y2 = 450, 200
        self.txt_pat = StringVar()
        self.namentry = Entry(self.can, textvariable=self.txt_pat,
            highlightbackground='grey', bd=4)
        self.txt_pat.set(line1)
        self.namentry_window = self.can.create_window(self.x2, self.y2,
            window = self.namentry)
    except UnboundLocalError as ub_error1:
        print("+ + File 1 not created !", ub_error1)

    try:
        with open('./newpatient/entryfile.txt', 'r') as namefile:
            line1 = namefile.readline()
            line2 = namefile.readline()
            birth_pat = line2
    except FileNotFoundError as callfile:
        print("+ File entryfile.txt doesn't exist !", callfile)

    try:
        self.txt_pat = line1
        self.x2, self.y2 = 450, 200
        self.birth_pat = StringVar()
        self.birthentry = Entry(self.can, textvariable=self.birth_pat,
            highlightbackground='grey', bd=4)
        self.birth_pat.set(line1)
        self.birthentry_window = self.can.create_window(self.x2, self.y2,
            window = self.birthentry)
    except UnboundLocalError as ub_error1:
        print("+ + File 1 not created !", ub_error1)

    # Native
    self.x15, self.y15 = 250, 250
    self.nativelab = Label(self.can, text="Native :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.nativelab_window = self.can.create_window(self.x15, self.y15,
        window = self.nativelab)

    self.x16, self.y16 = 450, 250
    self.native = StringVar()
    self.nativaentry = Entry(self.can, textvariable=self.native,
        highlightbackground='grey', bd=3)
    self.nativaentry_window = self.can.create_window(self.x16, self.y16,
        window = self.nativaentry)

    # Phone
    self.x20, self.y20 = 250, 300
    self.phonelabel = Label(self.can, text="Phone Number :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.phonelabel_window = self.can.create_window(self.x20, self.y20,
        window = self.phonelabel)

    self.x21, self.y21 = 450, 300
    self.txtphone = StringVar()
    self.phonentry = Entry(self.can, textvariable=self.txtphone,
        highlightbackground='grey', bd=3)
    self.phonentry_window = self.can.create_window(self.x21, self.y21,
        window = self.phonentry)

    # Street
    self.x30, self.y30 = 250, 350
    self.addrlabel = Label(self.can, text="Street :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.addrlabel_window = self.can.create_window(self.x30, self.y30,
        window = self.addrlabel)

    self.x31, self.y31 = 450, 350
    self.addrtxt = StringVar()
    self.addrentry = Entry(self.can, textvariable=self.addrtxt,
        highlightbackground='grey', bd=4)
    self.addrtxt.set("Street")
    self.addrentry_window = self.can.create_window(self.x31, self.y31,
        window = self.addrentry)

    self.x32, self.y32 = 450, 400
    self.citytxt = StringVar()
    self.cityentry = Entry(self.can, textvariable=self.citytxt,
        highlightbackground='grey', bd=4)
    self.citytxt.set("City")
    self.cityentry_window = self.can.create_window(self.x32, self.y32,
        window = self.cityentry)

    # e-mail
    self.x40, self.y40 = 250, 450
    self.mailabel = Label(self.can, text="e-mail :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.mailabel_window = self.can.create_window(self.x40, self.y40,
        window = self.mailabel)

    self.x41, self.y41 = 450, 450
    self.mailtxt = StringVar()
    self.entrymail = Entry(self.can, textvariable=self.mailtxt,
        highlightbackground='grey', bd=3)
    self.mailtxt.set("")
    self.entrymail_window = self.can.create_window(self.x41, self.y41,
        window = self.entrymail)

    # Assurance
    self.x50, self.y50 = 250, 500
    self.mailabel = Label(self.can, text="Insurance :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.mailabel_window = self.can.create_window(self.x50, self.y50,
        window = self.mailabel)

    self.x51, self.y51 = 450, 500
    self.assurance = StringVar()
    self.entryassu = Entry(self.can, textvariable=self.assurance,
        highlightbackground='grey', bd=3)
    self.entryassu_window = self.can.create_window(self.x51, self.y51,
        window = self.entryassu)

    # Police
    self.x50, self.y50 = 250, 550
    self.mailabel = Label(self.can, text="Policy Number :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.mailabel_window = self.can.create_window(self.x50, self.y50,
        window = self.mailabel)

    self.x51, self.y51 = 450, 550
    self.policy = StringVar()
    self.entrypolicy = Entry(self.can, textvariable=self.policy,
        highlightbackground='grey', bd=3)
    self.entrypolicy_window = self.can.create_window(self.x51, self.y51,
        window = self.entrypolicy)

    self.x52, self.y52 = 350, 620
    self.b52 = Button(self.can, text="Save", font=16,
        width=30, bd=3, bg='RoyalBlue3', fg='yellow',
        highlightbackground='RoyalBlue3',
        activebackground='pale turquoise',
        command = lambda: recorderData(self.namentry, self.birthentry, 
            self.native, self.nativaentry, self.txtphone, self.phonentry,
            self.addrtxt, self.addrentry, self.citytxt, self.cityentry,
            self.mailtxt, self.entrymail, self.assurance, self.entryassu,
            self.policy, self.entrypolicy))
    self.fb52_window = self.can.create_window(self.x52, self.y52, window=self.b52)

    self.can.configure(scrollregion=self.can.bbox(ALL))
