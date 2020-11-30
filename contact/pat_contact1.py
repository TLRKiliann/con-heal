#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *


#def Window(self):
def Window(self):
    """
        Main function to define 
        design for contact interface.
    """
    self.can.delete(ALL)
    self.can.configure(background='DodgerBlue2')

    def nameData():
        """
            Display name
        """
        txt_pat = StringVar()
        try:
            with open('./newpatient/entryfile.txt', 'r') as namefile:
                line1 = namefile.readline()
        except FileNotFoundError as fileout:
            print("No file entryfile.txt exist", fileout)

        self.x1, self.y1 = 950, 350
        self.t1 = Text(self.can, height=25, width=40, font=18, relief=SUNKEN)
        self.t1.insert(INSERT, "Patient Name : " + line1 + "\n\n")
        self.t1.insert(INSERT, "Native : \n\n")
        self.t1.insert(INSERT, "Phone : \n\n")
        self.t1.insert(INSERT, "Address : \n\n")
        self.t1.insert(INSERT, "e-mail : \n\n")
        self.t1.insert(INSERT, "Assurance : \n\n")
        self.t1.insert(INSERT, "Policy : \n\n")
        self.ft1=self.can.create_window(self.x1, self.y1, window=self.t1)

    def nativaData(native, nativa_write):
        """
            Display origin
        """
        try:
            with open('./newpatient/entryfile.txt', 'r') as namefile:
                line1 = namefile.readline()
                line2 = namefile.readline()
        except FileNotFoundError as fileout:
            print("No file entryfile.txt exist", fileout)

        try:
            with open('./contact/contact1.txt', 'w') as nativefile:
                nativefile.write(str(native.get()) + '\n')
        except FileNotFoundError as err_w:
            print("No file contact1.txt exist", err_w)

        try:
            with open('./contact/contact1.txt', 'r') as nativa_r:
                read_nativa = nativa_r.readline()
        except FileNotFoundError as err_r:
            print("No file contact1.txt exist", err_r)

        self.x1, self.y1 = 950, 350
        self.t1 = Text(self.can, height=25, width=40, font=18, relief=SUNKEN)
        self.t1.insert(INSERT, "Patient Name : " + line1 + "\n\n")
        self.t1.insert(INSERT, "Birthdate : " + line2 + "\n\n")
        self.t1.insert(INSERT, "Native : " + read_nativa + "\n\n")
        self.t1.insert(INSERT, "Phone : \n\n")
        self.t1.insert(INSERT, "Address : \n\n")
        self.t1.insert(INSERT, "e-mail : \n\n")
        self.t1.insert(INSERT, "Assurance : \n\n")
        self.t1.insert(INSERT, "Policy : \n\n")
        self.ft1=self.can.create_window(self.x1, self.y1, window=self.t1)


    def phoneData(phonetxt, phone_write):
        """
            Display phone
        """
        try:
            with open('./newpatient/entryfile.txt', 'r') as namefile:
                line1 = namefile.readline()
                line2 = namefile.readline()
        except FileNotFoundError as fileout:
            print("No file entryfile.txt exist", fileout)

        try:
            with open('./contact/contact1.txt', 'a+') as phonefile:
                phonefile.write(str(phonetxt.get()) + '\n')
        except FileNotFoundError as err_w:
            print("No file contact1.txt exist", err_w)

        try:
            with open('./contact/contact1.txt', 'r') as phone_r:
                native = phone_r.readline()
                phone = phone_r.readline()
        except FileNotFoundError as err_r:
            print("No file contact1.txt exist", err_r)

        self.x1, self.y1 = 950, 350
        self.t1 = Text(self.can, height=25, width=40, font=18, relief=SUNKEN)
        self.t1.insert(INSERT, "Patient Name : " + line1 + "\n\n")
        self.t1.insert(INSERT, "Birthdate : " + line2 + "\n\n")
        self.t1.insert(INSERT, "Native : " + native + "\n\n")
        self.t1.insert(INSERT, "Phone : " + str(phonetxt.get()) + "\n\n")
        self.t1.insert(INSERT, "Address : \n\n")
        self.t1.insert(INSERT, "e-mail : \n\n")
        self.t1.insert(INSERT, "Assurance : \n\n")
        self.t1.insert(INSERT, "Policy : \n\n")
        self.ft1=self.can.create_window(self.x1, self.y1, window=self.t1)

    def addrData(addrtxt, addr_write, citytxt, city_write):
        """
            Display address
        """
        try:
            with open('./newpatient/entryfile.txt', 'r') as namefile:
                line1 = namefile.readline()
                line2 = namefile.readline()
        except FileNotFoundError as fileout:
            print("No file entryfile.txt exist", fileout)

        try:
            with open('./contact/contact1.txt', 'a+') as addr_file:
                addr_file.write(str(addrtxt.get()) + '\n')
                addr_file.write(str(citytxt.get()) + '\n')
        except FileNotFoundError as err_w:
            print("No file contact1.txt exist", err_w)

        try:
            with open('./contact/contact1.txt', 'r') as add_r:
                native = add_r.readline()
                phone = add_r.readline()
                streetad = add_r.readline()
                cityadd = add_r.readline()
        except FileNotFoundError as err_r:
            print("No file contact1.txt exist", err_r)

        self.x1, self.y1 = 950, 350
        self.t1 = Text(self.can, height=25, width=40, font=18, relief=SUNKEN)
        self.t1.insert(INSERT, "Patient Name : " + line1 + "\n\n")
        self.t1.insert(INSERT, "Birthdate : " + line2 + "\n\n")
        self.t1.insert(INSERT, "Native : " + native + "\n\n")
        self.t1.insert(INSERT, "Phone : " + phone + "\n\n")
        self.t1.insert(INSERT, "Street : " + streetad + "\n\n")
        self.t1.insert(INSERT, "City : " + cityadd + "\n\n")
        self.t1.insert(INSERT, "e-mail : \n\n")
        self.t1.insert(INSERT, "Assurance : \n\n")
        self.t1.insert(INSERT, "Policy : \n\n")
        self.ft1=self.can.create_window(self.x1, self.y1, window=self.t1)

    def mailData(mailtxt, mail_write):
        """
            Display e-mail
        """
        try:
            with open('./newpatient/entryfile.txt', 'r') as namefile:
                line1 = namefile.readline()
                line2 = namefile.readline()
        except FileNotFoundError as fileout:
            print("No file entryfile.txt exist", fileout)

        try:
            with open('./contact/contact1.txt', 'a+') as addr_file:
                addr_file.write(str(mailtxt.get()) + '\n')
        except FileNotFoundError as err_w:
            print("No file contact1.txt exist", err_w)

        try:
            with open('./contact/contact1.txt', 'r') as add_r:
                native = add_r.readline()
                phone = add_r.readline()
                streetad = add_r.readline()
                cityadd = add_r.readline()
                mail = add_r.readline()
        except FileNotFoundError as err_r:
            print("No file contact1.txt exist", err_r)

        self.x1, self.y1 = 950, 350
        self.t1 = Text(self.can, height=25, width=40, font=18, relief=SUNKEN)
        self.t1.insert(INSERT, "Patient Name : " + line1 + "\n\n")
        self.t1.insert(INSERT, "Birthdate : " + line2 + "\n\n")
        self.t1.insert(INSERT, "Native : " + native + "\n\n")
        self.t1.insert(INSERT, "Phone : " + phone + "\n\n")
        self.t1.insert(INSERT, "Street : " + streetad + "\n\n")
        self.t1.insert(INSERT, "City : " + cityadd + "\n\n")
        self.t1.insert(INSERT, "e-mail : " + mail + "\n\n")
        self.t1.insert(INSERT, "Assurance : \n\n")
        self.t1.insert(INSERT, "Policy : \n\n")
        self.ft1=self.can.create_window(self.x1, self.y1, window=self.t1)


    def assuData(assurance, assu_write):
        """
            Display insurance
        """
        try:
            with open('./newpatient/entryfile.txt', 'r') as namefile:
                line1 = namefile.readline()
                line2 = namefile.readline()
        except FileNotFoundError as fileout:
            print("No file entryfile.txt exist", fileout)

        try:
            with open('./contact/contact1.txt', 'a+') as assufile:
                assufile.write(str(assurance.get()) + '\n')
        except FileNotFoundError as err_w:
            print("No file contact1.txt exist", err_w)

        try:
            with open('./contact/contact1.txt', 'r') as assu_r:
                native = assu_r.readline()
                phone = assu_r.readline()
                street = assu_r.readline()
                cityadd = assu_r.readline()
                email = assu_r.readline()
                assu = assu_r.readline()
        except FileNotFoundError as err_r:
            print("No file contact1.txt exist", err_r)

        self.x1, self.y1 = 950, 350
        self.t1 = Text(self.can, height=25, width=40, font=18, relief=SUNKEN)
        self.t1.delete('1.0', END)
        self.t1.update()
        self.t1.insert(INSERT, "Patient Name : " + line1 + "\n\n")
        self.t1.insert(INSERT, "Birthdate : " + line2 + "\n\n")
        self.t1.insert(INSERT, "Native : " + native + "\n\n")
        self.t1.insert(INSERT, "Phone : " + phone + "\n\n")
        self.t1.insert(INSERT, "Street : " + street + "\n\n")
        self.t1.insert(INSERT, "City : " + cityadd + "\n\n")
        self.t1.insert(INSERT, "e-mail : " + email + "\n\n")
        self.t1.insert(INSERT, "Insurance : " + assu + "\n\n")
        self.t1.insert(INSERT, "Policy : \n\n")
        self.ft1=self.can.create_window(self.x1, self.y1, window=self.t1)

    def policyData(policy, poli_write):
        """
            Display policy
        """
        try:
            with open('./newpatient/entryfile.txt', 'r') as namefile:
                line1 = namefile.readline()
                line2 = namefile.readline()
        except FileNotFoundError as fileout:
            print("No file entryfile.txt exist", fileout)

        try:
            with open('./contact/contact1.txt', 'a+') as assufile:
                assufile.write(str(policy.get()) + '\n')
        except FileNotFoundError as err_w:
            print("No file contact1.txt exist", err_w)

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
        self.t1 = Text(self.can, height=25, width=40, font=18, relief=SUNKEN)
        self.t1.delete('1.0', END)
        self.t1.update()
        self.t1.insert(INSERT, "Patient Name : " + line1 + "\n\n")
        self.t1.insert(INSERT, "Birthdate : " + line2 + "\n\n")
        self.t1.insert(INSERT, "Native : " + native + "\n\n")
        self.t1.insert(INSERT, "Phone : " + phone + "\n\n")
        self.t1.insert(INSERT, "Street : " + street + "\n\n")
        self.t1.insert(INSERT, "City : " + state + "\n\n")
        self.t1.insert(INSERT, "e-mail : " + email + "\n\n")
        self.t1.insert(INSERT, "Insurance : " + assu + "\n\n")
        self.t1.insert(INSERT, "Policy : " + polins + "\n\n")
        self.ft1=self.can.create_window(self.x1, self.y1, window=self.t1)

    nameData()
    # !!! In one file for function txtbox !!!
    # Label title
    self.x11, self.y11 = 625, 20
    self.labelname = Label(self.can, text="Contact",
        font=('helvetica', 28, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.labelname = self.can.create_window(self.x11, self.y11,
        window = self.labelname)  

    # Name
    self.x1, self.y1 = 200, 100
    self.labelname = Label(self.can, text="Patient Name :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.labelname = self.can.create_window(self.x1, self.y1,
        window = self.labelname)

    try:
        with open('./newpatient/entryfile.txt', 'r') as namefile:
            line1 = namefile.readline()
            txt_pat = line1
    except FileNotFoundError as callfile:
        print("File entryfile.txt doesn't exist !", callfile)

    try:
        txt_pat = line1
        self.x2, self.y2 = 400, 100
        txt_pat = StringVar()
        self.name_write = Entry(self.can, textvariable=txt_pat,
            highlightbackground='grey', bd=4)
        txt_pat.set(line1)
        self.name_write = self.can.create_window(self.x2, self.y2,
            window = self.name_write)
    except UnboundLocalError as ub_error1:
        print("+ File 1 not created !", ub_error1)

    # Native
    self.x15, self.y15 = 200, 250
    self.nativelab = Label(self.can, text="Native :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.nativelab = self.can.create_window(self.x15, self.y15,
        window = self.nativelab)

    self.x16, self.y16 = 400, 250
    native = StringVar()
    nativa_write = Entry(self.can, textvariable=native,
        highlightbackground='grey', bd=3)
    nativa_write = self.can.create_window(self.x16, self.y16,
        window = nativa_write)

    self.x17, self.y17 = 575, 250
    self.b17 = Button(self.can, text="Enter", font=16,
        width=8, bd=3, bg='RoyalBlue3', fg='white',
        highlightbackground='RoyalBlue3',
        activebackground='pale turquoise',
        command = lambda: nativaData(native, nativa_write))
    self.fb17 = self.can.create_window(self.x17, self.y17, window=self.b17)

    # Phone
    self.x20, self.y20 = 200, 300
    self.phonelabel = Label(self.can, text="Phone Number :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.phonelabel = self.can.create_window(self.x20, self.y20,
        window = self.phonelabel)

    self.x21, self.y21 = 400, 300
    phonetxt = StringVar()
    phone_write = Entry(self.can, textvariable=phonetxt,
        highlightbackground='grey', bd=3)
    phone_write = self.can.create_window(self.x21, self.y21,
        window = phone_write)

    self.x22, self.y22 = 575, 300
    self.b22 = Button(self.can, text="Enter", font=16,
        width=8, bd=3, bg='RoyalBlue3', fg='white',
        highlightbackground='RoyalBlue3',
        activebackground='pale turquoise',
        command = lambda: phoneData(phonetxt, phone_write))
    self.fb22 = self.can.create_window(self.x22, self.y22, window=self.b22)

    # Address
    self.x30, self.y30 = 200, 350
    self.addrlabel = Label(self.can, text="Address :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.addrlabel = self.can.create_window(self.x30, self.y30,
        window = self.addrlabel)

    self.x31, self.y31 = 400, 350
    addrtxt = StringVar()
    addr_write = Entry(self.can, textvariable=addrtxt,
        highlightbackground='grey', bd=4)
    addrtxt.set("Street")
    addr_write = self.can.create_window(self.x31, self.y31,
        window = addr_write)

    self.x32, self.y32 = 400, 400
    citytxt = StringVar()
    city_write = Entry(self.can, textvariable=citytxt,
        highlightbackground='grey', bd=4)
    citytxt.set("City")
    city_write = self.can.create_window(self.x32, self.y32,
        window = city_write)

    self.x33, self.y33 = 575, 400
    self.b33 = Button(self.can, text="Enter", font=16,
        width=8, bd=3, bg='RoyalBlue3', fg='white',
        highlightbackground='RoyalBlue3',
        activebackground='pale turquoise',
        command = lambda: addrData(addrtxt, addr_write, citytxt, city_write))
    self.fb33 = self.can.create_window(self.x33, self.y33, window=self.b33)

    # e-mail
    self.x40, self.y40 = 200, 450
    self.mailabel = Label(self.can, text="e-mail :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.mailabel = self.can.create_window(self.x40, self.y40,
        window = self.mailabel)

    self.x41, self.y41 = 400, 450
    mailtxt = StringVar()
    mail_write = Entry(self.can, textvariable=mailtxt,
        highlightbackground='grey', bd=3)
    mailtxt.set("")
    mail_write = self.can.create_window(self.x41, self.y41,
        window = mail_write)

    self.x42, self.y42 = 575, 450
    self.b42 = Button(self.can, text="Enter", font=16,
        width=8, bd=3, bg='RoyalBlue3', fg='white',
        highlightbackground='RoyalBlue3',
        activebackground='pale turquoise',
        command = lambda: mailData(mailtxt, mail_write))
    self.fb42 = self.can.create_window(self.x42, self.y42, window=self.b42)

    # Assurance
    self.x50, self.y50 = 200, 500
    self.mailabel = Label(self.can, text="Insurance :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.mailabel = self.can.create_window(self.x50, self.y50,
        window = self.mailabel)

    self.x51, self.y51 = 400, 500
    assurance = StringVar()
    assu_write = Entry(self.can, textvariable=assurance,
        highlightbackground='grey', bd=3)
    assu_write = self.can.create_window(self.x51, self.y51,
        window = assu_write)

    self.x52, self.y52 = 575, 500
    self.b52 = Button(self.can, text="Enter", font=16,
        width=8, bd=3, bg='RoyalBlue3', fg='white',
        highlightbackground='RoyalBlue3',
        activebackground='pale turquoise',
        command = lambda: assuData(assurance, assu_write))
    self.fb52 = self.can.create_window(self.x52, self.y52, window=self.b52)

    # Police
    self.x50, self.y50 = 200, 550
    self.mailabel = Label(self.can, text="Policy Number :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.mailabel = self.can.create_window(self.x50, self.y50,
        window = self.mailabel)

    self.x51, self.y51 = 400, 550
    policy = StringVar()
    poli_write = Entry(self.can, textvariable=policy,
        highlightbackground='grey', bd=3)
    poli_write = self.can.create_window(self.x51, self.y51,
        window = poli_write)

    self.x52, self.y52 = 575, 550
    self.b52 = Button(self.can, text="Enter", font=16,
        width=8, bd=3, bg='RoyalBlue3', fg='white',
        highlightbackground='RoyalBlue3',
        activebackground='pale turquoise',
        command = lambda: policyData(policy, poli_write))
    self.fb52 = self.can.create_window(self.x52, self.y52, window=self.b52)

    self.can.configure(scrollregion=self.can.bbox(ALL))
