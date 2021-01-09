#!/usr/bin/python3
# -*-coding:utf-8-*-


from tkinter import *
import tkinter
from tkinter import messagebox
import os
import subprocess
import platform
import time


def callLabo23(self):
    """
        To display labo into Canvas
    """
    self.can.delete(ALL)
    self.can.configure(bg='DodgerBlue2')

    self.x1, self.y1 = 540, 45
    self.labelname = Label(self.can, text="Labo check",
        font=('helvetica', 18, 'bold'), width=10,
        height=2, bg='DodgerBlue2', fg='white')
    self.labelname = self.can.create_window(self.x1, self.y1,
        window = self.labelname)

    with open('./newpatient/entryfile23.txt', 'r') as filename:
        line1 = filename.readline()

    self.x2, self.y2 = 720, 45
    entrytext = StringVar()
    self.entryname = Entry(self.can, textvariable=entrytext, width=20)
    entrytext.set(line1[:-1])
    self.entryname = self.can.create_window(self.x2, self.y2,
        window = self.entryname)

    self.x3, self.y3 = 625, 100
    self.labelresult = Label(self.can, text='--- Neuroleptiques ---',
        font="Times 14 bold", width=135,
        height=1, bg='RoyalBlue3', fg='white')
    self.labelresult = self.can.create_window(self.x3, self.y3,
        window = self.labelresult)

    def recordTofile():
        MsgBox = messagebox.askyesno('Record', 'Results will be saved into Care and Monitoring, ok ?')
        if MsgBox == 1:
            print("Ok, data saved")
            recordOption()
            confRec()
            #self.can.delete(ALL) # ---
            self.showPatients()
        else:
            messagebox.showinfo('Return', 'Ok, nothing changed')

    def recordOption():
        print("Date : " + time.strftime("%d/%m/%Y"))
        print("Nom du patient : ", entrytext.get())
        with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                file.write("----------------------------------------------------------\n")
                file.write("Date : ")
                file.write(time.strftime("%d/%m/%Y")+ '\n')
                file.write("Patient name : ")
                file.write(entrytext.get() + '\n')
                file2.write("\n---------------------------------------------------------\n")
                file2.write("Date : ")
                file2.write(time.strftime("%d/%m/%Y")+ '\n')
                file2.write("Patient name : ")
                file2.write(entrytext.get() + '\n')

        print(CheckVar1.get())
        if CheckVar1.get()==1:
            print("+ Abilify was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Abilify : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Abilify : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Abilify ok, nothing to do")
            
        print(CheckVar2.get())
        if CheckVar2.get()==1:
            print("+ Clopixol was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Clopixol : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Clopixol : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Clopixol ok, nothing to do")

        print(CheckVar3.get())
        if CheckVar3.get()==1:
            print("+ Clozapine was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Clozapine : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Clozapine : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Clozapine ok, nothing to do")
            
        print(CheckVar4.get())
        if CheckVar4.get()==1:
            print("+ Dogmatil was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Dogmatil : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Dogmatil : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Dogmatil ok, nothing to do")

        print(CheckVar5.get())
        if CheckVar5.get()==1:
            print("+ Entumine was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Entumine : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Entumine : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Entumine ok, nothing to do")

        print(CheckVar6.get())
        if CheckVar6.get()==1:
            print("+ Fluanxol was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Fluanxol : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Fluanxol : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Fluanxol ok, nothing to do")

        print(CheckVar7.get())
        if CheckVar7.get()==1:
            print("+ Haldol was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Haldol : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Haldol : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Haldol ok, nothing to do")

        print(CheckVar8.get())
        if CheckVar8.get()==1:
            print("+ Invega was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Invega : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Invega : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Invega ok, nothing to do")

        print(CheckVar9.get())
        if CheckVar9.get()==1:
            print("+ Nozinan was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Nozinan : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Nozinan : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Nozinan ok, nothing to do")

        print(CheckVar10.get())
        if CheckVar10.get()==1:
            print("+ Prazine was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Prazine : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Prazine : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Prazine ok, nothing to do")

        print(CheckVar12.get())
        if CheckVar12.get()==1:
            print("+ Quetiapine was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Quetiapine : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Quetiapine : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Quetiapine ok, nothing to do")

        print(CheckVar13.get())
        if CheckVar13.get()==1:
            print("+ Risperdal was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Risperdal : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Risperdal : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Risperdal ok, nothing to do")

        print(CheckVar14.get())
        if CheckVar14.get()==1:
            print("+ Serdolect was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Serdolect : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Serdolect : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Serdolect ok, nothing to do")

        print(CheckVar15.get())
        if CheckVar15.get()==1:
            print("+ Solian was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Solian : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Solian : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Solian ok, nothing to do")

        print(CheckVar16.get())
        if CheckVar16.get()==1:
            print("+ Tiapridal was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Tiapridal : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Tiapridal : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Tiapridal ok, nothing to do")

        print(CheckVar17.get())
        if CheckVar17.get()==1:
            print("+ Truxal was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Truxal : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Truxal : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Truxal ok, nothing to do")

        print(CheckVar18.get())
        if CheckVar18.get()==1:
            print("+ Zyprexa was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Zyprexa : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Zyprexa : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Zyprexa ok, nothing to do")

        print(CheckVar19.get())
        if CheckVar19.get()==1:
            print("+ Briviact was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Briviact : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Briviact : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Briviact ok, nothing to do")

        print(CheckVar20.get())
        if CheckVar20.get()==1:
            print("+ Carbamazepine was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Carbamazepine : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Carbamazepine : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Carbamazepine ok, nothing to do")

        print(CheckVar21.get())
        if CheckVar21.get()==1:
            print("+ Depakine was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Depakine : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Depakine : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Depakine ok, nothing to do")

        print(CheckVar22.get())
        if CheckVar22.get()==1:
            print("+ Ethosuximide was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Ethosuximide : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Ethosuximide : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Ethosuximide ok, nothing to do")

        print(CheckVar23.get())
        if CheckVar23.get()==1:
            print("+ Fycompa was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Fycompa : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Fycompa : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Fycompa ok, nothing to do")

        print(CheckVar24.get())
        if CheckVar24.get()==1:
            print("+ Gabitril was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Gabitril : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Gabitril : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Gabitril ok, nothing to do")

        print(CheckVar25.get())
        if CheckVar25.get()==1:
            print("+ Inovelon was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Inovelon : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Inovelon : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Inovelon ok, nothing to do")

        print(CheckVar26.get())
        if CheckVar26.get()==1:
            print("+ Keppra was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Keppra : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Keppra : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Keppra ok, nothing to do")

        print(CheckVar27.get())
        if CheckVar27.get()==1:
            print("+ Lamictal was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Lamictal : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Lamictal : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Lamictal ok, nothing to do")

        print(CheckVar28.get())
        if CheckVar28.get()==1:
            print("+ Lyrica was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Lyrica : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Lyrica : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Lyrica ok, nothing to do")

        print(CheckVar29.get())
        if CheckVar29.get()==1:
            print("+ Myzoline was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Myzoline : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Myzoline : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Myzoline ok, nothing to do")

        print(CheckVar30.get())
        if CheckVar30.get()==1:
            print("+ Neurontin was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Neurontin : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Neurontin : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Neurontin ok, nothing to do")

        print(CheckVar31.get())
        if CheckVar31.get()==1:
            print("+ Phenobarbital was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Phenobarbital : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Phenobarbital : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Phenobarbital ok, nothing to do")

        print(CheckVar32.get())
        if CheckVar32.get()==1:
            print("+ Phenytoine was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Phenytoine : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Phenytoine : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Phenytoine ok, nothing to do")

        print(CheckVar33.get())
        if CheckVar33.get()==1:
            print("+ Sabril was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Sabril : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Sabril : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Sabril ok, nothing to do")

        print(CheckVar34.get())
        if CheckVar34.get()==1:
            print("+ Taloxa was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Taloxa : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Taloxa : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Taloxa ok, nothing to do")

        print(CheckVar35.get())
        if CheckVar35.get()==1:
            print("+ Topamax was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Topamax : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Topamax : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Topamax ok, nothing to do")

        print(CheckVar36.get())
        if CheckVar36.get()==1:
            print("+ Trileptal was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Trileptal : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Trileptal : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Trileptal ok, nothing to do")

        print(CheckVar37.get())
        if CheckVar37.get()==1:
            print("+ Trobalt was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Trobalt : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Trobalt : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Trobalt ok, nothing to do")

        print(CheckVar38.get())
        if CheckVar38.get()==1:
            print("+ Vimpat was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Vimpat : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Vimpat : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Vimpat ok, nothing to do")

        print(CheckVar39.get())
        if CheckVar39.get()==1:
            print("+ Zonegran was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Zonegran : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Zonegran : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Zonegran ok, nothing to do")

        print(CheckVar40.get())
        if CheckVar40.get()==1:
            print("+ Anafranil was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Anafranil : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Anafranil : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Anafranil ok, nothing to do")

        print(CheckVar41.get())
        if CheckVar41.get()==1:
            print("+ Citalopram was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Citalopram : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Citalopram : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Citalopram ok, nothing to do")

        print(CheckVar42.get())
        if CheckVar42.get()==1:
            print("+ Cipralex was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Cipralex : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Cipralex : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Cipralex ok, nothing to do")

        print(CheckVar43.get())
        if CheckVar43.get()==1:
            print("+ Cymbalta was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Cymbalta : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Cymbalta : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Cymbalta ok, nothing to do")

        print(CheckVar44.get())
        if CheckVar44.get()==1:
            print("+ Deroxat was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Deroxat : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Deroxat : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Deroxat ok, nothing to do")

        print(CheckVar45.get())
        if CheckVar45.get()==1:
            print("+ Effexor was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Effexor : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Effexor : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Effexor ok, nothing to do")

        print(CheckVar46.get())
        if CheckVar46.get()==1:
            print("+ Floxifral was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Floxifral : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Floxifral : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Floxifral ok, nothing to do")

        print(CheckVar47.get())
        if CheckVar47.get()==1:
            print("+ Fluctine was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Fluctine : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Fluctine : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Fluctine ok, nothing to do")

        print(CheckVar48.get())
        if CheckVar48.get()==1:
            print("+ Ludiomil was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Ludiomil : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Ludiomil : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Ludiomil ok, nothing to do")

        print(CheckVar49.get())
        if CheckVar49.get()==1:
            print("+ Remeron was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Remeron : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Remeron : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Remeron ok, nothing to do")

        print(CheckVar50.get())
        if CheckVar50.get()==1:
            print("+ Saroten was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Saroten : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Saroten : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Saroten ok, nothing to do")

        print(CheckVar51.get())
        if CheckVar51.get()==1:
            print("+ Sertraline was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Sertraline : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Sertraline : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Sertraline ok, nothing to do")

        print(CheckVar52.get())
        if CheckVar52.get()==1:
            print("+ Surmontil was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Surmontil : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Surmontil : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Surmontil ok, nothing to do")

        print(CheckVar53.get())
        if CheckVar53.get()==1:
            print("+ Wellbutrin was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Wellbutrin : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Wellbutrin : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Wellbutrin ok, nothing to do")

        print(CheckVar54.get())
        if CheckVar54.get()==1:
            print("+ Lithium was checked !")
            with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
                with open('./labo/doc_labo/result23.txt', 'a+') as file2:
                    file.write("# Lithium : " + time.strftime("%d/%m/%Y") + " checked\n")
                    file2.write("# Lithium : " + time.strftime("%d/%m/%Y") + " checked\n")
        else:
            print("+ Lithium ok, nothing to do")

        with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as endfile:
            with open('./labo/doc_labo/result23.txt', 'a+') as endfile2:
                endfile.write("---------------------------------------------------------\n\n")
                endfile2.write("---------------------------------------------------------\n\n")

    def confRec():
        messagebox.showinfo("Confirmation", "Record confirmed and finished !")

    def comburTips():
        self.master.wm_attributes('-alpha', 0.8)
        self.master.update()
        subprocess.run('./labo/combtest23.py', check=True)
        self.master.wm_attributes('-alpha', 1.0)
        self.master.update()

    def awayOut():
        try:
            self.can.delete(ALL)
            self.showPatients()
        except (OSError, ValueError) as p_out:
            print("Error from labo to way out", p_out)

    self.x4, self.y4 = 134, 125
    CheckVar1 = IntVar()
    self.C1 = Checkbutton(self.can, text="Abilify (aripiprazol)", fg='navy',
        bg='cyan', variable=CheckVar1,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C1 = self.can.create_window(self.x4, self.y4,
        window = self.C1)

    self.x5, self.y5 = 134, 148
    CheckVar2 = IntVar()
    self.C2 = Checkbutton(self.can, text="Clopixol (zuclopenthixol)", fg='navy',
        bg='cyan', variable=CheckVar2,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C2 = self.can.create_window(self.x5, self.y5,
        window = self.C2)

    self.x6, self.y6 = 134, 171
    CheckVar3 = IntVar()
    self.C3 = Checkbutton(self.can, text="Clozapine (clopin, leponex)", fg='navy',
        bg='cyan', variable=CheckVar3,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C3 = self.can.create_window(self.x6, self.y6,
        window = self.C3)

    self.x7, self.y7 = 134, 194
    CheckVar4 = IntVar()
    self.C4 = Checkbutton(self.can, text="Dogmatil (sulprid)", fg='navy',
        bg='cyan', variable=CheckVar4,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C4 = self.can.create_window(self.x7, self.y7,
        window = self.C4)

    self.x8, self.y8 = 134, 217
    CheckVar5 = IntVar()
    self.C5 = Checkbutton(self.can, text="Entumine (clotiapin)", fg='navy',
        bg='cyan', variable=CheckVar5,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C5 = self.can.create_window(self.x8, self.y8,
        window = self.C5)

    self.x9, self.y9 = 461, 125
    CheckVar6 = IntVar()
    self.C6 = Checkbutton(self.can, text="Fluanxol (flupentixol)", fg='navy',
        bg='cyan', variable=CheckVar6,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C6 = self.can.create_window(self.x9, self.y9,
        window = self.C6)

    self.x10, self.y10 = 461, 148
    CheckVar7 = IntVar()
    self.C7 = Checkbutton(self.can, text="Haldol (haloperidol)", fg='navy', 
        bg='cyan', variable=CheckVar7, 
        onvalue=1, offvalue=0, height=1, 
        width=26, anchor="w")
    self.C7 = self.can.create_window(self.x10, self.y10,
        window = self.C7)

    self.x11, self.y11 = 461, 171
    CheckVar8 = IntVar()
    self.C8 = Checkbutton(self.can, text="Invega (paliperidon)", fg='navy', 
        bg='cyan', variable=CheckVar8, 
        onvalue=1, offvalue=0, height=1, 
        width=26, anchor="w")
    self.C8 = self.can.create_window(self.x11, self.y11,
        window = self.C8)

    self.x12, self.y12 = 461, 194
    CheckVar9 = IntVar()
    self.C9 = Checkbutton(self.can, text="Nozinan (levomepromazin)", fg='navy', 
        bg='cyan', variable=CheckVar9, 
        onvalue=1, offvalue=0, height=1, 
        width=26, anchor="w")
    self.C9 = self.can.create_window(self.x12, self.y12,
        window = self.C9)

    self.x13, self.y13 = 461, 217
    CheckVar10 = IntVar()
    self.C10 = Checkbutton(self.can, text="Prazine (promazin)", fg='navy', 
        bg='cyan', variable=CheckVar10, 
        onvalue=1, offvalue=0, height=1, 
        width=26, anchor="w")
    self.C10 = self.can.create_window(self.x13, self.y13,
        window = self.C10)

    self.x14, self.y14 = 790, 125
    CheckVar12 = IntVar()
    self.C12 = Checkbutton(self.can, text="Quetiapine (seroquel, sequase)", fg='navy',
        bg='cyan', variable=CheckVar12,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C12 = self.can.create_window(self.x14, self.y14,
        window = self.C12)

    self.x15, self.y15 = 790, 148
    CheckVar13 = IntVar()
    self.C13 = Checkbutton(self.can, text="Risperdal (risperidon)", fg='navy', 
        bg='cyan', variable=CheckVar13, 
        onvalue=1, offvalue=0, height=1, 
        width=26, anchor="w")
    self.C13 = self.can.create_window(self.x15, self.y15,
        window = self.C13)

    self.x16, self.y16 = 790, 171
    CheckVar14 = IntVar()
    self.C14 = Checkbutton(self.can, text="Serdolect (sertindol)", fg='navy', 
        bg='cyan', variable=CheckVar14, 
        onvalue=1, offvalue=0, height=1, 
        width=26, anchor="w")
    self.C14 = self.can.create_window(self.x16, self.y16,
        window = self.C14)

    self.x17, self.y17 = 790, 194
    CheckVar15 = IntVar()
    self.C15 = Checkbutton(self.can, text="Solian (amisulprid)", fg='navy', 
        bg='cyan', variable=CheckVar15, 
        onvalue=1, offvalue=0, height=1, 
        width=26, anchor="w")
    self.C15 = self.can.create_window(self.x17, self.y17,
        window = self.C15)

    self.x18, self.y18 = 790, 217
    CheckVar16 = IntVar()
    self.C16 = Checkbutton(self.can, text="Tiapridal (tiaprid)", fg='navy', 
        bg='cyan', variable=CheckVar16, 
        onvalue=1, offvalue=0, height=1, 
        width=26, anchor="w")
    self.C16 = self.can.create_window(self.x18, self.y18,
        window = self.C16)

    self.x19, self.y19 = 1117, 125
    CheckVar17 = IntVar()
    self.C17 = Checkbutton(self.can, text="Truxal (chlorprothixen)", fg='navy',
        bg='cyan', variable=CheckVar17,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C17 = self.can.create_window(self.x19, self.y19,
        window = self.C17)

    self.x20, self.y20 = 1117, 148
    CheckVar18 = IntVar()
    self.C18 = Checkbutton(self.can, text="Zyprexa (olanzapin)", fg='navy',
        bg='cyan', variable=CheckVar18,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C18 = self.can.create_window(self.x20, self.y20,
        window = self.C18)

    # MAE
    self.x21, self.y21 = 625, 243
    self.labelresult2 = Label(self.can, text='--- Médicaments anti-épileptiques ---',
        font="Times 14 bold", width=135,
        height=1, bg='RoyalBlue3', fg='white')
    self.labelresult2 = self.can.create_window(self.x21, self.y21,
        window = self.labelresult2)

    #separator = Label(self.can, height=5, bd=2, relief=SUNKEN)
    #separator.grid(sticky='ns', row=2, column=1)

    self.x22, self.y22 = 134, 268
    CheckVar19 = IntVar()
    self.C19 = Checkbutton(self.can, text="Briviact (brivaracetam)", fg='navy',
        bg='cyan', variable=CheckVar19,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C19 = self.can.create_window(self.x22, self.y22,
        window = self.C19)

    self.x23, self.y23 = 134, 291
    CheckVar20 = IntVar()
    self.C20 = Checkbutton(self.can, text="Carbamazepine (tegretol)", fg='navy',
        bg='cyan', variable=CheckVar20,
        onvalue=1, offvalue=0, height=1,
        width=26, anchor="w")
    self.C20 = self.can.create_window(self.x23, self.y23,
        window = self.C20)
    
    self.x24, self.y24 = 134, 314
    CheckVar21 = IntVar()
    self.C21 = Checkbutton(self.can, text="Depakine (valproate)", fg='navy',
        bg='cyan', variable=CheckVar21, 
        onvalue=1, offvalue=0, height=1, 
        width=26, anchor="w")
    self.C21 = self.can.create_window(self.x24, self.y24,
        window = self.C21)

    self.x25, self.y25 = 134, 337
    CheckVar22 = IntVar()
    self.C22 = Checkbutton(self.can, text="Ethosuximide (petinimid)", fg='navy',
        bg='cyan', variable=CheckVar22, 
        onvalue=1, offvalue=0, height=1, 
        width=26, anchor="w")
    self.C22 = self.can.create_window(self.x25, self.y25,
        window = self.C22)

    self.x26, self.y26 = 134, 360
    CheckVar23 = IntVar()
    self.C23 = Checkbutton(self.can, text="Fycompa (perampanel)", fg='navy',
        bg='cyan', variable=CheckVar23, 
        onvalue=1, offvalue=0, height=1, 
        width=26, anchor="w")
    self.C23 = self.can.create_window(self.x26, self.y26,
        window = self.C23)

    self.x27, self.y27 = 134, 383
    CheckVar24 = IntVar()
    self.C24 = Checkbutton(self.can, text="Gabitril (tiagabine)", fg='navy',
        bg='cyan', variable=CheckVar24, 
        onvalue=1, offvalue=0, height=1, 
        width=26, anchor="w")
    self.C24 = self.can.create_window(self.x27, self.y27,
        window = self.C24)
    
    self.x28, self.y28 = 461, 268
    CheckVar25 = IntVar()
    self.C25 = Checkbutton(self.can, text="Inovelon (rufinamid)", fg='navy',
        bg='cyan', variable=CheckVar25, 
        onvalue=1, offvalue=0, height=1, 
        width=26, anchor="w")
    self.C25 = self.can.create_window(self.x28, self.y28,
        window = self.C25)

    self.x29, self.y29 = 461, 291
    CheckVar26 = IntVar()
    self.C26 = Checkbutton(self.can, text="Keppra (levetiracetam)", fg='navy',
        bg='cyan', variable=CheckVar26, 
        onvalue=1, offvalue=0, height=1, 
        width=26, anchor="w")
    self.C26 = self.can.create_window(self.x29, self.y29,
        window = self.C26)

    self.x30, self.y30 = 461, 314
    CheckVar27 = IntVar()
    self.C27 = Checkbutton(self.can, text="Lamictal (lamotrigine)", fg='navy',
        bg='cyan', variable=CheckVar27, 
        onvalue=1, offvalue=0, height=1, 
        width=26, anchor="w")
    self.C27 = self.can.create_window(self.x30, self.y30,
        window = self.C27)

    self.x31, self.y31 = 461, 337
    CheckVar28 = IntVar()
    self.C28 = Checkbutton(self.can, text="Lyrica (pregabalin)", fg='navy', 
        bg='cyan', variable=CheckVar28, 
        onvalue=1, offvalue=0, height=1, 
        width=26, anchor="w")
    self.C28 = self.can.create_window(self.x31, self.y31,
        window = self.C28)

    self.x32, self.y32 = 461, 360
    CheckVar29 = IntVar()
    self.C29 = Checkbutton(self.can, text="Myzoline (primidon)", fg='navy', 
        bg='cyan', variable=CheckVar29, 
        onvalue=1, offvalue=0, height=1, 
        width=26, anchor="w")
    self.C29 = self.can.create_window(self.x32, self.y32,
        window = self.C29)

    self.x33, self.y33 = 461, 383
    CheckVar30 = IntVar()
    self.C30 = Checkbutton(self.can, text="Neurontin (gabapentin)", fg='navy', 
        bg='cyan', variable=CheckVar30, 
        onvalue=1, offvalue=0, height=1, 
        width=26, anchor="w")
    self.C30 = self.can.create_window(self.x33, self.y33,
        window = self.C30)

    self.x34, self.y34 = 790, 268
    CheckVar31 = IntVar()
    self.C31 = Checkbutton(self.can, text="Phenobarbital (aphenylbarbit)", fg='navy', 
        bg='cyan', variable=CheckVar31, 
        onvalue=1, offvalue=0, height=1, 
        width=26, anchor="w")
    self.C31 = self.can.create_window(self.x34, self.y34,
        window = self.C31)

    self.x35, self.y35 = 790, 291
    CheckVar32 = IntVar()
    self.C32 = Checkbutton(self.can, text="Phenytoïne", fg='navy', 
        bg='cyan', variable=CheckVar32, 
        onvalue=1, offvalue=0, height=1, 
        width=26, anchor="w")
    self.C32 = self.can.create_window(self.x35, self.y35,
        window = self.C32)

    self.x36, self.y36 = 790, 314
    CheckVar33 = IntVar()
    self.C33 = Checkbutton(self.can, text="Sabril (vigabatrin)", fg='navy', 
        bg='cyan', variable=CheckVar33, 
        onvalue=1, offvalue=0, height=1, 
        width=26, anchor="w")
    self.C33 = self.can.create_window(self.x36, self.y36,
        window = self.C33)

    self.x37, self.y37 = 790, 337
    CheckVar34 = IntVar()
    self.C34 = Checkbutton(self.can, text="Taloxa (felbamate)", fg='navy', 
        bg='cyan', variable=CheckVar34, 
        onvalue=1, offvalue=0, height=1, 
        width=26, anchor="w")
    self.C34 = self.can.create_window(self.x37, self.y37,
        window = self.C34)

    self.x38, self.y38 = 790, 360
    CheckVar35 = IntVar()
    self.C35 = Checkbutton(self.can, text="Topamax (topiramate)", fg='navy', 
        bg='cyan', variable=CheckVar35, 
        onvalue=1, offvalue=0, height=1, 
        width=26, anchor="w")
    self.C35 = self.can.create_window(self.x38, self.y38,
        window = self.C35)

    self.x39, self.y39 = 790, 383
    CheckVar36 = IntVar()
    self.C36 = Checkbutton(self.can, text="Trileptal (oxcarbazepin)", fg='navy', 
        bg='cyan', variable=CheckVar36, 
        onvalue=1, offvalue=0, height=1, 
        width=26, anchor="w")
    self.C36 = self.can.create_window(self.x39, self.y39,
        window = self.C36)

    self.x40, self.y40 = 1117, 268
    CheckVar37 = IntVar()
    self.C37 = Checkbutton(self.can, text="Trobalt (retigabin)", fg='navy', 
        bg='cyan', variable=CheckVar37, 
        onvalue=1, offvalue=0, height=1, 
        width=26, anchor="w")
    self.C37 = self.can.create_window(self.x40, self.y40,
        window = self.C37)

    self.x41, self.y41 = 1117, 291
    CheckVar38 = IntVar()
    self.C38 = Checkbutton(self.can, text="Vimpat (lacosamid)", fg='navy', 
        bg='cyan', variable=CheckVar38, 
        onvalue=1, offvalue=0, height=1, 
        width=26, anchor="w")
    self.C38 = self.can.create_window(self.x41, self.y41,
        window = self.C38)

    self.x42, self.y42 = 1117, 314
    CheckVar39 = IntVar()
    self.C39 = Checkbutton(self.can, text="Zonegran (zonisamid)", fg='navy', 
        bg='cyan', variable=CheckVar39, 
        onvalue=1, offvalue=0, height=1, 
        width=26, anchor="w")
    self.C39 = self.can.create_window(self.x42, self.y42,
        window = self.C39)

    # ATD
    self.x43, self.y43 = 625, 409
    self.labelresult3 = Label(self.can, text='--- Antidépresseurs ---',
        font="Times 14 bold", width=135,
        height=1, bg='RoyalBlue3', fg='white')
    self.labelresult3 = self.can.create_window(self.x43, self.y43,
        window = self.labelresult3)

    self.x44, self.y44 = 134, 434
    CheckVar40 = IntVar()
    self.C40 = Checkbutton(self.can, text="Anafrani (clomipramin)", fg='navy', 
        bg='cyan', variable=CheckVar40, 
        onvalue=1, offvalue=0, height=1, 
        width=26, anchor="w")
    self.C40 = self.can.create_window(self.x44, self.y44,
        window = self.C40)

    self.x45, self.y45 = 134, 457
    CheckVar41 = IntVar()
    self.C41 = Checkbutton(self.can, text="Citalopram", fg='navy', 
        bg='cyan', variable=CheckVar41, 
        onvalue=1, offvalue=0, height=1, 
        width=26, anchor="w")
    self.C41 = self.can.create_window(self.x45, self.y45,
        window = self.C41)

    self.x46, self.y46 = 134, 480
    CheckVar42 = IntVar()
    self.C42 = Checkbutton(self.can, text="Cipralex (escitalopram)", fg='navy', 
        bg='cyan', variable=CheckVar42, 
        onvalue=1, offvalue=0, height=1, 
        width=26, anchor="w")
    self.C42 = self.can.create_window(self.x46, self.y46,
        window = self.C42)

    self.x47, self.y47 = 134, 503
    CheckVar43 = IntVar()
    self.C43 = Checkbutton(self.can, text="Cymbalta (duloxetin)", fg='navy', 
        bg='cyan', variable=CheckVar43, 
        onvalue=1, offvalue=0, height=1, 
        width=26, anchor="w")
    self.C43 = self.can.create_window(self.x47, self.y47,
        window = self.C43)

    self.x48, self.y48 = 461, 434
    CheckVar44 = IntVar()
    self.C44 = Checkbutton(self.can, text="Deroxat (paroxetin)", fg='navy', 
        bg='cyan', variable=CheckVar44, 
        onvalue=1, offvalue=0, height=1, 
        width=26, anchor="w")
    self.C44 = self.can.create_window(self.x48, self.y48,
        window = self.C44)

    self.x49, self.y49 = 461, 457
    CheckVar45 = IntVar()
    self.C45 = Checkbutton(self.can, text="Effexor (venlafaxin)", fg='navy', 
        bg='cyan', variable=CheckVar45, 
        onvalue=1, offvalue=0, height=1, 
        width=26, anchor="w")
    self.C45 = self.can.create_window(self.x49, self.y49,
        window = self.C45)

    self.x50, self.y50 = 461, 480
    CheckVar46 = IntVar()
    self.C46 = Checkbutton(self.can, text="Floxifral (fluvoxamin)", fg='navy', 
        bg='cyan', variable=CheckVar46, 
        onvalue=1, offvalue=0, height=1, 
        width=26, anchor="w")
    self.C46 = self.can.create_window(self.x50, self.y50,
        window = self.C46)

    self.x51, self.y51 = 461, 503
    CheckVar47 = IntVar()
    self.C47 = Checkbutton(self.can, text="Fluctine (fluoxetin)", fg='navy', 
        bg='cyan', variable=CheckVar47, 
        onvalue=1, offvalue=0, height=1, 
        width=26, anchor="w")
    self.C47 = self.can.create_window(self.x51, self.y51,
        window = self.C47)

    self.x52, self.y52 = 790, 434
    CheckVar48 = IntVar()
    self.C48 = Checkbutton(self.can, text="Ludiomil (maprotilin)", fg='navy', 
        bg='cyan', variable=CheckVar48, 
        onvalue=1, offvalue=0, height=1, 
        width=26, anchor="w")
    self.C48 = self.can.create_window(self.x52, self.y52,
        window = self.C48)

    self.x53, self.y53 = 790, 457
    CheckVar49 = IntVar()
    self.C49 = Checkbutton(self.can, text="Remeron (mirtazapin)", fg='navy', 
        bg='cyan', variable=CheckVar49, 
        onvalue=1, offvalue=0, height=1, 
        width=26, anchor="w")
    self.C49 = self.can.create_window(self.x53, self.y53,
        window = self.C49)

    self.x54, self.y54 = 790, 480
    CheckVar50 = IntVar()
    self.C50 = Checkbutton(self.can, text="Saroten (amitriptylin)", fg='navy', 
        bg='cyan', variable=CheckVar50, 
        onvalue=1, offvalue=0, height=1, 
        width=26, anchor="w")
    self.C50 = self.can.create_window(self.x54, self.y54,
        window = self.C50)

    self.x55, self.y55 = 790, 503
    CheckVar51 = IntVar()
    self.C51 = Checkbutton(self.can, text="Sertraline (zoloft)", fg='navy', 
        bg='cyan', variable=CheckVar51, 
        onvalue=1, offvalue=0, height=1, 
        width=26, anchor="w")
    self.C51 = self.can.create_window(self.x55, self.y55,
        window = self.C51)

    self.x56, self.y56 = 1117, 434
    CheckVar52 = IntVar()
    self.C52 = Checkbutton(self.can, text="Surmontil (trimipramin)", fg='navy', 
        bg='cyan', variable=CheckVar52, 
        onvalue=1, offvalue=0, height=1, 
        width=26, anchor="w")
    self.C52 = self.can.create_window(self.x56, self.y56,
        window = self.C52)

    self.x57, self.y57 = 1117, 457
    CheckVar53 = IntVar()
    self.C53 = Checkbutton(self.can, text="Wellbutrin (bupropion)", fg='navy', 
        bg='cyan', variable=CheckVar53, 
        onvalue=1, offvalue=0, height=1, 
        width=26, anchor="w")
    self.C53 = self.can.create_window(self.x57, self.y57,
        window = self.C53)

    self.x58, self.y58 = 1117, 530
    self.buttonstix = Button(self.can, text='Stix', width=10, bd=3,
        fg='cyan', bg='RoyalBlue3', activebackground='pale turquoise',
        highlightbackground='cyan', command=comburTips)
    self.buttonstix = self.can.create_window(self.x58, self.y58,
        window = self.buttonstix)

    # Printable
    self.x59, self.y59 = 298, 528
    self.labelresult4 = Label(self.can, text='--- Printable ---', 
        font="Times 14 bold", width=62,
        height=1, bg='RoyalBlue3', fg='white')
    self.labelresult4 = self.can.create_window(self.x59, self.y59,
        window = self.labelresult4)

    def sheetLabo():
        """
            For openning file at pdf 
            format with a bit prog-sys code.
            For Linux, Windows and MAC.
        """

        becall = platform.system()
        print(platform.system())
        
        if becall == 'Linux':
            os.system('gio open "./labo/labosheet.pdf"') # Linux
        elif becall =='Darwin':
            subprocess.call('open', './labo/labosheet.pdf' ) # Mac
        else:
            os.startfile('./labo/labosheet.pdf') # Windows

    # Buttons printable sheet
    self.x60, self.y60 = 140, 620
    self.buttonSheet = Button(self.can,
        text="Complete lab sheet", width=15,
        fg='cyan', bg='navy',
        activebackground='pale turquoise',
        command=sheetLabo)
    self.buttonSheet = self.can.create_window(self.x60,
        self.y60, window = self.buttonSheet)

    def sheetMicrobio():
        """
            For openning file at pdf 
            format with a bit prog-sys code.
            For Linux, Windows and MAC.
        """

        callplatform = platform.system()
        print(platform.system())
        
        if callplatform == 'Linux':
            os.system('gio open "./labo/microbio.pdf"') # Linux
        elif callplatform =='Darwin':
            subprocess.call('open', './labo/microbio.pdf' ) # Mac
        else:
            os.startfile('./labo/microbio.pdf') # Windows

    self.x61, self.y61 = 460, 620
    self.buttonMicro = Button(self.can,
        text="Microbiology sheet", width=15,
        fg='cyan', bg='navy',
        activebackground='pale turquoise',
        command=sheetMicrobio)
    self.buttonMicro = self.can.create_window(self.x61,
        self.y61, window = self.buttonMicro)

    def printLabo():
        """
            Need to be modified in 
            function of platform's 
            user !!! Here, it's 
            for linux ! ;)
        """

        #lpr = subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
        #lpr.stdin.write('4.15.0-96-generic')
        pass

    # Lithium
    self.x62, self.y62 = 790, 528
    self.labelinfuri = Label(self.can, text='--- Lithium ---', 
        font="Times 14 bold", width=26,
        height=1, bg='RoyalBlue3', fg='white')
    self.labelinfuri = self.can.create_window(self.x62, self.y62,
        window = self.labelinfuri)

    self.x63, self.y63 = 790, 553
    CheckVar54 = IntVar()
    self.C54 = Checkbutton(self.can, text="Lithiofor (lithium)", fg='navy', 
        bg='cyan', variable=CheckVar54, 
        onvalue=1, offvalue=0, height=1, 
        width=26, anchor="w")
    self.C54 = self.can.create_window(self.x63, self.y63,
        window = self.C54)

    # Button save and quit
    self.x64, self.y64 = 790, 620
    self.buttonsave = Button(self.can, text="Save", width=10, bd=3,
        fg='yellow', bg='RoyalBlue3', activebackground='pale turquoise',
        highlightbackground='cyan', command=recordTofile)
    self.buttonsave = self.can.create_window(self.x64, self.y64,
        window = self.buttonsave)

    self.x65, self.y65 = 1110, 620
    self.buttonquit = Button(self.can, text='Return to main menu', width=20, bd=3,
        fg='white', bg='RoyalBlue3', activebackground='pale turquoise',
        highlightbackground='cyan', command=awayOut)
    self.buttonquit = self.can.create_window(self.x65, self.y65,
        window = self.buttonquit)

    self.can.configure(scrollregion=self.can.bbox(ALL))