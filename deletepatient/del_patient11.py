#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    To delete all files for patient 11
    when usr delete patient by pressing
    the delete button.
"""


import os


def delFuncFile11():
    """
        This function delete all files with
        a test before removing files.
    """
    try:
        if os.path.getsize('./14besoins/doc_suivi11/main_14b.txt'):
            os.remove('./14besoins/doc_suivi11/main_14b.txt')
            print("+ File main_14b.txt deleted")
    except FileNotFoundError as filefunc1:
        print("+ File main_14b.txt does not exist", filefunc1)

    try:
        if os.path.getsize('./14besoins/doc_suivi11/patient11_14b.txt'):
            os.remove('./14besoins/doc_suivi11/patient11_14b.txt')
            print("+ File patient11_14b.txt deleted")
    except FileNotFoundError as filefunc2:
        print("+ File patient11_14b.txt does not exist", filefunc2)

    try:
        if os.path.getsize('./ttt/doc_ttt11/convdose.json'):
            os.remove('./ttt/doc_ttt11/convdose.json')
            print("+ File convdose.json deleted")
    except FileNotFoundError as filefunc3:
        print("+ File convdose.json does not exist", filefunc3)

    try:
        if os.path.getsize('./ttt/doc_ttt11/intro_ttt.txt'):
            os.remove('./ttt/doc_ttt11/intro_ttt.txt')
            print("+ File intro_ttt.txt deleted")
    except FileNotFoundError as filefunc4:
        print("+ File intro_ttt.txt does not exist", filefunc4)

    try:
        if os.path.getsize('./ttt/doc_ttt11/convres.json'):
            os.remove('./ttt/doc_ttt11/convres.json')
            print("+ File convres.json deleted")
    except FileNotFoundError as filefunc5:
        print("+ File convres.json does not exist", filefunc5)

    try:
        if os.path.getsize('./ttt/doc_ttt11/intro_res.txt'):
            os.remove('./ttt/doc_ttt11/intro_res.txt')
            print("+ File intro_res.txt deleted")
    except FileNotFoundError as filefunc6:
        print("+ File intro_res.txt does not exist", filefunc6)

    try:
        if os.path.getsize('./calBmi/doc_BMI11/file_bmi.json'):
            os.remove('./calBmi/doc_BMI11/file_bmi.json')
            print("+ File file_bmi.json deleted")
    except FileNotFoundError as filefunc7:
        print("+ File file_bmi.json does not exist", filefunc7)

    try:
        if os.path.getsize('./calBmi/doc_BMI11/file_kg.json'):
            os.remove('./calBmi/doc_BMI11/file_kg.json')
            print("+ File file_kg.json deleted")
    except FileNotFoundError as filefunc8:
        print("+ File file_kg.json does not exist", filefunc8)

    try:
        if os.path.getsize('./calBmi/doc_BMI11/custom_kg.txt'):
            os.remove('./calBmi/doc_BMI11/custom_kg.txt')
            print("+ File custom_kg.txt deleted")
    except FileNotFoundError as filefunc81:
        print("+ File custom_kg.txt does not exist", filefunc81)

    try:
        if os.path.getsize('./calBmi/bmi11.txt'):
            os.remove('./calBmi/bmi11.txt')
            print("+ File bmi11.txt deleted")
    except FileNotFoundError as filefunc9:
        print("+ File bmi11.txt does not exist", filefunc9)

    try:
        if os.path.getsize('./diag/doc_diag11/diagrecap11.txt'):
            os.remove('./diag/doc_diag11/diagrecap11.txt')
            print("+ File diagrecap11.txt deleted")
    except FileNotFoundError as filefunc10:
        print("+ File diagrecap11.txt does not exist", filefunc10)

    try:
        if os.path.getsize('./labo/doc_labo/result11.txt'):
            os.remove('./labo/doc_labo/result11.txt')
            print("+ File result11.txt deleted")
    except FileNotFoundError as filefunc11:
        print("+ File result11.txt does not exist", filefunc11)

    try:
        if os.path.getsize('./patient_agenda/events11/doc_events/fix_agenda/fixed_rdv.txt'):
            os.remove('./patient_agenda/events11/doc_events/fix_agenda/fixed_rdv.txt')
            print("+ File fixed_rdv.txt deleted")
    except FileNotFoundError as filefunc12:
        print("+ File fixed_rdv.txt does not exist", filefunc12)

    try:
        if os.path.getsize('./patient_agenda/events11/doc_events/fix_agenda/modifrdv.txt'):
            os.remove('./patient_agenda/events11/doc_events/fix_agenda/modifrdv.txt')
            print("+ File modifrdv.txt deleted")
    except FileNotFoundError as filefunc13:
        print("+ File modifrdv.txt does not exist", filefunc13)

    try:
        if os.path.getsize('./patient_agenda/events11/doc_events/fix_agenda/patient_value.json'):
            os.remove('./patient_agenda/events11/doc_events/fix_agenda/patient_value.json')
            print("+ File patient_value.json deleted")
    except FileNotFoundError as filefunc14:
        print("+ File patient_value.json does not exist", filefunc14)

    try:
        if os.path.getsize('./patient_agenda/events11/doc_events/patient_rdv.json'):
            os.remove('./patient_agenda/events11/doc_events/patient_rdv.json')
            print("+ File patient_rdv.json deleted")
    except FileNotFoundError as filefunc15:
        print("+ File patient_rdv.json does not exist", filefunc15)

    try:
        if os.path.getsize('./patient_agenda/events11/patient_calendar.txt'):
            os.remove('./patient_agenda/events11/patient_calendar.txt')
            print("+ File patient_calendar.txt deleted")
    except FileNotFoundError as filefunc16:
        print("+ File patient_calendar.txt does not exist", filefunc16)

    try:
        if os.path.getsize('./vmed/doc_vmed11/resultvmed11.txt'):
            os.remove('./vmed/doc_vmed11/resultvmed11.txt')
            print("+ File resultvmed11.txt deleted")
    except FileNotFoundError as filefunc17:
        print("+ File resultvmed11.txt does not exist", filefunc17)

    try:
        if os.path.getsize('./allergy/allergyfile11.txt'):
            os.remove('./allergy/allergyfile11.txt')
            print("+ File allergyfile11.txt deleted")
    except FileNotFoundError as filefunc18:
        print("+ File allergyfile11.txt does not exist", filefunc18)

    try:
        if os.path.getsize('./newpatient/entryfile11.txt'):
            with open('./newpatient/entryfile11.txt', 'w') as file:
                file.write("-----------")
            print("+ File entryfile11.txt deleted")
    except FileNotFoundError as filefunc19:
        print("+ File entryfile11.txt does not exist", filefunc19)

    try:
        if os.path.exists('./Backup/Files11/Backup_param11.txt'):
            print("+ Backup_param11.txt exist")
            shutil.copy('./Backup/Files11/Backup_param11.txt',
                './Backup/old/oldfiles11/Backup_param11.txt')
            os.remove('./Backup/Files11/Backup_param11.txt')
    except FileNotFoundError as nf_param:
        print("Not found", nf_param)

    try:
        if os.path.exists('./Backup/Files11/Backup_patient11.txt'):
            print("+ Backup_patient11.txt exist")
            shutil.copy('./Backup/Files11/Backup_patient11.txt',
                './Backup/old/oldfiles11/Backup_patient11.txt')
            os.remove('./Backup/Files11/Backup_patient11.txt')
    except FileNotFoundError as nf_oldfile:
        print("Not found", nf_oldfile)

    try:
        if os.path.exists('./Backup/Files11/Backup_careneeds11.txt'):
            print("+ Backup_careneeds11.txt exist")
            shutil.copy('./Backup/Files11/Backup_careneeds11.txt',
                './Backup/old/oldfiles11/Backup_careneeds11.txt')
            os.remove('./Backup/Files11/Backup_careneeds11.txt')
    except FileNotFoundError as nf_oldfile2:
        print("Not found", nf_oldfile2)

    try:
        if os.path.exists('./Backup/Files11/Backup_diag11.txt'):
            print("+ Backup_diag11.txt exist")
            shutil.copy('./Backup/Files11/Backup_diag11.txt',
                './Backup/old/oldfiles11/Backup_diag11.txt')
            os.remove('./Backup/Files11/Backup_diag11.txt')
    except FileNotFoundError as nf_oldfile3:
        print("Not found", nf_oldfile3)

    try:
        if os.path.exists('./Backup/Files11/Backup_Bmi11.txt'):
            print("+ Backup_Bmi11.txt exist")
            shutil.copy('./Backup/Files11/Backup_Bmi11.txt',
                './Backup/old/oldfiles11/Backup_Bmi11.txt')
            os.remove('./Backup/Files11/Backup_Bmi11.txt')
    except FileNotFoundError as nf_oldfile4:
        print("Not found", nf_oldfile4)

    try:
        if os.path.exists('./Backup/Files11/Backup_resultvmed11.txt'):
            print("+ Backup_resultvmed11.txt exist")
            shutil.copy('./Backup/Files11/Backup_resultvmed11.txt',
                './Backup/old/oldfiles11/Backup_resultvmed11.txt')
            os.remove('./Backup/Files11/Backup_resultvmed11.txt')
    except FileNotFoundError as nf_oldfile5:
        print("Not found", nf_oldfile5)

    try:
        if os.path.exists('./Backup/Files11/Backup_ttt11.txt'):
            print("+ Backup_ttt11.txt exist")
            shutil.copy('./Backup/Files11/Backup_ttt11.txt',
                './Backup/old/oldfiles11/Backup_ttt11.txt')
            os.remove('./Backup/Files11/Backup_ttt11.txt')
    except FileNotFoundError as nf_oldfile6:
        print("Not found", nf_oldfile6)

    print("!!! All files have been deleted !!!")
    