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
                print("+ File contactdoc1.txt created !", testf)

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

        try:
            if os.path.getsize('./contact/contactdoc2.txt'):
                print("+ Ok, contactdoc2.txt exist (t1)")
        except FileNotFoundError as nfd2:
            print("+ No file contactdoc2.txt exist", nfd2)
            with open('./contact/contactdoc2.txt', 'w') as testfd2:
                print("+ File contactdoc2.txt created !", testfd2)

        self.x2, self.y2 = 900, 820
        self.txtBox2 = Text(self.can, height=15, width=40, font=18, relief=SUNKEN)
        self.txtBox2.delete('1.0', END)
        self.txtBox2.update()
        self.ftxtBox2_window = self.can.create_window(self.x2, self.y2, window=self.txtBox2)

        try:
            if os.path.exists('./contact/contactdoc2.txt'):
                with open('./contact/contactdoc2.txt', 'r') as policydoc:
                    docline1 = policydoc.readline()
                    docphone = policydoc.readline()
                    dociphone2 = policydoc.readline()
                    docstreet = policydoc.readline()
                    docstate = policydoc.readline()
                    docemail = policydoc.readline()
                    docfax = policydoc.readline()
                self.txtBox2.insert(INSERT, "--- Data Doctor 2 ---\n")
                self.txtBox2.insert(END, "\nDoctor : " + docline1)
                self.txtBox2.insert(END, "\nPhone : " + docphone)
                self.txtBox2.insert(END, "\nMobile : " + dociphone2)
                self.txtBox2.insert(END, "\nStreet : " + docstreet)
                self.txtBox2.insert(END, "\nCity : " + docstate)
                self.txtBox2.insert(END, "\ne-mail : " + docemail)
                self.txtBox2.insert(END, "\nFax : " + docfax)
            else:
                pass
        except FileNotFoundError as err_r3:
            print("+ No file contactdoc2.txt exist", err_r3)

        try:
            if os.path.getsize('./contact/contactdoc3.txt'):
                print("+ Ok, contactdoc3.txt exist (t1)")
        except FileNotFoundError as nfd3:
            print("+ No file contactdoc3.txt exist", nfd3)
            with open('./contact/contactdoc3.txt', 'w') as testfd3:
                print("+ File contactdoc3.txt created !", testfd3)

        self.x3, self.y3 = 900, 1270
        self.txtBox3 = Text(self.can, height=15, width=40, font=18, relief=SUNKEN)
        self.txtBox3.delete('1.0', END)
        self.txtBox3.update()
        self.ftxtBox3_window = self.can.create_window(self.x3, self.y3, window=self.txtBox3)

        try:
            if os.path.exists('./contact/contactdoc3.txt'):
                with open('./contact/contactdoc3.txt', 'r') as policydoc3:
                    doc3line1 = policydoc3.readline()
                    doc3phone = policydoc3.readline()
                    doc3iphone2 = policydoc3.readline()
                    doc3street = policydoc3.readline()
                    doc3state = policydoc3.readline()
                    doc3email = policydoc3.readline()
                    doc3fax = policydoc3.readline()
                self.txtBox3.insert(INSERT, "--- Data Doctor 3 ---\n")
                self.txtBox3.insert(END, "\nDoctor : " + doc3line1)
                self.txtBox3.insert(END, "\nPhone : " + doc3phone)
                self.txtBox3.insert(END, "\nMobile : " + doc3iphone2)
                self.txtBox3.insert(END, "\nStreet : " + doc3street)
                self.txtBox3.insert(END, "\nCity : " + doc3state)
                self.txtBox3.insert(END, "\ne-mail : " + doc3email)
                self.txtBox3.insert(END, "\nFax : " + doc3fax)
            else:
                pass
        except FileNotFoundError as err_r3:
            print("+ No file contactdoc3.txt exist", err_r3)


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

    def recorderDoc2(namentry2, txtphone2, phonentry2, txtmobile2,
        mobilentry2, addrtxt2, addrentry2, citytxt2, cityentry2,
        mailtxt2, entrymail2, faxtxt2, entryfax2):

        try:
            if os.path.getsize('./contact/contactdoc2.txt'):
                print("+ Ok, contactdoc2.txt exist (t3)")
        except FileNotFoundError as errfnf2:
            print("+ No file contactdoc2.txt exist", errfnf2)
            with open('./contact/contactdoc2.txt', 'w') as testf2:
                print("+ File contactdoc2.txt created !", testf2)

        try:
            with open('./contact/contactdoc2.txt', 'w') as datadoc:
                datadoc.write(namentry2.get())
                datadoc.write("\n" + phonentry2.get())
                datadoc.write("\n" + mobilentry2.get())
                datadoc.write("\n" + addrentry2.get())
                datadoc.write("\n" + cityentry2.get())
                datadoc.write("\n" + entrymail2.get())
                datadoc.write("\n" + entryfax2.get())
        except FileNotFoundError as fn2:
            print("+ File not found !", fn2)

        try:
            if os.path.getsize('./contact/finaldoc2.txt'):
                os.remove('./contact/finaldoc2.txt')
        except FileNotFoundError as err_termin2:
            print("+ finaldoc2 not found !(t4)", err_termin2)
            with open('./contact/finaldoc2.txt', 'a+'):
                print("+ finaldoc2.txt exist!")
        try:
            with open('./contact/finaldoc2.txt', 'w') as finalf:
                finalf.write("Doctor : " + namentry2.get())
                finalf.write("\nPhone : " + phonentry2.get())
                finalf.write("\nMobile : " + mobilentry2.get())
                finalf.write("\nStreet : " + addrentry2.get())
                finalf.write("\nCity : " + cityentry2.get())
                finalf.write("\ne-mail : " + entrymail2.get())
                finalf.write("\nFax : " + entryfax2.get())
        except FileNotFoundError as err_final2:
            print("+ finaldoc2.txt not created (t4)", err_final2)

        allInData()

    def recorderDoc3(namentry3, txtphone3, phonentry3, txtmobile3,
        mobilentry3, addrtxt3, addrentry3, citytxt3, cityentry3,
        mailtxt3, entrymail3, faxtxt3, entryfax3):

        try:
            if os.path.getsize('./contact/contactdoc3.txt'):
                print("+ Ok, contactdoc3.txt exist (t3)")
        except FileNotFoundError as errfnf3:
            print("+ No file contactdoc3.txt exist", errfnf3)
            with open('./contact/contactdoc3.txt', 'w') as testf3:
                print("+ File contactdoc3.txt created !", testf3)

        try:
            with open('./contact/contactdoc3.txt', 'w') as datadoc3:
                datadoc3.write(namentry3.get())
                datadoc3.write("\n" + phonentry3.get())
                datadoc3.write("\n" + mobilentry3.get())
                datadoc3.write("\n" + addrentry3.get())
                datadoc3.write("\n" + cityentry3.get())
                datadoc3.write("\n" + entrymail3.get())
                datadoc3.write("\n" + entryfax3.get())
        except FileNotFoundError as fn3:
            print("+ File not found !", fn3)

        try:
            if os.path.getsize('./contact/finaldoc3.txt'):
                os.remove('./contact/finaldoc3.txt')
        except FileNotFoundError as err_termin3:
            print("+ finaldoc3 not found !(t4)", err_termin3)
            with open('./contact/finaldoc3.txt', 'a+'):
                print("+ finaldoc3.txt exist!")
        try:
            with open('./contact/finaldoc3.txt', 'w') as finalf3:
                finalf3.write("Doctor : " + namentry3.get())
                finalf3.write("\nPhone : " + phonentry3.get())
                finalf3.write("\nMobile : " + mobilentry3.get())
                finalf3.write("\nStreet : " + addrentry3.get())
                finalf3.write("\nCity : " + cityentry3.get())
                finalf3.write("\ne-mail : " + entrymail3.get())
                finalf3.write("\nFax : " + entryfax3.get())
        except FileNotFoundError as err_final3:
            print("+ finaldoc3.txt not created (t4)", err_final3)

        allInData()

    allInData()

    # Label title
    self.x11, self.y11 = 250, 100
    self.lbltitle = Label(self.can, text="Contact",
        font=('helvetica', 40, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.lbltitle_window = self.can.create_window(self.x11, self.y11,
        window = self.lbltitle)

    # Label title2
    self.x12, self.y12 = 470, 100
    self.labtitle = Label(self.can, text="Doctors",
        font=('Times', 40, 'italic'),
        bg='DodgerBlue2', fg='coral')
    self.labtitle_window = self.can.create_window(self.x12, self.y12,
        window = self.labtitle)

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

    self.x32, self.y32 = 250, 400
    self.labcity = Label(self.can, text="City :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.labcity_window = self.can.create_window(self.x32, self.y32,
        window = self.labcity)

    self.citytxt = line5
    self.x33, self.y33 = 450, 400
    self.citytxt = StringVar()
    self.cityentry = Entry(self.can, textvariable=self.citytxt,
        highlightbackground='grey', bd=4)
    self.citytxt.set(line5[:-1])
    self.cityentry_window = self.can.create_window(self.x33, self.y33,
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

    self.x52, self.y52 = 350, 570
    self.b52 = Button(self.can, text="Save", font=16,
        width=30, bd=3, bg='RoyalBlue3', fg='yellow',
        highlightbackground='cyan',
        activebackground='pale turquoise',
        command = lambda: recorderData(self.namentry, self.txtphone,
            self.phonentry, self.txtmobile, self.mobilentry,
            self.addrtxt, self.addrentry, self.citytxt, self.cityentry,
            self.mailtxt, self.entrymail, self.faxtxt, self.entryfax))
    self.fb52_window = self.can.create_window(self.x52, self.y52, window=self.b52)

    # Name 2
    self.x60, self.y60 = 250, 670
    self.lbldocname = Label(self.can, text="Doctor :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.lbldocname_window = self.can.create_window(self.x60, self.y60,
        window = self.lbldocname)

    try:
        with open('./contact/contactdoc2.txt', 'r') as docfile2:
            docline1 = docfile2.readline()
            docline2 = docfile2.readline()
            docline3 = docfile2.readline()
            docline4 = docfile2.readline()
            docline5 = docfile2.readline()
            docline6 = docfile2.readline()
            docline7 = docfile2.readline()
            docline8 = docfile2.readline()
            docline9 = docfile2.readline()
    except FileNotFoundError as callfiledoc2:
        print("+ File contactdoc2.txt doesn't exist !", callfiledoc2)

    try:
        self.txt_doc2 = docline1
        self.x62, self.y62 = 450, 670
        self.txt_doc2 = StringVar()
        self.namentry2 = Entry(self.can, textvariable=self.txt_doc2,
            highlightbackground='grey', bd=4)
        self.txt_doc2.set(docline1[:-1])
        self.namentry2_window = self.can.create_window(self.x62, self.y62,
            window = self.namentry2)
    except UnboundLocalError as err_doc2:
        print("+ File 1 not created !", err_doc2)

    # Phone
    self.x63, self.y63 = 250, 720
    self.phonelabel2 = Label(self.can, text="Phone :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.phonelabel2_window = self.can.create_window(self.x63, self.y63,
        window = self.phonelabel2)

    self.txtphone2 = docline2
    self.x64, self.y64 = 450, 720
    self.txtphone2 = StringVar()
    self.phonentry2 = Entry(self.can, textvariable=self.txtphone2,
        highlightbackground='grey', bd=3)
    self.txtphone2.set(docline2[:-1])
    self.phonentry2_window = self.can.create_window(self.x64, self.y64,
        window = self.phonentry2)

    # Mobile
    self.x65, self.y65 = 250, 770
    self.lblmobile2 = Label(self.can, text="Mobile :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.lblmobile2_window = self.can.create_window(self.x65, self.y65,
        window = self.lblmobile2)

    self.txtmobile2 = docline3
    self.x66, self.y66 = 450, 770
    self.txtmobile2 = StringVar()
    self.mobilentry2 = Entry(self.can, textvariable=self.txtmobile2,
        highlightbackground='grey', bd=3)
    self.txtmobile2.set(docline3[:-1])
    self.mobilentry2_window = self.can.create_window(self.x66, self.y66,
        window = self.mobilentry2)

    # Street
    self.x67, self.y67 = 250, 820
    self.addrlabel2 = Label(self.can, text="Street :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.addrlabel2_window = self.can.create_window(self.x67, self.y67,
        window = self.addrlabel2)

    self.addrtxt2 = docline4
    self.x68, self.y68 = 450, 820
    self.addrtxt2 = StringVar()
    self.addrentry2 = Entry(self.can, textvariable=self.addrtxt2,
        highlightbackground='grey', bd=4)
    self.addrtxt2.set(docline4[:-1])
    self.addrentry2_window = self.can.create_window(self.x68, self.y68,
        window = self.addrentry2)

    self.x69, self.y69 = 250, 870
    self.labcity2 = Label(self.can, text="City :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.labcity2_window = self.can.create_window(self.x69, self.y69,
        window = self.labcity2)

    self.citytxt2 = docline5
    self.x70, self.y70 = 450, 870
    self.citytxt2 = StringVar()
    self.cityentry2 = Entry(self.can, textvariable=self.citytxt2,
        highlightbackground='grey', bd=4)
    self.citytxt2.set(docline5[:-1])
    self.cityentry2_window = self.can.create_window(self.x70, self.y70,
        window = self.cityentry2)

    # e-mail
    self.x71, self.y71 = 250, 920
    self.mailabel2 = Label(self.can, text="e-mail :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.mailabel2_window = self.can.create_window(self.x71, self.y71,
        window = self.mailabel2)

    self.mailtxt2 = docline6
    self.x72, self.y72 = 450, 920
    self.mailtxt2 = StringVar()
    self.entrymail2 = Entry(self.can, textvariable=self.mailtxt2,
        highlightbackground='grey', bd=3)
    self.mailtxt2.set(docline6[:-1])
    self.entrymail2_window = self.can.create_window(self.x72, self.y72,
        window = self.entrymail2)

    # Fax
    self.x73, self.y73 = 250, 970
    self.lblfax2 = Label(self.can, text="Fax :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.lblfax2_window = self.can.create_window(self.x73, self.y73,
        window = self.lblfax2)

    self.faxtxt2 = docline7
    self.x74, self.y74 = 450, 970
    self.faxtxt2 = StringVar()
    self.entryfax2 = Entry(self.can, textvariable=self.faxtxt2,
        highlightbackground='grey', bd=3)
    self.faxtxt2.set(docline7)
    self.entryfax2_window = self.can.create_window(self.x74, self.y74,
        window = self.entryfax2)

    self.x75, self.y75 = 350, 1040
    self.bat75 = Button(self.can, text="Save", font=16,
        width=30, bd=3, bg='RoyalBlue3', fg='yellow',
        highlightbackground='cyan',
        activebackground='pale turquoise',
        command = lambda: recorderDoc2(self.namentry2, self.txtphone2,
            self.phonentry2, self.txtmobile2, self.mobilentry2,
            self.addrtxt2, self.addrentry2, self.citytxt2, self.cityentry2,
            self.mailtxt2, self.entrymail2, self.faxtxt2, self.entryfax2))
    self.fbat75_window = self.can.create_window(self.x75, self.y75, window=self.bat75)

    # Name 3
    self.x80, self.y80 = 250, 1140
    self.lbldocname3 = Label(self.can, text="Doctor :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.lbldocname3_window = self.can.create_window(self.x80, self.y80,
        window = self.lbldocname3)

    try:
        with open('./contact/contactdoc3.txt', 'r') as docfile3:
            doc3line1 = docfile3.readline()
            doc3line2 = docfile3.readline()
            doc3line3 = docfile3.readline()
            doc3line4 = docfile3.readline()
            doc3line5 = docfile3.readline()
            doc3line6 = docfile3.readline()
            doc3line7 = docfile3.readline()
            doc3line8 = docfile3.readline()
            doc3line9 = docfile3.readline()
    except FileNotFoundError as callfiledoc3:
        print("+ File contactdoc3.txt doesn't exist !", callfiledoc3)

    try:
        self.txt_doc3 = doc3line1
        self.x81, self.y81 = 450, 1140
        self.txt_doc3 = StringVar()
        self.namentry3 = Entry(self.can, textvariable=self.txt_doc3,
            highlightbackground='grey', bd=4)
        self.txt_doc3.set(doc3line1[:-1])
        self.namentry3_window = self.can.create_window(self.x81, self.y81,
            window = self.namentry3)
    except UnboundLocalError as err_doc3:
        print("+ File 1 not created !", err_doc3)

    # Phone
    self.x82, self.y82 = 250, 1190
    self.phonelabel3 = Label(self.can, text="Phone :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.phonelabel3_window = self.can.create_window(self.x82, self.y82,
        window = self.phonelabel3)

    self.txtphone3 = doc3line2
    self.x83, self.y83 = 450, 1190
    self.txtphone3 = StringVar()
    self.phonentry3 = Entry(self.can, textvariable=self.txtphone3,
        highlightbackground='grey', bd=3)
    self.txtphone3.set(doc3line2[:-1])
    self.phonentry3_window = self.can.create_window(self.x83, self.y83,
        window = self.phonentry3)

    # Mobile
    self.x84, self.y84 = 250, 1240
    self.lblmobile3 = Label(self.can, text="Mobile :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.lblmobile3_window = self.can.create_window(self.x84, self.y84,
        window = self.lblmobile3)

    self.txtmobile3 = doc3line3
    self.x85, self.y85 = 450, 1240
    self.txtmobile3 = StringVar()
    self.mobilentry3 = Entry(self.can, textvariable=self.txtmobile3,
        highlightbackground='grey', bd=3)
    self.txtmobile3.set(doc3line3[:-1])
    self.mobilentry3_window = self.can.create_window(self.x85, self.y85,
        window = self.mobilentry3)

    # Street
    self.x86, self.y86 = 250, 1290
    self.addrlabel3 = Label(self.can, text="Street :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.addrlabel3_window = self.can.create_window(self.x86, self.y86,
        window = self.addrlabel3)

    self.addrtxt3 = doc3line4
    self.x87, self.y87 = 450, 1290
    self.addrtxt3 = StringVar()
    self.addrentry3 = Entry(self.can, textvariable=self.addrtxt3,
        highlightbackground='grey', bd=4)
    self.addrtxt3.set(doc3line4[:-1])
    self.addrentry3_window = self.can.create_window(self.x87, self.y87,
        window = self.addrentry3)

    self.x88, self.y88 = 250, 1340
    self.labcity3 = Label(self.can, text="City :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.labcity3_window = self.can.create_window(self.x88, self.y88,
        window = self.labcity3)

    self.citytxt3 = doc3line5
    self.x89, self.y89 = 450, 1340
    self.citytxt3 = StringVar()
    self.cityentry3 = Entry(self.can, textvariable=self.citytxt3,
        highlightbackground='grey', bd=4)
    self.citytxt3.set(doc3line5[:-1])
    self.cityentry3_window = self.can.create_window(self.x89, self.y89,
        window = self.cityentry3)

    # e-mail
    self.x90, self.y90 = 250, 1390
    self.mailabel3 = Label(self.can, text="e-mail :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.mailabel3_window = self.can.create_window(self.x90, self.y90,
        window = self.mailabel3)

    self.mailtxt3 = doc3line6
    self.x91, self.y91 = 450, 1390
    self.mailtxt3 = StringVar()
    self.entrymail3 = Entry(self.can, textvariable=self.mailtxt3,
        highlightbackground='grey', bd=3)
    self.mailtxt3.set(doc3line6[:-1])
    self.entrymail3_window = self.can.create_window(self.x91, self.y91,
        window = self.entrymail3)

    # Fax
    self.x92, self.y92 = 250, 1440
    self.lblfax3 = Label(self.can, text="Fax :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.lblfax3_window = self.can.create_window(self.x92, self.y92,
        window = self.lblfax3)

    self.faxtxt3 = doc3line7
    self.x93, self.y93 = 450, 1440
    self.faxtxt3 = StringVar()
    self.entryfax3 = Entry(self.can, textvariable=self.faxtxt3,
        highlightbackground='grey', bd=3)
    self.faxtxt3.set(doc3line7[:-1])
    self.entryfax3_window = self.can.create_window(self.x93, self.y93,
        window = self.entryfax3)

    self.x94, self.y94 = 350, 1530
    self.bat94 = Button(self.can, text="Save", font=16,
        width=30, bd=3, bg='RoyalBlue3', fg='yellow',
        highlightbackground='cyan',
        activebackground='pale turquoise',
        command = lambda: recorderDoc3(self.namentry3, self.txtphone3,
            self.phonentry3, self.txtmobile3, self.mobilentry3,
            self.addrtxt3, self.addrentry3, self.citytxt3, self.cityentry3,
            self.mailtxt3, self.entrymail3, self.faxtxt3, self.entryfax3))
    self.fbat94_window = self.can.create_window(self.x94, self.y94, window=self.bat94)

    self.can.configure(scrollregion=self.can.bbox(ALL))
