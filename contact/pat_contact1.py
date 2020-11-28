#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
import time


class Window(Frame):
    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        Frame.__init__(self, master, bg='RoyalBlue2')                  
        self.master = master    
        self.master.title("Time-Track")
        self.pack(fill=BOTH, expand=1)

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label="Patient contact", font=('Times 12'),
            background='black', activebackground='cyan', foreground='cyan',
            activeforeground='black', command=self.patient)
        file.add_command(label="Familiy contact", font=('Times 12'),
            background='black', activebackground='cyan', foreground='cyan', 
            activeforeground='black', command=self.family)
        file.add_command(label="Dr contact", font=('Times 12'),
            background='black', activebackground='cyan', foreground='cyan',
            activeforeground='black', command=self.doctor)
        file.add_command(label="Home care system", font=('Times 12'),
            background='black', activebackground='cyan', foreground='cyan',
            activeforeground='black', command=self.reseau)
        file.add_command(label="Legal guardian", font=('Times 12'),
            background='black', activebackground='cyan', foreground='cyan',
            activeforeground='black', command=self.curateur)
        file.add_separator(background='black')
        file.add_command(label="Exit", font=('Times 12'),
            background='black', activebackground='cyan', foreground='cyan',
            activeforeground='black', command=self.client_exit)
        menu.add_cascade(label="File", menu=file)

        edit = Menu(menu)
        edit.add_command(label="Patient", underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', command=self.pat_construct)
        edit.add_command(label="Familiy", underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', command=self.fam_construct)
        edit.add_command(label="Doctor", underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', command=self.doc_construct)
        edit.add_command(label="Home care system", underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', command=self.res_construct)
        edit.add_command(label="Legal guardian", underline=0, font=('Times 12'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', command=self.guard_construct)
        menu.add_cascade(label="Edit", menu=edit)


    def patient(self):

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

        textAss = StringVar()
        assEntry = Entry(self, textvariable=textAss)
        textAss.set("")
        assEntry.pack()

        buttonAss = Button(self, text='Enter', command='')
        buttonAss.pack()

        textMisce = StringVar()
        miscEntry = Entry(self, textvariable=textMisce)
        textMisce.set("")
        miscEntry.pack()

        buttonMisce = Button(self, text='Enter', command='')
        buttonMisce.pack()

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

root = Tk()
root.geometry("600x400")
app = Window(root)
root.mainloop()
