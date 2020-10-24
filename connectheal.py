#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
# from tkinter import ttk
from tkinter import messagebox
import tkinter.messagebox
import os
import subprocess
import time
import datetime
# import pymysql


class ScrollCanvas(Frame):
    """
        To prepare ScrollBar for main application.
    """
    def __init__(self, boss=None):
        Frame.__init__(self, borderwidth=borderwidth, relief=relief)
        self.can = Canvas(self, width=width, height=height, bd=bd,
            bg=bg, relief=relief)
        self.frame = Frame(self.can)
        self.vsb = Scrollbar(self, orient=VERTICAL, command=self.can.yview)
        self.can.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side=RIGHT, fill=Y)
        self.can.pack(side=LEFT, fill=BOTH, expand=YES)
        self.can.create_window((4,4), window=self.frame, anchor=NW,
                                  tags="self.frame")
        self.frame.bind("<Configure>", self.onFrameConfigure)

class MenuBar(Frame):
    """
        Menu down
    """
    def __init__(self, boss=None):
        Frame.__init__(self, borderwidth=5, bg='RoyalBlue3', padx=0)
        # 1st menu
        fileMenu = Menubutton(self, text='Menu', fg='white',
            font=("Times 14"), bg='grey30', relief=GROOVE)
        new_text=StringVar()

        fileMenu.pack(side=LEFT, padx=3)
        # Partie déroulante du menu 1st
        me1 = Menu(fileMenu, tearoff=0)
        me1.add_command(label='Accueil', underline=0, font=("Times 14 bold"),
            background='black',activebackground='aquamarine',
            foreground='aquamarine', activeforeground='black',
            command=boss.upDateAll)
        me1.add_command(label='Quit', font=("Times 14 bold"),
            background='black', activebackground='red',
            foreground='red', activeforeground='white',
            command=boss.msgExit)
        # Integration of 1st menu
        fileMenu.configure(activeforeground='black', activebackground='cyan',
            menu=me1)

# Main app
class Application(Frame):
    """
        Main app which content scrollbar and more...
    """
    def __init__(self, boss=None):
        Frame.__init__(self, borderwidth=5, bg='RoyalBlue4', padx=20, pady=20, relief=GROOVE)
        self.master.title('Time-Track- Developed by ko@l@tr33 - 2020')
        mBar = MenuBar(self)
        mBar.pack(side=TOP, fill=X, expand=YES)
        # ScrollCanvas limite de la zone à parcourir avec la barre
        self.can = Canvas(self, width=1250, height=800, bg='grey18')
        self.frame = Frame(self.can)
        self.vsb = Scrollbar(self, orient=VERTICAL, command=self.can.yview)
        self.can.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side=RIGHT, fill=Y)
        #self.can.pack(side=LEFT, fill=BOTH, expand=YES)
        self.can.create_window((4,4), window=self.frame, anchor=NW, tags="self.frame")
        # Insertion of picture
        #self.photo = PhotoImage(file='./syno_gif/fondcolorbg.png')
        #self.item = self.can.create_image(625, 400, image=self.photo)
        # Insertion of text
        #self.can.create_text(625, 420, anchor=CENTER, 
        #    text="Python 3.6 - Tkinter 8.6 - GIMP 2.8",
        #    font=('Times New Roman', 18, 'bold'), fill='turquoise')
        #self.can.create_text(1240, 770, anchor=NE, text="ko@l@tr33",
        #    font=('Times', 12), fill='turquoise')
        # Configuration de la Scrollbar sur le Frame
        self.frame.bind("<Configure>", self.onFrameConfigure)
        self.can.pack(side=LEFT, fill=BOTH, expand=YES)
        # 3 buttons on welcome page.
        # Info button

        """
        # To backup (main file)
        self.updateFiletxt()
        dispAgBox()
        dispTttBox()
        dispResFunc()
        """

        # Display date
        self.x1, self.y1 = 1065, 70
        self.Date_write=Entry(self.can)
        self.data_time=StringVar()
        self.Date_write=Entry(self.can, textvariable=self.data_time, width=10,
            highlightbackground='grey', bd=4)
        self.data_time.set(time.strftime("%d/%m/%Y"))
        self.Date_write=self.can.create_window(self.x1, self.y1,
            window=self.Date_write)

        # Static time
        self.x2, self.y2 = 1165, 70
        self.Date_write2 = Entry(self.can)
        self.data_time2 = StringVar()
        self.Date_write2 = Entry(self.can, width=10, textvariable=self.data_time2,
            highlightbackground='grey', bd=4)
        self.data_time2.set(time.strftime("%H:%M:%S %p"))
        self.Date_write2=self.can.create_window(self.x2, self.y2,
            window=self.Date_write2)

        # To display time dynamically à revoir (new_file.py)
        # To introduce a new pytient
        self.x3, self.y3 = 200, 160
        self.b3=Button(self.can, width=10, font=16, bd=3, highlightbackground='blue',
            bg='RoyalBlue3', fg='white', activebackground='dark turquoise',
            activeforeground='white', text="New Entry", command=self.callPatient1)
        self.fb3=self.can.create_window(self.x3, self.y3, window=self.b3)

        # To add one patient and files
        self.x4, self.y4 = 400, 160
        self.b4=Button(self.can, width=10, font=16, bd=3, highlightbackground='blue',
            bg='RoyalBlue3', fg='cyan', activebackground='dark turquoise',
            activeforeground='white', text="Add patient", command=self.addPatientAfter)
        self.fb4=self.can.create_window(self.x4, self.y4, window=self.b4)
        
        # To refresh canvas + menu bar
        self.x5, self.y5 = 600, 160
        self.b5=Button(self.can, width=10, font=16, bd=3, bg='RoyalBlue3',
            fg='SpringGreen2', highlightbackground='blue',
            activebackground='yellow', activeforeground='SpringGreen2',
            text="Refresh", command=self.upDateAll)
        self.fb5=self.can.create_window(self.x5, self.y5, window=self.b5)

        # To delete one patient and all files
        self.x6, self.y6 = 800, 160
        self.b6=Button(self.can, width=10, font=16, bd=3, highlightbackground='blue',
            bg='RoyalBlue3', fg='coral', activebackground='red', 
            activeforeground='white', text="Delete patient", command=self.delEverPat)
        self.fb6=self.can.create_window(self.x6, self.y6, window=self.b6)

        """
        # Interact with database to display
        def DisplayData():
            sqlCon = pymysql.connect(host='127.0.0.1', user='root', password='Ko@l@tr3379', database='pydatabase')
            cur = sqlCon.cursor()
            cur.execute("SELECT * from pydatabase")
            result = cur.fetchall()
            if len(result) != 0:
                self.student_records.delete(*self.student_records.get_children())
                for row in result:
                    self.student_records.insert('',END,values =row)
                sqlCon.commit()
            sqlCon.close()

        # Interact with database to diplay database in frame
        def PyDataBaseInfo(ev):
            viewInfo = self.student_records.focus()
            learnerData = self.student_records.item(viewInfo)
            row = learnerData['values']
            StudentID.set(row[0])
            Firstname.set(row[1])
            Surname.set(row[2])
            Address.set(row[3])
            Gender.set(row[4])
            Mobile.set(row[5])

        """

        # To convert and for reading in my DB mysql
        try:
            with open('./newpatient/entryfile.txt', 'r') as namefile:
                line1 = namefile.readline()
        except FileNotFoundError as callfile:
            print("File entryfile.txt doesn't exist !", callfile)

        self.new_data1 = line1
        self.x10, self.y10 = 129, 230
        self.Data_write = Entry(self.can)
        self.new_data1 = StringVar()
        self.Data_write = Entry(self.can, textvariable=self.new_data1,
            highlightbackground='grey', bd=4)
        self.new_data1.set(line1)
        self.Data_write = self.can.create_window(self.x10, self.y10,
            window = self.Data_write)

        self.x11, self.y11 = 271, 230
        self.b11=Button(self.can, width=8, font=16, bg='blue violet', fg='cyan',
            activebackground='aquamarine', text="Allergy",
            command=self.allergyLink)
        self.fb11=self.can.create_window(self.x11, self.y11, window=self.b11)

        self.x12, self.y12 = 429, 230
        self.b12=Button(self.can, width=18, font=16, bg='RoyalBlue3', fg='cyan',
            activebackground='aquamarine', text="Diagnostic + ATCD",
            command='') #self.diag1)
        self.fb12=self.can.create_window(self.x12, self.y12, window=self.b12)
        self.pack()
        
    # Method to reconfigure scrollbar every time.
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.can.configure(scrollregion=self.can.bbox(ALL))

    def effacer(self):
        '''Reinitialize canvas when we pass through another'''
        self.can.delete(ALL)

    def msgExit(self):
        """
            If usr want to quit, a question 
            into a msgbox appear.
        """
        MsgBox = messagebox.askyesno('Quit system', 'Do you want to quit ?')
        if MsgBox == 1:
            self.master.destroy()
        else:
            messagebox.showinfo('Return', 'You will now return to the'
                'application screen')
    """
    #------------------

    StudentID = StringVar()
    Firstname = StringVar()
    Surname = StringVar()
    Address = StringVar()
    Gender = StringVar()
    Mobile = StringVar()

    #------------------

    def iExit():
        iExit = tkinter.messagebox.askyesno('MySQL Connection', 'Confirm if you want to exit ?')
        if iExit > 0:
            root.destroy()
            return

    def Reset():
        self.entStudentID.delete(0, END)
        self.entFirstname.delete(0, END)
        self.entSurname.delete(0, END)
        self.entAddress.delete(0, END)
        Gender.set("")
        self.entMobile.delete(0, END)

        # Interact with database to add
        def addData():
            if StudentID.get() == "" or Firstname.get() == "" or Surname.get() == "":
                tkinter.messagebox.showerror("MySQL Connection", "Enter Correct Details.")
            else:
                sqlCon = pymysql.connect(host='127.0.0.1', user='koala', password='', database='con_trackdb')
                cur = sqlCon.cursor()
                cur.execute("INSERT into con_trackdb values (%s,%s,%s,%s,%s,%s)",(

                StudentID.get(),
                Firstname.get(),
                Surname.get(),
                Address.get(),
                Gender.get(),
                Mobile.get(),
                ))
                sqlCon.commit()
                sqlCon.close()
                tkinter.messagebox.showinfo("MySQL connection", "Record Entered Successfully !")

    # Interact with database to add
    def addData():
        if StudentID.get() == "" or Firstname.get() == "" or Surname.get() == "":
            tkinter.messagebox.showerror("MySQL Connection", "Enter Correct Details.")
        else:
            sqlCon = pymysql.connect(host='127.0.0.1', user='root', password='Ko@l@tr3379', database='pydatabase')
            cur = sqlCon.cursor()
            cur.execute("INSERT into pydatabase values (%s,%s,%s,%s,%s,%s)",(

            StudentID.get(),
            Firstname.get(),
            Surname.get(),
            Address.get(),
            Gender.get(),
            Mobile.get(),
            ))
            sqlCon.commit()
            sqlCon.close()
            tkinter.messagebox.showinfo("MySQL connection", "Record Entered Successfully !")

    # Interact with database to display
    def DisplayData():
        sqlCon = pymysql.connect(host='127.0.0.1', user='root', password='Ko@l@tr3379', database='pydatabase')
        cur = sqlCon.cursor()
        cur.execute("SELECT * from pydatabase")
        result = cur.fetchall()
        if len(result) != 0:
            self.student_records.delete(*self.student_records.get_children())
            for row in result:
                self.student_records.insert('',END,values =row)
            sqlCon.commit()
        sqlCon.close()

    # Interact with database to diplay database in frame
    def PyDataBaseInfo(ev):
        viewInfo = self.student_records.focus()
        learnerData = self.student_records.item(viewInfo)
        row = learnerData['values']
        StudentID.set(row[0])
        Firstname.set(row[1])
        Surname.set(row[2])
        Address.set(row[3])
        Gender.set(row[4])
        Mobile.set(row[5])

    # Interact with database to update
    def update():
        sqlCon = pymysql.connect(host='127.0.0.1', user='root', password='Ko@l@tr3379', database='pydatabase')
        cur = sqlCon.cursor()
        cur.execute("UPDATE pydatabase set firstname=%s, surname=%s, address=%s, gender=%s, mobile=%s where stdid=%s",(
        Firstname.get(),
        Surname.get(),
        Address.get(),
        Gender.get(),
        Mobile.get(),
        StudentID.get()
        ))
        sqlCon.commit()
        DisplayData()
        sqlCon.close()
        tkinter.messagebox.showinfo("Data Entry Form", "Record Updated Successfully !")

    # Interact with database to delete
    def deleteDB():
        sqlCon = pymysql.connect(host='127.0.0.1', user='root', password='Ko@l@tr3379', database='pydatabase')
        cur = sqlCon.cursor()
        cur.execute("DELETE from pydatabase where stdid=%s", StudentID.get())
        sqlCon.commit()
        DisplayData()
        sqlCon.close()
        tkinter.messagebox.showinfo("Data Entry Form", "Record Successfully Deleted !")
        Reset()

    # Interact with database to search
    def searchDB():
        try:
            sqlCon = pymysql.connect(host='127.0.0.1', user='root', password='Ko@l@tr3379', database='pydatabase')
            cur = sqlCon.cursor()
            cur.execute("SELECT * from pydatabase where stdid=%s", StudentID.get())
            row = cur.fetchone()

            StudentID.set(row[0])
            Firstname.set(row[1])
            Surname.set(row[2])
            Address.set(row[3])
            Gender.set(row[4])
            Mobile.set(row[5])

            sqlCon.commit()
        except:
            tkinter.messagebox.showinfo("Data Entry Form", "No Such Record Found !")
            Reset()

        sqlCon.close()
    """

    def callPatient1(self):
        """
            To enter a new patient.
        """
        subprocess.run('./newpatient/entrypytientfile.py', check=True)

    def callRecord(self):
        subprocess.run('./newpatient/torecord.py', check=True)

    def addPatientAfter(self):
        """
            To add new patient after delete one of them
            and help to remind to enter allergy
        """
        messagebox.showwarning("Warning", "Don't forget to enter allergy too ! ;)")
        self.callRecord()

    def delEverPat(self):
        """
            To delete patient
        """
        subprocess.run('./deletepatient/deleverything.py', check=True)

    def allergyLink(self):
        """
            To add allergy to new patient 1
        """
        subprocess.run('./allergy/allerpatient1.py', check=True)


    def upDateAll(self):
        """
            To reset app by pressing 
            refresh button. Close,
            open directly and update
            data.
        """
        self.master.destroy()
        subprocess.run('./connectheal.py', check=True)

if __name__=='__main__':
    app = Application()
    app.mainloop()
