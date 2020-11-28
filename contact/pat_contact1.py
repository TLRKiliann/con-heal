#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *


#def Window(self):
def Window(self):
    # Define settings upon initialization. Here you can specify
    #bframe.__init__(self, bg='RoyalBlue2')
    self.can.delete(ALL)
    self.can.configure(background='DodgerBlue2')
    self.photo=PhotoImage(file='./syno_gif/title_tt3.png')
    self.item=self.can.create_image(625, 85, image=self.photo)
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

    def pat_construct(self):
        textBox = Text(self, height=18, width=50, font=18)
        textBox.insert(INSERT, "Patient Name : \n\n\n")
        textBox.insert(INSERT, "Phone : \n\n\n")
        textBox.insert(INSERT, "Address : \n\n\n")
        textBox.insert(INSERT, "e-mail : \n\n\n")
        textBox.insert(INSERT, "Assurance : \n\n\n")
        textBox.insert(INSERT, "Miscellanous : \n\n\n")
        textBox.pack(padx=30, pady=10)

    def fam_construct(self):
        textBox = Text(self, height=18, width=50, font=18)
        textBox.insert(INSERT, "Familiy : \n\n\n")
        textBox.insert(INSERT, "Phone : \n\n\n")
        textBox.insert(INSERT, "Address : \n\n\n")
        textBox.insert(INSERT, "e-mail : \n\n\n")
        textBox.pack(padx=30, pady=10)

    def doc_construct(self):
        textBox = Text(self, height=18, width=50, font=18)
        textBox.insert(INSERT, "Doctor : \n\n\n")
        textBox.insert(INSERT, "Phone : \n\n\n")
        textBox.insert(INSERT, "Address : \n\n\n")
        textBox.insert(INSERT, "e-mail : \n\n\n")
        textBox.pack(padx=30, pady=10)

    def res_construct(self):
        textBox = Text(self, height=18, width=50, font=18)
        textBox.insert(INSERT, "Home care system : \n\n\n")
        textBox.insert(INSERT, "Phone : \n\n\n")
        textBox.insert(INSERT, "Address : \n\n\n")
        textBox.insert(INSERT, "e-mail : \n\n\n")
        textBox.pack(padx=30, pady=10)

    def guard_construct(self):
        textBox = Text(self, height=18, width=50, font=18)
        textBox.insert(INSERT, "Legal guardian : \n\n\n")
        textBox.insert(INSERT, "Phone : \n\n\n")
        textBox.insert(INSERT, "Address : \n\n\n")
        textBox.insert(INSERT, "e-mail : \n\n\n")
        textBox.pack(padx=30, pady=10)

    def client_exit(self):
        exit()
    """

    try:
        with open('./newpatient/entryfile.txt', 'r') as namefile:
            line1 = namefile.readline()
    except FileNotFoundError as callfile:
        print("File entryfile.txt doesn't exist !", callfile)

    try:
        self.data_time=line1
        self.x10, self.y10 = 450, 200
        self.new_data1=StringVar()
        self.Data_write=Entry(self.can, textvariable=self.new_data1,
            highlightbackground='grey', bd=4)
        self.new_data1.set(line1)
        self.Data_write=self.can.create_window(self.x10, self.y10,
            window=self.Data_write)
    except UnboundLocalError as ub_error1:
        print("+ File 1 not created !", ub_error1)

    self.x11, self.y11 = 200, 200
    self.b11=Button(self.can, width=8, font=16, bg='blue violet', fg='white',
        activebackground='MediumOrchid1', text="Enter",
        command=self.callDataPat)
    self.fb11=self.can.create_window(self.x11, self.y11, window=self.b11)



    self.can.configure(scrollregion=self.can.bbox(ALL))
