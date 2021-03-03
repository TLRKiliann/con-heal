#!/usr/bin/python3
# -*-encoding:Utf-8-*-


from tkinter import *
import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import platform


# La ScrollBar en class! Préparation pour l'application.
class ScrollCanvas(tk.Frame):
    def __init__(self, boss=None):
        tk.Frame.__init__(self, borderwidth=borderwidth, relief=relief)
        self.can = tk.Canvas(self, width=width, height=height, bd=bd, bg=bg,
            relief=relief)
        self.frame = tk.Frame(self.can)

        self.vsb = tk.Scrollbar(self, orient=VERTICAL, command=self.can.yview)
        self.can.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side=tk.RIGHT, fill=Y)
        self.can.pack(side=tk.LEFT, fill=BOTH, expand=YES)
        self.can.create_window((4, 4), window=self.frame, anchor=tk.NW,
            tags="self.frame")
        self.frame.bind("<Configure>", self.onFrameConfigure)

# Class de la barre des menus
class MenuBar(tk.Frame):
    """Barre menu déroulant"""
    def __init__(self, boss=None):
        tk.Frame.__init__(self, borderwidth=5, bg='RoyalBlue3', padx=0)
        But2 = tk.Button(self, text ="Close", fg='cyan', bg='navy', relief=GROOVE,
            activebackground='cyan', command=boss.quit).pack(side=tk.LEFT, padx=3)

# Application principale
class Application(tk.Frame):
    def __init__(self, boss=None):
        tk.Frame.__init__(self)
        self.master.title('PDF MANUALS')
        mBar = MenuBar(self)
        mBar.pack(side=TOP, fill=X, expand=1)
        # ScrollCanvas limite de la zone à parcourir avec la barre
        self.can = tk.Canvas(self, width=900, height=750, bg='DodgerBlue2')
        self.frame = tk.Frame(self.can)
        self.vsb = tk.Scrollbar(self, orient=VERTICAL, command=self.can.yview)
        self.can.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side=tk.RIGHT, fill=Y)
        self.can.pack(side=tk.LEFT, fill=BOTH, expand=YES)
        self.can.create_window((4,4), window=self.frame, anchor=tk.NW,
            tags="self.frame")
        # Insertion du texte
        self.can.create_text(200, 65, anchor=tk.CENTER, text="PDF Manuals",
            font=('Times New Roman', 28), fill='yellow')

        self.can.create_text(200, 150, anchor='w', text="Monovettes",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(200, 200, anchor='w', text="Urines 1er jet",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(200, 250, anchor='w', text="Urines 2ème jet",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(200, 300, anchor='w', text="Urines/24h",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(200, 350, anchor='w', text="Baby urines",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(200, 400, anchor='w', text="Urine pic ovulaire",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(200, 450, anchor='w', text="Hemocultures",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(200, 500, anchor='w', text="Frottis",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(200, 550, anchor='w', text="Helicobacter pylori",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(200, 600, anchor='w', text="Expectoration",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(200, 650, anchor='w', text="Coprocultures",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(200, 700, anchor='w', text="Research oxyures",
            font=('Times New Roman', 18), fill='white')

        self.can.create_text(600, 65, anchor=tk.CENTER, text="Monitoring",
            font=('Times New Roman', 28), fill='yellow')

        self.can.create_text(600, 150, anchor='w', text="Id Suicidaires",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(600, 200, anchor='w', text="Angoisses",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(600, 250, anchor='w', text="Evaluation de l'Humeur",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(600, 300, anchor='w', text="Démence - Délirium",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(600, 350, anchor='w', text="Orientation (3 modes)",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(600, 400, anchor='w', text="Hallucinations Visuelles",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(600, 450, anchor='w', text="Hallucinations Auditives",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(600, 500, anchor='w', text="",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(600, 550, anchor='w', text="",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(600, 600, anchor='w', text="",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(600, 650, anchor='w', text="",
            font=('Times New Roman', 18), fill='white')
        self.can.create_text(600, 700, anchor='w', text="Crise d'Epilepsie (obs.)",
            font=('Times New Roman', 18), fill='white')

        self.can.pack(side=tk.LEFT, fill=BOTH, expand=1)

        # Configuration de la Scrollbar sur le Frame
        self.frame.bind("<Configure>", self.onFrameConfigure)
        
        # Button to read Diabetologia
        self.x2, self.y2 = 100, 150
        self.b2 = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.openMonov)
        self.fb2=self.can.create_window(self.x2, self.y2, window=self.b2)
        self.pack()
        
        # Button2 to open2 Oncology
        self.x4, self.y4 = 100, 200
        self.b4 = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.openUrinalOne)
        self.fb4=self.can.create_window(self.x4, self.y4, window=self.b4)
        self.pack()
        
        # Button3 to open3 Ophtalmology
        self.x6, self.y6 = 100, 250
        self.b6 = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.openUrinalSecond)
        self.fb6=self.can.create_window(self.x6, self.y6, window=self.b6)
        self.pack()
        
        # Button4 to open4 Dentist
        self.x8, self.y8 = 100, 300
        self.b8 = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.openUrin24h)
        self.fb8=self.can.create_window(self.x8, self.y8, window=self.b8)
        self.pack()
        
        # Button5 to open5 Stomatherapy
        self.x10, self.y10 = 100, 350
        self.b10 = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.openUrineBb)
        self.fb10=self.can.create_window(self.x10, self.y10, window=self.b10)
        self.pack()
        
        # Button6 to open6 Aromatherapy
        self.x12, self.y12 = 100, 400
        self.b12 = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.openUrinPicOv)
        self.fb12=self.can.create_window(self.x12, self.y12, window=self.b12)
        self.pack()
        
        # Button7 to open7 Physiotherapy
        self.x12, self.y12 = 100, 450
        self.b12 = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.openHemoc)
        self.fb12=self.can.create_window(self.x12, self.y12, window=self.b12)
        self.pack()
        
        # Button8 to open8 Ergotherapy
        self.x14, self.y14 = 100, 500
        self.b14 = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.openFrottis)
        self.fb14=self.can.create_window(self.x14, self.y14, window=self.b14)
        self.pack()
        
        # Button9 to open9 Podology
        self.x16, self.y16 = 100, 550
        self.b16 = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.openHelico)
        self.fb16=self.can.create_window(self.x16, self.y16, window=self.b16)
        self.pack()

        # Button9 to open9 Podology
        self.x17, self.y17 = 100, 600
        self.b17 = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.openExpecto)
        self.fb17=self.can.create_window(self.x17, self.y17, window=self.b17)
        self.pack()

        # Button9 to open9 Podology
        self.x18, self.y18 = 100, 650
        self.b18 = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.openCopro)
        self.fb18=self.can.create_window(self.x18, self.y18, window=self.b18)
        self.pack()

        # Button9 to open9 Podology
        self.x19, self.y19 = 100, 700
        self.b19 = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.openScotchTest)
        self.fb19=self.can.create_window(self.x19, self.y19, window=self.b19)



        self.x20, self.y20 = 500, 150
        self.b20 = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.openMonov)
        self.fb20=self.can.create_window(self.x20, self.y20, window=self.b20)
        self.pack()
        

        self.x21, self.y21 = 500, 200
        self.b21 = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue21', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.openUrinalOne)
        self.fb21=self.can.create_window(self.x21, self.y21, window=self.b21)
        self.pack()
        

        self.x22, self.y22 = 500, 250
        self.b22 = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.openUrinalSecond)
        self.fb22=self.can.create_window(self.x22, self.y22, window=self.b22)
        self.pack()
        

        self.x23, self.y23 = 500, 300
        self.b23 = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.openUrin24h)
        self.fb23=self.can.create_window(self.x23, self.y23, window=self.b23)
        self.pack()
        

        self.x24, self.y24 = 500, 350
        self.b24 = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.openUrineBb)
        self.fb24=self.can.create_window(self.x24, self.y24, window=self.b24)
        self.pack()
        

        self.x25, self.y25 = 500, 400
        self.b25 = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.openUrinPicOv)
        self.fb25=self.can.create_window(self.x25, self.y25, window=self.b25)
        self.pack()
        

        self.x26, self.y26 = 500, 450
        self.b26 = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.openHemoc)
        self.fb26=self.can.create_window(self.x26, self.y26, window=self.b26)
        self.pack()
        

        self.x27, self.y27 = 500, 500
        self.b27 = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.openFrottis)
        self.fb27=self.can.create_window(self.x27, self.y27, window=self.b27)
        self.pack()
        

        self.x28, self.y28 = 500, 550
        self.b28 = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.openHelico)
        self.fb28=self.can.create_window(self.x28, self.y28, window=self.b28)
        self.pack()


        self.x29, self.y29 = 500, 600
        self.b29 = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.openExpecto)
        self.fb29=self.can.create_window(self.x29, self.y29, window=self.b29)
        self.pack()


        self.x30, self.y30 = 500, 650
        self.b30 = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.openCopro)
        self.fb30=self.can.create_window(self.x30, self.y30, window=self.b30)
        self.pack()


        self.x31, self.y31 = 500, 700
        self.b31 = tk.Button(self.can, width=10, bd=3, font=16, bg='RoyalBlue4', fg='gold',
            activebackground='pale turquoise', text="open",
            highlightbackground='DodgerBlue2', command=self.openScotchTest)
        self.fb31=self.can.create_window(self.x31, self.y31, window=self.b31)
        self.pack()

    # Méthode pour reconfigurer la scrollbar à chaque fois
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.can.configure(scrollregion=self.can.bbox(ALL))

    def confRec(self):
        self.MsgBox2msg = messagebox.showinfo("Warning", "File 'VMED'"
            "was not created. No Medical Visit has been checked !")

    def openMonov(self):
        try:
            becall = platform.system()
            print(platform.system())
            if os.path.getsize('./manual/monovet.pdf'):
                print("+ File 'monovet.pdf' exist (read)!")
                if becall == 'Linux':
                    os.system('gio open "./manual/monovet.pdf"') # Linux
                elif becall =='Darwin':
                    subprocess.call('open', './manual/monovet.pdf' ) # Mac
                else:
                    os.startfile('./manual/monovet.pdf') # Windows
        except FileNotFoundError as outputcom:
                print("+ Sorry, file 'monovet.pdf' not exist !", outputcom)
                self.confRec()

    def openUrinalOne(self):
        try:
            becall = platform.system()
            print(platform.system())
            if os.path.getsize('./manual/premierjet.pdf'):
                print("+ File 'premierjet.pdf' exist (read)!")
                if becall == 'Linux':
                    os.system('gio open "./manual/premierjet.pdf"') # Linux
                elif becall =='Darwin':
                    subprocess.call('open', './manual/premierjet.pdf' ) # Mac
                else:
                    os.startfile('./manual/premierjet.pdf') # Windows
        except FileNotFoundError as outputcom:
                print("+ Sorry, file 'premierjet.pdf' not exist !", outputcom)
                self.confRec()

    def openUrinalSecond(self):
        try:
            becall = platform.system()
            print(platform.system())
            if os.path.getsize('./manual/secondjet.pdf'):
                print("+ File 'secondjet.pdf' exist (read)!")
                if becall == 'Linux':
                    os.system('gio open "./manual/secondjet.pdf"') # Linux
                elif becall =='Darwin':
                    subprocess.call('open', './manual/secondjet.pdf' ) # Mac
                else:
                    os.startfile('./manual/secondjet.pdf') # Windows
        except FileNotFoundError as outputcom2:
                print("+ Sorry, file 'secondjet.pdf' not exist !", outputcom2)
                self.confRec()

    def openUrin24h(self):
        try:
            becall = platform.system()
            print(platform.system())
            if os.path.getsize('./manual/urine24h.pdf'):
                print("+ File 'urine24h.pdf' exist (read)!")
                if becall == 'Linux':
                    os.system('gio open "./manual/urine24h.pdf"') # Linux
                elif becall =='Darwin':
                    subprocess.call('open', './manual/urine24h.pdf' ) # Mac
                else:
                    os.startfile('./manual/urine24h.pdf') # Windows
        except FileNotFoundError as outputcom3:
                print("+ Sorry, file 'urine24h.pdf' not exist !", outputcom3)
                self.confRec()

    def openUrineBb(self):
        try:
            becall = platform.system()
            print(platform.system())
            if os.path.getsize('./manual/urinebaby.pdf'):
                print("+ File 'urinebaby.pdf' exist (read)!")
                if becall == 'Linux':
                    os.system('gio open "./manual/urinebaby.pdf"') # Linux
                elif becall =='Darwin':
                    subprocess.call('open', './manual/urinebaby.pdf' ) # Mac
                else:
                    os.startfile('./manual/urinebaby.pdf') # Windows
        except FileNotFoundError as outputcom4:
                print("+ Sorry, file 'urinebaby.pdf' not exist !", outputcom4)
                self.confRec()

    def openUrinPicOv(self):
        try:
            becall = platform.system()
            print(platform.system())
            if os.path.getsize('./manual/urinepicovulr.pdf'):
                print("+ File 'urinepicovulr.pdf' exist (read)!")
                if becall == 'Linux':
                    os.system('gio open "./manual/urinepicovulr.pdf"') # Linux
                elif becall =='Darwin':
                    subprocess.call('open', './manual/urinepicovulr.pdf' ) # Mac
                else:
                    os.startfile('./manual/urinepicovulr.pdf') # Windows
        except FileNotFoundError as outputcom5:
                print("+ Sorry, file 'urinepicovulr.pdf' not exist !", outputcom5)
                self.confRec()

    def openHemoc(self):
        try:
            becall = platform.system()
            print(platform.system())
            if os.path.getsize('./manual/hemoc.pdf'):
                print("+ File 'hemoc.pdf' exist (read)!")
                if becall == 'Linux':
                    os.system('gio open "./manual/hemoc.pdf"') # Linux
                elif becall =='Darwin':
                    subprocess.call('open', './manual/hemoc.pdf' ) # Mac
                else:
                    os.startfile('./manual/hemoc.pdf') # Windows
        except FileNotFoundError as outputcom6:
                print("+ Sorry, file 'hemoc.pdf' not exist !", outputcom6)
                self.confRec()

    def openFrottis(self):
        try:
            becall = platform.system()
            print(platform.system())
            if os.path.getsize('./manual/frottis.pdf'):
                print("+ File 'frottis.pdf' exist (read)!")
                if becall == 'Linux':
                    os.system('gio open "./manual/frottis.pdf"') # Linux
                elif becall =='Darwin':
                    subprocess.call('open', './manual/frottis.pdf' ) # Mac
                else:
                    os.startfile('./manual/frottis.pdf') # Windows
        except FileNotFoundError as outputcom7:
                print("+ Sorry, file 'frottis.pdf' not exist !", outputcom7)
                self.confRec()

    def openHelico(self):
        try:
            becall = platform.system()
            print(platform.system())
            if os.path.getsize('./manual/helicobacter.pdf'):
                print("+ File 'helicobacter.pdf' exist (read)!")
                if becall == 'Linux':
                    os.system('gio open "./manual/helicobacter.pdf"') # Linux
                elif becall =='Darwin':
                    subprocess.call('open', './manual/helicobacter.pdf' ) # Mac
                else:
                    os.startfile('./manual/helicobacter.pdf') # Windows
        except FileNotFoundError as outputcom8:
                print("+ Sorry, file 'helicobacter.pdf' not exist !", outputcom8)
                self.confRec()

    def openExpecto(self):
        try:
            becall = platform.system()
            print(platform.system())
            if os.path.getsize('./manual/expecto.pdf'):
                print("+ File 'expecto.pdf' exist (read)!")
                if becall == 'Linux':
                    os.system('gio open "./manual/expecto.pdf"') # Linux
                elif becall =='Darwin':
                    subprocess.call('open', './manual/expecto.pdf' ) # Mac
                else:
                    os.startfile('./manual/expecto.pdf') # Windows
        except FileNotFoundError as outputcom9:
                print("+ Sorry, file 'expecto.pdf' not exist !", outputcom9)
                self.confRec()

    def openCopro(self):
        try:
            becall = platform.system()
            print(platform.system())
            if os.path.getsize('./manual/copro.pdf'):
                print("+ File 'copro.pdf' exist (read)!")
                if becall == 'Linux':
                    os.system('gio open "./manual/copro.pdf"') # Linux
                elif becall =='Darwin':
                    subprocess.call('open', './manual/copro.pdf' ) # Mac
                else:
                    os.startfile('./manual/copro.pdf') # Windows
        except FileNotFoundError as outputcom10:
                print("+ Sorry, file 'copro.pdf' not exist !", outputcom10)
                self.confRec()

    def openScotchTest(self):
        try:
            becall = platform.system()
            print(platform.system())
            if os.path.getsize('./manual/scotchtest.pdf'):
                print("+ File 'scotchtest.pdf' exist (read)!")
                if becall == 'Linux':
                    os.system('gio open "./manual/scotchtest.pdf"') # Linux
                elif becall =='Darwin':
                    subprocess.call('open', './manual/scotchtest.pdf' ) # Mac
                else:
                    os.startfile('./manual/scotchtest.pdf') # Windows
        except FileNotFoundError as outputcom11:
                print("+ Sorry, file 'scotchtest.pdf' not exist !", outputcom11)
                self.confRec()

if __name__=='__main__':
    app = Application()
    app.mainloop()