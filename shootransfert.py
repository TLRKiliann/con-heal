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
        print("Not found", nf_file2) --ok--

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