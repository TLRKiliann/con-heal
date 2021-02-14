#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    To delete all files for patient 3
    when usr delete patient by pressing
    the delete button.
"""


from tkinter import *
from tkinter import messagebox
import os
import subprocess
import shutil


def delFuncFile3():
    """
        This function delete all files with
        a test before removing files.
    """
    backproc = subprocess.run(["scp", "-r", "./Backup/Files3",
        "pi@192.168.18.12:~/tt_doc/doc_txt3/Backup3"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(backproc.stderr))
    if backproc.stderr == b'':
        print("+ File Backup3 uploaded !")
        #messagebox.showinfo("INFO", "entryfile8.txt uploaded...")
    else:
        print("+ No folder to upload !")
        messagebox.showerror("Error", "No Backup3 to upload...")

    delproc = subprocess.run(["ssh",
        "pi@192.168.18.12", "rm -r ~/tt_doc/doc_txt3/Files3/*"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(delproc.stderr))
    if delproc.stderr == b'':
        print("+ Files3 has been deleted on server !")
        messagebox.showinfo("INFO", "Files3 has been deleted on server !")
    else:
        print("!!! Error", "Not deleted Files3 on server !!!")
        messagebox.showerror("Error", "!!! Not deleted Files3 on server !!!")

    try:
        if os.path.getsize('./need/doc_suivi3/main_14b.txt'):
            os.remove('./need/doc_suivi3/main_14b.txt')
            print("+ File main_14b.txt deleted")
    except FileNotFoundError as filefunc1:
        print("+ File main_14b.txt does not exist", filefunc1)

    try:
        if os.path.getsize('./need/doc_suivi3/patient3_14b.txt'):
            os.remove('./need/doc_suivi3/patient3_14b.txt')
            print("+ File patient3_14b.txt deleted")
    except FileNotFoundError as filefunc2:
        print("+ File patient3_14b.txt does not exist", filefunc2)

    try:
        if os.path.getsize('./ttt/doc_ttt3/convdose.json'):
            os.remove('./ttt/doc_ttt3/convdose.json')
            print("+ File convdose.json deleted")
    except FileNotFoundError as filefunc3:
        print("+ File convdose.json does not exist", filefunc3)

    try:
        if os.path.getsize('./ttt/doc_ttt3/intro_ttt.txt'):
            os.remove('./ttt/doc_ttt3/intro_ttt.txt')
            print("+ File intro_ttt.txt deleted")
    except FileNotFoundError as filefunc4:
        print("+ File intro_ttt.txt does not exist", filefunc4)

    try:
        if os.path.getsize('./ttt/doc_ttt3/convres.json'):
            os.remove('./ttt/doc_ttt3/convres.json')
            print("+ File convres.json deleted")
    except FileNotFoundError as filefunc5:
        print("+ File convres.json does not exist", filefunc5)

    try:
        if os.path.getsize('./ttt/doc_ttt3/intro_res.txt'):
            os.remove('./ttt/doc_ttt3/intro_res.txt')
            print("+ File intro_res.txt deleted")
    except FileNotFoundError as filefunc6:
        print("+ File intro_res.txt does not exist", filefunc6)

    try:
        if os.path.getsize('./param/paramdata3.txt'):
            os.remove('./param/paramdata3.txt')
            print("+ File paramdata3.txt deleted")
    except FileNotFoundError as filefunc61:
        print("+ File paramdata3.txt does not exist", filefunc61)

    try:
        if os.path.getsize('./param/aspifile3/diastol.json'):
            os.remove('./param/aspifile3/diastol.json')
            print("+ File diastol.json deleted")
    except FileNotFoundError as filefunc62:
        print("+ File diastol.json does not exist", filefunc62)

    try:
        if os.path.getsize('./param/aspifile3/dlr.json'):
            os.remove('./param/aspifile3/dlr.json')
            print("+ File dlr.json deleted")
    except FileNotFoundError as filefunc63:
        print("+ File dlr.json does not exist", filefunc63)

    try:
        if os.path.getsize('./param/aspifile3/freq.json'):
            os.remove('./param/aspifile3/freq.json')
            print("+ File freq.json deleted")
    except FileNotFoundError as filefunc64:
        print("+ File freq.json does not exist", filefunc64)

    try:
        if os.path.getsize('./param/aspifile3/gly.json'):
            os.remove('./param/aspifile3/gly.json')
            print("+ File gly.json deleted")
    except FileNotFoundError as filefunc65:
        print("+ File gly.json does not exist", filefunc65)

    try:
        if os.path.getsize('./param/aspifile3/puls.json'):
            os.remove('./param/aspifile3/puls.json')
            print("+ File puls.json deleted")
    except FileNotFoundError as filefunc66:
        print("+ File puls.json does not exist", filefunc66)

    try:
        if os.path.getsize('./param/aspifile3/sat.json'):
            os.remove('./param/aspifile3/sat.json')
            print("+ File sat.json deleted")
    except FileNotFoundError as filefunc67:
        print("+ File sat.json does not exist", filefunc67)

    try:
        if os.path.getsize('./param/aspifile3/systol.json'):
            os.remove('./param/aspifile3/systol.json')
            print("+ File systol.json deleted")
    except FileNotFoundError as filefunc68:
        print("+ File systol.json does not exist", filefunc68)

    try:
        if os.path.getsize('./param/aspifile3/temp.json'):
            os.remove('./param/aspifile3/temp.json')
            print("+ File temp.json deleted")
    except FileNotFoundError as filefunc69:
        print("+ File temp.json does not exist", filefunc69)

    try:
        if os.path.getsize('./calBmi/doc_BMI3/file_bmi.json'):
            os.remove('./calBmi/doc_BMI3/file_bmi.json')
            print("+ File file_bmi.json deleted")
    except FileNotFoundError as filefunc7:
        print("+ File file_bmi.json does not exist", filefunc7)

    try:
        if os.path.getsize('./calBmi/doc_BMI3/file_kg.json'):
            os.remove('./calBmi/doc_BMI3/file_kg.json')
            print("+ File file_kg.json deleted")
    except FileNotFoundError as filefunc8:
        print("+ File file_kg.json does not exist", filefunc8)

    try:
        if os.path.getsize('./calBmi/doc_BMI3/custom_kg.txt'):
            os.remove('./calBmi/doc_BMI3/custom_kg.txt')
            print("+ File custom_kg.txt deleted")
    except FileNotFoundError as filefunc81:
        print("+ File custom_kg.txt does not exist", filefunc81)

    try:
        if os.path.getsize('./calBmi/bmi3.txt'):
            os.remove('./calBmi/bmi3.txt')
            print("+ File bmi3.txt deleted")
    except FileNotFoundError as filefunc9:
        print("+ File bmi3.txt does not exist", filefunc9)

    try:
        if os.path.getsize('./diag/doc_diag3/diagrecap3.txt'):
            os.remove('./diag/doc_diag3/diagrecap3.txt')
            print("+ File diagrecap3.txt deleted")
    except FileNotFoundError as filefunc10:
        print("+ File diagrecap3.txt does not exist", filefunc10)

    try:
        if os.path.getsize('./labo/doc_labo/result3.txt'):
            os.remove('./labo/doc_labo/result3.txt')
            print("+ File result3.txt deleted")
    except FileNotFoundError as filefunc11:
        print("+ File result3.txt does not exist", filefunc11)

    try:
        if os.path.getsize('./patient_agenda/events3/doc_events/fix_agenda/fixed_rdv.txt'):
            os.remove('./patient_agenda/events3/doc_events/fix_agenda/fixed_rdv.txt')
            print("+ File fixed_rdv.txt deleted")
    except FileNotFoundError as filefunc12:
        print("+ File fixed_rdv.txt does not exist", filefunc12)

    try:
        if os.path.getsize('./patient_agenda/events3/doc_events/fix_agenda/modifrdv.txt'):
            os.remove('./patient_agenda/events3/doc_events/fix_agenda/modifrdv.txt')
            print("+ File modifrdv.txt deleted")
    except FileNotFoundError as filefunc13:
        print("+ File modifrdv.txt does not exist", filefunc13)

    try:
        if os.path.getsize('./patient_agenda/events3/doc_events/fix_agenda/patient_value.json'):
            os.remove('./patient_agenda/events3/doc_events/fix_agenda/patient_value.json')
            print("+ File patient_value.json deleted")
    except FileNotFoundError as filefunc14:
        print("+ File patient_value.json does not exist", filefunc14)

    try:
        if os.path.getsize('./patient_agenda/events3/doc_events/patient_rdv.json'):
            os.remove('./patient_agenda/events3/doc_events/patient_rdv.json')
            print("+ File patient_rdv.json deleted")
    except FileNotFoundError as filefunc15:
        print("+ File patient_rdv.json does not exist", filefunc15)

    try:
        if os.path.getsize('./patient_agenda/events3/patient_calendar.txt'):
            os.remove('./patient_agenda/events3/patient_calendar.txt')
            print("+ File patient_calendar.txt deleted")
    except FileNotFoundError as filefunc16:
        print("+ File patient_calendar.txt does not exist", filefunc16)

    try:
        if os.path.getsize('./vmed/doc_vmed3/resultvmed3.txt'):
            os.remove('./vmed/doc_vmed3/resultvmed3.txt')
            print("+ File resultvmed3.txt.txt deleted")
    except FileNotFoundError as filefunc17:
        print("+ File resultvmed3.txt.txt does not exist", filefunc17)

    try:
        if os.path.getsize('./allergy/allergyfile3.txt'):
            os.remove('./allergy/allergyfile3.txt')
            print("+ File allergyfile3.txt deleted")
    except FileNotFoundError as filefunc18:
        print("+ File allergyfile3.txt does not exist", filefunc18)

    try:
        if os.path.getsize('./newpatient/entryfile3.txt'):
            with open('./newpatient/entryfile3.txt', 'w') as file:
                file.write("---")
            print("+ File entryfile3.txt reborn")
    except FileNotFoundError as filefunc19:
        print("+ File entryfile3.txt does not exist", filefunc19)

    proc = subprocess.run(["scp", "./newpatient/entryfile3.txt",
        "pi@192.168.18.12:~/tt_doc/doc_txt3/Files3/entryfile3.txt"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File entryfile3.txt uploaded !")
        #messagebox.showinfo("INFO", "entryfile3.txt uploaded...")
    else:
        print("+ No file to upload !")
        messagebox.showerror("Error", "No entryfile3.txt to upload...")

    try:
        if os.path.exists('./Backup/Files3/Backup_param3.txt'):
            print("+ Backup_param3.txt exist")
            shutil.copy('./Backup/Files3/Backup_param3.txt',
                './Backup/old/oldfiles3/Backup_param3.txt')
            os.remove('./Backup/Files3/Backup_param3.txt')
    except FileNotFoundError as nf_param:
        print("Not found", nf_param)

    try:
        if os.path.exists('./Backup/Files3/Backup_patient3.txt'):
            print("+ Backup_patient3.txt exist")
            shutil.copy('./Backup/Files3/Backup_patient3.txt',
                './Backup/old/oldfiles3/Backup_patient3.txt')
            os.remove('./Backup/Files3/Backup_patient3.txt')
    except FileNotFoundError as nf_oldfile:
        print("Not found", nf_oldfile)

    try:
        if os.path.exists('./Backup/Files3/Backup_careneeds3.txt'):
            print("+ Backup_careneeds3.txt exist")
            shutil.copy('./Backup/Files3/Backup_careneeds3.txt',
                './Backup/old/oldfiles3/Backup_careneeds3.txt')
            os.remove('./Backup/Files3/Backup_careneeds3.txt')
    except FileNotFoundError as nf_oldfile2:
        print("Not found", nf_oldfile2)

    try:
        if os.path.exists('./Backup/Files3/Backup_diag3.txt'):
            print("+ Backup_diag3.txt exist")
            shutil.copy('./Backup/Files3/Backup_diag3.txt',
                './Backup/old/oldfiles3/Backup_diag3.txt')
            os.remove('./Backup/Files3/Backup_diag3.txt')
    except FileNotFoundError as nf_oldfile3:
        print("Not found", nf_oldfile3)

    try:
        if os.path.exists('./Backup/Files3/Backup_Bmi3.txt'):
            print("+ Backup_Bmi3.txt exist")
            shutil.copy('./Backup/Files3/Backup_Bmi3.txt',
                './Backup/old/oldfiles3/Backup_Bmi3.txt')
            os.remove('./Backup/Files3/Backup_Bmi3.txt')
    except FileNotFoundError as nf_oldfile4:
        print("Not found", nf_oldfile4)

    try:
        if os.path.exists('./Backup/Files3/Backup_resultvmed3.txt'):
            print("+ Backup_resultvmed3.txt exist")
            shutil.copy('./Backup/Files3/Backup_resultvmed3.txt',
                './Backup/old/oldfiles3/Backup_resultvmed3.txt')
            os.remove('./Backup/Files3/Backup_resultvmed3.txt')
    except FileNotFoundError as nf_oldfile5:
        print("Not found", nf_oldfile5)

    try:
        if os.path.exists('./Backup/Files3/Backup_ttt3.txt'):
            print("+ Backup_ttt3.txt exist")
            shutil.copy('./Backup/Files3/Backup_ttt3.txt',
                './Backup/old/oldfiles3/Backup_ttt3.txt')
            os.remove('./Backup/Files3/Backup_ttt3.txt')
    except FileNotFoundError as nf_oldfile6:
        print("Not found", nf_oldfile6)

    print("!!! All files have been deleted !!!")
    