#!/usr/bin/python3
# -*- coding : utf-8 -*-


import os
import shutil


def loaderfile():
    try:
        if os.path.exists('./Backup/Files1/Backup_patient.txt'):
            shutil.copy('./Backup/Files1/Backup_patient.txt',
                './newpatient/entryfile.txt')
            print("+ entryfile 1 copied")
    except FileNotFoundError as nf_file:
        print("+ Not found or not created", nf_file)
    loadernext()

def loadernext():
    try:
        if os.path.exists('./Backup/Files2/Backup_patient2.txt'):
            shutil.copy('./Backup/Files2/Backup_patient2.txt',
                './newpatient/entryfile2.txt')
            print("+ entryfile 2 copied")
    except FileNotFoundError as nf_file2:
        print("+ Not found or not created", nf_file2)
    nextload()

def nextload():
    try:
        if os.path.exists('./Backup/Files3/Backup_patient3.txt'):
            shutil.copy('./Backup/Files3/Backup_patient3.txt',
                './newpatient/entryfile3.txt')
            print("+ entryfile 3 copied")
    except FileNotFoundError as nf_file3:
        print("+ Not found or not created", nf_file3)
    secondload()

def secondload():
    try:
        if os.path.exists('./Backup/Files4/Backup_patient4.txt'):
            shutil.copy('./Backup/Files4/Backup_patient4.txt',
                './newpatient/entryfile4.txt')
            print("+ entryfile 4 copied")
    except FileNotFoundError as nf_file4:
        print("+ Not found or not created", nf_file4)
    thirdnextload()

def thirdnextload():
    try:
        if os.path.exists('./Backup/Files5/Backup_patient5.txt'):
            shutil.copy('./Backup/Files5/Backup_patient5.txt',
                './newpatient/entryfile5.txt')
            print("+ entryfile 5 copied")
    except FileNotFoundError as nf_file5:
        print("+ Not found or not created", nf_file5)
    fourthload()

def fourthload():
    try:
        if os.path.exists('./Backup/Files6/Backup_patient6.txt'):
            shutil.copy('./Backup/Files6/Backup_patient6.txt',
                './newpatient/entryfile6.txt')
            print("+ entryfile 6 copied")
    except FileNotFoundError as nf_file6:
        print("+ Not found or not created", nf_file6)
    nextload5()

def nextload5():
    try:
        if os.path.exists('./Backup/Files7/Backup_patient7.txt'):
            shutil.copy('./Backup/Files7/Backup_patient7.txt',
                './newpatient/entryfile7.txt')
            print("+ entryfile 7 copied")
    except FileNotFoundError as nf_file7:
        print("+ Not found or not created", nf_file7)
    nextload6()

def nextload6():
    try:
        if os.path.exists('./Backup/Files8/Backup_patient8.txt'):
            shutil.copy('./Backup/Files8/Backup_patient8.txt',
                './newpatient/entryfile8.txt')
            print("+ entryfile 8 copied")
    except FileNotFoundError as nf_file8:
        print("+ Not found or not created", nf_file8)
    nextload7()

def nextload7():
    try:
        if os.path.exists('./Backup/Files9/Backup_patient9.txt'):
            shutil.copy('./Backup/Files9/Backup_patient9.txt',
                './newpatient/entryfile9.txt')
            print("+ entryfile 9 copied")
    except FileNotFoundError as nf_file9:
        print("+ Not found or not created", nf_file9)
    nextload8()

def nextload8():
    try:
        if os.path.exists('./Backup/Files10/Backup_patient10.txt'):
            shutil.copy('./Backup/Files10/Backup_patient10.txt',
                './newpatient/entryfile10.txt')
            print("+ entryfile 10 copied")
    except FileNotFoundError as nf_file10:
        print("+ Not found or not created", nf_file10)
    nextload9()

def nextload9():
    try:
        if os.path.exists('./Backup/Files11/Backup_patient11.txt'):
            shutil.copy('./Backup/Files11/Backup_patient11.txt',
                './newpatient/entryfile11.txt')
            print("+ entryfile 11 copied")
    except FileNotFoundError as nf_file11:
        print("+ Not found or not created", nf_file11)
    nextload10()

def nextload10():
    try:
        if os.path.exists('./Backup/Files12/Backup_patient12.txt'):
            shutil.copy('./Backup/Files12/Backup_patient12.txt',
                './newpatient/entryfile12.txt')
            print("+ entryfile 12 copied")
    except FileNotFoundError as nf_file12:
        print("+ Not found or not created", nf_file12)
    eleventhload()

def eleventhload():
    try:
        if os.path.exists('./Backup/Files13/Backup_patient13.txt'):
            shutil.copy('./Backup/Files13/Backup_patient13.txt',
                './newpatient/entryfile13.txt')
            print("+ entryfile 13 copied")
    except FileNotFoundError as nf_file13:
        print("+ Not found or not created", nf_file13)
    twelvethload()

def twelvethload():
    try:
        if os.path.exists('./Backup/Files14/Backup_patient14.txt'):
            shutil.copy('./Backup/Files14/Backup_patient14.txt',
                './newpatient/entryfile14.txt')
            print("+ entryfile 14 copied")
    except FileNotFoundError as nf_file14:
        print("+ Not found or not created", nf_file14)
    fourteenload()

def fourteenload():
    try:
        if os.path.exists('./Backup/Files15/Backup_patient15.txt'):
            shutil.copy('./Backup/Files15/Backup_patient15.txt',
                './newpatient/entryfile15.txt')
            print("+ entryfile 15 copied")
    except FileNotFoundError as nf_file15:
        print("+ Not found or not created", nf_file15)
    fiveteenload()

def fiveteenload():
    try:
        if os.path.exists('./Backup/Files16/Backup_patient16.txt'):
            shutil.copy('./Backup/Files16/Backup_patient16.txt',
                './newpatient/entryfile16.txt')
            print("+ entryfile 16 copied")
    except FileNotFoundError as nf_file16:
        print("+ Not found or not created", nf_file16)
    afterload()

def afterload():
    try:
        if os.path.exists('./Backup/Files17/Backup_patient17.txt'):
            shutil.copy('./Backup/Files17/Backup_patient17.txt',
                './newpatient/entryfile17.txt')
            print("+ entryfile 17 copied")
    except FileNotFoundError as nf_file17:
        print("+ Not found or not created", nf_file17)
    loadingforever()

def loadingforever():
    try:
        if os.path.exists('./Backup/Files18/Backup_patient18.txt'):
            shutil.copy('./Backup/Files18/Backup_patient18.txt',
                './newpatient/entryfile18.txt')
            print("+ entryfile 18 copied")
    except FileNotFoundError as nf_file18:
        print("+ Not found or not created", nf_file18)
    neverload()

def neverload():
    try:
        if os.path.exists('./Backup/Files19/Backup_patient19.txt'):
            shutil.copy('./Backup/Files19/Backup_patient19.txt',
                './newpatient/entryfile19.txt')
            print("+ entryfile 19 copied")
    except FileNotFoundError as nf_file19:
        print("+ Not found or not created", nf_file19)
    twentyload()

def twentyload():
    try:
        if os.path.exists('./Backup/Files20/Backup_patient20.txt'):
            shutil.copy('./Backup/Files20/Backup_patient20.txt',
                './newpatient/entryfile20.txt')
            print("+ entryfile 20 copied")
    except FileNotFoundError as nf_file20:
        print("+ Not found or not created", nf_file20)
    aftertwenty()

def aftertwenty():
    try:
        if os.path.exists('./Backup/Files21/Backup_patient21.txt'):
            shutil.copy('./Backup/Files21/Backup_patient21.txt',
                './newpatient/entryfile21.txt')
            print("+ entryfile 21 copied")
    except FileNotFoundError as nf_file21:
        print("+ Not found or not created", nf_file21)
    twentytwoload()

def twentytwoload():
    try:
        if os.path.exists('./Backup/Files22/Backup_patient22.txt'):
            shutil.copy('./Backup/Files22/Backup_patient22.txt',
                './newpatient/entryfile22.txt')
            print("+ entryfile 22 copied")
    except FileNotFoundError as nf_file22:
        print("+ Not found or not created", nf_file22)
    twentythreeload()

def twentythreeload():
    try:
        if os.path.exists('./Backup/Files23/Backup_patient23.txt'):
            shutil.copy('./Backup/Files23/Backup_patient23.txt',
                './newpatient/entryfile23.txt')
            print("+ entryfile 23 copied")
    except FileNotFoundError as nf_file23:
        print("+ Not found or not created", nf_file23)
    backload()

def backload():
    try:
        if os.path.exists('./Backup/Files24/Backup_patient24.txt'):
            shutil.copy('./Backup/Files24/Backup_patient24.txt',
                './newpatient/entryfile24.txt')
            print("+ entryfile 24 copied")
    except FileNotFoundError as nf_file24:
        print("+ Not found or not created", nf_file24)

    # Don't need for Vital Parameters...
    # Don't need for BMI...

    # Requiered for ttt + res
    # Requiered for labo
    # Required for VM, Diag, 14needs
