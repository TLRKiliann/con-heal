#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    To delete all files for patient 2
    when usr delete patient by pressing
    the delete button.
"""


import os
import shutil


def delFuncFile2():
    """
        This function delete all files with
        a test before removing files.
    """
    try:
        if os.path.getsize('./14besoins/doc_suivi2/main_14b.txt'):
            os.remove('./14besoins/doc_suivi2/main_14b.txt')
            print("+ File main_14b.txt deleted")
    except FileNotFoundError as filefunc1:
        print("+ File main_14b.txt does not exist", filefunc1)

    try:
        if os.path.getsize('./14besoins/doc_suivi2/patient2_14b.txt'):
            os.remove('./14besoins/doc_suivi2/patient2_14b.txt')
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

    try:
        if os.path.exists('./Backup/Files2/Backup_param2.txt'):
            print("+ Backup_param2.txt exist")
            shutil.copy('./Backup/Files2/Backup_param2.txt',
                './Backup/old/oldfiles2/Backup_param2.txt')
            os.remove('./Backup/Files2/Backup_param2.txt')
    except FileNotFoundError as nf_param:
        print("Not found", nf_param)

    try:
        if os.path.exists('./Backup/Files2/Backup_patient2.txt'):
            print("+ Backup_patient2.txt exist")
            shutil.copy('./Backup/Files2/Backup_patient2.txt',
                './Backup/old/oldfiles2/Backup_patient2.txt')
            os.remove('./Backup/Files2/Backup_patient2.txt')
    except FileNotFoundError as nf_oldfile:
        print("Not found", nf_oldfile)

    try:
        if os.path.exists('./Backup/Files2/Backup_careneeds2.txt'):
            print("+ Backup_careneeds2.txt exist")
            shutil.copy('./Backup/Files2/Backup_careneeds2.txt',
                './Backup/old/oldfiles2/Backup_careneeds2.txt')
            os.remove('./Backup/Files2/Backup_careneeds2.txt')
    except FileNotFoundError as nf_oldfile2:
        print("Not found", nf_oldfile2)

    try:
        if os.path.exists('./Backup/Files2/Backup_diag2.txt'):
            print("+ Backup_diag2.txt exist")
            shutil.copy('./Backup/Files2/Backup_diag2.txt',
                './Backup/old/oldfiles2/Backup_diag2.txt')
            os.remove('./Backup/Files2/Backup_diag2.txt')
    except FileNotFoundError as nf_oldfile3:
        print("Not found", nf_oldfile3)

    try:
        if os.path.exists('./Backup/Files2/Backup_Bmi2.txt'):
            print("+ Backup_Bmi2.txt exist")
            shutil.copy('./Backup/Files2/Backup_Bmi2.txt',
                './Backup/old/oldfiles2/Backup_Bmi2.txt')
            os.remove('./Backup/Files2/Backup_Bmi2.txt')
    except FileNotFoundError as nf_oldfile4:
        print("Not found", nf_oldfile4)

    try:
        if os.path.exists('./Backup/Files2/Backup_resultvmed2.txt'):
            print("+ Backup_resultvmed2.txt exist")
            shutil.copy('./Backup/Files2/Backup_resultvmed2.txt',
                './Backup/old/oldfiles2/Backup_resultvmed2.txt')
            os.remove('./Backup/Files2/Backup_resultvmed2.txt')
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
    