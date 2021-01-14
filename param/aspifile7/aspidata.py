#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
    This file is made to make 4 more. I could have made only 3,
    but I preferred to do it this way. Thus, systol and diastol
    each have values associated with the dates.
    Easier to reformat lists for plot_prog.py afterwards.
"""


import subprocess
import json
import pexpect


file = open('./param/aspifile7/systol.json')
data = json.load(file)

try:
    for (key, value) in data.items():
        print("Key: " + key)
        print("Valeur: " + str(value))
        print("\nTo represent the data_get:\n")
        print(data.get("data"))
        print("\n")
        print("Valeur: " + str(value[0]))
        print("\n")
        print("Date: " + str(value[0]["Date"]))
        print("Systol: " + str(value[0]["Systol"]))
        print("\n")
except IndexError as err_read:
    print("+ Error from aspidata.py", err_read)

print("\nList of dates :\n")

data_list1 = []
for value in zip(value):
    data_list1.append(value[0]['Date'])

print("--- Data_list1 de aspidata.py :---\n", data_list1)
print("\n")

with open('./param/aspifile7/data_date.json', 'a+') as datafile:
    json.dump(data_list1, datafile, indent=4)

for (key, value) in data.items():
    print(key, value)
    print("\n")

print("\nList of systol :\n")

data_list2 = []
for value in zip(value):
    data_list2.append((value[0])['Systol'])

print(data_list2)
print("\n")
print("\nThat seems correct!\n")

with open('./param/aspifile7/data_Systol.json', 'a+') as datafile:
    json.dump(data_list2, datafile, indent=4)

#second file ttt
filedias = open('./param/aspifile7/diastol.json')
data = json.load(filedias)

try:
    for (key, value) in data.items():
        print("Key: " + key)
        print("Valeur: " + str(value))
        print("\nTo represent the data_get:\n")
        print(data.get("data"))
        print("\n")
        print("Valeur: " + str(value[0]))
        print("\n")
        print("Date: " + str(value[0]["Date"]))
        print("Diastol: " + str(value[0]["Diastol"]))
        print("\n")
except IndexError as err_readia:
    print("+ Error from aspidata.py", err_readia)

print("\nList of dates\n")

data_listdia = []
for value in zip(value):
    data_listdia.append(value[0]['Date'])

with open('./param/aspifile7/data_dia.json', 'a+') as datafiled:
    json.dump(data_listdia, datafiled, indent=4)

for (key, value) in data.items():
    print(key, value)
    print("\n")

print("\nList of diastol :\n")

data_list2 = []
for value in zip(value):
    data_list2.append((value[0])['Diastol'])

print(data_list2)
print("\n")
print("\nThat seems correct!\n")

with open('./param/aspifile7/data_Diastol.json', 'a+') as datafile2d:
    json.dump(data_list2, datafile2d, indent=4)

"""
This track ask you password...
subprocess.run(["scp", "./param/aspifile7/diastol.json",
    "esteban@192.168.18.8:~/doc_txt/diastol.json"])
subprocess.run(["scp", "./param/aspifile7/systol.json",
    "esteban@192.168.18.8:~/doc_txt/systol.json"])
"""

try:
    var_password  = "----"
    var_commandsys = ("scp ./param/aspifile7/systol.json esteban@192.168.18.8:~/doc_txt/systol.json")
    #make sure in the above command that username and hostname are according to your server
    sys_child = pexpect.spawn(var_commandsys)
    i = sys_child.expect(["password:", pexpect.EOF])

    if i == 0: # send password                
            sys_child.sendline(var_password)
            sys_child.expect(pexpect.EOF)
            print("No problem ! Upload done !!!")
    elif i == 1: 
            print("Got the key or connection timeout")
            pass

except Exception as e:
    print("Oops ! Something went wrong buddy...")
    print(e)

try:
    tovar_password  = "----"
    var_commandia = ("scp ./param/aspifile7/diastol.json esteban@192.168.18.8:~/doc_txt/diastol.json")
    #make sure in the above command that username and hostname are according to your server
    var_child = pexpect.spawn(var_commandia)
    fu = var_child.expect(["password:", pexpect.EOF])

    if fu == 0: # send password
            var_child.sendline(tovar_password)
            var_child.expect(pexpect.EOF)
            print("No problem ! Upload done !!!")
    elif fu == 1: 
            print("Got the key or connection timeout")
            pass

except Exception as ex:
    print("Oops ! Something went wrong buddy...")
    print(ex)

print("\nLoading 'plot_prog.py'...")
subprocess.run('./param/aspifile7/plot/plot_prog.py', check=True)
