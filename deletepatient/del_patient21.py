#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    To delete all files for patient 21
    when usr delete patient by pressing
    the delete button.
"""


from tkinter import *
from tkinter import messagebox
import os
import subprocess
import shutil


def delFuncFile21():
    """
        This function delete all files with
        a test before removing files.
    """
    backproc = subprocess.run(["scp", "-r", "./Backup/Files21",
        "pi@192.168.18.12:~/tt_doc/doc_txt21/Backup21"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(backproc.stderr))
    if backproc.stderr == b'':
        print("+ Backup21 done on server ! !")
        messagebox.showinfo("INFO", "Backup21 done on server !")
    else:
        print("!!! No Backup21 done on server !!!")
        messagebox.showerror("Error", "!!! No Backup21 done on server !!!")

    delproc = subprocess.run(["ssh",
        "pi@192.168.18.12", "rm -r ~/tt_doc/doc_txt21/Files21/*"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(delproc.stderr))
    if delproc.stderr == b'':
        print("+ Files21 has been deleted on server !")
        messagebox.showinfo("INFO", "Files21 has been deleted on server !")
    else:
        print("!!! Error", "Not deleted Files21 on server !!!")
        messagebox.showerror("Error", "!!! Not deleted Files21 on server !!!")

    try:
        if os.path.getsize('./need/doc_suivi21/main_14b.txt'):
            os.remove('./need/doc_suivi21/main_14b.txt')
            print("+ File main_14b.txt deleted")
    except FileNotFoundError as filefunc1:
        print("+ File main_14b.txt does not exist", filefunc1)

    try:
        if os.path.getsize('./need/doc_suivi21/patient21_14b.txt'):
            os.remove('./need/doc_suivi21/patient21_14b.txt')
            print("+ File patient21_14b.txt deleted")
    except FileNotFoundError as filefunc2:
        print("+ File patient21_14b.txt does not exist", filefunc2)

    try:
        if os.path.getsize('./ttt/doc_ttt21/convdose.json'):
            os.remove('./ttt/doc_ttt21/convdose.json')
            print("+ File convdose.json deleted")
    except FileNotFoundError as filefunc3:
        print("+ File convdose.json does not exist", filefunc3)

    try:
        if os.path.getsize('./ttt/doc_ttt21/intro_ttt.txt'):
            os.remove('./ttt/doc_ttt21/intro_ttt.txt')
            print("+ File intro_ttt.txt deleted")
    except FileNotFoundError as filefunc4:
        print("+ File intro_ttt.txt does not exist", filefunc4)

    try:
        if os.path.getsize('./ttt/doc_ttt21/convres.json'):
            os.remove('./ttt/doc_ttt21/convres.json')
            print("+ File convres.json deleted")
    except FileNotFoundError as filefunc5:
        print("+ File convres.json does not exist", filefunc5)

    try:
        if os.path.getsize('./ttt/doc_ttt21/intro_res.txt'):
            os.remove('./ttt/doc_ttt21/intro_res.txt')
            print("+ File intro_res.txt deleted")
    except FileNotFoundError as filefunc6:
        print("+ File intro_res.txt does not exist", filefunc6)

    try:
        if os.path.getsize('./param/paramdata21.txt'):
            os.remove('./param/paramdata21.txt')
            print("+ File paramdata21.txt deleted")
    except FileNotFoundError as filefunc61:
        print("+ File paramdata21.txt does not exist", filefunc61)

    try:
        if os.path.getsize('./param/aspifile21/diastol.json'):
            os.remove('./param/aspifile21/diastol.json')
            print("+ File diastol.json deleted")
    except FileNotFoundError as filefunc62:
        print("+ File diastol.json does not exist", filefunc62)

    try:
        if os.path.getsize('./param/aspifile21/dlr.json'):
            os.remove('./param/aspifile21/dlr.json')
            print("+ File dlr.json deleted")
    except FileNotFoundError as filefunc63:
        print("+ File dlr.json does not exist", filefunc63)

    try:
        if os.path.getsize('./param/aspifile21/freq.json'):
            os.remove('./param/aspifile21/freq.json')
            print("+ File freq.json deleted")
    except FileNotFoundError as filefunc64:
        print("+ File freq.json does not exist", filefunc64)

    try:
        if os.path.getsize('./param/aspifile21/gly.json'):
            os.remove('./param/aspifile21/gly.json')
            print("+ File gly.json deleted")
    except FileNotFoundError as filefunc65:
        print("+ File gly.json does not exist", filefunc65)

    try:
        if os.path.getsize('./param/aspifile21/puls.json'):
            os.remove('./param/aspifile21/puls.json')
            print("+ File puls.json deleted")
    except FileNotFoundError as filefunc66:
        print("+ File puls.json does not exist", filefunc66)

    try:
        if os.path.getsize('./param/aspifile21/sat.json'):
            os.remove('./param/aspifile21/sat.json')
            print("+ File sat.json deleted")
    except FileNotFoundError as filefunc67:
        print("+ File sat.json does not exist", filefunc67)

    try:
        if os.path.getsize('./param/aspifile21/systol.json'):
            os.remove('./param/aspifile21/systol.json')
            print("+ File systol.json deleted")
    except FileNotFoundError as filefunc68:
        print("+ File systol.json does not exist", filefunc68)

    try:
        if os.path.getsize('./param/aspifile21/temp.json'):
            os.remove('./param/aspifile21/temp.json')
            print("+ File temp.json deleted")
    except FileNotFoundError as filefunc69:
        print("+ File temp.json does not exist", filefunc69)

    try:
        if os.path.getsize('./calBmi/doc_BMI21/file_bmi.json'):
            os.remove('./calBmi/doc_BMI21/file_bmi.json')
            print("+ File file_bmi.json deleted")
    except FileNotFoundError as filefunc7:
        print("+ File file_bmi.json does not exist", filefunc7)

    try:
        if os.path.getsize('./calBmi/doc_BMI21/file_kg.json'):
            os.remove('./calBmi/doc_BMI21/file_kg.json')
            print("+ File file_kg.json deleted")
    except FileNotFoundError as filefunc8:
        print("+ File file_kg.json does not exist", filefunc8)

    try:
        if os.path.getsize('./calBmi/doc_BMI21/custom_kg.txt'):
            os.remove('./calBmi/doc_BMI21/custom_kg.txt')
            print("+ File custom_kg.txt deleted")
    except FileNotFoundError as filefunc81:
        print("+ File custom_kg.txt does not exist", filefunc81)

    try:
        if os.path.getsize('./calBmi/bmi21.txt'):
            os.remove('./calBmi/bmi21.txt')
            print("+ File bmi21.txt deleted")
    except FileNotFoundError as filefunc9:
        print("+ File bmi21.txt does not exist", filefunc9)

    try:
        if os.path.getsize('./diag/doc_diag21/diagrecap21.txt'):
            os.remove('./diag/doc_diag21/diagrecap21.txt')
            print("+ File diagrecap21.txt deleted")
    except FileNotFoundError as filefunc10:
        print("+ File diagrecap21.txt does not exist", filefunc10)

    try:
        if os.path.getsize('./labo/doc_labo/result21.txt'):
            os.remove('./labo/doc_labo/result21.txt')
            print("+ File result21.txt deleted")
    except FileNotFoundError as filefunc11:
        print("+ File result21.txt does not exist", filefunc11)

    try:
        if os.path.getsize('./patient_agenda/events21/doc_events/fix_agenda/fixed_rdv.txt'):
            os.remove('./patient_agenda/events21/doc_events/fix_agenda/fixed_rdv.txt')
            print("+ File fixed_rdv.txt deleted")
    except FileNotFoundError as filefunc12:
        print("+ File fixed_rdv.txt does not exist", filefunc12)

    try:
        if os.path.getsize('./patient_agenda/events21/doc_events/fix_agenda/modifrdv.txt'):
            os.remove('./patient_agenda/events21/doc_events/fix_agenda/modifrdv.txt')
            print("+ File modifrdv.txt deleted")
    except FileNotFoundError as filefunc13:
        print("+ File modifrdv.txt does not exist", filefunc13)

    try:
        if os.path.getsize('./patient_agenda/events21/doc_events/fix_agenda/patient_value.json'):
            os.remove('./patient_agenda/events21/doc_events/fix_agenda/patient_value.json')
            print("+ File patient_value.json deleted")
    except FileNotFoundError as filefunc14:
        print("+ File patient_value.json does not exist", filefunc14)

    try:
        if os.path.getsize('./patient_agenda/events21/doc_events/patient_rdv.json'):
            os.remove('./patient_agenda/events21/doc_events/patient_rdv.json')
            print("+ File patient_rdv.json deleted")
    except FileNotFoundError as filefunc15:
        print("+ File patient_rdv.json does not exist", filefunc15)

    try:
        if os.path.getsize('./patient_agenda/events21/patient_calendar.txt'):
            os.remove('./patient_agenda/events21/patient_calendar.txt')
            print("+ File patient_calendar.txt deleted")
    except FileNotFoundError as filefunc16:
        print("+ File patient_calendar.txt does not exist", filefunc16)

    try:
        if os.path.getsize('./vmed/doc_vmed21/resultvmed21.txt'):
            os.remove('./vmed/doc_vmed21/resultvmed21.txt')
            print("+ File resultvmed21.txt deleted")
    except FileNotFoundError as filefunc17:
        print("+ File resultvmed21.txt does not exist", filefunc17)

    try:
        if os.path.getsize('./allergy/allergyfile21.txt'):
            os.remove('./allergy/allergyfile21.txt')
            print("+ File allergyfile21.txt deleted")
    except FileNotFoundError as filefunc18:
        print("+ File allergyfile21.txt does not exist", filefunc18)

    try:
        if os.path.getsize('./newpatient/entryfile21.txt'):
            with open('./newpatient/entryfile21.txt', 'w') as file:
                file.write("---------------------")
            print("+ File entryfile21.txt deleted")
    except FileNotFoundError as filefunc19:
        print("+ File entryfile21.txt does not exist", filefunc19)

    proc = subprocess.run(["scp", "./newpatient/entryfile21.txt",
        "pi@192.168.18.12:~/tt_doc/doc_txt21/Files21/entryfile21.txt"],
        stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ File entryfile21.txt uploaded !")
        #messagebox.showinfo("INFO", "entryfile21.txt uploaded...")
    else:
        print("+ No file to upload !")
        messagebox.showerror("Error", "No entryfile21.txt to upload...")

    try:
        if os.path.getsize('./auxequip/doc_equip21/auxiliary1.txt'):
            os.remove('./auxequip/doc_equip21/auxiliary1.txt')
            print("+ File auxiliary1.txt deleted")
    except FileNotFoundError as filefunc20:
        print("+ File auxiliary1.txt does not exist", filefunc20)

    try:
        if os.path.getsize('./contact/conpact21/finalfile1.txt'):
            os.remove('./contact/conpact21/finalfile1.txt')
            print("+ File finalfile1.txt deleted")
    except FileNotFoundError as filefunc21:
        print("+ File finalfile1.txt does not exist", filefunc21)

    try:
        if os.path.getsize('./contact/conpact21/finaldoc1.txt'):
            os.remove('./contact/conpact21/finaldoc1.txt')
            print("+ File finaldoc1.txt deleted")
    except FileNotFoundError as filefunc22:
        print("+ File finaldoc1.txt does not exist", filefunc22)

    try:
        if os.path.getsize('./contact/conpact21/finaldoc2.txt'):
            os.remove('./contact/conpact21/finaldoc2.txt')
            print("+ File finaldoc2.txt deleted")
    except FileNotFoundError as filefunc23:
        print("+ File finaldoc2.txt does not exist", filefunc23)

    try:
        if os.path.getsize('./contact/conpact21/finaldoc3.txt'):
            os.remove('./contact/conpact21/finaldoc3.txt')
            print("+ File finaldoc3.txt deleted")
    except FileNotFoundError as filefunc24:
        print("+ File finaldoc3.txt does not exist", filefunc24)

    try:
        if os.path.getsize('./contact/conpact21/finalfam1.txt'):
            os.remove('./contact/conpact21/finalfam1.txt')
            print("+ File finalfam1.txt deleted")
    except FileNotFoundError as filefunc25:
        print("+ File finalfam1.txt does not exist", filefunc25)

    try:
        if os.path.getsize('./contact/conpact21/finalhcs1.txt'):
            os.remove('./contact/conpact21/finalhcs1.txt')
            print("+ File finalhcs1.txt deleted")
    except FileNotFoundError as filefunc26:
        print("+ File finalhcs1.txt does not exist", filefunc26)

    try:
        if os.path.getsize('./contact/conpact21/finalhcs2.txt'):
            os.remove('./contact/conpact21/finalhcs2.txt')
            print("+ File finalhcs2.txt deleted")
    except FileNotFoundError as filefunc27:
        print("+ File finalhcs2.txt does not exist", filefunc27)

    try:
        if os.path.getsize('./contact/conpact21/finalhcs3.txt'):
            os.remove('./contact/conpact21/finalhcs3.txt')
            print("+ File finalhcs3.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File finalhcs3.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./medidoc/doc_dmst21/parcours.txt'):
            os.remove('./medidoc/doc_dmst21/parcours.txt')
            print("+ File parcours.txt deleted")
    except FileNotFoundError as filefunc29:
        print("+ File parcours.txt does not exist", filefunc29)

    try:
        if os.path.getsize('./medidoc/doc_dmst21/pbm.txt'):
            os.remove('./medidoc/doc_dmst21/pbm.txt')
            print("+ File pbm.txt deleted")
    except FileNotFoundError as filefunc30:
        print("+ File pbm.txt does not exist", filefunc30)

    try:
        if os.path.getsize('./medidoc/doc_dmst21/project.txt'):
            os.remove('./medidoc/doc_dmst21/project.txt')
            print("+ File project.txt deleted")
    except FileNotFoundError as filefunc31:
        print("+ File project.txt does not exist", filefunc31)

    try:
        if os.path.getsize('./medidoc/doc_dmst21/rslt_dmst1.txt'):
            os.remove('./medidoc/doc_dmst21/rslt_dmst1.txt')
            print("+ File rslt_dmst1.txt deleted")
    except FileNotFoundError as filefunc32:
        print("+ File rslt_dmst1.txt does not exist", filefunc32)

    try:
        if os.path.exists('./Backup/Files21/Backup_param21.txt'):
            print("+ Backup_param21.txt exist")
            shutil.copy('./Backup/Files21/Backup_param21.txt',
                './Backup/old/oldfiles21/Backup_param21.txt')
            os.remove('./Backup/Files21/Backup_param21.txt')
    except FileNotFoundError as nf_param:
        print("Not found", nf_param)

    try:
        if os.path.exists('./Backup/Files21/Backup_patient21.txt'):
            print("+ Backup_patient21.txt exist")
            shutil.copy('./Backup/Files21/Backup_patient21.txt',
                './Backup/old/oldfiles21/Backup_patient21.txt')
            os.remove('./Backup/Files21/Backup_patient21.txt')
    except FileNotFoundError as nf_oldfile:
        print("Not found", nf_oldfile)

    try:
        if os.path.exists('./Backup/Files21/Backup_careneeds21.txt'):
            print("+ Backup_careneeds21.txt exist")
            shutil.copy('./Backup/Files21/Backup_careneeds21.txt',
                './Backup/old/oldfiles21/Backup_careneeds21.txt')
            os.remove('./Backup/Files21/Backup_careneeds21.txt')
    except FileNotFoundError as nf_oldfile2:
        print("Not found", nf_oldfile2)

    try:
        if os.path.exists('./Backup/Files21/Backup_diag21.txt'):
            print("+ Backup_diag21.txt exist")
            shutil.copy('./Backup/Files21/Backup_diag21.txt',
                './Backup/old/oldfiles21/Backup_diag21.txt')
            os.remove('./Backup/Files21/Backup_diag21.txt')
    except FileNotFoundError as nf_oldfile3:
        print("Not found", nf_oldfile3)

    try:
        if os.path.exists('./Backup/Files21/Backup_Bmi21.txt'):
            print("+ Backup_Bmi21.txt exist")
            shutil.copy('./Backup/Files21/Backup_Bmi21.txt',
                './Backup/old/oldfiles21/Backup_Bmi21.txt')
            os.remove('./Backup/Files21/Backup_Bmi21.txt')
    except FileNotFoundError as nf_oldfile4:
        print("Not found", nf_oldfile4)

    try:
        if os.path.exists('./Backup/Files21/Backup_resultvmed21.txt'):
            print("+ Backup_resultvmed21.txt exist")
            shutil.copy('./Backup/Files21/Backup_resultvmed21.txt',
                './Backup/old/oldfiles21/Backup_resultvmed21.txt')
            os.remove('./Backup/Files21/Backup_resultvmed21.txt')
    except FileNotFoundError as nf_oldfile5:
        print("Not found", nf_oldfile5)

    try:
        if os.path.exists('./Backup/Files21/Backup_ttt21.txt'):
            print("+ Backup_ttt21.txt exist")
            shutil.copy('./Backup/Files21/Backup_ttt21.txt',
                './Backup/old/oldfiles21/Backup_ttt21.txt')
            os.remove('./Backup/Files21/Backup_ttt21.txt')
    except FileNotFoundError as nf_oldfile6:
        print("Not found", nf_oldfile6)

    try:
        if os.path.exists('./Backup/Files21'):
            print("+ Files21 doc exist !")
            shutil.rmtree('./Backup/Files21')
            print("+ Files21 doc deleted !")
    except OSError as doc_nf:
        print("Not found", doc_nf)

    print("!!! All files have been deleted !!!")
    print("Backup in old was made !")
    