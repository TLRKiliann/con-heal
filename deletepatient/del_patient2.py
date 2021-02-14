#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    To delete all files for patient 2
    when usr delete patient by pressing
    the delete button.
"""


from tkinter import *
from tkinter import messagebox
import os
import subprocess
import shutil


def delFuncFile2():
    """
        This function delete all files with
        a test before removing files.
    """
    backproc = subprocess.run(["scp", "-r", "./Backup/Files2",
        "pi@192.168.18.12:~/tt_doc/doc_txt2/Backup2"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(backproc.stderr))
    if backproc.stderr == b'':
        print("+ Backup2 done on server ! !")
        messagebox.showinfo("INFO", "Backup2 done on server !")
    else:
        print("!!! No Backup2 done on server !!!")
        messagebox.showerror("Error", "!!! No Backup2 done on server !!!")

    delproc = subprocess.run(["ssh",
        "pi@192.168.18.12", "rm -r ~/tt_doc/doc_txt2/Files2/*"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(delproc.stderr))
    if delproc.stderr == b'':
        print("+ Files2 has been deleted on server !")
        messagebox.showinfo("INFO", "Files2 has been deleted on server !")
    else:
        print("!!! Error", "Not deleted Files2 on server !!!")
        messagebox.showerror("Error", "!!! Not deleted Files2 on server !!!")

    try:
        if os.path.getsize('./need/doc_suivi2/main_14b.txt'):
            os.remove('./need/doc_suivi2/main_14b.txt')
            print("+ File main_14b.txt deleted")
    except FileNotFoundError as filefunc1:
        print("+ File main_14b.txt does not exist", filefunc1)

    try:
        if os.path.getsize('./need/doc_suivi2/patient2_14b.txt'):
            os.remove('./need/doc_suivi2/patient2_14b.txt')
            print("+ File patient2_14b.txt deleted")
    except FileNotFoundError as filefunc2:
        print("+ File patient2_14b.txt does not exist", filefunc2)

    try:
        if os.path.getsize('./ttt/doc_ttt2/convdose.json'):
            os.remove('./ttt/doc_ttt2/convdose.json')
            print("+ File convdose.json deleted")
    except FileNotFoundError as filefunc3:
        print("+ File convdose.json does not exist", filefunc3)

    try:
        if os.path.getsize('./ttt/doc_ttt2/intro_ttt.txt'):
            os.remove('./ttt/doc_ttt2/intro_ttt.txt')
            print("+ File intro_ttt.txt deleted")
    except FileNotFoundError as filefunc4:
        print("+ File intro_ttt.txt does not exist", filefunc4)

    try:
        if os.path.getsize('./ttt/doc_ttt2/convres.json'):
            os.remove('./ttt/doc_ttt2/convres.json')
            print("+ File convres.json deleted")
    except FileNotFoundError as filefunc5:
        print("+ File convres.json does not exist", filefunc5)

    try:
        if os.path.getsize('./ttt/doc_ttt2/intro_res.txt'):
            os.remove('./ttt/doc_ttt2/intro_res.txt')
            print("+ File intro_res.txt deleted")
    except FileNotFoundError as filefunc6:
        print("+ File intro_res.txt does not exist", filefunc6)

    try:
        if os.path.getsize('./param/paramdata2.txt'):
            os.remove('./param/paramdata2.txt')
            print("+ File paramdata2.txt deleted")
    except FileNotFoundError as filefunc61:
        print("+ File paramdata2.txt does not exist", filefunc61)

    try:
        if os.path.getsize('./param/aspifile2/diastol.json'):
            os.remove('./param/aspifile2/diastol.json')
            print("+ File diastol.json deleted")
    except FileNotFoundError as filefunc62:
        print("+ File diastol.json does not exist", filefunc62)

    try:
        if os.path.getsize('./param/aspifile2/dlr.json'):
            os.remove('./param/aspifile2/dlr.json')
            print("+ File dlr.json deleted")
    except FileNotFoundError as filefunc63:
        print("+ File dlr.json does not exist", filefunc63)

    try:
        if os.path.getsize('./param/aspifile2/freq.json'):
            os.remove('./param/aspifile2/freq.json')
            print("+ File freq.json deleted")
    except FileNotFoundError as filefunc64:
        print("+ File freq.json does not exist", filefunc64)

    try:
        if os.path.getsize('./param/aspifile2/gly.json'):
            os.remove('./param/aspifile2/gly.json')
            print("+ File gly.json deleted")
    except FileNotFoundError as filefunc65:
        print("+ File gly.json does not exist", filefunc65)

    try:
        if os.path.getsize('./param/aspifile2/puls.json'):
            os.remove('./param/aspifile2/puls.json')
            print("+ File puls.json deleted")
    except FileNotFoundError as filefunc66:
        print("+ File puls.json does not exist", filefunc66)

    try:
        if os.path.getsize('./param/aspifile2/sat.json'):
            os.remove('./param/aspifile2/sat.json')
            print("+ File sat.json deleted")
    except FileNotFoundError as filefunc67:
        print("+ File sat.json does not exist", filefunc67)

    try:
        if os.path.getsize('./param/aspifile2/systol.json'):
            os.remove('./param/aspifile2/systol.json')
            print("+ File systol.json deleted")
    except FileNotFoundError as filefunc68:
        print("+ File systol.json does not exist", filefunc68)

    try:
        if os.path.getsize('./param/aspifile2/temp.json'):
            os.remove('./param/aspifile2/temp.json')
            print("+ File temp.json deleted")
    except FileNotFoundError as filefunc69:
        print("+ File temp.json does not exist", filefunc69)

    try:
        if os.path.getsize('./calBmi/doc_BMI2/file_bmi.json'):
            os.remove('./calBmi/doc_BMI2/file_bmi.json')
            print("+ File file_bmi.json deleted")
    except FileNotFoundError as filefunc7:
        print("+ File file_bmi.json does not exist", filefunc7)

    try:
        if os.path.getsize('./calBmi/doc_BMI2/file_kg.json'):
            os.remove('./calBmi/doc_BMI2/file_kg.json')
            print("+ File file_kg.json deleted")
    except FileNotFoundError as filefunc8:
        print("+ File file_kg.json does not exist", filefunc8)

    try:
        if os.path.getsize('./calBmi/doc_BMI2/custom_kg.txt'):
            os.remove('./calBmi/doc_BMI2/custom_kg.txt')
            print("+ File custom_kg.txt deleted")
    except FileNotFoundError as filefunc81:
        print("+ File custom_kg.txt does not exist", filefunc81)

    try:
        if os.path.getsize('./calBmi/bmi2.txt'):
            os.remove('./calBmi/bmi2.txt')
            print("+ File bmi2.txt deleted")
    except FileNotFoundError as filefunc9:
        print("+ File bmi2.txt does not exist", filefunc9)

    try:
        if os.path.getsize('./diag/doc_diag2/diagrecap2.txt'):
            os.remove('./diag/doc_diag2/diagrecap2.txt')
            print("+ File diagrecap.txt deleted")
    except FileNotFoundError as filefunc10:
        print("+ File diagrecap.txt does not exist", filefunc10)

    try:
        if os.path.getsize('./labo/doc_labo/result2.txt'):
            os.remove('./labo/doc_labo/result2.txt')
            print("+ File result2.txt deleted")
    except FileNotFoundError as filefunc11:
        print("+ File result2.txt does not exist", filefunc11)

    try:
        if os.path.getsize('./patient_agenda/events2/doc_events/fix_agenda/fixed_rdv.txt'):
            os.remove('./patient_agenda/events2/doc_events/fix_agenda/fixed_rdv.txt')
            print("+ File fixed_rdv.txt deleted")
    except FileNotFoundError as filefunc12:
        print("+ File fixed_rdv.txt does not exist", filefunc12)

    try:
        if os.path.getsize('./patient_agenda/events2/doc_events/fix_agenda/modifrdv.txt'):
            os.remove('./patient_agenda/events2/doc_events/fix_agenda/modifrdv.txt')
            print("+ File modifrdv.txt deleted")
    except FileNotFoundError as filefunc13:
        print("+ File modifrdv.txt does not exist", filefunc13)

    try:
        if os.path.getsize('./patient_agenda/events2/doc_events/fix_agenda/patient_value.json'):
            os.remove('./patient_agenda/events2/doc_events/fix_agenda/patient_value.json')
            print("+ File patient_value.json deleted")
    except FileNotFoundError as filefunc14:
        print("+ File patient_value.json does not exist", filefunc14)

    try:
        if os.path.getsize('./patient_agenda/events2/doc_events/patient_rdv.json'):
            os.remove('./patient_agenda/events2/doc_events/patient_rdv.json')
            print("+ File patient_rdv.json deleted")
    except FileNotFoundError as filefunc15:
        print("+ File patient_rdv.json does not exist", filefunc15)

    try:
        if os.path.getsize('./patient_agenda/events2/patient_calendar.txt'):
            os.remove('./patient_agenda/events2/patient_calendar.txt')
            print("+ File patient_calendar.txt deleted")
    except FileNotFoundError as filefunc16:
        print("+ File patient_calendar.txt does not exist", filefunc16)

    try:
        if os.path.getsize('./vmed/doc_vmed2/resultvmed2.txt'):
            os.remove('./vmed/doc_vmed2/resultvmed2.txt')
            print("+ File resultvmed2.txt.txt deleted")
    except FileNotFoundError as filefunc17:
        print("+ File resultvmed2.txt.txt does not exist", filefunc17)

    try:
        if os.path.getsize('./allergy/allergyfile2.txt'):
            os.remove('./allergy/allergyfile2.txt')
            print("+ File allergyfile2.txt deleted")
    except FileNotFoundError as filefunc18:
        print("+ File allergyfile2.txt does not exist", filefunc18)

    try:
        if os.path.getsize('./newpatient/entryfile2.txt'):
            with open('./newpatient/entryfile2.txt', 'w') as file:
                file.write("--")
            print("+ File entryfile2.txt reborn")
    except FileNotFoundError as filefunc19:
        print("+ File entryfile2.txt not exist", filefunc19)

    proc = subprocess.run(["scp", "./newpatient/entryfile2.txt",
        "pi@192.168.18.12:~/tt_doc/doc_txt2/Files2/entryfile2.txt"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File entryfile2.txt uploaded !")
        #messagebox.showinfo("INFO", "entryfile2.txt uploaded...")
    else:
        print("+ No file to upload !")
        messagebox.showerror("Error", "No entryfile2.txt to upload...")

    try:
        if os.path.exists('./Backup/Files2/paramdata2.txt'):
            print("+ paramdata2.txt exist")
            shutil.copy('./Backup/Files2/paramdata2.txt',
                './Backup/old/oldfiles2/paramdata2.txt')
            os.remove('./Backup/Files2/paramdata2.txt')
    except FileNotFoundError as nf_param:
        print("Not found", nf_param)

    try:
        if os.path.exists('./Backup/Files2/patient2_14b.txt'):
            print("+ patient2_14b.txt exist")
            shutil.copy('./Backup/Files2/patient2_14b.txt',
                './Backup/old/oldfiles2/patient2_14b.txt')
            os.remove('./Backup/Files2/patient2_14b.txt')
    except FileNotFoundError as nf_oldfile:
        print("Not found", nf_oldfile)

    try:
        if os.path.exists('./Backup/Files2/main_14b.txt'):
            print("+ main_14b.txt exist")
            shutil.copy('./Backup/Files2/main_14b.txt',
                './Backup/old/oldfiles2/main_14b.txt')
            os.remove('./Backup/Files2/main_14b.txt')
    except FileNotFoundError as nf_oldfile2:
        print("Not found", nf_oldfile2)

    try:
        if os.path.exists('./Backup/Files2/diagrecap2.txt'):
            print("+ diagrecap2.txt exist")
            shutil.copy('./Backup/Files2/diagrecap2.txt',
                './Backup/old/oldfiles2/diagrecap2.txt')
            os.remove('./Backup/Files2/diagrecap2.txt')
    except FileNotFoundError as nf_oldfile3:
        print("Not found", nf_oldfile3)

    try:
        if os.path.exists('./Backup/Files2/file_bmi.json'):
            print("+ file_bmi.json exist")
            shutil.copy('./Backup/Files2/file_bmi.json',
                './Backup/old/oldfiles2/file_bmi.json')
            os.remove('./Backup/Files2/file_bmi.json')
    except FileNotFoundError as nf_oldfile41:
        print("Not found", nf_oldfile41)

    try:
        if os.path.exists('./Backup/Files2/file_kg.json'):
            print("+ file_kg.json exist")
            shutil.copy('./Backup/Files2/file_kg.json',
                './Backup/old/oldfiles2/file_kg.json')
            os.remove('./Backup/Files2/file_kg.json')
    except FileNotFoundError as nf_oldfile42:
        print("Not found", nf_oldfile42)

    try:
        if os.path.exists('./Backup/Files2/bmi2.json'):
            print("+ bmi2.json exist")
            shutil.copy('./Backup/Files2/bmi2.json',
                './Backup/old/oldfiles2/bmi2.json')
            os.remove('./Backup/Files2/bmi2.json')
    except FileNotFoundError as nf_oldfile43:
        print("Not found", nf_oldfile43)

    try:
        if os.path.exists('./Backup/Files2/resultvmed2.txt'):
            print("+ resultvmed2.txt exist")
            shutil.copy('./Backup/Files2/resultvmed2.txt',
                './Backup/old/oldfiles2/resultvmed2.txt')
            os.remove('./Backup/Files2/resultvmed2.txt')
    except FileNotFoundError as nf_oldfile5:
        print("Not found", nf_oldfile5)

    try:
        if os.path.exists('./Backup/Files2/Backup_ttt2.txt'):
            print("+ Backup_ttt2.txt exist")
            shutil.copy('./Backup/Files2/Backup_ttt2.txt',
                './Backup/old/oldfiles2/Backup_ttt2.txt')
            os.remove('./Backup/Files2/Backup_ttt2.txt')
    except FileNotFoundError as nf_oldfile6:
        print("Not found", nf_oldfile6)

    print("!!! All files have been deleted !!!")
    