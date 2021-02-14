#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    To delete all files for patient 4
    when usr delete patient by pressing
    the delete button.
"""


from tkinter import *
from tkinter import messagebox
import os
import subprocess
import shutil


def delFuncFile4():
    """
        This function delete all files with
        a test before removing files.
    """
    backproc = subprocess.run(["scp", "-r", "./Backup/Files4",
        "pi@192.168.18.12:~/tt_doc/doc_txt4/Backup4"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(backproc.stderr))
    if backproc.stderr == b'':
        print("+ File Backup4 uploaded !")
        #messagebox.showinfo("INFO", "entryfile8.txt uploaded...")
    else:
        print("+ No folder to upload !")
        messagebox.showerror("Error", "No Backup4 to upload...")

    delproc = subprocess.run(["ssh",
        "pi@192.168.18.12", "rm -r ~/tt_doc/doc_txt4/Files4/*"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(delproc.stderr))
    if delproc.stderr == b'':
        print("+ Files4 has been deleted on server !")
        messagebox.showinfo("INFO", "Files4 has been deleted on server !")
    else:
        print("!!! Error", "Not deleted Files4 on server !!!")
        messagebox.showerror("Error", "!!! Not deleted Files4 on server !!!")

    try:
        if os.path.getsize('./need/doc_suivi4/main_14b.txt'):
            os.remove('./need/doc_suivi4/main_14b.txt')
            print("+ File main_14b.txt deleted")
    except FileNotFoundError as filefunc:
        print("+ File main_14b.txt does not exist", filefunc)

    try:
        if os.path.getsize('./need/doc_suivi4/patient4_14b.txt'):
            os.remove('./need/doc_suivi4/patient4_14b.txt')
            print("+ File patient4_14b.txt deleted")
    except FileNotFoundError as filefunc2:
        print("+ File patient4_14b.txt does not exist", filefunc2)

    try:
        if os.path.getsize('./ttt/doc_ttt4/convdose.json'):
            os.remove('./ttt/doc_ttt4/convdose.json')
            print("+ File convdose.json deleted")
    except FileNotFoundError as filefunc3:
        print("+ File convdose.json does not exist", filefunc3)

    try:
        if os.path.getsize('./ttt/doc_ttt4/intro_ttt.txt'):
            os.remove('./ttt/doc_ttt4/intro_ttt.txt')
            print("+ File intro_ttt.txt deleted")
    except FileNotFoundError as filefunc4:
        print("+ File intro_ttt.txt does not exist", filefunc4)

    try:
        if os.path.getsize('./ttt/doc_ttt4/convres.json'):
            os.remove('./ttt/doc_ttt4/convres.json')
            print("+ File convres.json deleted")
    except FileNotFoundError as filefunc5:
        print("+ File convres.json does not exist", filefunc5)

    try:
        if os.path.getsize('./ttt/doc_ttt4/intro_res.txt'):
            os.remove('./ttt/doc_ttt4/intro_res.txt')
            print("+ File intro_res.txt deleted")
    except FileNotFoundError as filefunc6:
        print("+ File intro_res.txt does not exist", filefunc6)

    try:
        if os.path.getsize('./param/paramdata4.txt'):
            os.remove('./param/paramdata4.txt')
            print("+ File paramdata4.txt deleted")
    except FileNotFoundError as filefunc61:
        print("+ File paramdata4.txt does not exist", filefunc61)

    try:
        if os.path.getsize('./param/aspifile4/diastol.json'):
            os.remove('./param/aspifile4/diastol.json')
            print("+ File diastol.json deleted")
    except FileNotFoundError as filefunc62:
        print("+ File diastol.json does not exist", filefunc62)

    try:
        if os.path.getsize('./param/aspifile4/dlr.json'):
            os.remove('./param/aspifile4/dlr.json')
            print("+ File dlr.json deleted")
    except FileNotFoundError as filefunc63:
        print("+ File dlr.json does not exist", filefunc63)

    try:
        if os.path.getsize('./param/aspifile4/freq.json'):
            os.remove('./param/aspifile4/freq.json')
            print("+ File freq.json deleted")
    except FileNotFoundError as filefunc64:
        print("+ File freq.json does not exist", filefunc64)

    try:
        if os.path.getsize('./param/aspifile4/gly.json'):
            os.remove('./param/aspifile4/gly.json')
            print("+ File gly.json deleted")
    except FileNotFoundError as filefunc65:
        print("+ File gly.json does not exist", filefunc65)

    try:
        if os.path.getsize('./param/aspifile4/puls.json'):
            os.remove('./param/aspifile4/puls.json')
            print("+ File puls.json deleted")
    except FileNotFoundError as filefunc66:
        print("+ File puls.json does not exist", filefunc66)

    try:
        if os.path.getsize('./param/aspifile4/sat.json'):
            os.remove('./param/aspifile4/sat.json')
            print("+ File sat.json deleted")
    except FileNotFoundError as filefunc67:
        print("+ File sat.json does not exist", filefunc67)

    try:
        if os.path.getsize('./param/aspifile4/systol.json'):
            os.remove('./param/aspifile4/systol.json')
            print("+ File systol.json deleted")
    except FileNotFoundError as filefunc68:
        print("+ File systol.json does not exist", filefunc68)

    try:
        if os.path.getsize('./param/aspifile4/temp.json'):
            os.remove('./param/aspifile4/temp.json')
            print("+ File temp.json deleted")
    except FileNotFoundError as filefunc69:
        print("+ File temp.json does not exist", filefunc69)

    try:
        if os.path.getsize('./calBmi/doc_BMI4/file_bmi.json'):
            os.remove('./calBmi/doc_BMI4/file_bmi.json')
            print("+ File bmi.json deleted")
    except FileNotFoundError as filefunc7:
        print("+ File bmi.json does not exist", filefunc7)

    try:
        if os.path.getsize('./calBmi/doc_BMI4/file_kg.json'):
            os.remove('./calBmi/doc_BMI4/file_kg.json')
            print("+ File file_kg.json deleted")
    except FileNotFoundError as filefunc8:
        print("+ File file_kg.json does not exist", filefunc8)

    try:
        if os.path.getsize('./calBmi/doc_BMI4/custom_kg.txt'):
            os.remove('./calBmi/doc_BMI4/custom_kg.txt')
            print("+ File custom_kg.txt deleted")
    except FileNotFoundError as filefunc81:
        print("+ File custom_kg.txt does not exist", filefunc81)

    try:
        if os.path.getsize('./calBmi/bmi4.txt'):
            os.remove('./calBmi/bmi4.txt')
            print("+ File bmi4.txt deleted")
    except FileNotFoundError as filefunc9:
        print("+ File bmi4.txt does not exist", filefunc9)

    try:
        if os.path.getsize('./diag/doc_diag4/diagrecap4.txt'):
            os.remove('./diag/doc_diag4/diagrecap4.txt')
            print("+ File diagrecap4.txt deleted")
    except FileNotFoundError as filefunc10:
        print("+ File diagrecap4.txt does not exist", filefunc10)

    try:
        if os.path.getsize('./labo/doc_labo/result4.txt'):
            os.remove('./labo/doc_labo/result4.txt')
            print("+ File result4.txt deleted")
    except FileNotFoundError as filefunc11:
        print("+ File result4.txt does not exist", filefunc11)

    try:
        if os.path.getsize('./patient_agenda/events4/doc_events/fix_agenda/fixed_rdv.txt'):
            os.remove('./patient_agenda/events4/doc_events/fix_agenda/fixed_rdv.txt')
            print("+ File fixed_rdv.txt deleted")
    except FileNotFoundError as filefunc12:
        print("+ File fixed_rdv.txt does not exist", filefunc12)

    try:
        if os.path.getsize('./patient_agenda/events4/doc_events/fix_agenda/modifrdv.txt'):
            os.remove('./patient_agenda/events4/doc_events/fix_agenda/modifrdv.txt')
            print("+ File modifrdv.txt deleted")
    except FileNotFoundError as filefunc13:
        print("+ File modifrdv.txt does not exist", filefunc13)

    try:
        if os.path.getsize('./patient_agenda/events4/doc_events/fix_agenda/patient_value.json'):
            os.remove('./patient_agenda/events4/doc_events/fix_agenda/patient_value.json')
            print("+ File patient_value.json deleted")
    except FileNotFoundError as filefunc14:
        print("+ File patient_value.json does not exist", filefunc14)

    try:
        if os.path.getsize('./patient_agenda/events4/doc_events/patient_rdv.json'):
            os.remove('./patient_agenda/events4/doc_events/patient_rdv.json')
            print("+ File patient_rdv.json deleted")
    except FileNotFoundError as filefunc15:
        print("+ File patient_rdv does not exist", filefunc15)

    try:
        if os.path.getsize('./patient_agenda/events4/patient_calendar.txt'):
            os.remove('./patient_agenda/events4/patient_calendar.txt')
            print("+ File patient_calendar.txt deleted")
    except FileNotFoundError as filefunc16:
        print("+ File patient_calendar.txt does not exist", filefunc16)

    try:
        if os.path.getsize('./vmed/doc_vmed4/resultvmed4.txt'):
            os.remove('./vmed/doc_vmed4/resultvmed4.txt')
            print("+ File resultvmed4.txt.txt deleted")
    except FileNotFoundError as filefunc17:
        print("+ File resultvmed4.txt.txt does not exist", filefunc17)

    try:
        if os.path.getsize('./allergy/allergyfile4.txt'):
            os.remove('./allergy/allergyfile4.txt')
            print("+ File allergyfile4.txt deleted")
    except FileNotFoundError as filefunc18:
        print("+ File allergyfile4.txt does not exist", filefunc18)

    try:
        if os.path.getsize('./newpatient/entryfile4.txt'):
            with open('./newpatient/entryfile4.txt', 'w') as file:
                file.write("----")
            print("+ File entryfile4.txt reborn")
    except FileNotFoundError as filefunc19:
        print("+ File entryfile4.txt does not exist", filefunc19)

    proc = subprocess.run(["scp", "./newpatient/entryfile4.txt",
        "pi@192.168.18.12:~/tt_doc/doc_txt4/Files4/entryfile4.txt"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File entryfile4.txt uploaded !")
        #messagebox.showinfo("INFO", "entryfile4.txt uploaded...")
    else:
        print("+ No file to upload !")
        messagebox.showerror("Error", "No entryfile4.txt to upload...")

    try:
        if os.path.exists('./Backup/Files4/Backup_param4.txt'):
            print("+ Backup_param4.txt exist")
            shutil.copy('./Backup/Files4/Backup_param4.txt',
                './Backup/old/oldfiles4/Backup_param4.txt')
            os.remove('./Backup/Files4/Backup_param4.txt')
    except FileNotFoundError as nf_param:
        print("Not found", nf_param)

    try:
        if os.path.exists('./Backup/Files4/Backup_patient4.txt'):
            print("+ Backup_patient4.txt exist")
            shutil.copy('./Backup/Files4/Backup_patient4.txt',
                './Backup/old/oldfiles4/Backup_patient4.txt')
            os.remove('./Backup/Files4/Backup_patient4.txt')
    except FileNotFoundError as nf_oldfile:
        print("Not found", nf_oldfile)

    try:
        if os.path.exists('./Backup/Files4/Backup_careneeds4.txt'):
            print("+ Backup_careneeds4.txt exist")
            shutil.copy('./Backup/Files4/Backup_careneeds4.txt',
                './Backup/old/oldfiles4/Backup_careneeds4.txt')
            os.remove('./Backup/Files4/Backup_careneeds4.txt')
    except FileNotFoundError as nf_oldfile2:
        print("Not found", nf_oldfile2)

    try:
        if os.path.exists('./Backup/Files4/Backup_diag4.txt'):
            print("+ Backup_diag4.txt exist")
            shutil.copy('./Backup/Files4/Backup_diag4.txt',
                './Backup/old/oldfiles4/Backup_diag4.txt')
            os.remove('./Backup/Files4/Backup_diag4.txt')
    except FileNotFoundError as nf_oldfile3:
        print("Not found", nf_oldfile3)

    try:
        if os.path.exists('./Backup/Files4/Backup_Bmi4.txt'):
            print("+ Backup_Bmi4.txt exist")
            shutil.copy('./Backup/Files4/Backup_Bmi4.txt',
                './Backup/old/oldfiles4/Backup_Bmi4.txt')
            os.remove('./Backup/Files4/Backup_Bmi4.txt')
    except FileNotFoundError as nf_oldfile4:
        print("Not found", nf_oldfile4)

    try:
        if os.path.exists('./Backup/Files4/Backup_resultvmed4.txt'):
            print("+ Backup_resultvmed4.txt exist")
            shutil.copy('./Backup/Files4/Backup_resultvmed4.txt',
                './Backup/old/oldfiles4/Backup_resultvmed4.txt')
            os.remove('./Backup/Files4/Backup_resultvmed4.txt')
    except FileNotFoundError as nf_oldfile5:
        print("Not found", nf_oldfile5)

    try:
        if os.path.exists('./Backup/Files4/Backup_ttt4.txt'):
            print("+ Backup_ttt4.txt exist")
            shutil.copy('./Backup/Files4/Backup_ttt4.txt',
                './Backup/old/oldfiles4/Backup_ttt4.txt')
            os.remove('./Backup/Files4/Backup_ttt4.txt')
    except FileNotFoundError as nf_oldfile6:
        print("Not found", nf_oldfile6)

    print("!!! All files have been deleted !!!")
    