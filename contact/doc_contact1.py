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
            if os.path.getsize('./contact/contactdoc1.txt'):
                print("+ Ok, contactdoc1.txt exist (t1)")
        except FileNotFoundError as errfnf:
            print("+ No file contactdoc1.txt exist", errfnf)
            with open('./contact/contactdoc1.txt', 'w') as testf:
                print("+ File contactdoc1.txt created !")

        self.x1, self.y1 = 900, 350
        self.txtBox = Text(self.can, height=15, width=40, font=18, relief=SUNKEN)
        self.txtBox.delete('1.0', END)
        self.txtBox.update()
        self.ftxtBox_window = self.can.create_window(self.x1, self.y1, window=self.txtBox)

        try:
            if os.path.exists('./contact/contactdoc1.txt'):
                with open('./contact/contactdoc1.txt', 'r') as policyfile:
                    line1 = policyfile.readline()
                    phone = policyfile.readline()
                    iphone2 = policyfile.readline()
                    street = policyfile.readline()
                    state = policyfile.readline()
                    email = policyfile.readline()
                    fax = policyfile.readline()
                self.txtBox.insert(INSERT, "--- Data Doctor ---\n")
                self.txtBox.insert(END, "\nDoctor : " + line1)
                self.txtBox.insert(END, "\nPhone : " + phone)
                self.txtBox.insert(END, "\nMobile : " + iphone2)
                self.txtBox.insert(END, "\nStreet : " + street)
                self.txtBox.insert(END, "\nCity : " + state)
                self.txtBox.insert(END, "\ne-mail : " + email)
                self.txtBox.insert(END, "\nFax : " + fax)
            else:
                pass
        except FileNotFoundError as err_r:
            print("+ No file contactdoc1.txt exist", err_r)

    def recorderData(namentry, txtphone, phonentry, txtmobile,
        mobilentry, addrtxt, addrentry, citytxt, cityentry,
        mailtxt, entrymail, faxtxt, entryfax):
        """
            Display origin
        """
        self.x1, self.y1 = 900, 350
        self.txtBox = Text(self.can, height=15, width=40, font=18, relief=SUNKEN)
        self.txtBox.delete('1.0', END)
        self.ftxtBox_window = self.can.create_window(self.x1, self.y1, window=self.txtBox)

        try:
            if os.path.getsize('./contact/contactdoc1.txt'):
                print("+ Ok, contactdoc1.txt exist (t2)")
        except FileNotFoundError as errfnf:
            print("+ No file contactdoc1.txt exist", errfnf)
            with open('./contact/contactdoc1.txt', 'w') as testf:
                print("+ File contactdoc1.txt created !")

        try:
            with open('./contact/contactdoc1.txt', 'w') as iofile:
                iofile.write(namentry.get())
                iofile.write("\n" + phonentry.get())
                iofile.write("\n" + mobilentry.get())
                iofile.write("\n" + addrentry.get())
                iofile.write("\n" + cityentry.get())
                iofile.write("\n" + entrymail.get())
                iofile.write("\n" + entryfax.get())
        except FileNotFoundError as fn:
            print("+ File not found !", fn)

        try:
            if os.path.getsize('./contact/finaldoc1.txt'):
                os.remove('./contact/finaldoc1.txt')
        except FileNotFoundError as err_termin:
            print("+ finaldoc1 not found !(t2)", err_termin)
            with open('./contact/finaldoc1.txt', 'a+'):
                print("+ finaldoc1.txt exist!")
        try:
            with open('./contact/finaldoc1.txt', 'w') as terminfile:
                terminfile.write("Doctor : " + namentry.get())
                terminfile.write("\nPhone : " + phonentry.get())
                terminfile.write("\nMobile : " + mobilentry.get())
                terminfile.write("\nStreet : " + addrentry.get())
                terminfile.write("\nCity : " + cityentry.get())
                terminfile.write("\ne-mail : " + entrymail.get())
                terminfile.write("\nFax : " + entryfax.get())
        except FileNotFoundError as err2_final:
            print("+ finaldoc1.txt not created (t2)", err2_final)

        allInData()

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
    self.labelname = Label(self.can, text="Doctor :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.labelname_window = self.can.create_window(self.x1, self.y1,
        window = self.labelname)

    try:
        with open('./contact/contactdoc1.txt', 'r') as namefile:
            linex = namefile.readline()
            line2 = namefile.readline()
            line3 = namefile.readline()
            line4 = namefile.readline()
            line5 = namefile.readline()
            line6 = namefile.readline()
            line7 = namefile.readline()
            line8 = namefile.readline()
            line9 = namefile.readline()
    except FileNotFoundError as callfile:
        print("+ File contactdoc1.txt doesn't exist !", callfile)

    try:
        self.txt_pat = linex
        self.x2, self.y2 = 450, 200
        self.txt_pat = StringVar()
        self.namentry = Entry(self.can, textvariable=self.txt_pat,
            highlightbackground='grey', bd=4)
        self.txt_pat.set(linex[:-1])
        self.namentry_window = self.can.create_window(self.x2, self.y2,
            window = self.namentry)
    except UnboundLocalError as ub_error1:
        print("+ File 1 not created !", ub_error1)

    # Phone
    self.x20, self.y20 = 250, 250
    self.phonelabel = Label(self.can, text="Phone :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.phonelabel_window = self.can.create_window(self.x20, self.y20,
        window = self.phonelabel)

    self.txtphone = line2
    self.x21, self.y21 = 450, 250
    self.txtphone = StringVar()
    self.phonentry = Entry(self.can, textvariable=self.txtphone,
        highlightbackground='grey', bd=3)
    self.txtphone.set(line2[:-1])
    self.phonentry_window = self.can.create_window(self.x21, self.y21,
        window = self.phonentry)

    # Mobile
    self.x20, self.y20 = 250, 300
    self.lblmobile = Label(self.can, text="Mobile :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.lblmobile_window = self.can.create_window(self.x20, self.y20,
        window = self.lblmobile)

    self.txtmobile = line3
    self.x21, self.y21 = 450, 300
    self.txtmobile = StringVar()
    self.mobilentry = Entry(self.can, textvariable=self.txtmobile,
        highlightbackground='grey', bd=3)
    self.txtmobile.set(line3[:-1])
    self.mobilentry_window = self.can.create_window(self.x21, self.y21,
        window = self.mobilentry)

    # Street
    self.x30, self.y30 = 250, 350
    self.addrlabel = Label(self.can, text="Street :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.addrlabel_window = self.can.create_window(self.x30, self.y30,
        window = self.addrlabel)

    self.addrtxt = line4
    self.x31, self.y31 = 450, 350
    self.addrtxt = StringVar()
    self.addrentry = Entry(self.can, textvariable=self.addrtxt,
        highlightbackground='grey', bd=4)
    self.addrtxt.set(line4[:-1])
    self.addrentry_window = self.can.create_window(self.x31, self.y31,
        window = self.addrentry)

    self.citytxt = line5
    self.x32, self.y32 = 450, 400
    self.citytxt = StringVar()
    self.cityentry = Entry(self.can, textvariable=self.citytxt,
        highlightbackground='grey', bd=4)
    self.citytxt.set(line5[:-1])
    self.cityentry_window = self.can.create_window(self.x32, self.y32,
        window = self.cityentry)

    # e-mail
    self.x40, self.y40 = 250, 450
    self.mailabel = Label(self.can, text="e-mail :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.mailabel_window = self.can.create_window(self.x40, self.y40,
        window = self.mailabel)

    self.mailtxt = line6
    self.x41, self.y41 = 450, 450
    self.mailtxt = StringVar()
    self.entrymail = Entry(self.can, textvariable=self.mailtxt,
        highlightbackground='grey', bd=3)
    self.mailtxt.set(line6[:-1])
    self.entrymail_window = self.can.create_window(self.x41, self.y41,
        window = self.entrymail)

    # Fax
    self.x50, self.y50 = 250, 500
    self.lblfax = Label(self.can, text="Fax :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.lblfax_window = self.can.create_window(self.x50, self.y50,
        window = self.lblfax)

    self.faxtxt = line7
    self.x51, self.y51 = 450, 500
    self.faxtxt = StringVar()
    self.entryfax = Entry(self.can, textvariable=self.faxtxt,
        highlightbackground='grey', bd=3)
    self.faxtxt.set(line7[:-1])
    self.entryfax_window = self.can.create_window(self.x51, self.y51,
        window = self.entryfax)

    self.x52, self.y52 = 350, 620
    self.b52 = Button(self.can, text="Save", font=16,
        width=30, bd=3, bg='RoyalBlue3', fg='yellow',
        highlightbackground='cyan',
        activebackground='pale turquoise',
        command = lambda: recorderData(self.namentry, self.txtphone,
            self.phonentry, self.txtmobile, self.mobilentry,
            self.addrtxt, self.addrentry, self.citytxt, self.cityentry,
            self.mailtxt, self.entrymail, self.faxtxt, self.entryfax))
    self.fb52_window = self.can.create_window(self.x52, self.y52, window=self.b52)

    self.can.configure(scrollregion=self.can.bbox(ALL))
