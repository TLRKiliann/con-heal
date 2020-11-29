#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *


#def Window(self):
def Window(self):
    # Define settings upon initialization. Here you can specify
    #bframe.__init__(self, bg='RoyalBlue2')
    self.can.delete(ALL)
    self.can.configure(background='DodgerBlue2')
    """



    def family(self):
        textPat = StringVar()
        patEntry = Entry(self, textvariable=textPat)
        textPat.set(line1)
        patEntry.pack()

        buttonPat = Button(self, text='Enter', command='')
        buttonPat.pack()

        textPhone = IntVar()
        phoneEntry = Entry(self, textvariable=textPhone)
        textPhone.set("")
        phoneEntry.pack()

        buttonPhone = Button(self, text='Enter', command='')
        buttonPhone.pack()

        textAddr = StringVar()
        addrEntry = Entry(self, textvariable=textAddr)
        textAddr.set("")
        addrEntry.pack()

        buttonAddr = Button(self, text='Enter', command='')
        buttonAddr.pack()

        textMail = StringVar()
        mailEntry = Entry(self, textvariable=textMail)
        textMail.set("")
        mailEntry.pack()

        buttonMail = Button(self, text='Enter', command='')
        buttonMail.pack()

    def doctor(self):
        textPat = StringVar()
        patEntry = Entry(self, textvariable=textPat)
        textPat.set(line1)
        patEntry.pack()

        buttonPat = Button(self, text='Enter', command='')
        buttonPat.pack()

        textPhone = IntVar()
        phoneEntry = Entry(self, textvariable=textPhone)
        textPhone.set("")
        phoneEntry.pack()

        buttonPhone = Button(self, text='Enter', command='')
        buttonPhone.pack()

        textAddr = StringVar()
        addrEntry = Entry(self, textvariable=textAddr)
        textAddr.set("")
        addrEntry.pack()

        buttonAddr = Button(self, text='Enter', command='')
        buttonAddr.pack()

        textMail = StringVar()
        mailEntry = Entry(self, textvariable=textMail)
        textMail.set("")
        mailEntry.pack()

        buttonMail = Button(self, text='Enter', command='')
        buttonMail.pack()

    def reseau(self):
        textPat = StringVar()
        patEntry = Entry(self, textvariable=textPat)
        textPat.set(line1)
        patEntry.pack()

        buttonPat = Button(self, text='Enter', command='')
        buttonPat.pack()

        textPhone = IntVar()
        phoneEntry = Entry(self, textvariable=textPhone)
        textPhone.set("")
        phoneEntry.pack()

        buttonPhone = Button(self, text='Enter', command='')
        buttonPhone.pack()

        textAddr = StringVar()
        addrEntry = Entry(self, textvariable=textAddr)
        textAddr.set("")
        addrEntry.pack()

        buttonAddr = Button(self, text='Enter', command='')
        buttonAddr.pack()

        textMail = StringVar()
        mailEntry = Entry(self, textvariable=textMail)
        textMail.set("")
        mailEntry.pack()

        buttonMail = Button(self, text='Enter', command='')
        buttonMail.pack()

    def curateur(self):
        textPat = StringVar()
        patEntry = Entry(self, textvariable=textPat)
        textPat.set(line1)
        patEntry.pack()

        buttonPat = Button(self, text='Enter', command='')
        buttonPat.pack()

        textPhone = IntVar()
        phoneEntry = Entry(self, textvariable=textPhone)
        textPhone.set("")
        phoneEntry.pack()

        buttonPhone = Button(self, text='Enter', command='')
        buttonPhone.pack()

        textAddr = StringVar()
        addrEntry = Entry(self, textvariable=textAddr)
        textAddr.set("")
        addrEntry.pack()

        buttonAddr = Button(self, text='Enter', command='')
        buttonAddr.pack()

        textMail = StringVar()
        mailEntry = Entry(self, textvariable=textMail)
        textMail.set("")
        mailEntry.pack()

        buttonMail = Button(self, text='Enter', command='')
        buttonMail.pack()

    """

    def nameData():
        """
            Next page after enter patient 1
        """
        txt_pat = StringVar()
        
        try:
            with open('./newpatient/entryfile.txt', 'r') as namefile:
                line1 = namefile.readline()
                txt_pat = line1
        except FileNotFoundError as fileout:
            print("No file entryfile.txt exist", fileout)

        self.x1, self.y1 = 950, 350
        self.t1 = Text(self.can, height=30, width=40, font=18, relief=SUNKEN)
        self.t1.insert(INSERT, "Patient Name : " + line1 + "\n\n")
        self.t1.insert(INSERT, "Phone : \n\n\n")
        self.t1.insert(INSERT, "Address : \n\n\n")
        self.t1.insert(INSERT, "e-mail : \n\n\n")
        self.t1.insert(INSERT, "Assurance : \n\n\n")
        self.t1.insert(INSERT, "Miscellanous : \n\n\n")
        self.ft1=self.can.create_window(self.x1, self.y1, window=self.t1)

    def phoneData(phonetxt, phone_write):
        """
            Next page after enter patient 1
        """

        try:
            with open('./newpatient/entryfile.txt', 'r') as namefile:
                line1 = namefile.readline()
                txt_pat = line1
        except FileNotFoundError as fileout:
            print("No file entryfile.txt exist", fileout)

        try:
            with open('./contact/contactphone.txt', 'w') as phonefile:
                phonefile.write('Phone : ' + str(phonetxt.get()) + '\n')
        except FileNotFoundError as err_w:
            print("No file contactphone.txt exist", err_w)

        try:
            with open('./contact/contactphone.txt', 'r') as phone_r:
                phone = phone_r.readline()
        except FileNotFoundError as err_r:
            print("No file contactphone.txt exist", err_r)

        self.x1, self.y1 = 950, 350
        self.t1 = Text(self.can, height=30, width=40, font=18, relief=SUNKEN)
        self.t1.insert(INSERT, "Patient Name : " + line1 + "\n\n")
        self.t1.insert(INSERT, "Phone : " + str(phonetxt.get()) + "\n\n\n")
        self.t1.insert(INSERT, "Address : \n\n\n")
        self.t1.insert(INSERT, "e-mail : \n\n\n")
        self.t1.insert(INSERT, "Assurance : \n\n\n")
        self.t1.insert(INSERT, "Miscellanous : \n\n\n")
        self.ft1=self.can.create_window(self.x1, self.y1, window=self.t1)

    # Name
    self.x1, self.y1 = 100, 100
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
        self.x2, self.y2 = 300, 100
        txt_pat = StringVar()
        self.name_write = Entry(self.can, textvariable=txt_pat,
            highlightbackground='grey', bd=4)
        txt_pat.set(line1)
        self.name_write = self.can.create_window(self.x2, self.y2,
            window = self.name_write)
    except UnboundLocalError as ub_error1:
        print("+ File 1 not created !", ub_error1)
    
    self.x3, self.y3 = 500, 100
    self.b3 = Button(self.can, text="Enter", font=36,
        width=8, bd=3, bg='RoyalBlue3', fg='white',
        highlightbackground='RoyalBlue3',
        activebackground='pale turquoise', command=nameData)
    self.fb3 = self.can.create_window(self.x3, self.y3, window=self.b3)
    #nameData() # For test. It will be at bottom when script will be finished.

    # Phone
    self.x20, self.y20 = 100, 150
    self.phonelabel = Label(self.can, text="Phone Number :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.phonelabel = self.can.create_window(self.x20, self.y20,
        window = self.phonelabel)

    # On work !
    self.x21, self.y21 = 300, 150
    phonetxt = StringVar()
    phone_write = Entry(self.can, textvariable=phonetxt,
        highlightbackground='grey', bd=3)
    phone_write = self.can.create_window(self.x21, self.y21,
        window = phone_write)

    self.x22, self.y22 = 500, 150
    self.b22 = Button(self.can, text="Enter", font=16,
        width=8, bd=3, bg='RoyalBlue3', fg='white',
        highlightbackground='RoyalBlue3',
        activebackground='pale turquoise', command = lambda: honeData(phonetxt, phone_write))
    self.fb22 = self.can.create_window(self.x22, self.y22, window=self.b22)

    # Address
    self.x30, self.y30 = 100, 200
    self.addrlabel = Label(self.can, text="Address :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.addrlabel = self.can.create_window(self.x30, self.y30,
        window = self.addrlabel)

    self.x31, self.y31 = 300, 200
    addrtxt = StringVar()
    self.addr_write = Entry(self.can, textvariable=addrtxt,
        highlightbackground='grey', bd=4)
    addrtxt.set("Street")
    self.addr_write = self.can.create_window(self.x31, self.y31,
        window = self.addr_write)

    self.x32, self.y32 = 300, 250
    citytxt = StringVar()
    self.city_write = Entry(self.can, textvariable=citytxt,
        highlightbackground='grey', bd=4)
    citytxt.set("City")
    self.city_write = self.can.create_window(self.x32, self.y32,
        window = self.city_write)

    self.x33, self.y33 = 500, 250
    self.b33 = Button(self.can, text="Enter", font=16,
        width=8, bd=3, bg='RoyalBlue3', fg='white',
        highlightbackground='RoyalBlue3',
        activebackground='pale turquoise', command="")
    self.fb33 = self.can.create_window(self.x33, self.y33, window=self.b33)

    # e-mail
    self.x40, self.y40 = 100, 300
    self.mailabel = Label(self.can, text="e-mail :",
        font=('helvetica', 18, 'bold'),
        bg='DodgerBlue2', fg='white')
    self.mailabel = self.can.create_window(self.x40, self.y40,
        window = self.mailabel)

    self.x41, self.y41 = 300, 300
    mailtxt = StringVar()
    self.mail_write = Entry(self.can, textvariable=mailtxt,
        highlightbackground='grey', bd=3)
    mailtxt.set("")
    self.mail_write = self.can.create_window(self.x41, self.y41,
        window = self.mail_write)

    self.x42, self.y42 = 500, 300
    self.b42 = Button(self.can, text="Enter", font=16,
        width=8, bd=3, bg='RoyalBlue3', fg='white',
        highlightbackground='RoyalBlue3',
        activebackground='pale turquoise', command="")
    self.fb42 = self.can.create_window(self.x42, self.y42, window=self.b42)

    self.can.configure(scrollregion=self.can.bbox(ALL))
