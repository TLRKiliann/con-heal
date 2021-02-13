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
                            shutil.copy('./newpatient/entryfile.txt',
                                './Backup/Files1/entryfile.txt')
                            print("+ entryfile 1 copied")
                    except FileNotFoundError as nf_file:
                        print("Not found", nf_file)

                    try:
                        if os.path.exists('./newpatient/entryfile2.txt'):
                            shutil.copy('./newpatient/entryfile2.txt',
                                './Backup/Files2/entryfile2.txt')
                            print("+ entryfile 2 copied")
                    except FileNotFoundError as nf_file2:
                        print("Not found", nf_file2)

                    try:
                        if os.path.exists('./newpatient/entryfile3.txt'):
                            shutil.copy('./newpatient/entryfile3.txt',
                                './Backup/Files3/entryfile3.txt')
                            print("+ entryfile 3 copied")
                    except FileNotFoundError as nf_file3:
                        print("Not found", nf_file3)

                    try:
                        if os.path.exists('./newpatient/entryfile4.txt'):
                            shutil.copy('./newpatient/entryfile4.txt',
                                './Backup/Files4/entryfile4.txt')
                            print("+ entryfile 4 copied")
                    except FileNotFoundError as nf_file4:
                        print("Not found", nf_file4)

                    try:
                        if os.path.exists('./newpatient/entryfile5.txt'):
                            shutil.copy('./newpatient/entryfile5.txt',
                                './Backup/Files5/entryfile5.txt')
                            print("+ entryfile 5 copied")
                    except FileNotFoundError as nf_file5:
                        print("Not found", nf_file5)

                    try:
                        if os.path.exists('./newpatient/entryfile6.txt'):
                            shutil.copy('./newpatient/entryfile6.txt',
                                './Backup/Files6/entryfile6.txt')
                            print("+ entryfile 6 copied")
                    except FileNotFoundError as nf_file6:
                        print("Not found", nf_file6)

                    try:
                        if os.path.exists('./newpatient/entryfile7.txt'):
                            shutil.copy('./newpatient/entryfile7.txt',
                                './Backup/Files7/entryfile7.txt')
                            print("+ entryfile 7 copied")
                    except FileNotFoundError as nf_file7:
                        print("Not found", nf_file7)

                    try:
                        if os.path.exists('./newpatient/entryfile8.txt'):
                            shutil.copy('./newpatient/entryfile8.txt',
                                './Backup/Files8/entryfile8.txt')
                            print("+ entryfile 8 copied")
                    except FileNotFoundError as nf_file8:
                        print("Not found", nf_file8)

                    try:
                        if os.path.exists('./newpatient/entryfile9.txt'):
                            shutil.copy('./newpatient/entryfile9.txt',
                                './Backup/Files9/entryfile9.txt')
                            print("+ entryfile 9 copied")
                    except FileNotFoundError as nf_file9:
                        print("Not found", nf_file9)

                    try:
                        if os.path.exists('./newpatient/entryfile10.txt'):
                            shutil.copy('./newpatient/entryfile10.txt',
                                './Backup/Files10/entryfile10.txt')
                            print("+ entryfile 10 copied")
                    except FileNotFoundError as nf_file10:
                        print("Not found", nf_file10)

                    try:
                        if os.path.exists('./newpatient/entryfile11.txt'):
                            shutil.copy('./newpatient/entryfile11.txt',
                                './Backup/Files11/entryfile11.txt')
                            print("+ entryfile 11 copied")
                    except FileNotFoundError as nf_file11:
                        print("Not found", nf_file11)

                    try:
                        if os.path.exists('./newpatient/entryfile12.txt'):
                            shutil.copy('./newpatient/entryfile12.txt',
                                './Backup/Files12/entryfile12.txt')
                            print("+ entryfile 12 copied")
                    except FileNotFoundError as nf_file12:
                        print("Not found", nf_file12)

                    try:
                        if os.path.exists('./newpatient/entryfile13.txt'):
                            shutil.copy('./newpatient/entryfile13.txt',
                                './Backup/Files13/entryfile13.txt')
                            print("+ entryfile 13 copied")
                    except FileNotFoundError as nf_file13:
                        print("Not found", nf_file13)

                    try:
                        if os.path.exists('./newpatient/entryfile14.txt'):
                            shutil.copy('./newpatient/entryfile14.txt',
                                './Backup/Files14/entryfile14.txt')
                            print("+ entryfile 14 copied")
                    except FileNotFoundError as nf_file14:
                        print("Not found", nf_file14)

                    try:
                        if os.path.exists('./newpatient/entryfile15.txt'):
                            shutil.copy('./newpatient/entryfile15.txt',
                                './Backup/Files15/entryfile15.txt')
                            print("+ entryfile 15 copied")
                    except FileNotFoundError as nf_file15:
                        print("Not found", nf_file15)

                    try:
                        if os.path.exists('./newpatient/entryfile16.txt'):
                            shutil.copy('./newpatient/entryfile16.txt',
                                './Backup/Files16/entryfile16.txt')
                            print("+ entryfile 16 copied")
                    except FileNotFoundError as nf_file16:
                        print("Not found", nf_file16)

                    try:
                        if os.path.exists('./newpatient/entryfile17.txt'):
                            shutil.copy('./newpatient/entryfile17.txt',
                                './Backup/Files17/entryfile17.txt')
                            print("+ entryfile 17 copied")
                    except FileNotFoundError as nf_file17:
                        print("Not found", nf_file17)

                    try:
                        if os.path.exists('./newpatient/entryfile18.txt'):
                            shutil.copy('./newpatient/entryfile18.txt',
                                './Backup/Files18/entryfile18.txt')
                            print("+ entryfile 18 copied")
                    except FileNotFoundError as nf_file18:
                        print("Not found", nf_file18)

                    try:
                        if os.path.exists('./newpatient/entryfile19.txt'):
                            shutil.copy('./newpatient/entryfile19.txt',
                                './Backup/Files19/entryfile19.txt')
                            print("+ entryfile 19 copied")
                    except FileNotFoundError as nf_file19:
                        print("Not found", nf_file19)

                    try:
                        if os.path.exists('./newpatient/entryfile20.txt'):
                            shutil.copy('./newpatient/entryfile20.txt',
                                './Backup/Files20/entryfile20.txt')
                            print("+ entryfile 20 copied")
                    except FileNotFoundError as nf_file20:
                        print("Not found", nf_file20)

                    try:
                        if os.path.exists('./newpatient/entryfile21.txt'):
                            shutil.copy('./newpatient/entryfile21.txt',
                                './Backup/Files21/entryfile21.txt')
                            print("+ entryfile 21 copied")
                    except FileNotFoundError as nf_file21:
                        print("Not found", nf_file21)

                    try:
                        if os.path.exists('./newpatient/entryfile22.txt'):
                            shutil.copy('./newpatient/entryfile22.txt',
                                './Backup/Files22/entryfile22.txt')
                            print("+ entryfile 22 copied")
                    except FileNotFoundError as nf_file22:
                        print("Not found", nf_file22)

                    try:
                        if os.path.exists('./newpatient/entryfile23.txt'):
                            shutil.copy('./newpatient/entryfile23.txt',
                                './Backup/Files23/entryfile23.txt')
                            print("+ entryfile 23 copied")
                    except FileNotFoundError as nf_file23:
                        print("Not found", nf_file23)

                    try:
                        if os.path.exists('./newpatient/entryfile24.txt'):
                            shutil.copy('./newpatient/entryfile24.txt',
                                './Backup/Files24/entryfile24.txt')
                            print("+ entryfile 24 copied")
                    except FileNotFoundError as nf_file24:
                        print("Not found", nf_file24)

                    try:
                        if os.path.exists('./ttt/doc_ttt/intro_ttt.txt'):
                            shutil.copy('./ttt/doc_ttt/intro_ttt.txt',
                                './Backup/Files1/intro_ttt.txt')
                            print("+ ttt 1 copied")
                    except FileNotFoundError as nf_ttt:
                        print("Not found", nf_ttt)

                    try:
                        if os.path.exists('./ttt/doc_ttt2/intro_ttt.txt'):
                            shutil.copy('./ttt/doc_ttt2/intro_ttt.txt',
                                './Backup/Files2/intro_ttt.txt')
                            print("+ ttt 2 copied")
                    except FileNotFoundError as nf_ttt2:
                        print("Not found", nf_ttt2)

                    try:
                        if os.path.exists('./ttt/doc_ttt3/intro_ttt.txt'):
                            shutil.copy('./ttt/doc_ttt3/intro_ttt.txt',
                                './Backup/Files3/intro_ttt.txt')
                            print("+ ttt 3 copied")
                    except FileNotFoundError as nf_ttt3:
                        print("Not found", nf_ttt3)

                    try:
                        if os.path.exists('./ttt/doc_ttt4/intro_ttt.txt'):
                            shutil.copy('./ttt/doc_ttt4/intro_ttt.txt',
                                './Backup/Files4/intro_ttt.txt')
                            print("+ ttt 4 copied")
                    except FileNotFoundError as nf_ttt4:
                        print("Not found", nf_ttt4)

                    try:
                        if os.path.exists('./ttt/doc_ttt5/intro_ttt.txt'):
                            shutil.copy('./ttt/doc_ttt5/intro_ttt.txt',
                                './Backup/Files5/intro_ttt.txt')
                            print("+ ttt 5 copied")
                    except FileNotFoundError as nf_ttt5:
                        print("Not found", nf_ttt5)

                    try:
                        if os.path.exists('./ttt/doc_ttt6/intro_ttt.txt'):
                            shutil.copy('./ttt/doc_ttt6/intro_ttt.txt',
                                './Backup/Files6/intro_ttt.txt')
                            print("+ ttt 6 copied")
                    except FileNotFoundError as nf_ttt6:
                        print("Not found", nf_ttt6)

                    try:
                        if os.path.exists('./ttt/doc_ttt7/intro_ttt.txt'):
                            shutil.copy('./ttt/doc_ttt7/intro_ttt.txt',
                                './Backup/Files7/intro_ttt.txt')
                            print("+ ttt 7 copied")
                    except FileNotFoundError as nf_ttt7:
                        print("Not found", nf_ttt7)

                    try:
                        if os.path.exists('./ttt/doc_ttt8/intro_ttt.txt'):
                            shutil.copy('./ttt/doc_ttt8/intro_ttt.txt',
                                './Backup/Files8/intro_ttt.txt')
                            print("+ ttt 8 copied")
                    except FileNotFoundError as nf_ttt8:
                        print("Not found", nf_ttt8)

                    try:
                        if os.path.exists('./ttt/doc_ttt9/intro_ttt.txt'):
                            shutil.copy('./ttt/doc_ttt9/intro_ttt.txt',
                                './Backup/Files9/intro_ttt.txt')
                            print("+ ttt 9 copied")
                    except FileNotFoundError as nf_ttt9:
                        print("Not found", nf_ttt9)

                    try:
                        if os.path.exists('./ttt/doc_ttt10/intro_ttt.txt'):
                            shutil.copy('./ttt/doc_ttt10/intro_ttt.txt',
                                './Backup/Files10/intro_ttt.txt')
                            print("+ ttt 10 copied")
                    except FileNotFoundError as nf_ttt10:
                        print("Not found", nf_ttt10)

                    try:
                        if os.path.exists('./ttt/doc_ttt11/intro_ttt.txt'):
                            shutil.copy('./ttt/doc_ttt11/intro_ttt.txt',
                                './Backup/Files11/intro_ttt.txt')
                            print("+ ttt 11 copied")
                    except FileNotFoundError as nf_ttt11:
                        print("Not found", nf_ttt11)

                    try:
                        if os.path.exists('./ttt/doc_ttt12/intro_ttt.txt'):
                            shutil.copy('./ttt/doc_ttt12/intro_ttt.txt',
                                './Backup/Files12/intro_ttt.txt')
                            print("+ ttt 12 copied")
                    except FileNotFoundError as nf_ttt12:
                        print("Not found", nf_ttt12)

                    try:
                        if os.path.exists('./ttt/doc_ttt13/intro_ttt.txt'):
                            shutil.copy('./ttt/doc_ttt13/intro_ttt.txt',
                                './Backup/Files13/intro_ttt.txt')
                            print("+ ttt 13 copied")
                    except FileNotFoundError as nf_ttt13:
                        print("Not found", nf_ttt13)

                    try:
                        if os.path.exists('./ttt/doc_ttt14/intro_ttt.txt'):
                            shutil.copy('./ttt/doc_ttt14/intro_ttt.txt',
                                './Backup/Files14/intro_ttt.txt')
                            print("+ ttt 14 copied")
                    except FileNotFoundError as nf_ttt14:
                        print("Not found", nf_ttt14)

                    try:
                        if os.path.exists('./ttt/doc_ttt15/intro_ttt.txt'):
                            shutil.copy('./ttt/doc_ttt15/intro_ttt.txt',
                                './Backup/Files15/intro_ttt.txt')
                            print("+ ttt 15 copied")
                    except FileNotFoundError as nf_ttt15:
                        print("Not found", nf_ttt15)

                    try:
                        if os.path.exists('./ttt/doc_ttt16/intro_ttt.txt'):
                            shutil.copy('./ttt/doc_ttt16/intro_ttt.txt',
                                './Backup/Files16/intro_ttt.txt')
                            print("+ ttt 16 copied")
                    except FileNotFoundError as nf_ttt16:
                        print("Not found", nf_ttt16)

                    try:
                        if os.path.exists('./ttt/doc_ttt17/intro_ttt.txt'):
                            shutil.copy('./ttt/doc_ttt17/intro_ttt.txt',
                                './Backup/Files17/intro_ttt.txt')
                            print("+ ttt 17 copied")
                    except FileNotFoundError as nf_ttt17:
                        print("Not found", nf_ttt17)

                    try:
                        if os.path.exists('./ttt/doc_ttt18/intro_ttt.txt'):
                            shutil.copy('./ttt/doc_ttt18/intro_ttt.txt',
                                './Backup/Files18/intro_ttt.txt')
                            print("+ ttt 18 copied")
                    except FileNotFoundError as nf_ttt18:
                        print("Not found", nf_ttt18)

                    try:
                        if os.path.exists('./ttt/doc_ttt19/intro_ttt.txt'):
                            shutil.copy('./ttt/doc_ttt19/intro_ttt.txt',
                                './Backup/Files19/intro_ttt.txt')
                            print("+ ttt 19 copied")
                    except FileNotFoundError as nf_ttt19:
                        print("Not found", nf_ttt19)

                    try:
                        if os.path.exists('./ttt/doc_ttt20/intro_ttt.txt'):
                            shutil.copy('./ttt/doc_ttt20/intro_ttt.txt',
                                './Backup/Files20/intro_ttt.txt')
                            print("+ ttt 20 copied")
                    except FileNotFoundError as nf_ttt20:
                        print("Not found", nf_ttt20)

                    try:
                        if os.path.exists('./ttt/doc_ttt21/intro_ttt.txt'):
                            shutil.copy('./ttt/doc_ttt21/intro_ttt.txt',
                                './Backup/Files21/intro_ttt.txt')
                            print("+ ttt 21 copied")
                    except FileNotFoundError as nf_ttt21:
                        print("Not found", nf_ttt21)

                    try:
                        if os.path.exists('./ttt/doc_ttt22/intro_ttt.txt'):
                            shutil.copy('./ttt/doc_ttt22/intro_ttt.txt',
                                './Backup/Files22/intro_ttt.txt')
                            print("+ ttt 22 copied")
                    except FileNotFoundError as nf_ttt22:
                        print("Not found", nf_ttt22)

                    try:
                        if os.path.exists('./ttt/doc_ttt23/intro_ttt.txt'):
                            shutil.copy('./ttt/doc_ttt23/intro_ttt.txt',
                                './Backup/Files23/intro_ttt.txt')
                            print("+ ttt 23 copied")
                    except FileNotFoundError as nf_ttt23:
                        print("Not found", nf_ttt23)

                    try:
                        if os.path.exists('./ttt/doc_ttt24/intro_ttt.txt'):
                            shutil.copy('./ttt/doc_ttt24/intro_ttt.txt',
                                './Backup/Files24/intro_ttt.txt')
                            print("+ ttt 24 copied")
                    except FileNotFoundError as nf_ttt24:
                        print("Not found", nf_ttt24)

                    try:
                        if os.path.exists('./ttt/doc_ttt/intro_res.txt'):
                            shutil.copy('./ttt/doc_ttt/intro_res.txt',
                                './Backup/Files1/intro_res.txt')
                            print("+ ttt 1 copied")
                    except FileNotFoundError as nf_res:
                        print("Not found", nf_res)

                    try:
                        if os.path.exists('./ttt/doc_ttt2/intro_res.txt'):
                            shutil.copy('./ttt/doc_ttt2/intro_res.txt',
                                './Backup/Files2/intro_res.txt')
                            print("+ ttt 2 copied")
                    except FileNotFoundError as nf_res2:
                        print("Not found", nf_res2)

                    try:
                        if os.path.exists('./ttt/doc_ttt3/intro_res.txt'):
                            shutil.copy('./ttt/doc_ttt3/intro_res.txt',
                                './Backup/Files3/intro_res.txt')
                            print("+ ttt 3 copied")
                    except FileNotFoundError as nf_res3:
                        print("Not found", nf_res3)

                    try:
                        if os.path.exists('./ttt/doc_ttt4/intro_res.txt'):
                            shutil.copy('./ttt/doc_ttt4/intro_res.txt',
                                './Backup/Files4/intro_res.txt')
                            print("+ ttt 4 copied")
                    except FileNotFoundError as nf_res4:
                        print("Not found", nf_res4)

                    try:
                        if os.path.exists('./ttt/doc_ttt5/intro_res.txt'):
                            shutil.copy('./ttt/doc_ttt5/intro_res.txt',
                                './Backup/Files5/intro_res.txt')
                            print("+ ttt 5 copied")
                    except FileNotFoundError as nf_res5:
                        print("Not found", nf_res5)

                    try:
                        if os.path.exists('./ttt/doc_ttt6/intro_res.txt'):
                            shutil.copy('./ttt/doc_ttt6/intro_res.txt',
                                './Backup/Files6/intro_res.txt')
                            print("+ ttt 6 copied")
                    except FileNotFoundError as nf_res6:
                        print("Not found", nf_res6)

                    try:
                        if os.path.exists('./ttt/doc_ttt7/intro_res.txt'):
                            shutil.copy('./ttt/doc_ttt7/intro_res.txt',
                                './Backup/Files7/intro_res.txt')
                            print("+ ttt 7 copied")
                    except FileNotFoundError as nf_res7:
                        print("Not found", nf_res7)

                    try:
                        if os.path.exists('./ttt/doc_ttt8/intro_res.txt'):
                            shutil.copy('./ttt/doc_ttt8/intro_res.txt',
                                './Backup/Files8/intro_res.txt')
                            print("+ ttt 8 copied")
                    except FileNotFoundError as nf_res8:
                        print("Not found", nf_res8)

                    try:
                        if os.path.exists('./ttt/doc_ttt9/intro_res.txt'):
                            shutil.copy('./ttt/doc_ttt9/intro_res.txt',
                                './Backup/Files9/intro_res.txt')
                            print("+ ttt 9 copied")
                    except FileNotFoundError as nf_res9:
                        print("Not found", nf_res9)

                    try:
                        if os.path.exists('./ttt/doc_ttt10/intro_res.txt'):
                            shutil.copy('./ttt/doc_ttt10/intro_res.txt',
                                './Backup/Files10/intro_res.txt')
                            print("+ ttt 10 copied")
                    except FileNotFoundError as nf_res10:
                        print("Not found", nf_res10)

                    try:
                        if os.path.exists('./ttt/doc_ttt11/intro_res.txt'):
                            shutil.copy('./ttt/doc_ttt11/intro_res.txt',
                                './Backup/Files11/intro_res.txt')
                            print("+ ttt 11 copied")
                    except FileNotFoundError as nf_res11:
                        print("Not found", nf_res11)

                    try:
                        if os.path.exists('./ttt/doc_ttt12/intro_res.txt'):
                            shutil.copy('./ttt/doc_ttt12/intro_res.txt',
                                './Backup/Files12/intro_res.txt')
                            print("+ ttt 12 copied")
                    except FileNotFoundError as nf_res12:
                        print("Not found", nf_res12)

                    try:
                        if os.path.exists('./ttt/doc_ttt13/intro_res.txt'):
                            shutil.copy('./ttt/doc_ttt13/intro_res.txt',
                                './Backup/Files13/intro_res.txt')
                            print("+ ttt 13 copied")
                    except FileNotFoundError as nf_res13:
                        print("Not found", nf_res13)

                    try:
                        if os.path.exists('./ttt/doc_ttt14/intro_res.txt'):
                            shutil.copy('./ttt/doc_ttt14/intro_res.txt',
                                './Backup/Files14/intro_res.txt')
                            print("+ ttt 14 copied")
                    except FileNotFoundError as nf_res14:
                        print("Not found", nf_res14)

                    try:
                        if os.path.exists('./ttt/doc_ttt15/intro_res.txt'):
                            shutil.copy('./ttt/doc_ttt15/intro_res.txt',
                                './Backup/Files15/intro_res.txt')
                            print("+ ttt 15 copied")
                    except FileNotFoundError as nf_res15:
                        print("Not found", nf_res15)

                    try:
                        if os.path.exists('./ttt/doc_ttt16/intro_res.txt'):
                            shutil.copy('./ttt/doc_ttt16/intro_res.txt',
                                './Backup/Files16/intro_res.txt')
                            print("+ ttt 16 copied")
                    except FileNotFoundError as nf_res16:
                        print("Not found", nf_res16)

                    try:
                        if os.path.exists('./ttt/doc_ttt17/intro_res.txt'):
                            shutil.copy('./ttt/doc_ttt17/intro_res.txt',
                                './Backup/Files17/intro_res.txt')
                            print("+ ttt 17 copied")
                    except FileNotFoundError as nf_res17:
                        print("Not found", nf_res17)

                    try:
                        if os.path.exists('./ttt/doc_ttt18/intro_res.txt'):
                            shutil.copy('./ttt/doc_ttt18/intro_res.txt',
                                './Backup/Files18/intro_res.txt')
                            print("+ ttt 18 copied")
                    except FileNotFoundError as nf_res18:
                        print("Not found", nf_res18)

                    try:
                        if os.path.exists('./ttt/doc_ttt19/intro_res.txt'):
                            shutil.copy('./ttt/doc_ttt19/intro_res.txt',
                                './Backup/Files19/intro_res.txt')
                            print("+ ttt 19 copied")
                    except FileNotFoundError as nf_res19:
                        print("Not found", nf_res19)

                    try:
                        if os.path.exists('./ttt/doc_ttt20/intro_res.txt'):
                            shutil.copy('./ttt/doc_ttt20/intro_res.txt',
                                './Backup/Files20/intro_res.txt')
                            print("+ ttt 20 copied")
                    except FileNotFoundError as nf_res20:
                        print("Not found", nf_res20)

                    try:
                        if os.path.exists('./ttt/doc_ttt21/intro_res.txt'):
                            shutil.copy('./ttt/doc_ttt21/intro_res.txt',
                                './Backup/Files21/intro_res.txt')
                            print("+ ttt 21 copied")
                    except FileNotFoundError as nf_res21:
                        print("Not found", nf_res21)

                    try:
                        if os.path.exists('./ttt/doc_ttt22/intro_res.txt'):
                            shutil.copy('./ttt/doc_ttt22/intro_res.txt',
                                './Backup/Files22/intro_res.txt')
                            print("+ ttt 22 copied")
                    except FileNotFoundError as nf_res22:
                        print("Not found", nf_res22)

                    try:
                        if os.path.exists('./ttt/doc_ttt23/intro_res.txt'):
                            shutil.copy('./ttt/doc_ttt23/intro_res.txt',
                                './Backup/Files23/intro_res.txt')
                            print("+ ttt 23 copied")
                    except FileNotFoundError as nf_res23:
                        print("Not found", nf_res23)

                    try:
                        if os.path.exists('./ttt/doc_ttt24/intro_res.txt'):
                            shutil.copy('./ttt/doc_ttt24/intro_res.txt',
                                './Backup/Files24/intro_res.txt')
                            print("+ ttt 24 copied")
                    except FileNotFoundError as nf_res24:
                        print("Not found", nf_res24)

                    try:
                        if os.path.exists('./diag/doc_diag/diagrecap1.txt'):
                            shutil.copy('./diag/doc_diag/diagrecap1.txt',
                                './Backup/Files1/diagrecap1.txt')
                            print("+ diag 1 copied")
                    except FileNotFoundError as nf_diag:
                        print("Not found", nf_diag)

                    try:
                        if os.path.exists('./diag/doc_diag2/diagrecap2.txt'):
                            shutil.copy('./diag/doc_diag2/diagrecap2.txt',
                                './Backup/Files2/diagrecap2.txt')
                            print("+ diag 2 copied")
                    except FileNotFoundError as nf_diag2:
                        print("Not found", nf_diag2)

                    try:
                        if os.path.exists('./diag/doc_diag3/diagrecap3.txt'):
                            shutil.copy('./diag/doc_diag3/diagrecap3.txt',
                                './Backup/Files3/diagrecap3.txt')
                            print("+ diag 3 copied")
                    except FileNotFoundError as nf_diag3:
                        print("Not found", nf_diag3)

                    try:
                        if os.path.exists('./diag/doc_diag4/diagrecap4.txt'):
                            shutil.copy('./diag/doc_diag4/diagrecap4.txt',
                                './Backup/Files4/diagrecap4.txt')
                            print("+ diag 4 copied")
                    except FileNotFoundError as nf_diag4:
                        print("Not found", nf_diag4)

                    try:
                        if os.path.exists('./diag/doc_diag5/diagrecap5.txt'):
                            shutil.copy('./diag/doc_diag5/diagrecap5.txt',
                                './Backup/Files5/diagrecap5.txt')
                            print("+ diag 5 copied")
                    except FileNotFoundError as nf_diag5:
                        print("Not found", nf_diag5)

                    try:
                        if os.path.exists('./diag/doc_diag6/diagrecap6.txt'):
                            shutil.copy('./diag/doc_diag6/diagrecap6.txt',
                                './Backup/Files6/diagrecap6.txt')
                            print("+ diag 6 copied")
                    except FileNotFoundError as nf_diag6:
                        print("Not found", nf_diag6)

                    try:
                        if os.path.exists('./diag/doc_diag7/diagrecap7.txt'):
                            shutil.copy('./diag/doc_diag7/diagrecap7.txt',
                                './Backup/Files7/diagrecap7.txt')
                            print("+ diag 7 copied")
                    except FileNotFoundError as nf_diag7:
                        print("Not found", nf_diag7)

                    try:
                        if os.path.exists('./diag/doc_diag8/diagrecap8.txt'):
                            shutil.copy('./diag/doc_diag8/diagrecap8.txt',
                                './Backup/Files8/diagrecap8.txt')
                            print("+ diag 8 copied")
                    except FileNotFoundError as nf_diag8:
                        print("Not found", nf_diag8)

                    try:
                        if os.path.exists('./diag/doc_diag9/diagrecap9.txt'):
                            shutil.copy('./diag/doc_diag9/diagrecap9.txt',
                                './Backup/Files9/diagrecap9.txt')
                            print("+ diag 9 copied")
                    except FileNotFoundError as nf_diag9:
                        print("Not found", nf_diag9)

                    try:
                        if os.path.exists('./diag/doc_diag10/diagrecap10.txt'):
                            shutil.copy('./diag/doc_diag10/diagrecap10.txt',
                                './Backup/Files10/diagrecap10.txt')
                            print("+ diag 10 copied")
                    except FileNotFoundError as nf_diag10:
                        print("Not found", nf_diag10)

                    try:
                        if os.path.exists('./diag/doc_diag11/diagrecap11.txt'):
                            shutil.copy('./diag/doc_diag11/diagrecap11.txt',
                                './Backup/Files11/diagrecap11.txt')
                            print("+ diag 11 copied")
                    except FileNotFoundError as nf_diag11:
                        print("Not found", nf_diag11)

                    try:
                        if os.path.exists('./diag/doc_diag12/diagrecap12.txt'):
                            shutil.copy('./diag/doc_diag12/diagrecap12.txt',
                                './Backup/Files12/diagrecap12.txt')
                            print("+ diag 12 copied")
                    except FileNotFoundError as nf_diag12:
                        print("Not found", nf_diag12)

                    try:
                        if os.path.exists('./diag/doc_diag13/diagrecap13.txt'):
                            shutil.copy('./diag/doc_diag13/diagrecap13.txt',
                                './Backup/Files13/diagrecap13.txt')
                            print("+ diag 13 copied")
                    except FileNotFoundError as nf_diag13:
                        print("Not found", nf_diag13)

                    try:
                        if os.path.exists('./diag/doc_diag14/diagrecap14.txt'):
                            shutil.copy('./diag/doc_diag14/diagrecap14.txt',
                                './Backup/Files14/diagrecap14.txt')
                            print("+ diag 14 copied")
                    except FileNotFoundError as nf_diag14:
                        print("Not found", nf_diag14)

                    try:
                        if os.path.exists('./diag/doc_diag15/diagrecap15.txt'):
                            shutil.copy('./diag/doc_diag15/diagrecap15.txt',
                                './Backup/Files15/diagrecap15.txt')
                            print("+ diag 15 copied")
                    except FileNotFoundError as nf_diag15:
                        print("Not found", nf_diag15)

                    try:
                        if os.path.exists('./diag/doc_diag16/diagrecap16.txt'):
                            shutil.copy('./diag/doc_diag16/diagrecap16.txt',
                                './Backup/Files16/diagrecap16.txt')
                            print("+ diag 16 copied")
                    except FileNotFoundError as nf_diag16:
                        print("Not found", nf_diag16)

                    try:
                        if os.path.exists('./diag/doc_diag17/diagrecap17.txt'):
                            shutil.copy('./diag/doc_diag17/diagrecap17.txt',
                                './Backup/Files17/diagrecap17.txt')
                            print("+ diag 17 copied")
                    except FileNotFoundError as nf_diag17:
                        print("Not found", nf_diag17)

                    try:
                        if os.path.exists('./diag/doc_diag18/diagrecap18.txt'):
                            shutil.copy('./diag/doc_diag18/diagrecap18.txt',
                                './Backup/Files18/diagrecap18.txt')
                            print("+ diag 18 copied")
                    except FileNotFoundError as nf_diag18:
                        print("Not found", nf_diag18)

                    try:
                        if os.path.exists('./diag/doc_diag19/diagrecap19.txt'):
                            shutil.copy('./diag/doc_diag19/diagrecap19.txt',
                                './Backup/Files19/diagrecap19.txt')
                            print("+ diag 19 copied")
                    except FileNotFoundError as nf_diag19:
                        print("Not found", nf_diag19)

                    try:
                        if os.path.exists('./diag/doc_diag20/diagrecap20.txt'):
                            shutil.copy('./diag/doc_diag20/diagrecap20.txt',
                                './Backup/Files20/diagrecap20.txt')
                            print("+ diag 20 copied")
                    except FileNotFoundError as nf_diag20:
                        print("Not found", nf_diag20)

                    try:
                        if os.path.exists('./diag/doc_diag21/diagrecap21.txt'):
                            shutil.copy('./diag/doc_diag21/diagrecap21.txt',
                                './Backup/Files21/diagrecap21.txt')
                            print("+ diag 21 copied")
                    except FileNotFoundError as nf_diag21:
                        print("Not found", nf_diag21)

                    try:
                        if os.path.exists('./diag/doc_diag22/diagrecap22.txt'):
                            shutil.copy('./diag/doc_diag22/diagrecap22.txt',
                                './Backup/Files22/diagrecap22.txt')
                            print("+ diag 22 copied")
                    except FileNotFoundError as nf_diag22:
                        print("Not found", nf_diag22)

                    try:
                        if os.path.exists('./diag/doc_diag23/diagrecap23.txt'):
                            shutil.copy('./diag/doc_diag23/diagrecap23.txt',
                                './Backup/Files23/diagrecap23.txt')
                            print("+ diag 23 copied")
                    except FileNotFoundError as nf_diag23:
                        print("Not found", nf_diag23)

                    try:
                        if os.path.exists('./diag/doc_diag24/diagrecap24.txt'):
                            shutil.copy('./diag/doc_diag24/diagrecap24.txt',
                                './Backup/Files24/diagrecap24.txt')
                            print("+ diag 24 copied")
                    except FileNotFoundError as nf_diag24:
                        print("Not found", nf_diag24)

                    try:
                        if os.path.exists('./need/doc_suivi/main_14b.txt'):
                            shutil.copy('./need/doc_suivi/main_14b.txt',
                                './Backup/Files1/main_14b.txt')
                            print("+ need 1 copied")
                    except FileNotFoundError as nf_main:
                        print("Not found", nf_main)

                    try:
                        if os.path.exists('./need/doc_suivi2/main_14b.txt'):
                            shutil.copy('./need/doc_suivi2/main_14b.txt',
                                './Backup/Files2/main_14b.txt')
                            print("+ need 2 copied")
                    except FileNotFoundError as nf_main2:
                        print("Not found", nf_main2)

                    try:
                        if os.path.exists('./need/doc_suivi3/main_14b.txt'):
                            shutil.copy('./need/doc_suivi3/main_14b.txt',
                                './Backup/Files3/main_14b.txt')
                            print("+ need 3 copied")
                    except FileNotFoundError as nf_main3:
                        print("Not found", nf_main3)

                    try:
                        if os.path.exists('./need/doc_suivi4/main_14b.txt'):
                            shutil.copy('./need/doc_suivi4/main_14b.txt',
                                './Backup/Files4/main_14b.txt')
                            print("+ need 4 copied")
                    except FileNotFoundError as nf_main4:
                        print("Not found", nf_main4)

                    try:
                        if os.path.exists('./need/doc_suivi5/main_14b.txt'):
                            shutil.copy('./need/doc_suivi5/main_14b.txt',
                                './Backup/Files5/main_14b.txt')
                            print("+ need 5 copied")
                    except FileNotFoundError as nf_main5:
                        print("Not found", nf_main5)

                    try:
                        if os.path.exists('./need/doc_suivi6/main_14b.txt'):
                            shutil.copy('./need/doc_suivi6/main_14b.txt',
                                './Backup/Files6/main_14b.txt')
                            print("+ need 6 copied")
                    except FileNotFoundError as nf_main6:
                        print("Not found", nf_main6)

                    try:
                        if os.path.exists('./need/doc_suivi7/main_14b.txt'):
                            shutil.copy('./need/doc_suivi7/main_14b.txt',
                                './Backup/Files7/main_14b.txt')
                            print("+ need 7 copied")
                    except FileNotFoundError as nf_main7:
                        print("Not found", nf_main7)

                    try:
                        if os.path.exists('./need/doc_suivi8/main_14b.txt'):
                            shutil.copy('./need/doc_suivi8/main_14b.txt',
                                './Backup/Files8/main_14b.txt')
                            print("+ need 8 copied")
                    except FileNotFoundError as nf_main8:
                        print("Not found", nf_main8)

                    try:
                        if os.path.exists('./need/doc_suivi9/main_14b.txt'):
                            shutil.copy('./need/doc_suivi9/main_14b.txt',
                                './Backup/Files9/main_14b.txt')
                            print("+ need 9 copied")
                    except FileNotFoundError as nf_main9:
                        print("Not found", nf_main9)

                    try:
                        if os.path.exists('./need/doc_suivi10/main_14b.txt'):
                            shutil.copy('./need/doc_suivi10/main_14b.txt',
                                './Backup/Files10/main_14b.txt')
                            print("+ need 10 copied")
                    except FileNotFoundError as nf_main10:
                        print("Not found", nf_main10)

                    try:
                        if os.path.exists('./need/doc_suivi11/main_14b.txt'):
                            shutil.copy('./need/doc_suivi11/main_14b.txt',
                                './Backup/Files11/main_14b.txt')
                            print("+ need 11 copied")
                    except FileNotFoundError as nf_main11:
                        print("Not found", nf_main11)

                    try:
                        if os.path.exists('./need/doc_suivi12/main_14b.txt'):
                            shutil.copy('./need/doc_suivi12/main_14b.txt',
                                './Backup/Files12/main_14b.txt')
                            print("+ need 12 copied")
                    except FileNotFoundError as nf_main12:
                        print("Not found", nf_main12)

                    try:
                        if os.path.exists('./need/doc_suivi13/main_14b.txt'):
                            shutil.copy('./need/doc_suivi13/main_14b.txt',
                                './Backup/Files13/main_14b.txt')
                            print("+ need 13 copied")
                    except FileNotFoundError as nf_main13:
                        print("Not found", nf_main13)

                    try:
                        if os.path.exists('./need/doc_suivi14/main_14b.txt'):
                            shutil.copy('./need/doc_suivi14/main_14b.txt',
                                './Backup/Files14/main_14b.txt')
                            print("+ need 14 copied")
                    except FileNotFoundError as nf_main14:
                        print("Not found", nf_main14)

                    try:
                        if os.path.exists('./need/doc_suivi15/main_14b.txt'):
                            shutil.copy('./need/doc_suivi15/main_14b.txt',
                                './Backup/Files15/main_14b.txt')
                            print("+ need 15 copied")
                    except FileNotFoundError as nf_main15:
                        print("Not found", nf_main15)

                    try:
                        if os.path.exists('./need/doc_suivi16/main_14b.txt'):
                            shutil.copy('./need/doc_suivi16/main_14b.txt',
                                './Backup/Files16/main_14b.txt')
                            print("+ need 16 copied")
                    except FileNotFoundError as nf_main16:
                        print("Not found", nf_main16)

                    try:
                        if os.path.exists('./need/doc_suivi17/main_14b.txt'):
                            shutil.copy('./need/doc_suivi17/main_14b.txt',
                                './Backup/Files17/main_14b.txt')
                            print("+ need 17 copied")
                    except FileNotFoundError as nf_main17:
                        print("Not found", nf_main17)

                    try:
                        if os.path.exists('./need/doc_suivi18/main_14b.txt'):
                            shutil.copy('./need/doc_suivi18/main_14b.txt',
                                './Backup/Files18/main_14b.txt')
                            print("+ need 18 copied")
                    except FileNotFoundError as nf_main18:
                        print("Not found", nf_main18)

                    try:
                        if os.path.exists('./need/doc_suivi19/main_14b.txt'):
                            shutil.copy('./need/doc_suivi19/main_14b.txt',
                                './Backup/Files19/main_14b.txt')
                            print("+ need 19 copied")
                    except FileNotFoundError as nf_main19:
                        print("Not found", nf_main19)

                    try:
                        if os.path.exists('./need/doc_suivi20/main_14b.txt'):
                            shutil.copy('./need/doc_suivi20/main_14b.txt',
                                './Backup/Files20/main_14b.txt')
                            print("+ need 20 copied")
                    except FileNotFoundError as nf_main20:
                        print("Not found", nf_main20)

                    try:
                        if os.path.exists('./need/doc_suivi21/main_14b.txt'):
                            shutil.copy('./need/doc_suivi21/main_14b.txt',
                                './Backup/Files21/main_14b.txt')
                            print("+ need 21 copied")
                    except FileNotFoundError as nf_main21:
                        print("Not found", nf_main21)

                    try:
                        if os.path.exists('./need/doc_suivi22/main_14b.txt'):
                            shutil.copy('./need/doc_suivi22/main_14b.txt',
                                './Backup/Files22/main_14b.txt')
                            print("+ need 22 copied")
                    except FileNotFoundError as nf_main22:
                        print("Not found", nf_main22)

                    try:
                        if os.path.exists('./need/doc_suivi23/main_14b.txt'):
                            shutil.copy('./need/doc_suivi23/main_14b.txt',
                                './Backup/Files23/main_14b.txt')
                            print("+ need 23 copied")
                    except FileNotFoundError as nf_main23:
                        print("Not found", nf_main23)

                    try:
                        if os.path.exists('./need/doc_suivi24/main_14b.txt'):
                            shutil.copy('./need/doc_suivi24/main_14b.txt',
                                './Backup/Files24/main_14b.txt')
                            print("+ need 24 copied")
                    except FileNotFoundError as nf_main24:
                        print("Not found", nf_main24)

                    try:
                        if os.path.exists('./vmed/doc_vmed/resultvmed.txt'):
                            shutil.copy('./vmed/doc_vmed/resultvmed.txt',
                                './Backup/Files1/resultvmed.txt')
                            print("+ resultvmed.txt copied")
                    except FileNotFoundError as nf_rvm:
                        print("Not found", nf_rvm)

                    try:
                        if os.path.exists('./vmed/doc_vmed2/resultvmed2.txt'):
                            shutil.copy('./vmed/doc_vmed2/resultvmed2.txt',
                                './Backup/Files2/resultvmed2.txt')
                            print("+ resultvmed2.txt copied")
                    except FileNotFoundError as nf_rvm2:
                        print("Not found", nf_rvm2)

                    try:
                        if os.path.exists('./vmed/doc_vmed3/resultvmed3.txt'):
                            shutil.copy('./vmed/doc_vmed3/resultvmed3.txt',
                                './Backup/Files3/resultvmed3.txt')
                            print("+ resultvmed3.txt copied")
                    except FileNotFoundError as nf_rvm3:
                        print("Not found", nf_rvm3)

                    try:
                        if os.path.exists('./vmed/doc_vmed4/resultvmed4.txt'):
                            shutil.copy('./vmed/doc_vmed4/resultvmed4.txt',
                                './Backup/Files4/resultvmed4.txt')
                            print("+ resultvmed4.txt copied")
                    except FileNotFoundError as nf_rvm4:
                        print("Not found", nf_rvm4)

                    try:
                        if os.path.exists('./vmed/doc_vmed5/resultvmed5.txt'):
                            shutil.copy('./vmed/doc_vmed5/resultvmed5.txt',
                                './Backup/Files5/resultvmed5.txt')
                            print("+ resultvmed5.txt copied")
                    except FileNotFoundError as nf_rvm5:
                        print("Not found", nf_rvm5)

                    try:
                        if os.path.exists('./vmed/doc_vmed6/resultvmed6.txt'):
                            shutil.copy('./vmed/doc_vmed6/resultvmed6.txt',
                                './Backup/Files6/resultvmed6.txt')
                            print("+ resultvmed6.txt copied")
                    except FileNotFoundError as nf_rvm6:
                        print("Not found", nf_rvm6)

                    try:
                        if os.path.exists('./vmed/doc_vmed7/resultvmed7.txt'):
                            shutil.copy('./vmed/doc_vmed7/resultvmed7.txt',
                                './Backup/Files7/resultvmed7.txt')
                            print("+ resultvmed7.txt copied")
                    except FileNotFoundError as nf_rvm7:
                        print("Not found", nf_rvm7)

                    try:
                        if os.path.exists('./vmed/doc_vmed8/resultvmed8.txt'):
                            shutil.copy('./vmed/doc_vmed8/resultvmed8.txt',
                                './Backup/Files8/resultvmed8.txt')
                            print("+ resultvmed8.txt copied")
                    except FileNotFoundError as nf_rvm8:
                        print("Not found", nf_rvm8)

                    try:
                        if os.path.exists('./vmed/doc_vmed9/resultvmed9.txt'):
                            shutil.copy('./vmed/doc_vmed9/resultvmed9.txt',
                                './Backup/Files9/resultvmed9.txt')
                            print("+ resultvmed9.txt copied")
                    except FileNotFoundError as nf_rvm9:
                        print("Not found", nf_rvm9)

                    try:
                        if os.path.exists('./vmed/doc_vmed10/resultvmed10.txt'):
                            shutil.copy('./vmed/doc_vmed10/resultvmed10.txt',
                                './Backup/Files10/resultvmed10.txt')
                            print("+ resultvmed10.txt copied")
                    except FileNotFoundError as nf_rvm10:
                        print("Not found", nf_rvm10)

                    try:
                        if os.path.exists('./vmed/doc_vmed11/resultvmed11.txt'):
                            shutil.copy('./vmed/doc_vmed11/resultvmed11.txt',
                                './Backup/Files11/resultvmed11.txt')
                            print("+ resultvmed11.txt copied")
                    except FileNotFoundError as nf_rvm11:
                        print("Not found", nf_rvm11)

                    try:
                        if os.path.exists('./vmed/doc_vmed12/resultvmed12.txt'):
                            shutil.copy('./vmed/doc_vmed12/resultvmed12.txt',
                                './Backup/Files12/resultvmed12.txt')
                            print("+ resultvmed12.txt copied")
                    except FileNotFoundError as nf_rvm12:
                        print("Not found", nf_rvm12)

                    try:
                        if os.path.exists('./vmed/doc_vmed13/resultvmed13.txt'):
                            shutil.copy('./vmed/doc_vmed13/resultvmed13.txt',
                                './Backup/Files13/resultvmed13.txt')
                            print("+ resultvmed13.txt copied")
                    except FileNotFoundError as nf_rvm13:
                        print("Not found", nf_rvm13)

                    try:
                        if os.path.exists('./vmed/doc_vmed14/resultvmed14.txt'):
                            shutil.copy('./vmed/doc_vmed14/resultvmed14.txt',
                                './Backup/Files14/resultvmed14.txt')
                            print("+ resultvmed14.txt copied")
                    except FileNotFoundError as nf_rvm14:
                        print("Not found", nf_rvm14)

                    try:
                        if os.path.exists('./vmed/doc_vmed15/resultvmed15.txt'):
                            shutil.copy('./vmed/doc_vmed15/resultvmed15.txt',
                                './Backup/Files15/resultvmed15.txt')
                            print("+ resultvmed15.txt copied")
                    except FileNotFoundError as nf_rvm15:
                        print("Not found", nf_rvm15)

                    try:
                        if os.path.exists('./vmed/doc_vmed16/resultvmed16.txt'):
                            shutil.copy('./vmed/doc_vmed16/resultvmed16.txt',
                                './Backup/Files16/resultvmed16.txt')
                            print("+ resultvmed16.txt copied")
                    except FileNotFoundError as nf_rvm16:
                        print("Not found", nf_rvm16)

                    try:
                        if os.path.exists('./vmed/doc_vmed17/resultvmed17.txt'):
                            shutil.copy('./vmed/doc_vmed17/resultvmed17.txt',
                                './Backup/Files17/resultvmed17.txt')
                            print("+ resultvmed17.txt copied")
                    except FileNotFoundError as nf_rvm17:
                        print("Not found", nf_rvm17)

                    try:
                        if os.path.exists('./vmed/doc_vmed18/resultvmed18.txt'):
                            shutil.copy('./vmed/doc_vmed18/resultvmed18.txt',
                                './Backup/Files18/resultvmed18.txt')
                            print("+ resultvmed18.txt copied")
                    except FileNotFoundError as nf_rvm18:
                        print("Not found", nf_rvm18)

                    try:
                        if os.path.exists('./vmed/doc_vmed19/resultvmed19.txt'):
                            shutil.copy('./vmed/doc_vmed19/resultvmed19.txt',
                                './Backup/Files19/resultvmed19.txt')
                            print("+ resultvmed19.txt copied")
                    except FileNotFoundError as nf_rvm19:
                        print("Not found", nf_rvm19)

                    try:
                        if os.path.exists('./vmed/doc_vmed20/resultvmed20.txt'):
                            shutil.copy('./vmed/doc_vmed20/resultvmed20.txt',
                                './Backup/Files20/resultvmed20.txt')
                            print("+ resultvmed20.txt copied")
                    except FileNotFoundError as nf_rvm20:
                        print("Not found", nf_rvm20)

                    try:
                        if os.path.exists('./vmed/doc_vmed21/resultvmed21.txt'):
                            shutil.copy('./vmed/doc_vmed21/resultvmed21.txt',
                                './Backup/Files21/resultvmed21.txt')
                            print("+ resultvmed21.txt copied")
                    except FileNotFoundError as nf_rvm21:
                        print("Not found", nf_rvm21)

                    try:
                        if os.path.exists('./vmed/doc_vmed22/resultvmed22.txt'):
                            shutil.copy('./vmed/doc_vmed22/resultvmed22.txt',
                                './Backup/Files22/resultvmed22.txt')
                            print("+ resultvmed22.txt copied")
                    except FileNotFoundError as nf_rvm22:
                        print("Not found", nf_rvm22)

                    try:
                        if os.path.exists('./vmed/doc_vmed23/resultvmed23.txt'):
                            shutil.copy('./vmed/doc_vmed23/resultvmed23.txt',
                                './Backup/Files23/resultvmed23.txt')
                            print("+ resultvmed23.txt copied")
                    except FileNotFoundError as nf_rvm23:
                        print("Not found", nf_rvm23)

                    try:
                        if os.path.exists('./vmed/doc_vmed24/resultvmed24.txt'):
                            shutil.copy('./vmed/doc_vmed24/resultvmed24.txt',
                                './Backup/Files24/resultvmed24.txt')
                            print("+ resultvmed24.txt copied")
                    except FileNotFoundError as nf_rvm24:
                        print("Not found", nf_rvm24)

                    x=str(x)
                    value.remove(x)
                    file_w = open("./Backup/xdate_file.json", "w")
                    listeDate = json.dump(listeDate, file_w, indent=4)
                    print("--- Backup done ---")
                    messagebox.showinfo('INFO', 'BACKUP done !')
                    messagebox.showinfo('INFO', 'Go to Global to read one of them !')
