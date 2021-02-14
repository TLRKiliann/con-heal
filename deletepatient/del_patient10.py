#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    To delete all files for patient 10
    when usr delete patient by pressing
    the delete button.
"""


import os
import subprocess
import shutil


def delFuncFile10():
    """
        This function delete all files with
        a test before removing files.
    """
    backproc = subprocess.run(["scp", "-r", "./Backup/Files10",
        "pi@192.168.18.12:~/tt_doc/doc_txt10/Backup10"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(backproc.stderr))
    if backproc.stderr == b'':
        print("+ File Backup10 uploaded !")
        #messagebox.showinfo("INFO", "entryfile8.txt uploaded...")
    else:
        print("+ No folder to upload !")
        messagebox.showerror("Error", "No Backup10 to upload...")

    try:
        if os.path.getsize('./need/doc_suivi10/main_14b.txt'):
            os.remove('./need/doc_suivi10/main_14b.txt')
            print("+ File main_14b.txt deleted")
    except FileNotFoundError as filefunc1:
        print("+ File main_14b.txt does not exist", filefunc1)

    try:
        if os.path.getsize('./need/doc_suivi10/patient10_14b.txt'):
            os.remove('./need/doc_suivi10/patient10_14b.txt')
            print("+ File patient10_14b.txt deleted")
    except FileNotFoundError as filefunc2:
        print("+ File patient10_14b.txt does not exist", filefunc2)

    try:
        if os.path.getsize('./ttt/doc_ttt10/convdose.json'):
            os.remove('./ttt/doc_ttt10/convdose.json')
            print("+ File convdose.json deleted")
    except FileNotFoundError as filefunc3:
        print("+ File convdose.json does not exist", filefunc3)

    try:
        if os.path.getsize('./ttt/doc_ttt10/intro_ttt.txt'):
            os.remove('./ttt/doc_ttt10/intro_ttt.txt')
            print("+ File intro_ttt.txt deleted")
    except FileNotFoundError as filefunc4:
        print("+ File intro_ttt.txt does not exist", filefunc4)

    try:
        if os.path.getsize('./ttt/doc_ttt10/convres.json'):
            os.remove('./ttt/doc_ttt10/convres.json')
            print("+ File convres.json deleted")
    except FileNotFoundError as filefunc5:
        print("+ File convres.json does not exist", filefunc5)

    try:
        if os.path.getsize('./ttt/doc_ttt10/intro_res.txt'):
            os.remove('./ttt/doc_ttt10/intro_res.txt')
            print("+ File intro_res.txt deleted")
    except FileNotFoundError as filefunc6:
        print("+ File intro_res.txt does not exist", filefunc6)

    try:
        if os.path.getsize('./param/paramdata10.txt'):
            os.remove('./param/paramdata10.txt')
            print("+ File paramdata10.txt deleted")
    except FileNotFoundError as filefunc61:
        print("+ File paramdata10.txt does not exist", filefunc61)

    try:
        if os.path.getsize('./param/aspifile10/diastol.json'):
            os.remove('./param/aspifile10/diastol.json')
            print("+ File diastol.json deleted")
    except FileNotFoundError as filefunc62:
        print("+ File diastol.json does not exist", filefunc62)

    try:
        if os.path.getsize('./param/aspifile10/dlr.json'):
            os.remove('./param/aspifile10/dlr.json')
            print("+ File dlr.json deleted")
    except FileNotFoundError as filefunc63:
        print("+ File dlr.json does not exist", filefunc63)

    try:
        if os.path.getsize('./param/aspifile10/freq.json'):
            os.remove('./param/aspifile10/freq.json')
            print("+ File freq.json deleted")
    except FileNotFoundError as filefunc64:
        print("+ File freq.json does not exist", filefunc64)

    try:
        if os.path.getsize('./param/aspifile10/gly.json'):
            os.remove('./param/aspifile10/gly.json')
            print("+ File gly.json deleted")
    except FileNotFoundError as filefunc65:
        print("+ File gly.json does not exist", filefunc65)

    try:
        if os.path.getsize('./param/aspifile10/puls.json'):
            os.remove('./param/aspifile10/puls.json')
            print("+ File puls.json deleted")
    except FileNotFoundError as filefunc66:
        print("+ File puls.json does not exist", filefunc66)

    try:
        if os.path.getsize('./param/aspifile10/sat.json'):
            os.remove('./param/aspifile10/sat.json')
            print("+ File sat.json deleted")
    except FileNotFoundError as filefunc67:
        print("+ File sat.json does not exist", filefunc67)

    try:
        if os.path.getsize('./param/aspifile10/systol.json'):
            os.remove('./param/aspifile10/systol.json')
            print("+ File systol.json deleted")
    except FileNotFoundError as filefunc68:
        print("+ File systol.json does not exist", filefunc68)

    try:
        if os.path.getsize('./param/aspifile10/temp.json'):
            os.remove('./param/aspifile10/temp.json')
            print("+ File temp.json deleted")
    except FileNotFoundError as filefunc69:
        print("+ File temp.json does not exist", filefunc69)

    try:
        if os.path.getsize('./calBmi/doc_BMI10/file_bmi.json'):
            os.remove('./calBmi/doc_BMI10/file_bmi.json')
            print("+ File file_bmi.json deleted")
    except FileNotFoundError as filefunc7:
        print("+ File file_bmi.json does not exist", filefunc7)

    try:
        if os.path.getsize('./calBmi/doc_BMI10/file_kg.json'):
            os.remove('./calBmi/doc_BMI10/file_kg.json')
            print("+ File file_kg.json deleted")
    except FileNotFoundError as filefunc8:
        print("+ File file_kg.json does not exist", filefunc8)

    try:
        if os.path.getsize('./calBmi/doc_BMI10/custom_kg.txt'):
            os.remove('./calBmi/doc_BMI10/custom_kg.txt')
            print("+ File custom_kg.txt deleted")
    except FileNotFoundError as filefunc81:
        print("+ File custom_kg.txt does not exist", filefunc81)

    try:
        if os.path.getsize('./calBmi/bmi10.txt'):
            os.remove('./calBmi/bmi10.txt')
            print("+ File bmi10.txt deleted")
    except FileNotFoundError as filefunc9:
        print("+ File bmi10.txt does not exist", filefunc9)

    try:
        if os.path.getsize('./diag/doc_diag10/diagrecap10.txt'):
            os.remove('./diag/doc_diag10/diagrecap10.txt')
            print("+ File diagrecap10.txt deleted")
    except FileNotFoundError as filefunc10:
        print("+ File diagrecap10.txt does not exist", filefunc10)

    try:
        if os.path.getsize('./labo/doc_labo/result10.txt'):
            os.remove('./labo/doc_labo/result10.txt')
            print("+ File result10.txt deleted")
    except FileNotFoundError as filefunc11:
        print("+ File result10.txt does not exist", filefunc11)

    try:
        if os.path.getsize('./patient_agenda/events10/doc_events/fix_agenda/fixed_rdv.txt'):
            os.remove('./patient_agenda/events10/doc_events/fix_agenda/fixed_rdv.txt')
            print("+ File fixed_rdv.txt deleted")
    except FileNotFoundError as filefunc12:
        print("+ File fixed_rdv.txt does not exist", filefunc12)

    try:
        if os.path.getsize('./patient_agenda/events10/doc_events/fix_agenda/modifrdv.txt'):
            os.remove('./patient_agenda/events10/doc_events/fix_agenda/modifrdv.txt')
            print("+ File modifrdv.txt deleted")
    except FileNotFoundError as filefunc13:
        print("+ File modifrdv.txt does not exist", filefunc13)

    try:
        if os.path.getsize('./patient_agenda/events10/doc_events/fix_agenda/patient_value.json'):
            os.remove('./patient_agenda/events10/doc_events/fix_agenda/patient_value.json')
            print("+ File patient_value.json deleted")
    except FileNotFoundError as filefunc14:
        print("+ File patient_value.json does not exist", filefunc14)

    try:
        if os.path.getsize('./patient_agenda/events10/doc_events/patient_rdv.json'):
            os.remove('./patient_agenda/events10/doc_events/patient_rdv.json')
            print("+ File patient_rdv.json deleted")
    except FileNotFoundError as filefunc15:
        print("+ File patient_rdv.json does not exist", filefunc15)

    try:
        if os.path.getsize('./patient_agenda/events10/patient_calendar.txt'):
            os.remove('./patient_agenda/events10/patient_calendar.txt')
            print("+ File patient_calendar.txt deleted")
    except FileNotFoundError as filefunc16:
        print("+ File patient_calendar.txt does not exist", filefunc16)

    try:
        if os.path.getsize('./vmed/doc_vmed10/resultvmed10.txt'):
            os.remove('./vmed/doc_vmed10/resultvmed10.txt')
            print("+ File resultvmed10.txt deleted")
    except FileNotFoundError as filefunc17:
        print("+ File resultvmed10.txt does not exist", filefunc17)

    try:
        if os.path.getsize('./allergy/allergyfile10.txt'):
            os.remove('./allergy/allergyfile10.txt')
            print("+ File allergyfile10.txt deleted")
    except FileNotFoundError as filefunc18:
        print("+ File allergyfile10.txt does not exist", filefunc18)

    try:
        if os.path.getsize('./newpatient/entryfile10.txt'):
            with open('./newpatient/entryfile10.txt', 'w') as file:
                file.write("----------")
            print("+ File entryfile10.txt deleted")
    except FileNotFoundError as filefunc19:
        print("+ File entryfile10.txt does not exist", filefunc19)

    proc = subprocess.run(["scp", "./newpatient/entryfile10.txt",
        "pi@192.168.18.12:~/tt_doc/doc_txt10/Files10/entryfile10.txt"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File entryfile10.txt uploaded !")
        #messagebox.showinfo("INFO", "entryfile10.txt uploaded...")
    else:
        print("+ No file to upload !")
        messagebox.showerror("Error", "No entryfile10.txt to upload...")

    try:
        if os.path.exists('./Backup/Files10/Backup_param10.txt'):
            print("+ Backup_param10.txt exist")
            shutil.copy('./Backup/Files10/Backup_param10.txt',
                './Backup/old/oldfiles10/Backup_param10.txt')
            os.remove('./Backup/Files10/Backup_param10.txt')
    except FileNotFoundError as nf_param:
        print("Not found", nf_param)

    try:
        if os.path.exists('./Backup/Files10/Backup_patient10.txt'):
            print("+ Backup_patient10.txt exist")
            shutil.copy('./Backup/Files10/Backup_patient10.txt',
                './Backup/old/oldfiles10/Backup_patient10.txt')
            os.remove('./Backup/Files10/Backup_patient10.txt')
    except FileNotFoundError as nf_oldfile:
        print("Not found", nf_oldfile)

    try:
        if os.path.exists('./Backup/Files10/Backup_careneeds10.txt'):
            print("+ Backup_careneeds10.txt exist")
            shutil.copy('./Backup/Files10/Backup_careneeds10.txt',
                './Backup/old/oldfiles10/Backup_careneeds10.txt')
            os.remove('./Backup/Files10/Backup_careneeds10.txt')
    except FileNotFoundError as nf_oldfile2:
        print("Not found", nf_oldfile2)

    try:
        if os.path.exists('./Backup/Files10/Backup_diag10.txt'):
            print("+ Backup_diag10.txt exist")
            shutil.copy('./Backup/Files10/Backup_diag10.txt',
                './Backup/old/oldfiles10/Backup_diag10.txt')
            os.remove('./Backup/Files10/Backup_diag10.txt')
    except FileNotFoundError as nf_oldfile3:
        print("Not found", nf_oldfile3)

    try:
        if os.path.exists('./Backup/Files10/Backup_Bmi10.txt'):
            print("+ Backup_Bmi10.txt exist")
            shutil.copy('./Backup/Files10/Backup_Bmi10.txt',
                './Backup/old/oldfiles10/Backup_Bmi10.txt')
            os.remove('./Backup/Files10/Backup_Bmi10.txt')
    except FileNotFoundError as nf_oldfile4:
        print("Not found", nf_oldfile4)

    try:
        if os.path.exists('./Backup/Files10/Backup_resultvmed10.txt'):
            print("+ Backup_resultvmed10.txt exist")
            shutil.copy('./Backup/Files10/Backup_resultvmed10.txt',
                './Backup/old/oldfiles10/Backup_resultvmed10.txt')
            os.remove('./Backup/Files10/Backup_resultvmed10.txt')
    except FileNotFoundError as nf_oldfile5:
        print("Not found", nf_oldfile5)

    try:
        if os.path.exists('./Backup/Files10/Backup_ttt10.txt'):
            print("+ Backup_ttt10.txt exist")
            shutil.copy('./Backup/Files10/Backup_ttt10.txt',
                './Backup/old/oldfiles10/Backup_ttt10.txt')
            os.remove('./Backup/Files10/Backup_ttt10.txt')
    except FileNotFoundError as nf_oldfile6:
        print("Not found", nf_oldfile6)

    print("!!! All files have been deleted !!!")
    