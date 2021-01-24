#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
from tkinter import messagebox
import datetime
import time
import os
import subprocess
import shutil


def dispAgBox():
    """
    Display messagebox for agenda if an
    appointment has been fixed for tomorrow.
    Display nothing if rdv canceled
    """
    # Patient 1
    try:
        with open('./newpatient/entryfile.txt', 'r') as namefile:
            line1 = namefile.readline()
            new_text1 = line1
    except FileNotFoundError as fileout1:
        print("No file entryfile.txt exist", fileout1)

    try:
        magicword = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if magicword in line:
                            print("Nous y voici !")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : ' \
                                + new_text1 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM1 = messagebox.askyesno("Ask", "Do you want to stop reminders ?")
                            if MSGREM1 == 1:
                                mwrename = magicword.replace("/", ".")
                                write_f = open(os.path.join(path, file), 'w')
                                write_f.write(" Rdv past--> " + mwrename + "\n" +
                                    lines[i+1] + lines[i+2] + "\n")
                                print("+ Modification finish")
                                break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile1:
        print("File 1 has not been found", infofile1)
    else:
        ("Error unknow")

    try:
        # To copy to ./Backup/Files1
        src = r'./patient_agenda/events/doc_events/fix_agenda/agenda_saved'
        dst = r'./Backup/Files1'
        shutil.copy(os.path.join(src, file), dst)
    except (OSError, FileNotFoundError) as e:
        print("+ No files from agenda_1 copied !!!", e)

    # To upload to server
    proc = subprocess.run(["scp", "-r", "./Backup/Files1",
        "pi@192.168.18.12:~/tt_doc/doc_txt1"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if proc.stderr == b'':
        print("+ './Backup/Files1' uploaded !")
    else:
        print("+ No file to upload !")
        messagebox.showerror("Error", "./Backup/Files1 not uploaded !")

    # Patient 2
    try:
        with open('./newpatient/entryfile2.txt', 'r') as namefile:
            line2 = namefile.readline()
            new_text2 = line2
    except FileNotFoundError as fileout2:
        print("No file entryfile2.txt exist", fileout2)

    try:
        magicword2 = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events2/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if magicword2 in line:
                            print("Nous y voici !")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : ' \
                                + new_text2 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM2 = messagebox.askyesno("Ask", "Do you want to stop reminders ?")
                            if MSGREM2 == 1:
                                mwrename2 = magicword2.replace("/", ".")
                                write_f = open(os.path.join(path, file), 'w')
                                write_f.write(" Rdv past--> " + mwrename2 + "\n" +
                                    lines[i+1] + lines[i+2] + "\n")
                                print("+ Modification finish")
                                break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile2:
        print("File 2 has not been found", infofile2)
    else:
        ("Error unknow")

    # To copy to ./Backup/Files2
    try:
        # To copy to ./Backup/Files2
        src2 = r'./patient_agenda/events2/doc_events/fix_agenda/agenda_saved'
        dst2 = r'./Backup/Files2'
        shutil.copy(os.path.join(src2, file), dst2)
    except (OSError, FileNotFoundError) as e2:
        print("+ No files from agenda_2 copied !!!", e2)
    
    secproc = subprocess.run(["scp", "-r", "./Backup/Files2",
        "pi@192.168.18.12:~/tt_doc/doc_txt2"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if secproc.stderr == b'':
        print("+ './Backup/Files2' uploaded !")
    else:
        print("+ No file to upload !")
        messagebox.showerror("Error", "./Backup/Files2 not uploaded !")

    # Patient 3
    try:
        with open('./newpatient/entryfile3.txt', 'r') as namefile:
            line3 = namefile.readline()
            new_text3 = line3
    except FileNotFoundError as fileout3:
        print("No file entryfile3.txt exist", fileout3)

    try:
        magicword3 = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events3/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if magicword3 in line:
                            print("Nous y voici !")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : ' \
                                + new_text3 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM3 = messagebox.askyesno("Ask", "Do you want to stop reminders ?")
                            if MSGREM3 == 1:
                                mwrename3 = magicword3.replace("/", ".")
                                write_f = open(os.path.join(path, file), 'w')
                                write_f.write(" Rdv past--> " + mwrename3 + "\n" +
                                    lines[i+1] + lines[i+2] + "\n")
                                print("+ Modification finish")
                                break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile3:
        print("File 3 has not been found", infofile3)
    else:
        ("Error unknow")

    # To copy to ./Backup/Files3
    try:
        # To copy to ./Backup/Files3
        src3 = r'./patient_agenda/events3/doc_events/fix_agenda/agenda_saved'
        dst3 = r'./Backup/Files3'
        shutil.copy(os.path.join(src3, file), dst3)
    except (OSError, FileNotFoundError) as err_3shut:
        print("+ No files from agenda_3 copied !!!", err_3shut)
    
    secproc = subprocess.run(["scp", "-r", "./Backup/Files3",
        "pi@192.168.18.12:~/tt_doc/doc_txt3"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if secproc.stderr == b'':
        print("+ './Backup/Files3' uploaded !")
    else:
        print("+ No file to upload !")
        messagebox.showerror("Error", "./Backup/Files3 not uploaded !")

    # Patient 4
    try:
        with open('./newpatient/entryfile4.txt', 'r') as namefile:
            line4 = namefile.readline()
            new_text4 = line4
    except FileNotFoundError as fileout4:
        print("No file entryfile4.txt exist", fileout4)

    try:
        magicword4 = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events4/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if magicword4 in line:
                            print("Nous y voici !")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : ' \
                                + new_text4 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM4 = messagebox.askyesno("Ask", "Do you want to stop reminders ?")
                            if MSGREM4 == 1:
                                mwrename4 = magicword4.replace("/", ".")
                                write_f = open(os.path.join(path, file), 'w')
                                write_f.write(" Rdv past--> " + mwrename4 + "\n" +
                                    lines[i+1] + lines[i+2] + "\n")
                                print("+ Modification finish")
                                break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile4:
        print("File 4 has not been found", infofile4)
    else:
        ("Error unknow")

    # To copy to ./Backup/Files4
    try:
        # To copy to ./Backup/Files4
        src4 = r'./patient_agenda/events4/doc_events/fix_agenda/agenda_saved'
        dst4 = r'./Backup/Files4'
        shutil.copy(os.path.join(src4, file), dst4)
    except (OSError, FileNotFoundError) as err_4shut:
        print("+ No files from agenda_4 copied !!!", err_4shut)
    
    secproc = subprocess.run(["scp", "-r", "./Backup/Files4",
        "pi@192.168.18.12:~/tt_doc/doc_txt4"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if secproc.stderr == b'':
        print("+ './Backup/Files4' uploaded !")
    else:
        print("+ No file to upload !")
        messagebox.showerror("Error", "./Backup/Files4 not uploaded !")

    # Patient 5
    try:
        with open('./newpatient/entryfile5.txt', 'r') as namefile:
            line5 = namefile.readline()
            new_text5 = line5
    except FileNotFoundError as fileout5:
        print("No file entryfile5.txt exist", fileout5)

    try:
        magicword5 = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events5/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if magicword5 in line:
                            print("Nous y voici !")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : ' \
                                + new_text5 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM5 = messagebox.askyesno("Ask", "Do you want to stop reminders ?")
                            if MSGREM5 == 1:
                                mwrename5 = magicword5.replace("/", ".")
                                write_f = open(os.path.join(path, file), 'w')
                                write_f.write(" Rdv past--> " + mwrename5 + "\n" +
                                    lines[i+1] + lines[i+2] + "\n")
                                print("+ Modification finish")
                                break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile5:
        print("File 5 has not been found", infofile5)
    else:
        ("Error unknow")

    # To copy to ./Backup/Files5
    try:
        # To copy to ./Backup/Files5
        src5 = r'./patient_agenda/events5/doc_events/fix_agenda/agenda_saved'
        dst5 = r'./Backup/Files5'
        shutil.copy(os.path.join(src5, file), dst5)
    except (OSError, FileNotFoundError) as err_5shut:
        print("+ No files from agenda_5 copied !!!", err_5shut)
    
    secproc = subprocess.run(["scp", "-r", "./Backup/Files5",
        "pi@192.168.18.12:~/tt_doc/doc_txt5"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if secproc.stderr == b'':
        print("+ './Backup/Files5' uploaded !")
    else:
        print("+ No file to upload !")
        messagebox.showerror("Error", "./Backup/Files5 not uploaded !")

    # Patient 6
    try:
        with open('./newpatient/entryfile6.txt', 'r') as namefile:
            line6 = namefile.readline()
            new_text6 = line6
    except FileNotFoundError as fileout6:
        print("No file entryfile6.txt exist", fileout6)

    try:
        magicword6 = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events6/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if magicword6 in line:
                            print("Nous y voici !")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : ' \
                                + new_text6 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM6 = messagebox.askyesno("Ask", "Do you want to stop reminders ?")
                            if MSGREM6 == 1:
                                mwrename6 = magicword6.replace("/", ".")
                                write_f = open(os.path.join(path, file), 'w')
                                write_f.write(" Rdv past--> " + mwrename6 + "\n" +
                                    lines[i+1] + lines[i+2] + "\n")
                                print("+ Modification finish")
                                break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile6:
        print("File 6 has not been found", infofile6)
    else:
        ("Error unknow")

    # To copy to ./Backup/Files6
    try:
        # To copy to ./Backup/Files6
        src6 = r'./patient_agenda/events6/doc_events/fix_agenda/agenda_saved'
        dst6 = r'./Backup/Files6'
        shutil.copy(os.path.join(src6, file), dst6)
    except (OSError, FileNotFoundError) as err_6shut:
        print("+ No files from agenda_6 copied !!!", err_6shut)
    
    secproc = subprocess.run(["scp", "-r", "./Backup/Files6",
        "pi@192.168.18.12:~/tt_doc/doc_txt6"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if secproc.stderr == b'':
        print("+ './Backup/Files6' uploaded !")
    else:
        print("+ No file to upload !")
        messagebox.showerror("Error", "./Backup/Files6 not uploaded !")

    # Patient 7
    try:
        with open('./newpatient/entryfile7.txt', 'r') as namefile:
            line7 = namefile.readline()
            new_text7 = line7
    except FileNotFoundError as fileout7:
        print("No file entryfile7.txt exist", fileout7)

    try:
        magicword7 = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events7/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if magicword7 in line:
                            print("Nous y voici !")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : ' \
                                + new_text7 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM7 = messagebox.askyesno("Ask", "Do you want to stop reminders ?")
                            if MSGREM7 == 1:
                                mwrename7 = magicword7.replace("/", ".")
                                write_f = open(os.path.join(path, file), 'w')
                                write_f.write(" Rdv past--> " + mwrename7 + "\n" +
                                    lines[i+1] + lines[i+2] + "\n")
                                print("+ Modification finish")
                                break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile7:
        print("File 7 has not been found", infofile7)
    else:
        ("Error unknow")

    # To copy to ./Backup/Files7
    try:
        # To copy to ./Backup/Files7
        src7 = r'./patient_agenda/events7/doc_events/fix_agenda/agenda_saved'
        dst7 = r'./Backup/Files7'
        shutil.copy(os.path.join(src7, file), dst7)
    except (OSError, FileNotFoundError) as err_7shut:
        print("+ No files from agenda_7 copied !!!", err_7shut)
    
    secproc = subprocess.run(["scp", "-r", "./Backup/Files7",
        "pi@192.168.18.12:~/tt_doc/doc_txt7"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if secproc.stderr == b'':
        print("+ './Backup/Files7' uploaded !")
    else:
        print("+ No file to upload !")
        messagebox.showerror("Error", "./Backup/Files7 not uploaded !")

    # Patient 8
    try:
        with open('./newpatient/entryfile8.txt', 'r') as namefile:
            line8 = namefile.readline()
            new_text8 = line8
    except FileNotFoundError as fileout8:
        print("No file entryfile8.txt exist", fileout8)

    try:
        magicword8 = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events8/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if magicword8 in line:
                            print("Nous y voici !")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : ' \
                                + new_text8 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM8 = messagebox.askyesno("Ask", "Do you want to stop reminders ?")
                            if MSGREM8 == 1:
                                mwrename8 = magicword8.replace("/", ".")
                                write_f = open(os.path.join(path, file), 'w')
                                write_f.write(" Rdv past--> " + mwrename8 + "\n" +
                                    lines[i+1] + lines[i+2] + "\n")
                                print("+ Modification finish")
                                break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile8:
        print("File 8 has not been found", infofile8)
    else:
        ("Error unknow")

    # To copy to ./Backup/Files8
    try:
        # To copy to ./Backup/Files8
        src8 = r'./patient_agenda/events8/doc_events/fix_agenda/agenda_saved'
        dst8 = r'./Backup/Files8'
        shutil.copy(os.path.join(src8, file), dst8)
    except (OSError, FileNotFoundError) as err_8shut:
        print("+ No files from agenda_8 copied !!!", err_8shut)
    
    secproc = subprocess.run(["scp", "-r", "./Backup/Files8",
        "pi@192.168.18.12:~/tt_doc/doc_txt8"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if secproc.stderr == b'':
        print("+ './Backup/Files8' uploaded !")
    else:
        print("+ No file to upload !")
        messagebox.showerror("Error", "./Backup/Files8 not uploaded !")

    # Patient 9
    try:
        with open('./newpatient/entryfile9.txt', 'r') as namefile:
            line9 = namefile.readline()
            new_text9 = line9
    except FileNotFoundError as fileout9:
        print("No file entryfile9.txt exist", fileout9)

    try:
        magicword9 = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events9/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if magicword9 in line:
                            print("Nous y voici !")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : ' \
                                + new_text9 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM9 = messagebox.askyesno("Ask", "Do you want to stop reminders ?")
                            if MSGREM9 == 1:
                                mwrename9 = magicword9.replace("/", ".")
                                write_f = open(os.path.join(path, file), 'w')
                                write_f.write(" Rdv past--> " + mwrename9 + "\n" +
                                    lines[i+1] + lines[i+2] + "\n")
                                print("+ Modification finish")
                                break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile9:
        print("File 9 has not been found", infofile9)
    else:
        ("Error unknow")

    # To copy to ./Backup/Files9
    try:
        # To copy to ./Backup/Files9
        src9 = r'./patient_agenda/events9/doc_events/fix_agenda/agenda_saved'
        dst9 = r'./Backup/Files9'
        shutil.copy(os.path.join(src9, file), dst9)
    except (OSError, FileNotFoundError) as err_9shut:
        print("+ No files from agenda_9 copied !!!", err_9shut)
    
    secproc = subprocess.run(["scp", "-r", "./Backup/Files9",
        "pi@192.168.18.12:~/tt_doc/doc_txt9"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if secproc.stderr == b'':
        print("+ './Backup/Files9' uploaded !")
    else:
        print("+ No file to upload !")
        messagebox.showerror("Error", "./Backup/Files9 not uploaded !")

    # Patient 10
    try:
        with open('./newpatient/entryfile10.txt', 'r') as namefile:
            line10 = namefile.readline()
            new_text10 = line10
    except FileNotFoundError as fileout10:
        print("No file entryfile10.txt exist", fileout10)

    try:
        magicword10 = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events10/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if magicword10 in line:
                            print("Nous y voici !")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : ' \
                                + new_text10 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM10 = messagebox.askyesno("Ask", "Do you want to stop reminders ?")
                            if MSGREM10 == 1:
                                mwrename10 = magicword10.replace("/", ".")
                                write_f = open(os.path.join(path, file), 'w')
                                write_f.write(" Rdv past--> " + mwrename10 + "\n" +
                                    lines[i+1] + lines[i+2] + "\n")
                                print("+ Modification finish")
                                break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile10:
        print("File 10 has not been found", infofile10)
    else:
        ("Error unknow")

    # To copy to ./Backup/Files10
    try:
        # To copy to ./Backup/Files10
        src10 = r'./patient_agenda/events10/doc_events/fix_agenda/agenda_saved'
        dst10 = r'./Backup/Files10'
        shutil.copy(os.path.join(src10, file), dst10)
    except (OSError, FileNotFoundError) as err_10shut:
        print("+ No files from agenda_10 copied !!!", err_10shut)
    
    secproc = subprocess.run(["scp", "-r", "./Backup/Files10",
        "pi@192.168.18.12:~/tt_doc/doc_txt10"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if secproc.stderr == b'':
        print("+ './Backup/Files10' uploaded !")
    else:
        print("+ No file to upload !")
        messagebox.showerror("Error", "./Backup/Files10 not uploaded !")

    # Patient 11
    try:
        with open('./newpatient/entryfile11.txt', 'r') as namefile:
            line11 = namefile.readline()
            new_text11 = line11
    except FileNotFoundError as fileout11:
        print("No file entryfile11.txt exist", fileout11)

    try:
        magicword11 = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events11/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if magicword11 in line:
                            print("Nous y voici !")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : ' \
                                + new_text11 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM11 = messagebox.askyesno("Ask", "Do you want to stop reminders ?")
                            if MSGREM11 == 1:
                                mwrename11 = magicword11.replace("/", ".")
                                write_f = open(os.path.join(path, file), 'w')
                                write_f.write(" Rdv past--> " + mwrename11 + "\n" +
                                    lines[i+1] + lines[i+2] + "\n")
                                print("+ Modification finish")
                                break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile11:
        print("File 11 has not been found", infofile11)
    else:
        ("Error unknow")

    # To copy to ./Backup/Files11
    try:
        # To copy to ./Backup/Files11
        src11 = r'./patient_agenda/events11/doc_events/fix_agenda/agenda_saved'
        dst11 = r'./Backup/Files11'
        shutil.copy(os.path.join(src11, file), dst11)
    except (OSError, FileNotFoundError) as err_11shut:
        print("+ No files from agenda_11 copied !!!", err_11shut)
    
    secproc = subprocess.run(["scp", "-r", "./Backup/Files11",
        "pi@192.168.18.12:~/tt_doc/doc_txt11"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if secproc.stderr == b'':
        print("+ './Backup/Files11' uploaded !")
    else:
        print("+ No file to upload !")
        messagebox.showerror("Error", "./Backup/Files11 not uploaded !")

    # Patient 12
    try:
        with open('./newpatient/entryfile12.txt', 'r') as namefile:
            line12 = namefile.readline()
            new_text12 = line12
    except FileNotFoundError as fileout12:
        print("No file entryfile12.txt exist", fileout12)

    try:
        magicword12 = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events12/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if magicword12 in line:
                            print("Nous y voici !")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : ' \
                                + new_text12 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM12 = messagebox.askyesno("Ask", "Do you want to stop reminders ?")
                            if MSGREM12 == 1:
                                mwrename12 = magicword12.replace("/", ".")
                                write_f = open(os.path.join(path, file), 'w')
                                write_f.write(" Rdv past--> " + mwrename12 + "\n" +
                                    lines[i+1] + lines[i+2] + "\n")
                                print("+ Modification finish")
                                break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile12:
        print("File 12 has not been found", infofile12)
    else:
        ("Error unknow")

    # To copy to ./Backup/Files12
    try:
        # To copy to ./Backup/Files12
        src12 = r'./patient_agenda/events12/doc_events/fix_agenda/agenda_saved'
        dst12 = r'./Backup/Files12'
        shutil.copy(os.path.join(src12, file), dst12)
    except (OSError, FileNotFoundError) as err_12shut:
        print("+ No files from agenda_12 copied !!!", err_12shut)
    
    secproc = subprocess.run(["scp", "-r", "./Backup/Files12",
        "pi@192.168.18.12:~/tt_doc/doc_txt12"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if secproc.stderr == b'':
        print("+ './Backup/Files12' uploaded !")
    else:
        print("+ No file to upload !")
        messagebox.showerror("Error", "./Backup/Files12 not uploaded !")

    # Patient 13
    try:
        with open('./newpatient/entryfile13.txt', 'r') as namefile:
            line13 = namefile.readline()
            new_text13 = line13
    except FileNotFoundError as fileout13:
        print("No file entryfile13.txt exist", fileout13)

    try:
        magicword13 = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events13/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if magicword13 in line:
                            print("Nous y voici !")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : ' \
                                + new_text13 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM13 = messagebox.askyesno("Ask", "Do you want to stop reminders ?")
                            if MSGREM13 == 1:
                                mwrename13 = magicword13.replace("/", ".")
                                write_f = open(os.path.join(path, file), 'w')
                                write_f.write(" Rdv past--> " + mwrename13 + "\n" +
                                    lines[i+1] + lines[i+2] + "\n")
                                print("+ Modification finish")
                                break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile13:
        print("File 13 has not been found", infofile13)
    else:
        ("Error unknow")

    # To copy to ./Backup/Files13
    try:
        # To copy to ./Backup/Files13
        src13 = r'./patient_agenda/events13/doc_events/fix_agenda/agenda_saved'
        dst13 = r'./Backup/Files13'
        shutil.copy(os.path.join(src13, file), dst13)
    except (OSError, FileNotFoundError) as err_13shut:
        print("+ No files from agenda_13 copied !!!", err_13shut)
    
    secproc = subprocess.run(["scp", "-r", "./Backup/Files13",
        "pi@192.168.18.12:~/tt_doc/doc_txt13"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if secproc.stderr == b'':
        print("+ './Backup/Files13' uploaded !")
    else:
        print("+ No file to upload !")
        messagebox.showerror("Error", "./Backup/Files13 not uploaded !")

    # Patient 14
    try:
        with open('./newpatient/entryfile14.txt', 'r') as namefile:
            line14 = namefile.readline()
            new_text14 = line14
    except FileNotFoundError as fileout14:
        print("No file entryfile14.txt exist", fileout14)

    try:
        magicword14 = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events14/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if magicword14 in line:
                            print("Nous y voici !")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : ' \
                                + new_text14 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM14 = messagebox.askyesno("Ask", "Do you want to stop reminders ?")
                            if MSGREM14 == 1:
                                mwrename14 = magicword14.replace("/", ".")
                                write_f = open(os.path.join(path, file), 'w')
                                write_f.write(" Rdv past--> " + mwrename14 + "\n" +
                                    lines[i+1] + lines[i+2] + "\n")
                                print("+ Modification finish")
                                break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile14:
        print("File 14 has not been found", infofile14)
    else:
        ("Error unknow")

    # To copy to ./Backup/Files14
    try:
        # To copy to ./Backup/Files14
        src14 = r'./patient_agenda/events14/doc_events/fix_agenda/agenda_saved'
        dst14 = r'./Backup/Files14'
        shutil.copy(os.path.join(src14, file), dst14)
    except (OSError, FileNotFoundError) as err_14shut:
        print("+ No files from agenda_14 copied !!!", err_14shut)
    
    secproc = subprocess.run(["scp", "-r", "./Backup/Files14",
        "pi@192.168.18.12:~/tt_doc/doc_txt14"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if secproc.stderr == b'':
        print("+ './Backup/Files14' uploaded !")
    else:
        print("+ No file to upload !")
        messagebox.showerror("Error", "./Backup/Files14 not uploaded !")

    # Patient 15
    try:
        with open('./newpatient/entryfile15.txt', 'r') as namefile:
            line15 = namefile.readline()
            new_text15 = line15
    except FileNotFoundError as fileout15:
        print("No file entryfile15.txt exist", fileout15)

    try:
        magicword15 = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events15/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if magicword15 in line:
                            print("Nous y voici !")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : ' \
                                + new_text15 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM15 = messagebox.askyesno("Ask", "Do you want to stop reminders ?")
                            if MSGREM15 == 1:
                                mwrename15 = magicword15.replace("/", ".")
                                write_f = open(os.path.join(path, file), 'w')
                                write_f.write(" Rdv past--> " + mwrename15 + "\n" +
                                    lines[i+1] + lines[i+2] + "\n")
                                print("+ Modification finish")
                                break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile15:
        print("File 15 has not been found", infofile15)
    else:
        ("Error unknow")

    # To copy to ./Backup/Files15
    try:
        # To copy to ./Backup/Files15
        src15 = r'./patient_agenda/events15/doc_events/fix_agenda/agenda_saved'
        dst15 = r'./Backup/Files15'
        shutil.copy(os.path.join(src15, file), dst15)
    except (OSError, FileNotFoundError) as err_15shut:
        print("+ No files from agenda_15 copied !!!", err_15shut)
    
    secproc = subprocess.run(["scp", "-r", "./Backup/Files15",
        "pi@192.168.18.12:~/tt_doc/doc_txt15"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if secproc.stderr == b'':
        print("+ './Backup/Files15' uploaded !")
    else:
        print("+ No file to upload !")
        messagebox.showerror("Error", "./Backup/Files15 not uploaded !")

    # Patient 16
    try:
        with open('./newpatient/entryfile16.txt', 'r') as namefile:
            line16 = namefile.readline()
            new_text16 = line16
    except FileNotFoundError as fileout16:
        print("No file entryfile16.txt exist", fileout16)

    try:
        magicword16 = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events16/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if magicword16 in line:
                            print("Nous y voici !")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : ' \
                                + new_text16 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM16 = messagebox.askyesno("Ask", "Do you want to stop reminders ?")
                            if MSGREM16 == 1:
                                mwrename16 = magicword16.replace("/", ".")
                                write_f = open(os.path.join(path, file), 'w')
                                write_f.write(" Rdv past--> " + mwrename16 + "\n" +
                                    lines[i+1] + lines[i+2] + "\n")
                                print("+ Modification finish")
                                break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile16:
        print("File 16 has not been found", infofile16)
    else:
        ("Error unknow")

    # To copy to ./Backup/Files16
    try:
        # To copy to ./Backup/Files16
        src16 = r'./patient_agenda/events16/doc_events/fix_agenda/agenda_saved'
        dst16 = r'./Backup/Files16'
        shutil.copy(os.path.join(src16, file), dst16)
    except (OSError, FileNotFoundError) as err_16shut:
        print("+ No files from agenda_16 copied !!!", err_16shut)
    
    secproc = subprocess.run(["scp", "-r", "./Backup/Files16",
        "pi@192.168.18.12:~/tt_doc/doc_txt16"], stderr=subprocess.PIPE)
    print("Result SCP transfert : %s" % repr(proc.stderr))
    if secproc.stderr == b'':
        print("+ './Backup/Files16' uploaded !")
    else:
        print("+ No file to upload !")
        messagebox.showerror("Error", "./Backup/Files16 not uploaded !")

    # Patient 17
    try:
        with open('./newpatient/entryfile17.txt', 'r') as namefile:
            line17 = namefile.readline()
            new_text17 = line17
    except FileNotFoundError as fileout17:
        print("No file entryfile17.txt exist", fileout17)

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events17/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if dateagenda in line:
                            print("Nous y voici !")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : ' \
                                + new_text17 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM17 = messagebox.askyesno("Ask", "Do you want to stop reminders ?")
                            if MSGREM17 == 1:
                                magicword = (datetime.datetime.now() + datetime.timedelta(\
                                    days=1)).strftime('%d/%m/%Y')
                                for path, dirs, files in os.walk('./patient_agenda/events17/'\
                                    'doc_events/fix_agenda/agenda_saved/'):
                                    for file in files:
                                        with open(os.path.join(path, file), 'r') as read_f:
                                            lines = read_f.readlines()
                                            for line in lines:
                                                line = lines[i]
                                                noway = "Fixed on :"
                                                if line[0:10] == noway:
                                                    print("+ There is noway : ")
                                                    print(line[0:10])
                                                elif magicword in line:
                                                    print("+ It is magicword : ")
                                                    print(line[0:10])
                                                    write_f = open(os.path.join(path, file), 'w')
                                                    write_f.write(" Rdv past--> " + lines[i+1] + \
                                                        lines[i+2] + "\n")
                                                    print("Modification finish")
                                                    break
                                                else:
                                                    print("None file has been writted")
                                                    break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile17:
        print("File 17 has not been found", infofile17)
    else:
        ("Error unknow")

    # Patient 18
    try:
        with open('./newpatient/entryfile18.txt', 'r') as namefile:
            line18 = namefile.readline()
            new_text18 = line18
    except FileNotFoundError as fileout18:
        print("No file entryfile18.txt exist", fileout18)

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events18/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if dateagenda in line:
                            print("Nous y voici !")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : ' \
                                + new_text18 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM18 = messagebox.askyesno("Ask", "Do you want to stop reminders ?")
                            if MSGREM18 == 1:
                                magicword = (datetime.datetime.now() + datetime.timedelta(\
                                    days=1)).strftime('%d/%m/%Y')
                                for path, dirs, files in os.walk('./patient_agenda/events18/'\
                                    'doc_events/fix_agenda/agenda_saved/'):
                                    for file in files:
                                        with open(os.path.join(path, file), 'r') as read_f:
                                            lines = read_f.readlines()
                                            for line in lines:
                                                line = lines[i]
                                                noway = "Fixed on :"
                                                if line[0:10] == noway:
                                                    print("+ There is noway : ")
                                                    print(line[0:10])
                                                elif magicword in line:
                                                    print("+ It is magicword : ")
                                                    print(line[0:10])
                                                    write_f = open(os.path.join(path, file), 'w')
                                                    write_f.write(" Rdv past--> " + lines[i+1] + \
                                                        lines[i+2] + "\n")
                                                    print("Modification finish")
                                                    break
                                                else:
                                                    print("None file has been writted")
                                                    break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile18:
        print("File 18 has not been found", infofile18)
    else:
        ("Error unknow")

    # Patient 19
    try:
        with open('./newpatient/entryfile19.txt', 'r') as namefile:
            line19 = namefile.readline()
            new_text19 = line19
    except FileNotFoundError as fileout19:
        print("No file entryfile19.txt exist", fileout19)

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events19/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if dateagenda in line:
                            print("Nous y voici !")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : ' \
                                + new_text19 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM19 = messagebox.askyesno("Ask", "Do you want to stop reminders ?")
                            if MSGREM19 == 1:
                                magicword = (datetime.datetime.now() + datetime.timedelta(\
                                    days=1)).strftime('%d/%m/%Y')
                                for path, dirs, files in os.walk('./patient_agenda/events19/'\
                                    'doc_events/fix_agenda/agenda_saved/'):
                                    for file in files:
                                        with open(os.path.join(path, file), 'r') as read_f:
                                            lines = read_f.readlines()
                                            for line in lines:
                                                line = lines[i]
                                                noway = "Fixed on :"
                                                if line[0:10] == noway:
                                                    print("+ There is noway : ")
                                                    print(line[0:10])
                                                elif magicword in line:
                                                    print("+ It is magicword : ")
                                                    print(line[0:10])
                                                    write_f = open(os.path.join(path, file), 'w')
                                                    write_f.write(" Rdv past--> " + lines[i+1] + \
                                                        lines[i+2] + "\n")
                                                    print("Modification finish")
                                                    break
                                                else:
                                                    print("None file has been writted")
                                                    break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile19:
        print("File 19 has not been found", infofile19)
    else:
        ("Error unknow")

    # Patient 20
    try:
        with open('./newpatient/entryfile20.txt', 'r') as namefile:
            line20 = namefile.readline()
            new_text20 = line20
    except FileNotFoundError as fileout20:
        print("No file entryfile20.txt exist", fileout20)

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events20/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if dateagenda in line:
                            print("Nous y voici !")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : ' \
                                + new_text20 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM20 = messagebox.askyesno("Ask", "Do you want to stop reminders ?")
                            if MSGREM20 == 1:
                                magicword = (datetime.datetime.now() + datetime.timedelta(\
                                    days=1)).strftime('%d/%m/%Y')
                                for path, dirs, files in os.walk('./patient_agenda/events20/'\
                                    'doc_events/fix_agenda/agenda_saved/'):
                                    for file in files:
                                        with open(os.path.join(path, file), 'r') as read_f:
                                            lines = read_f.readlines()
                                            for line in lines:
                                                line = lines[i]
                                                noway = "Fixed on :"
                                                if line[0:10] == noway:
                                                    print("+ There is noway : ")
                                                    print(line[0:10])
                                                elif magicword in line:
                                                    print("+ It is magicword : ")
                                                    print(line[0:10])
                                                    write_f = open(os.path.join(path, file), 'w')
                                                    write_f.write(" Rdv past--> " + lines[i+1] + \
                                                        lines[i+2] + "\n")
                                                    print("Modification finish")
                                                    break
                                                else:
                                                    print("None file has been writted")
                                                    break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile20:
        print("File 20 has not been found", infofile20)
    else:
        ("Error unknow")

    # Patient 21
    try:
        with open('./newpatient/entryfile21.txt', 'r') as namefile:
            line21 = namefile.readline()
            new_text21 = line21
    except FileNotFoundError as fileout21:
        print("No file entryfile21.txt exist", fileout21)

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events21/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if dateagenda in line:
                            print("Nous y voici !")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : ' \
                                + new_text21 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM21 = messagebox.askyesno("Ask", "Do you want to stop reminders ?")
                            if MSGREM21 == 1:
                                magicword = (datetime.datetime.now() + datetime.timedelta(\
                                    days=1)).strftime('%d/%m/%Y')
                                for path, dirs, files in os.walk('./patient_agenda/events21/'\
                                    'doc_events/fix_agenda/agenda_saved/'):
                                    for file in files:
                                        with open(os.path.join(path, file), 'r') as read_f:
                                            lines = read_f.readlines()
                                            for line in lines:
                                                line = lines[i]
                                                noway = "Fixed on :"
                                                if line[0:10] == noway:
                                                    print("+ There is noway : ")
                                                    print(line[0:10])
                                                elif magicword in line:
                                                    print("+ It is magicword : ")
                                                    print(line[0:10])
                                                    write_f = open(os.path.join(path, file), 'w')
                                                    write_f.write(" Rdv past--> " + lines[i+1] + \
                                                        lines[i+2] + "\n")
                                                    print("Modification finish")
                                                    break
                                                else:
                                                    print("None file has been writted")
                                                    break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile21:
        print("File 21 has not been found", infofile21)
    else:
        ("Error unknow")

    # Patient 22
    try:
        with open('./newpatient/entryfile22.txt', 'r') as namefile:
            line22 = namefile.readline()
            new_text22 = line22
    except FileNotFoundError as fileout22:
        print("No file entryfile22.txt exist", fileout22)

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events22/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if dateagenda in line:
                            print("Nous y voici !")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : ' \
                                + new_text22 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM22 = messagebox.askyesno("Ask", "Do you want to stop reminders ?")
                            if MSGREM22 == 1:
                                magicword = (datetime.datetime.now() + datetime.timedelta(\
                                    days=1)).strftime('%d/%m/%Y')
                                for path, dirs, files in os.walk('./patient_agenda/events22/'\
                                    'doc_events/fix_agenda/agenda_saved/'):
                                    for file in files:
                                        with open(os.path.join(path, file), 'r') as read_f:
                                            lines = read_f.readlines()
                                            for line in lines:
                                                line = lines[i]
                                                noway = "Fixed on :"
                                                if line[0:10] == noway:
                                                    print("+ There is noway : ")
                                                    print(line[0:10])
                                                elif magicword in line:
                                                    print("+ It is magicword : ")
                                                    print(line[0:10])
                                                    write_f = open(os.path.join(path, file), 'w')
                                                    write_f.write(" Rdv past--> " + lines[i+1] + \
                                                        lines[i+2] + "\n")
                                                    print("Modification finish")
                                                    break
                                                else:
                                                    print("None file has been writted")
                                                    break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile22:
        print("File 22 has not been found", infofile22)
    else:
        ("Error unknow")

    # Patient 23
    try:
        with open('./newpatient/entryfile23.txt', 'r') as namefile:
            line23 = namefile.readline()
            new_text23 = line23
    except FileNotFoundError as fileout23:
        print("No file entryfile23.txt exist", fileout23)

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events23/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if dateagenda in line:
                            print("Nous y voici !")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : ' \
                                + new_text23 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM23 = messagebox.askyesno("Ask", "Do you want to stop reminders ?")
                            if MSGREM23 == 1:
                                magicword = (datetime.datetime.now() + datetime.timedelta(\
                                    days=1)).strftime('%d/%m/%Y')
                                for path, dirs, files in os.walk('./patient_agenda/events23/'\
                                    'doc_events/fix_agenda/agenda_saved/'):
                                    for file in files:
                                        with open(os.path.join(path, file), 'r') as read_f:
                                            lines = read_f.readlines()
                                            for line in lines:
                                                line = lines[i]
                                                noway = "Fixed on :"
                                                if line[0:10] == noway:
                                                    print("+ There is noway : ")
                                                    print(line[0:10])
                                                elif magicword in line:
                                                    print("+ It is magicword : ")
                                                    print(line[0:10])
                                                    write_f = open(os.path.join(path, file), 'w')
                                                    write_f.write(" Rdv past--> " + lines[i+1] + \
                                                        lines[i+2] + "\n")
                                                    print("Modification finish")
                                                    break
                                                else:
                                                    print("None file has been writted")
                                                    break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile23:
        print("File 23 has not been found", infofile23)
    else:
        ("Error unknow")

    # Patient 24
    try:
        with open('./newpatient/entryfile24.txt', 'r') as namefile:
            line24 = namefile.readline()
            new_text24 = line24
    except FileNotFoundError as fileout24:
        print("No file entryfile24.txt exist", fileout24)

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(\
            days=1)).strftime('%d/%m/%Y')
        for path, dirs, files in os.walk('./patient_agenda/events24/'
            'doc_events/fix_agenda/agenda_saved/'):
            for file in files:
                with open(os.path.join(path, file), 'r') as read_f:
                    lines = read_f.readlines()
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if dateagenda in line:
                            print("Nous y voici !")
                            print(lines[i])
                            print(lines[i+1])
                            print(lines[i+2])
                            messagebox.showwarning('Info', 'Look at AGENDA, '
                                'there is an appointment tomorrow for : ' \
                                + new_text24 + lines[i] + lines[i+1] + \
                                lines[i+2])

                            MSGREM24 = messagebox.askyesno("Ask", "Do you want to stop reminders ?")
                            if MSGREM24 == 1:
                                magicword = (datetime.datetime.now() + datetime.timedelta(\
                                    days=1)).strftime('%d/%m/%Y')
                                for path, dirs, files in os.walk('./patient_agenda/events24/'\
                                    'doc_events/fix_agenda/agenda_saved/'):
                                    for file in files:
                                        with open(os.path.join(path, file), 'r') as read_f:
                                            lines = read_f.readlines()
                                            for line in lines:
                                                line = lines[i]
                                                noway = "Fixed on :"
                                                if line[0:10] == noway:
                                                    print("+ There is noway : ")
                                                    print(line[0:10])
                                                elif magicword in line:
                                                    print("+ It is magicword : ")
                                                    print(line[0:10])
                                                    write_f = open(os.path.join(path, file), 'w')
                                                    write_f.write(" Rdv past--> " + lines[i+1] + \
                                                        lines[i+2] + "\n")
                                                    print("Modification finish")
                                                    break
                                                else:
                                                    print("None file has been writted")
                                                    break
                            else:
                                pass
    except (FileNotFoundError, IndexError) as infofile24:
        print("File 24 has not been found", infofile24)
    else:
        ("Error unknow")
