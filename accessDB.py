#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    App for many doing severals interactions
    with a MySQL database in python code.
    My first one.
    Install python3-pymysql on your workstation
    not in your virtualenv (otherwise doesn't work)!
    > sudo apt install python3-pymysql
    then install pymysql into your virtualenv.
    > pip3 install pymysql or PyMySQL
"""


from tkinter import *
from tkinter import ttk
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError as err_report:
    print("+ An error occured about pymysql !", err_report)
    pass


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

class TrackDB(Frame):
    """
        Main app to display first page.
    """
    def __init__(self, boss=None):
        Frame.__init__(self, borderwidth=5, bg='RoyalBlue4', padx=20, pady=20, relief=GROOVE)
        self.master.title('Heal-Track Developed by ko@l@tr33 - 2020')
        # ScrollCanvas limite de la zone à parcourir avec la barre
        self.can = Canvas(self, width=1250, height=800, bg='RoyalBlue2')
        self.frame = Frame(self.can)
        self.vsb = Scrollbar(self, orient=VERTICAL, command=self.can.yview)
        self.can.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side=RIGHT, fill=Y)
        self.can.create_window((4,4), window=self.frame, anchor=NW, tags="self.frame")
        self.frame.bind("<Configure>", self.onFrameConfigure)
        self.can.pack(side=LEFT, fill=BOTH, expand=YES)

        ID = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        Born = StringVar()
        Allergy = StringVar()
        Diagnostic = StringVar()
        
        def searchDB():
            sqlCon = pymysql.connect(host='127.0.0.1', user='root', password='Ko@l@tr3379', database='timetrackconn')
            cur = sqlCon.cursor()
            cur.execute("SELECT * from timetrackconn")
            result = cur.fetchall()
            if len(result) != 0:
                self.student_records.delete(*self.student_records.get_children())
                for row in result:
                    self.student_records.insert('', END, values = row)
                sqlCon.commit()
            sqlCon.close()

        self.student_records=ttk.Treeview(self.can, height=24,columns=("stdid", 
            "firstname", "surname", "born", "allergy", "maindiagnostic"))

        self.student_records.heading("stdid", text="ID")
        self.student_records.heading("firstname", text="Firstname")
        self.student_records.heading("surname", text="Surname")
        self.student_records.heading("born", text="Born")
        self.student_records.heading("allergy", text="Allergy")
        self.student_records.heading("maindiagnostic", text="Diagnostic")

        self.student_records['show']="headings"

        self.student_records.column("stdid", width=75)
        self.student_records.column("firstname", width=150)
        self.student_records.column("surname", width=150)
        self.student_records.column("born", width=125)
        self.student_records.column("allergy", width=200)
        self.student_records.column("maindiagnostic", width=200)

        self.student_records.pack(fill=BOTH, expand=YES)

        #self.student_records.bind("<ButtonRelease-1>", PyDataBaseInfo)
        self.btnSearch = Button(self.can, font=('arial', 12, 'bold'), text="Display All", bd=4, 
            padx=8, pady=1, width=16, height=1, fg='white', bg='RoyalBlue3',
            activebackground='cyan', activeforeground='RoyalBlue3', command=searchDB)
        self.btnSearch.pack(side=LEFT)

        self.butBox = Button(self.can, font=('arial', 12, 'bold'), text="Quit", bd=4, 
            padx=8, pady=1, width=16, height=1, fg='white', bg='RoyalBlue3',
            activebackground='cyan', activeforeground='RoyalBlue3', command=quit)
        self.butBox.pack(side=RIGHT)

        self.pack()

    # Method to reconfigure scrollbar every time.
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.can.configure(scrollregion=self.can.bbox(ALL))

if __name__=='__main__':
    gui = TrackDB()
    gui.mainloop()
