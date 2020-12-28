#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
from tkinter import messagebox
import json
import time
import os
import shutil


def dataBackToSave(self):
    """
        To make backup if it's the
        good day and delete the value
        of date after backup.
    """
    listeDate = []
    with open("./Backup/xdate_file.json") as file_r:
        listeDate = json.load(file_r)
        for index, value in listeDate.items():
            for x in value:
                print(x)
                if time.strftime("%d/%m/%Y") == x:
                    print("------------------------------")
                    print("Today : ", x)
                    print("------------------------------")
                    print("Backup of ALL files !")

                    try:
                        if os.path.exists('./newpatient/entryfile.txt'):
                            print("+ entryfile 1 copied")
                            shutil.copy('./newpatient/entryfile.txt',
                                './Backup/Files1/Backup_patient.txt')
                    except FileNotFoundError as nf_file:
                        print("Not found", nf_file)

                    try:
                        if os.path.exists('./newpatient/entryfile2.txt'):
                            print("+ entryfile 2 copied")
                            shutil.copy('./newpatient/entryfile2.txt',
                                './Backup/Files2/Backup_patient2.txt')
                    except FileNotFoundError as nf_file2:
                        print("Not found", nf_file2)

                    try:
                        if os.path.exists('./newpatient/entryfile3.txt'):
                            print("+ entryfile 3 copied")
                            shutil.copy('./newpatient/entryfile3.txt',
                                './Backup/Files3/Backup_patient3.txt')
                    except FileNotFoundError as nf_file3:
                        print("Not found", nf_file3)

                    try:
                        if os.path.exists('./newpatient/entryfile4.txt'):
                            print("+ entryfile 4 copied")
                            shutil.copy('./newpatient/entryfile4.txt',
                                './Backup/Files4/Backup_patient4.txt')
                    except FileNotFoundError as nf_file4:
                        print("Not found", nf_file4)

                    try:
                        if os.path.exists('./newpatient/entryfile5.txt'):
                            print("+ entryfile 5 copied")
                            shutil.copy('./newpatient/entryfile5.txt',
                                './Backup/Files5/Backup_patient5.txt')
                    except FileNotFoundError as nf_file5:
                        print("Not found", nf_file5)

                    try:
                        if os.path.exists('./newpatient/entryfile6.txt'):
                            print("+ entryfile 6 copied")
                            shutil.copy('./newpatient/entryfile6.txt',
                                './Backup/Files6/Backup_patient6.txt')
                    except FileNotFoundError as nf_file6:
                        print("Not found", nf_file6)

                    try:
                        if os.path.exists('./newpatient/entryfile7.txt'):
                            print("+ entryfile 7 copied")
                            shutil.copy('./newpatient/entryfile7.txt',
                                './Backup/Files7/Backup_patient7.txt')
                    except FileNotFoundError as nf_file7:
                        print("Not found", nf_file7)

                    try:
                        if os.path.exists('./newpatient/entryfile8.txt'):
                            print("+ entryfile 8 copied")
                            shutil.copy('./newpatient/entryfile8.txt',
                                './Backup/Files8/Backup_patient8.txt')
                    except FileNotFoundError as nf_file8:
                        print("Not found", nf_file8)

                    try:
                        if os.path.exists('./newpatient/entryfile9.txt'):
                            print("+ entryfile 9 copied")
                            shutil.copy('./newpatient/entryfile9.txt',
                                './Backup/Files9/Backup_patient9.txt')
                    except FileNotFoundError as nf_file9:
                        print("Not found", nf_file9)

                    try:
                        if os.path.exists('./newpatient/entryfile10.txt'):
                            print("+ entryfile 10 copied")
                            shutil.copy('./newpatient/entryfile10.txt',
                                './Backup/Files10/Backup_patient10.txt')
                    except FileNotFoundError as nf_file10:
                        print("Not found", nf_file10)

                    try:
                        if os.path.exists('./newpatient/entryfile11.txt'):
                            print("+ entryfile 11 copied")
                            shutil.copy('./newpatient/entryfile11.txt',
                                './Backup/Files11/Backup_patient11.txt')
                    except FileNotFoundError as nf_file11:
                        print("Not found", nf_file11)

                    try:
                        if os.path.exists('./newpatient/entryfile12.txt'):
                            print("+ entryfile 12 copied")
                            shutil.copy('./newpatient/entryfile12.txt',
                                './Backup/Files12/Backup_patient12.txt')
                    except FileNotFoundError as nf_file12:
                        print("Not found", nf_file12)
                        
                    try:
                        if os.path.exists('./newpatient/entryfile13.txt'):
                            print("+ entryfile 13 copied")
                            shutil.copy('./newpatient/entryfile13.txt',
                                './Backup/Files13/Backup_patient13.txt')
                    except FileNotFoundError as nf_file13:
                        print("Not found", nf_file13)

                    try:
                        if os.path.exists('./newpatient/entryfile14.txt'):
                            print("+ entryfile 14 copied")
                            shutil.copy('./newpatient/entryfile14.txt',
                                './Backup/Files14/Backup_patient14.txt')
                    except FileNotFoundError as nf_file14:
                        print("Not found", nf_file14)

                    try:
                        if os.path.exists('./newpatient/entryfile15.txt'):
                            print("+ entryfile 15 copied")
                            shutil.copy('./newpatient/entryfile15.txt',
                                './Backup/Files15/Backup_patient15.txt')
                    except FileNotFoundError as nf_file15:
                        print("Not found", nf_file15)

                    try:
                        if os.path.exists('./newpatient/entryfile16.txt'):
                            print("+ entryfile 16 copied")
                            shutil.copy('./newpatient/entryfile16.txt',
                                './Backup/Files16/Backup_patient16.txt')
                    except FileNotFoundError as nf_file16:
                        print("Not found", nf_file16)

                    try:
                        if os.path.exists('./newpatient/entryfile17.txt'):
                            print("+ entryfile 17 copied")
                            shutil.copy('./newpatient/entryfile17.txt',
                                './Backup/Files17/Backup_patient17.txt')
                    except FileNotFoundError as nf_file17:
                        print("Not found", nf_file17)

                    try:
                        if os.path.exists('./newpatient/entryfile18.txt'):
                            print("+ entryfile 18 copied")
                            shutil.copy('./newpatient/entryfile18.txt',
                                './Backup/Files18/Backup_patient18.txt')
                    except FileNotFoundError as nf_file18:
                        print("Not found", nf_file18)

                    try:
                        if os.path.exists('./newpatient/entryfile19.txt'):
                            print("+ entryfile 19 copied")
                            shutil.copy('./newpatient/entryfile19.txt',
                                './Backup/Files19/Backup_patient19.txt')
                    except FileNotFoundError as nf_file19:
                        print("Not found", nf_file19)

                    try:
                        if os.path.exists('./newpatient/entryfile20.txt'):
                            print("+ entryfile 20 copied")
                            shutil.copy('./newpatient/entryfile20.txt',
                                './Backup/Files20/Backup_patient20.txt')
                    except FileNotFoundError as nf_file20:
                        print("Not found", nf_file20)

                    try:
                        if os.path.exists('./newpatient/entryfile21.txt'):
                            print("+ entryfile 21 copied")
                            shutil.copy('./newpatient/entryfile21.txt',
                                './Backup/Files21/Backup_patient21.txt')
                    except FileNotFoundError as nf_file21:
                        print("Not found", nf_file21)

                    try:
                        if os.path.exists('./newpatient/entryfile22.txt'):
                            print("+ entryfile 22 copied")
                            shutil.copy('./newpatient/entryfile22.txt',
                                './Backup/Files22/Backup_patient22.txt')
                    except FileNotFoundError as nf_file22:
                        print("Not found", nf_file22)

                    try:
                        if os.path.exists('./newpatient/entryfile23.txt'):
                            print("+ entryfile 23 copied")
                            shutil.copy('./newpatient/entryfile23.txt',
                                './Backup/Files23/Backup_patient23.txt')
                    except FileNotFoundError as nf_file23:
                        print("Not found", nf_file23)

                    try:
                        if os.path.exists('./newpatient/entryfile24.txt'):
                            print("+ entryfile 24 copied")
                            shutil.copy('./newpatient/entryfile24.txt',
                                './Backup/Files24/Backup_patient24.txt')
                    except FileNotFoundError as nf_file24:
                        print("Not found", nf_file24)

                    try:
                        if os.path.exists('./calBmi/bmi.txt'):
                            print("+ bmi 1 copied")
                            shutil.copy('./calBmi/bmi.txt',
                                './Backup/Files1/Backup_Bmi.txt')
                    except FileNotFoundError as nf_bmi1:
                        print("Not found", nf_bmi1)

                    try:
                        if os.path.exists('./calBmi/bmi2.txt'):
                            print("+ bmi 2 copied")
                            shutil.copy('./calBmi/bmi2.txt',
                                './Backup/Files2/Backup_Bmi2.txt')
                    except FileNotFoundError as nf_bmi2:
                        print("Not found", nf_bmi2)

                    try:
                        if os.path.exists('./calBmi/bmi3.txt'):
                            print("+ bmi 3 copied")
                            shutil.copy('./calBmi/bmi3.txt',
                                './Backup/Files3/Backup_Bmi3.txt')
                    except FileNotFoundError as nf_bmi3:
                        print("Not found", nf_bmi3)

                    try:
                        if os.path.exists('./calBmi/bmi4.txt'):
                            print("+ bmi 4 copied")
                            shutil.copy('./calBmi/bmi4.txt',
                                './Backup/Files4/Backup_Bmi4.txt')
                    except FileNotFoundError as nf_bmi4:
                        print("Not found", nf_bmi4)

                    try:
                        if os.path.exists('./calBmi/bmi5.txt'):
                            print("+ bmi 5 copied")
                            shutil.copy('./calBmi/bmi5.txt',
                                './Backup/Files5/Backup_Bmi5.txt')
                    except FileNotFoundError as nf_bmi5:
                        print("Not found", nf_bmi5)

                    try:
                        if os.path.exists('./calBmi/bmi6.txt'):
                            print("+ bmi 6 copied")
                            shutil.copy('./calBmi/bmi6.txt',
                                './Backup/Files6/Backup_Bmi6.txt')
                    except FileNotFoundError as nf_bmi6:
                        print("Not found", nf_bmi6)

                    try:
                        if os.path.exists('./calBmi/bmi7.txt'):
                            print("+ bmi 7 copied")
                            shutil.copy('./calBmi/bmi7.txt',
                                './Backup/Files7/Backup_Bmi7.txt')
                    except FileNotFoundError as nf_bmi7:
                        print("Not found", nf_bmi7)

                    try:
                        if os.path.exists('./calBmi/bmi8.txt'):
                            print("+ bmi 8 copied")
                            shutil.copy('./calBmi/bmi8.txt',
                                './Backup/Files8/Backup_Bmi8.txt')
                    except FileNotFoundError as nf_bmi8:
                        print("Not found", nf_bmi8)

                    try:
                        if os.path.exists('./calBmi/bmi9.txt'):
                            print("+ bmi 9 copied")
                            shutil.copy('./calBmi/bmi9.txt',
                                './Backup/Files9/Backup_Bmi9.txt')
                    except FileNotFoundError as nf_bmi9:
                        print("Not found", nf_bmi9)

                    try:
                        if os.path.exists('./calBmi/bmi10.txt'):
                            print("+ bmi 10 copied")
                            shutil.copy('./calBmi/bmi10.txt',
                                './Backup/Files10/Backup_Bmi10.txt')
                    except FileNotFoundError as nf_bmi10:
                        print("Not found", nf_bmi10)

                    try:
                        if os.path.exists('./calBmi/bmi11.txt'):
                            print("+ bmi 11 copied")
                            shutil.copy('./calBmi/bmi11.txt',
                                './Backup/Files11/Backup_Bmi11.txt')
                    except FileNotFoundError as nf_bmi11:
                        print("Not found", nf_bmi11)

                    try:
                        if os.path.exists('./calBmi/bmi12.txt'):
                            print("+ bmi 12 copied")
                            shutil.copy('./calBmi/bmi12.txt',
                                './Backup/Files12/Backup_Bmi12.txt')
                    except FileNotFoundError as nf_bmi12:
                        print("Not found", nf_bmi12)

                    try:
                        if os.path.exists('./calBmi/bmi13.txt'):
                            print("+ bmi 13 copied")
                            shutil.copy('./calBmi/bmi13.txt',
                                './Backup/Files13/Backup_Bmi13.txt')
                    except FileNotFoundError as nf_bmi13:
                        print("Not found", nf_bmi13)

                    try:
                        if os.path.exists('./calBmi/bmi14.txt'):
                            print("+ bmi 14 copied")
                            shutil.copy('./calBmi/bmi14.txt',
                                './Backup/Files14/Backup_Bmi14.txt')
                    except FileNotFoundError as nf_bmi14:
                        print("Not found", nf_bmi14)

                    try:
                        if os.path.exists('./calBmi/bmi15.txt'):
                            print("+ bmi 15 copied")
                            shutil.copy('./calBmi/bmi15.txt',
                                './Backup/Files15/Backup_Bmi15.txt')
                    except FileNotFoundError as nf_bmi15:
                        print("Not found", nf_bmi15)

                    try:
                        if os.path.exists('./calBmi/bmi16.txt'):
                            print("+ bmi 16 copied")
                            shutil.copy('./calBmi/bmi16.txt',
                                './Backup/Files16/Backup_Bmi16.txt')
                    except FileNotFoundError as nf_bmi16:
                        print("Not found", nf_bmi16)

                    try:
                        if os.path.exists('./calBmi/bmi17.txt'):
                            print("+ bmi 17 copied")
                            shutil.copy('./calBmi/bmi17.txt',
                                './Backup/Files17/Backup_Bmi17.txt')
                    except FileNotFoundError as nf_bmi17:
                        print("Not found", nf_bmi17)

                    try:
                        if os.path.exists('./calBmi/bmi18.txt'):
                            print("+ bmi 18 copied")
                            shutil.copy('./calBmi/bmi18.txt',
                                './Backup/Files18/Backup_Bmi18.txt')
                    except FileNotFoundError as nf_bmi18:
                        print("Not found", nf_bmi18)

                    try:
                        if os.path.exists('./calBmi/bmi19.txt'):
                            print("+ bmi 19 copied")
                            shutil.copy('./calBmi/bmi19.txt',
                                './Backup/Files19/Backup_Bmi19.txt')
                    except FileNotFoundError as nf_bmi19:
                        print("Not found", nf_bmi19)

                    try:
                        if os.path.exists('./calBmi/bmi20.txt'):
                            print("+ bmi 20 copied")
                            shutil.copy('./calBmi/bmi20.txt',
                                './Backup/Files20/Backup_Bmi20.txt')
                    except FileNotFoundError as nf_bmi20:
                        print("Not found", nf_bmi20)

                    try:
                        if os.path.exists('./calBmi/bmi21.txt'):
                            print("+ bmi 21 copied")
                            shutil.copy('./calBmi/bmi21.txt',
                                './Backup/Files21/Backup_Bmi21.txt')
                    except FileNotFoundError as nf_bmi21:
                        print("Not found", nf_bmi21)

                    try:
                        if os.path.exists('./calBmi/bmi22.txt'):
                            print("+ bmi 22 copied")
                            shutil.copy('./calBmi/bmi22.txt',
                                './Backup/Files22/Backup_Bmi22.txt')
                    except FileNotFoundError as nf_bmi22:
                        print("Not found", nf_bmi22)

                    try:
                        if os.path.exists('./calBmi/bmi23.txt'):
                            print("+ bmi 23 copied")
                            shutil.copy('./calBmi/bmi23.txt',
                                './Backup/Files23/Backup_Bmi23.txt')
                    except FileNotFoundError as nf_bmi23:
                        print("Not found", nf_bmi23)

                    try:
                        if os.path.exists('./calBmi/bmi24.txt'):
                            print("+ bmi 24 copied")
                            shutil.copy('./calBmi/bmi24.txt',
                                './Backup/Files24/Backup_Bmi24.txt')
                    except FileNotFoundError as nf_bmi24:
                        print("Not found", nf_bmi24)

                    try:
                        if os.path.exists('./ttt/doc_ttt/intro_ttt.txt'):
                            print("+ ttt 1 copied")
                            shutil.copy('./ttt/doc_ttt/intro_ttt.txt',
                                './Backup/Files1/Backup_ttt.txt')
                    except FileNotFoundError as nf_ttt:
                        print("Not found", nf_ttt)

                    try:
                        if os.path.exists('./ttt/doc_ttt2/intro_ttt.txt'):
                            print("+ ttt 2 copied")
                            shutil.copy('./ttt/doc_ttt2/intro_ttt.txt',
                                './Backup/Files2/Backup_ttt2.txt')
                    except FileNotFoundError as nf_ttt2:
                        print("Not found", nf_ttt2)

                    try:
                        if os.path.exists('./ttt/doc_ttt3/intro_ttt.txt'):
                            print("+ ttt 3 copied")
                            shutil.copy('./ttt/doc_ttt3/intro_ttt.txt',
                                './Backup/Files3/Backup_ttt3.txt')
                    except FileNotFoundError as nf_ttt3:
                        print("Not found", nf_ttt3)

                    try:
                        if os.path.exists('./ttt/doc_ttt4/intro_ttt.txt'):
                            print("+ ttt 4 copied")
                            shutil.copy('./ttt/doc_ttt4/intro_ttt.txt',
                                './Backup/Files4/Backup_ttt4.txt')
                    except FileNotFoundError as nf_ttt4:
                        print("Not found", nf_ttt4)

                    try:
                        if os.path.exists('./ttt/doc_ttt5/intro_ttt.txt'):
                            print("+ ttt 5 copied")
                            shutil.copy('./ttt/doc_ttt5/intro_ttt.txt',
                                './Backup/Files5/Backup_ttt5.txt')
                    except FileNotFoundError as nf_ttt5:
                        print("Not found", nf_ttt5)

                    try:
                        if os.path.exists('./ttt/doc_ttt6/intro_ttt.txt'):
                            print("+ ttt 6 copied")
                            shutil.copy('./ttt/doc_ttt6/intro_ttt.txt',
                                './Backup/Files6/Backup_ttt6.txt')
                    except FileNotFoundError as nf_ttt6:
                        print("Not found", nf_ttt6)

                    try:
                        if os.path.exists('./ttt/doc_ttt7/intro_ttt.txt'):
                            print("+ ttt 7 copied")
                            shutil.copy('./ttt/doc_ttt7/intro_ttt.txt',
                                './Backup/Files7/Backup_ttt7.txt')
                    except FileNotFoundError as nf_ttt7:
                        print("Not found", nf_ttt7)

                    try:
                        if os.path.exists('./ttt/doc_ttt8/intro_res.txt'):
                            print("+ ttt 8 copied")
                            shutil.copy('./ttt/doc_ttt8/intro_res.txt',
                                './Backup/Files8/Backup_res8.txt')
                    except FileNotFoundError as nf_ttt8:
                        print("Not found", nf_ttt8)

                    try:
                        if os.path.exists('./ttt/doc_ttt9/intro_res.txt'):
                            print("+ ttt 9 copied")
                            shutil.copy('./ttt/doc_ttt9/intro_res.txt',
                                './Backup/Files9/Backup_res9.txt')
                    except FileNotFoundError as nf_ttt9:
                        print("Not found", nf_ttt9)

                    try:
                        if os.path.exists('./ttt/doc_ttt10/intro_res.txt'):
                            print("+ ttt 10 copied")
                            shutil.copy('./ttt/doc_ttt10/intro_res.txt',
                                './Backup/Files10/Backup_res10.txt')
                    except FileNotFoundError as nf_ttt10:
                        print("Not found", nf_ttt10)

                    try:
                        if os.path.exists('./ttt/doc_ttt11/intro_res.txt'):
                            print("+ ttt 11 copied")
                            shutil.copy('./ttt/doc_ttt11/intro_res.txt',
                                './Backup/Files11/Backup_res11.txt')
                    except FileNotFoundError as nf_ttt11:
                        print("Not found", nf_ttt11)

                    try:
                        if os.path.exists('./ttt/doc_ttt12/intro_res.txt'):
                            print("+ ttt 12 copied")
                            shutil.copy('./ttt/doc_ttt12/intro_res.txt',
                                './Backup/Files12/Backup_res12.txt')
                    except FileNotFoundError as nf_ttt12:
                        print("Not found", nf_ttt12)

                    try:
                        if os.path.exists('./ttt/doc_ttt13/intro_res.txt'):
                            print("+ ttt 13 copied")
                            shutil.copy('./ttt/doc_ttt13/intro_res.txt',
                                './Backup/Files13/Backup_res13.txt')
                    except FileNotFoundError as nf_ttt13:
                        print("Not found", nf_ttt13)

                    try:
                        if os.path.exists('./ttt/doc_ttt14/intro_res.txt'):
                            print("+ ttt 14 copied")
                            shutil.copy('./ttt/doc_ttt14/intro_res.txt',
                                './Backup/Files14/Backup_res14.txt')
                    except FileNotFoundError as nf_ttt14:
                        print("Not found", nf_ttt14)

                    try:
                        if os.path.exists('./ttt/doc_ttt15/intro_res.txt'):
                            print("+ ttt 15 copied")
                            shutil.copy('./ttt/doc_ttt15/intro_res.txt',
                                './Backup/Files15/Backup_res15.txt')
                    except FileNotFoundError as nf_ttt15:
                        print("Not found", nf_ttt15)

                    try:
                        if os.path.exists('./ttt/doc_ttt16/intro_res.txt'):
                            print("+ ttt 16 copied")
                            shutil.copy('./ttt/doc_ttt16/intro_res.txt',
                                './Backup/Files16/Backup_res16.txt')
                    except FileNotFoundError as nf_ttt16:
                        print("Not found", nf_ttt16)

                    try:
                        if os.path.exists('./ttt/doc_ttt17/intro_res.txt'):
                            print("+ ttt 17 copied")
                            shutil.copy('./ttt/doc_ttt17/intro_res.txt',
                                './Backup/Files17/Backup_res17.txt')
                    except FileNotFoundError as nf_ttt17:
                        print("Not found", nf_ttt17)

                    try:
                        if os.path.exists('./ttt/doc_ttt18/intro_res.txt'):
                            print("+ ttt 18 copied")
                            shutil.copy('./ttt/doc_ttt18/intro_res.txt',
                                './Backup/Files18/Backup_res18.txt')
                    except FileNotFoundError as nf_ttt18:
                        print("Not found", nf_ttt18)

                    try:
                        if os.path.exists('./ttt/doc_ttt19/intro_res.txt'):
                            print("+ ttt 19 copied")
                            shutil.copy('./ttt/doc_ttt19/intro_res.txt',
                                './Backup/Files19/Backup_res19.txt')
                    except FileNotFoundError as nf_ttt19:
                        print("Not found", nf_ttt19)

                    try:
                        if os.path.exists('./ttt/doc_ttt20/intro_res.txt'):
                            print("+ ttt 20 copied")
                            shutil.copy('./ttt/doc_ttt20/intro_res.txt',
                                './Backup/Files20/Backup_res20.txt')
                    except FileNotFoundError as nf_ttt20:
                        print("Not found", nf_ttt20)

                    try:
                        if os.path.exists('./ttt/doc_ttt21/intro_res.txt'):
                            print("+ ttt 21 copied")
                            shutil.copy('./ttt/doc_ttt21/intro_res.txt',
                                './Backup/Files21/Backup_res21.txt')
                    except FileNotFoundError as nf_ttt21:
                        print("Not found", nf_ttt21)

                    try:
                        if os.path.exists('./ttt/doc_ttt22/intro_res.txt'):
                            print("+ ttt 22 copied")
                            shutil.copy('./ttt/doc_ttt22/intro_res.txt',
                                './Backup/Files22/Backup_res22.txt')
                    except FileNotFoundError as nf_ttt22:
                        print("Not found", nf_ttt22)

                    try:
                        if os.path.exists('./ttt/doc_ttt23/intro_res.txt'):
                            print("+ ttt 23 copied")
                            shutil.copy('./ttt/doc_ttt23/intro_res.txt',
                                './Backup/Files23/Backup_res23.txt')
                    except FileNotFoundError as nf_ttt23:
                        print("Not found", nf_ttt23)

                    try:
                        if os.path.exists('./ttt/doc_ttt24/intro_res.txt'):
                            print("+ ttt 24 copied")
                            shutil.copy('./ttt/doc_ttt24/intro_res.txt',
                                './Backup/Files24/Backup_res24.txt')
                    except FileNotFoundError as nf_ttt24:
                        print("Not found", nf_ttt24)

                    try:
                        if os.path.exists('./diag/doc_diag/diagrecap1.txt'):
                            print("+ diag 1 copied")
                            shutil.copy('./diag/doc_diag/diagrecap1.txt',
                                './Backup/Files1/Backup_diag1.txt')
                    except FileNotFoundError as nf_diag:
                        print("Not found", nf_diag)

                    try:
                        if os.path.exists('./diag/doc_diag2/diagrecap2.txt'):
                            print("+ diag 2 copied")
                            shutil.copy('./diag/doc_diag2/diagrecap2.txt',
                                './Backup/Files2/Backup_diag2.txt')
                    except FileNotFoundError as nf_diag2:
                        print("Not found", nf_diag2)

                    try:
                        if os.path.exists('./diag/doc_diag3/diagrecap3.txt'):
                            print("+ diag 3 copied")
                            shutil.copy('./diag/doc_diag3/diagrecap3.txt',
                                './Backup/Files3/Backup_diag3.txt')
                    except FileNotFoundError as nf_diag3:
                        print("Not found", nf_diag3)

                    try:
                        if os.path.exists('./diag/doc_diag4/diagrecap4.txt'):
                            print("+ diag 4 copied")
                            shutil.copy('./diag/doc_diag4/diagrecap4.txt',
                                './Backup/Files4/Backup_diag4.txt')
                    except FileNotFoundError as nf_diag4:
                        print("Not found", nf_diag4)

                    try:
                        if os.path.exists('./diag/doc_diag5/diagrecap5.txt'):
                            print("+ diag 5 copied")
                            shutil.copy('./diag/doc_diag5/diagrecap5.txt',
                                './Backup/Files5/Backup_diag5.txt')
                    except FileNotFoundError as nf_diag5:
                        print("Not found", nf_diag5)

                    try:
                        if os.path.exists('./diag/doc_diag6/diagrecap6.txt'):
                            print("+ diag 6 copied")
                            shutil.copy('./diag/doc_diag6/diagrecap6.txt',
                                './Backup/Files6/Backup_diag6.txt')
                    except FileNotFoundError as nf_diag6:
                        print("Not found", nf_diag6)

                    try:
                        if os.path.exists('./diag/doc_diag7/diagrecap7.txt'):
                            print("+ diag 7 copied")
                            shutil.copy('./diag/doc_diag7/diagrecap7.txt',
                                './Backup/Files7/Backup_diag7.txt')
                    except FileNotFoundError as nf_diag7:
                        print("Not found", nf_diag7)

                    try:
                        if os.path.exists('./diag/doc_diag8/diagrecap8.txt'):
                            print("+ diag 8 copied")
                            shutil.copy('./diag/doc_diag8/diagrecap8.txt',
                                './Backup/Files8/Backup_diag8.txt')
                    except FileNotFoundError as nf_diag8:
                        print("Not found", nf_diag8)

                    try:
                        if os.path.exists('./diag/doc_diag9/diagrecap9.txt'):
                            print("+ diag 9 copied")
                            shutil.copy('./diag/doc_diag9/diagrecap9.txt',
                                './Backup/Files9/Backup_diag9.txt')
                    except FileNotFoundError as nf_diag9:
                        print("Not found", nf_diag9)

                    try:
                        if os.path.exists('./diag/doc_diag10/diagrecap10.txt'):
                            print("+ diag 10 copied")
                            shutil.copy('./diag/doc_diag10/diagrecap10.txt',
                                './Backup/Files10/Backup_diag10.txt')
                    except FileNotFoundError as nf_diag10:
                        print("Not found", nf_diag10)

                    try:
                        if os.path.exists('./diag/doc_diag11/diagrecap11.txt'):
                            print("+ diag 11 copied")
                            shutil.copy('./diag/doc_diag11/diagrecap11.txt',
                                './Backup/Files11/Backup_diag11.txt')
                    except FileNotFoundError as nf_diag11:
                        print("Not found", nf_diag11)

                    try:
                        if os.path.exists('./diag/doc_diag12/diagrecap12.txt'):
                            print("+ diag 12 copied")
                            shutil.copy('./diag/doc_diag12/diagrecap12.txt',
                                './Backup/Files12/Backup_diag12.txt')
                    except FileNotFoundError as nf_diag12:
                        print("Not found", nf_diag12)

                    try:
                        if os.path.exists('./diag/doc_diag13/diagrecap13.txt'):
                            print("+ diag 13 copied")
                            shutil.copy('./diag/doc_diag13/diagrecap13.txt',
                                './Backup/Files13/Backup_diag13.txt')
                    except FileNotFoundError as nf_diag13:
                        print("Not found", nf_diag13)

                    try:
                        if os.path.exists('./diag/doc_diag14/diagrecap14.txt'):
                            print("+ diag 14 copied")
                            shutil.copy('./diag/doc_diag14/diagrecap14.txt',
                                './Backup/Files14/Backup_diag14.txt')
                    except FileNotFoundError as nf_diag14:
                        print("Not found", nf_diag14)

                    try:
                        if os.path.exists('./diag/doc_diag15/diagrecap15.txt'):
                            print("+ diag 15 copied")
                            shutil.copy('./diag/doc_diag15/diagrecap15.txt',
                                './Backup/Files15/Backup_diag15.txt')
                    except FileNotFoundError as nf_diag15:
                        print("Not found", nf_diag15)

                    try:
                        if os.path.exists('./diag/doc_diag16/diagrecap16.txt'):
                            print("+ diag 16 copied")
                            shutil.copy('./diag/doc_diag16/diagrecap16.txt',
                                './Backup/Files16/Backup_diag16.txt')
                    except FileNotFoundError as nf_diag16:
                        print("Not found", nf_diag16)

                    try:
                        if os.path.exists('./diag/doc_diag17/diagrecap17.txt'):
                            print("+ diag 17 copied")
                            shutil.copy('./diag/doc_diag17/diagrecap17.txt',
                                './Backup/Files17/Backup_diag17.txt')
                    except FileNotFoundError as nf_diag17:
                        print("Not found", nf_diag17)

                    try:
                        if os.path.exists('./diag/doc_diag18/diagrecap18.txt'):
                            print("+ diag 18 copied")
                            shutil.copy('./diag/doc_diag18/diagrecap18.txt',
                                './Backup/Files18/Backup_diag18.txt')
                    except FileNotFoundError as nf_diag18:
                        print("Not found", nf_diag18)

                    try:
                        if os.path.exists('./diag/doc_diag19/diagrecap19.txt'):
                            print("+ diag 19 copied")
                            shutil.copy('./diag/doc_diag19/diagrecap19.txt',
                                './Backup/Files19/Backup_diag19.txt')
                    except FileNotFoundError as nf_diag19:
                        print("Not found", nf_diag19)

                    try:
                        if os.path.exists('./diag/doc_diag20/diagrecap20.txt'):
                            print("+ diag 20 copied")
                            shutil.copy('./diag/doc_diag20/diagrecap20.txt',
                                './Backup/Files20/Backup_diag20.txt')
                    except FileNotFoundError as nf_diag20:
                        print("Not found", nf_diag20)

                    try:
                        if os.path.exists('./diag/doc_diag21/diagrecap21.txt'):
                            print("+ diag 21 copied")
                            shutil.copy('./diag/doc_diag21/diagrecap21.txt',
                                './Backup/Files21/Backup_diag21.txt')
                    except FileNotFoundError as nf_diag21:
                        print("Not found", nf_diag21)

                    try:
                        if os.path.exists('./diag/doc_diag22/diagrecap22.txt'):
                            print("+ diag 22 copied")
                            shutil.copy('./diag/doc_diag22/diagrecap22.txt',
                                './Backup/Files22/Backup_diag22.txt')
                    except FileNotFoundError as nf_diag22:
                        print("Not found", nf_diag22)

                    try:
                        if os.path.exists('./diag/doc_diag23/diagrecap23.txt'):
                            print("+ diag 23 copied")
                            shutil.copy('./diag/doc_diag23/diagrecap23.txt',
                                './Backup/Files23/Backup_diag23.txt')
                    except FileNotFoundError as nf_diag23:
                        print("Not found", nf_diag23)

                    try:
                        if os.path.exists('./diag/doc_diag24/diagrecap24.txt'):
                            print("+ diag 24 copied")
                            shutil.copy('./diag/doc_diag24/diagrecap24.txt',
                                './Backup/Files24/Backup_diag24.txt')
                    except FileNotFoundError as nf_diag24:
                        print("Not found", nf_diag24)

                    try:
                        if os.path.exists('./14besoins/doc_suivi/main_14b.txt'):
                            print("+ 14besoins 1 copied")
                            shutil.copy('./14besoins/doc_suivi/main_14b.txt',
                                './Backup/Files1/Backup_careneeds1.txt')
                    except FileNotFoundError as nf_main:
                        print("Not found", nf_main)

                    try:
                        if os.path.exists('./14besoins/doc_suivi2/main_14b.txt'):
                            print("+ 14besoins 2 copied")
                            shutil.copy('./14besoins/doc_suivi2/main_14b.txt',
                                './Backup/Files2/Backup_careneeds2.txt')
                    except FileNotFoundError as nf_main2:
                        print("Not found", nf_main2)

                    try:
                        if os.path.exists('./14besoins/doc_suivi3/main_14b.txt'):
                            print("+ 14besoins 3 copied")
                            shutil.copy('./14besoins/doc_suivi3/main_14b.txt',
                                './Backup/Files3/Backup_careneeds3.txt')
                    except FileNotFoundError as nf_main3:
                        print("Not found", nf_main3)

                    try:
                        if os.path.exists('./14besoins/doc_suivi4/main_14b.txt'):
                            print("+ 14besoins 4 copied")
                            shutil.copy('./14besoins/doc_suivi4/main_14b.txt',
                                './Backup/Files4/Backup_careneeds4.txt')
                    except FileNotFoundError as nf_main4:
                        print("Not found", nf_main4)

                    try:
                        if os.path.exists('./14besoins/doc_suivi5/main_14b.txt'):
                            print("+ 14besoins 5 copied")
                            shutil.copy('./14besoins/doc_suivi5/main_14b.txt',
                                './Backup/Files5/Backup_careneeds5.txt')
                    except FileNotFoundError as nf_main5:
                        print("Not found", nf_main5)

                    try:
                        if os.path.exists('./14besoins/doc_suivi6/main_14b.txt'):
                            print("+ 14besoins 6 copied")
                            shutil.copy('./14besoins/doc_suivi6/main_14b.txt',
                                './Backup/Files6/Backup_careneeds6.txt')
                    except FileNotFoundError as nf_main6:
                        print("Not found", nf_main6)

                    try:
                        if os.path.exists('./14besoins/doc_suivi7/main_14b.txt'):
                            print("+ 14besoins 7 copied")
                            shutil.copy('./14besoins/doc_suivi7/main_14b.txt',
                                './Backup/Files7/Backup_careneeds7.txt')
                    except FileNotFoundError as nf_main7:
                        print("Not found", nf_main7)

                    try:
                        if os.path.exists('./14besoins/doc_suivi8/main_14b.txt'):
                            print("+ 14besoins 8 copied")
                            shutil.copy('./14besoins/doc_suivi8/main_14b.txt',
                                './Backup/Files8/Backup_careneeds8.txt')
                    except FileNotFoundError as nf_main8:
                        print("Not found", nf_main8)

                    try:
                        if os.path.exists('./14besoins/doc_suivi9/main_14b.txt'):
                            print("+ 14besoins 9 copied")
                            shutil.copy('./14besoins/doc_suivi9/main_14b.txt',
                                './Backup/Files9/Backup_careneeds9.txt')
                    except FileNotFoundError as nf_main9:
                        print("Not found", nf_main9)

                    try:
                        if os.path.exists('./14besoins/doc_suivi10/main_14b.txt'):
                            print("+ 14besoins 10 copied")
                            shutil.copy('./14besoins/doc_suivi10/main_14b.txt',
                                './Backup/Files10/Backup_careneeds10.txt')
                    except FileNotFoundError as nf_main10:
                        print("Not found", nf_main10)

                    try:
                        if os.path.exists('./14besoins/doc_suivi11/main_14b.txt'):
                            print("+ 14besoins 11 copied")
                            shutil.copy('./14besoins/doc_suivi11/main_14b.txt',
                                './Backup/Files11/Backup_careneeds11.txt')
                    except FileNotFoundError as nf_main11:
                        print("Not found", nf_main11)

                    try:
                        if os.path.exists('./14besoins/doc_suivi12/main_14b.txt'):
                            print("+ 14besoins 12 copied")
                            shutil.copy('./14besoins/doc_suivi12/main_14b.txt',
                                './Backup/Files12/Backup_careneeds12.txt')
                    except FileNotFoundError as nf_main12:
                        print("Not found", nf_main12)

                    try:
                        if os.path.exists('./14besoins/doc_suivi13/main_14b.txt'):
                            print("+ 14besoins 13 copied")
                            shutil.copy('./14besoins/doc_suivi13/main_14b.txt',
                                './Backup/Files13/Backup_careneeds13.txt')
                    except FileNotFoundError as nf_main13:
                        print("Not found", nf_main13)

                    try:
                        if os.path.exists('./14besoins/doc_suivi14/main_14b.txt'):
                            print("+ 14besoins 14 copied")
                            shutil.copy('./14besoins/doc_suivi14/main_14b.txt',
                                './Backup/Files14/Backup_careneeds14.txt')
                    except FileNotFoundError as nf_main14:
                        print("Not found", nf_main14)

                    try:
                        if os.path.exists('./14besoins/doc_suivi15/main_14b.txt'):
                            print("+ 14besoins 15 copied")
                            shutil.copy('./14besoins/doc_suivi15/main_14b.txt',
                                './Backup/Files15/Backup_careneeds15.txt')
                    except FileNotFoundError as nf_main15:
                        print("Not found", nf_main15)

                    try:
                        if os.path.exists('./14besoins/doc_suivi16/main_14b.txt'):
                            print("+ 14besoins 16 copied")
                            shutil.copy('./14besoins/doc_suivi16/main_14b.txt',
                                './Backup/Files16/Backup_careneeds16.txt')
                    except FileNotFoundError as nf_main16:
                        print("Not found", nf_main16)

                    try:
                        if os.path.exists('./14besoins/doc_suivi17/main_14b.txt'):
                            print("+ 14besoins 17 copied")
                            shutil.copy('./14besoins/doc_suivi17/main_14b.txt',
                                './Backup/Files17/Backup_careneeds17.txt')
                    except FileNotFoundError as nf_main17:
                        print("Not found", nf_main17)

                    try:
                        if os.path.exists('./14besoins/doc_suivi18/main_14b.txt'):
                            print("+ 14besoins 18 copied")
                            shutil.copy('./14besoins/doc_suivi18/main_14b.txt',
                                './Backup/Files18/Backup_careneeds18.txt')
                    except FileNotFoundError as nf_main18:
                        print("Not found", nf_main18)

                    try:
                        if os.path.exists('./14besoins/doc_suivi19/main_14b.txt'):
                            print("+ 14besoins 19 copied")
                            shutil.copy('./14besoins/doc_suivi19/main_14b.txt',
                                './Backup/Files19/Backup_careneeds19.txt')
                    except FileNotFoundError as nf_main19:
                        print("Not found", nf_main19)

                    try:
                        if os.path.exists('./14besoins/doc_suivi20/main_14b.txt'):
                            print("+ 14besoins 20 copied")
                            shutil.copy('./14besoins/doc_suivi20/main_14b.txt',
                                './Backup/Files20/Backup_careneeds20.txt')
                    except FileNotFoundError as nf_main20:
                        print("Not found", nf_main20)

                    try:
                        if os.path.exists('./14besoins/doc_suivi21/main_14b.txt'):
                            print("+ 14besoins 21 copied")
                            shutil.copy('./14besoins/doc_suivi21/main_14b.txt',
                                './Backup/Files21/Backup_careneeds21.txt')
                    except FileNotFoundError as nf_main21:
                        print("Not found", nf_main21)

                    try:
                        if os.path.exists('./14besoins/doc_suivi22/main_14b.txt'):
                            print("+ 14besoins 22 copied")
                            shutil.copy('./14besoins/doc_suivi22/main_14b.txt',
                                './Backup/Files22/Backup_careneeds22.txt')
                    except FileNotFoundError as nf_main22:
                        print("Not found", nf_main22)

                    try:
                        if os.path.exists('./14besoins/doc_suivi23/main_14b.txt'):
                            print("+ 14besoins 23 copied")
                            shutil.copy('./14besoins/doc_suivi23/main_14b.txt',
                                './Backup/Files23/Backup_careneeds23.txt')
                    except FileNotFoundError as nf_main23:
                        print("Not found", nf_main23)

                    try:
                        if os.path.exists('./14besoins/doc_suivi24/main_14b.txt'):
                            print("+ 14besoins 24 copied")
                            shutil.copy('./14besoins/doc_suivi24/main_14b.txt',
                                './Backup/Files24/Backup_careneeds24.txt')
                    except FileNotFoundError as nf_main24:
                        print("Not found", nf_main24)

                    try:
                        if os.path.exists('./vmed/doc_vmed/resultvmed.txt'):
                            print("+ resultvmed.txt copied")
                            shutil.copy('./vmed/doc_vmed/resultvmed.txt',
                                './Backup/Files1/Backup_resultvmed.txt')
                    except FileNotFoundError as nf_rvm:
                        print("Not found", nf_rvm)

                    try:
                        if os.path.exists('./vmed/doc_vmed2/resultvmed2.txt'):
                            print("+ resultvmed2.txt copied")
                            shutil.copy('./vmed/doc_vmed2/resultvmed2.txt',
                                './Backup/Files2/Backup_resultvmed2.txt')
                    except FileNotFoundError as nf_rvm2:
                        print("Not found", nf_rvm2)

                    try:
                        if os.path.exists('./vmed/doc_vmed3/resultvmed3.txt'):
                            print("+ resultvmed3.txt copied")
                            shutil.copy('./vmed/doc_vmed3/resultvmed3.txt',
                                './Backup/Files3/Backup_resultvmed3.txt')
                    except FileNotFoundError as nf_rvm3:
                        print("Not found", nf_rvm3)

                    try:
                        if os.path.exists('./vmed/doc_vmed4/resultvmed4.txt'):
                            print("+ resultvmed4.txt copied")
                            shutil.copy('./vmed/doc_vmed4/resultvmed4.txt',
                                './Backup/Files4/Backup_resultvmed4.txt')
                    except FileNotFoundError as nf_rvm4:
                        print("Not found", nf_rvm4)

                    try:
                        if os.path.exists('./vmed/doc_vmed5/resultvmed5.txt'):
                            print("+ resultvmed5.txt copied")
                            shutil.copy('./vmed/doc_vmed5/resultvmed5.txt',
                                './Backup/Files5/Backup_resultvmed5.txt')
                    except FileNotFoundError as nf_rvm5:
                        print("Not found", nf_rvm5)

                    try:
                        if os.path.exists('./vmed/doc_vmed6/resultvmed6.txt'):
                            print("+ resultvmed6.txt copied")
                            shutil.copy('./vmed/doc_vmed6/resultvmed6.txt',
                                './Backup/Files6/Backup_resultvmed6.txt')
                    except FileNotFoundError as nf_rvm6:
                        print("Not found", nf_rvm6)

                    try:
                        if os.path.exists('./vmed/doc_vmed7/resultvmed7.txt'):
                            print("+ resultvmed7.txt copied")
                            shutil.copy('./vmed/doc_vmed7/resultvmed7.txt',
                                './Backup/Files7/Backup_resultvmed7.txt')
                    except FileNotFoundError as nf_rvm7:
                        print("Not found", nf_rvm7)

                    try:
                        if os.path.exists('./vmed/doc_vmed8/resultvmed8.txt'):
                            print("+ resultvmed8.txt copied")
                            shutil.copy('./vmed/doc_vmed8/resultvmed8.txt',
                                './Backup/Files8/Backup_resultvmed8.txt')
                    except FileNotFoundError as nf_rvm8:
                        print("Not found", nf_rvm8)

                    try:
                        if os.path.exists('./vmed/doc_vmed9/resultvmed9.txt'):
                            print("+ resultvmed9.txt copied")
                            shutil.copy('./vmed/doc_vmed9/resultvmed9.txt',
                                './Backup/Files9/Backup_resultvmed9.txt')
                    except FileNotFoundError as nf_rvm9:
                        print("Not found", nf_rvm9)

                    try:
                        if os.path.exists('./vmed/doc_vmed10/resultvmed10.txt'):
                            print("+ resultvmed10.txt copied")
                            shutil.copy('./vmed/doc_vmed10/resultvmed10.txt',
                                './Backup/Files10/Backup_resultvmed10.txt')
                    except FileNotFoundError as nf_rvm10:
                        print("Not found", nf_rvm10)

                    try:
                        if os.path.exists('./vmed/doc_vmed11/resultvmed11.txt'):
                            print("+ resultvmed11.txt copied")
                            shutil.copy('./vmed/doc_vmed11/resultvmed11.txt',
                                './Backup/Files11/Backup_resultvmed11.txt')
                    except FileNotFoundError as nf_rvm11:
                        print("Not found", nf_rvm11)

                    try:
                        if os.path.exists('./vmed/doc_vmed12/resultvmed12.txt'):
                            print("+ resultvmed12.txt copied")
                            shutil.copy('./vmed/doc_vmed12/resultvmed12.txt',
                                './Backup/Files12/Backup_resultvmed12.txt')
                    except FileNotFoundError as nf_rvm12:
                        print("Not found", nf_rvm12)

                    try:
                        if os.path.exists('./vmed/doc_vmed13/resultvmed13.txt'):
                            print("+ resultvmed13.txt copied")
                            shutil.copy('./vmed/doc_vmed13/resultvmed13.txt',
                                './Backup/Files13/Backup_resultvmed13.txt')
                    except FileNotFoundError as nf_rvm13:
                        print("Not found", nf_rvm13)

                    try:
                        if os.path.exists('./vmed/doc_vmed14/resultvmed14.txt'):
                            print("+ resultvmed14.txt copied")
                            shutil.copy('./vmed/doc_vmed14/resultvmed14.txt',
                                './Backup/Files14/Backup_resultvmed14.txt')
                    except FileNotFoundError as nf_rvm14:
                        print("Not found", nf_rvm14)

                    try:
                        if os.path.exists('./vmed/doc_vmed15/resultvmed15.txt'):
                            print("+ resultvmed15.txt copied")
                            shutil.copy('./vmed/doc_vmed15/resultvmed15.txt',
                                './Backup/Files15/Backup_resultvmed15.txt')
                    except FileNotFoundError as nf_rvm15:
                        print("Not found", nf_rvm15)

                    try:
                        if os.path.exists('./vmed/doc_vmed16/resultvmed16.txt'):
                            print("+ resultvmed16.txt copied")
                            shutil.copy('./vmed/doc_vmed16/resultvmed16.txt',
                                './Backup/Files16/Backup_resultvmed16.txt')
                    except FileNotFoundError as nf_rvm16:
                        print("Not found", nf_rvm16)

                    try:
                        if os.path.exists('./vmed/doc_vmed17/resultvmed17.txt'):
                            print("+ resultvmed17.txt copied")
                            shutil.copy('./vmed/doc_vmed17/resultvmed17.txt',
                                './Backup/Files17/Backup_resultvmed17.txt')
                    except FileNotFoundError as nf_rvm17:
                        print("Not found", nf_rvm17)

                    try:
                        if os.path.exists('./vmed/doc_vmed18/resultvmed18.txt'):
                            print("+ resultvmed18.txt copied")
                            shutil.copy('./vmed/doc_vmed18/resultvmed18.txt',
                                './Backup/Files18/Backup_resultvmed18.txt')
                    except FileNotFoundError as nf_rvm18:
                        print("Not found", nf_rvm18)

                    try:
                        if os.path.exists('./vmed/doc_vmed19/resultvmed19.txt'):
                            print("+ resultvmed19.txt copied")
                            shutil.copy('./vmed/doc_vmed19/resultvmed19.txt',
                                './Backup/Files19/Backup_resultvmed19.txt')
                    except FileNotFoundError as nf_rvm19:
                        print("Not found", nf_rvm19)

                    try:
                        if os.path.exists('./vmed/doc_vmed20/resultvmed20.txt'):
                            print("+ resultvmed20.txt copied")
                            shutil.copy('./vmed/doc_vmed20/resultvmed20.txt',
                                './Backup/Files20/Backup_resultvmed20.txt')
                    except FileNotFoundError as nf_rvm20:
                        print("Not found", nf_rvm20)

                    try:
                        if os.path.exists('./vmed/doc_vmed21/resultvmed21.txt'):
                            print("+ resultvmed21.txt copied")
                            shutil.copy('./vmed/doc_vmed21/resultvmed21.txt',
                                './Backup/Files21/Backup_resultvmed21.txt')
                    except FileNotFoundError as nf_rvm21:
                        print("Not found", nf_rvm21)

                    try:
                        if os.path.exists('./vmed/doc_vmed22/resultvmed22.txt'):
                            print("+ resultvmed22.txt copied")
                            shutil.copy('./vmed/doc_vmed22/resultvmed22.txt',
                                './Backup/Files22/Backup_resultvmed22.txt')
                    except FileNotFoundError as nf_rvm22:
                        print("Not found", nf_rvm22)

                    try:
                        if os.path.exists('./vmed/doc_vmed23/resultvmed23.txt'):
                            print("+ resultvmed23.txt copied")
                            shutil.copy('./vmed/doc_vmed23/resultvmed23.txt',
                                './Backup/Files23/Backup_resultvmed23.txt')
                    except FileNotFoundError as nf_rvm23:
                        print("Not found", nf_rvm23)

                    try:
                        if os.path.exists('./vmed/doc_vmed24/resultvmed24.txt'):
                            print("+ resultvmed24.txt copied")
                            shutil.copy('./vmed/doc_vmed24/resultvmed24.txt',
                                './Backup/Files24/Backup_resultvmed24.txt')
                    except FileNotFoundError as nf_rvm24:
                        print("Not found", nf_rvm24)

                    x=str(x)
                    value.remove(x)
                    file_w = open("./Backup/xdate_file.json", "w")
                    listeDate = json.dump(listeDate, file_w, indent=4)
                    print("--- Backup done ---")
                    messagebox.showinfo('INFO', 'BACKUP done !')
                    messagebox.showinfo('INFO', 'Go to Global to read one of them !')
