#!/usr/bin/python3
# -*- coding : utf-8 -*-


import os
import shutil


def loaderfile():
    try:
        if os.path.exists('./newpatient/entryfile.txt'):
            shutil.copy('./Backup/Files1/Backup_patient.txt',
                './newpatient/entryfile.txt')
            print("+ entryfile 1 copied")
    except FileNotFoundError as nf_file:
        print("Not found", nf_file)

    try:
        if os.path.exists('./newpatient/entryfile2.txt'):
            shutil.copy('./Backup/Files2/Backup_patient2.txt',
                './newpatient/entryfile2.txt')
            print("+ entryfile 2 copied")
    except FileNotFoundError as nf_file2:
        print("Not found", nf_file2)

    try:
        if os.path.exists('./newpatient/entryfile3.txt'):
            shutil.copy('./Backup/Files3/Backup_patient3.txt',
                './newpatient/entryfile3.txt')
            print("+ entryfile 3 copied")
    except FileNotFoundError as nf_file3:
        print("Not found", nf_file3)

    try:
        if os.path.exists('./newpatient/entryfile4.txt'):
            shutil.copy('./Backup/Files4/Backup_patient4.txt',
                './newpatient/entryfile4.txt')
            print("+ entryfile 4 copied")
    except FileNotFoundError as nf_file4:
        print("Not found", nf_file4)

    try:
        if os.path.exists('./newpatient/entryfile5.txt'):
            shutil.copy('./Backup/Files5/Backup_patient5.txt',
                './newpatient/entryfile5.txt')
            print("+ entryfile 5 copied")
    except FileNotFoundError as nf_file5:
        print("Not found", nf_file5)

    try:
        if os.path.exists('./newpatient/entryfile6.txt'):
            shutil.copy('./Backup/Files6/Backup_patient6.txt',
                './newpatient/entryfile6.txt')
            print("+ entryfile 6 copied")
    except FileNotFoundError as nf_file6:
        print("Not found", nf_file6)

    try:
        if os.path.exists('./newpatient/entryfile7.txt'):
            shutil.copy('./Backup/Files7/Backup_patient7.txt',
                './newpatient/entryfile7.txt')
            print("+ entryfile 7 copied")
    except FileNotFoundError as nf_file7:
        print("Not found", nf_file7)

    try:
        if os.path.exists('./newpatient/entryfile8.txt'):
            shutil.copy('./Backup/Files8/Backup_patient8.txt',
                './newpatient/entryfile8.txt')
            print("+ entryfile 8 copied")
    except FileNotFoundError as nf_file8:
        print("Not found", nf_file8)

    try:
        if os.path.exists('./newpatient/entryfile9.txt'):
            shutil.copy('./Backup/Files9/Backup_patient9.txt',
                './newpatient/entryfile9.txt')
            print("+ entryfile 9 copied")
    except FileNotFoundError as nf_file9:
        print("Not found", nf_file9)

    try:
        if os.path.exists('./newpatient/entryfile10.txt'):
            shutil.copy('./Backup/Files10/Backup_patient10.txt',
                './newpatient/entryfile10.txt')
            print("+ entryfile 10 copied")
    except FileNotFoundError as nf_file10:
        print("Not found", nf_file10)