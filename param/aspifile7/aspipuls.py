#!/usr/bin/python3
# -*- coding: utf-8 -*-


import subprocess
import json


file = open('./param/aspifile7/puls.json')
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
        print("Puls: " + str(value[0]["Puls"]))
        print("\n")
except IndexError as err_read:
    print("+ Error from aspidata.py", err_read)

print("\nList of dates\n")

data_list1 = []
for value in zip(value):
    data_list1.append(value[0]['Date'])
    print(value[0]['Date'])

print("\nThat seems ok!\n")

with open('./param/aspifile7/data_datepuls.json', 'a+') as datafile:
    json.dump(data_list1, datafile, indent=4)

for (key, value) in data.items():
    print(key, value)
    print("\n")

print("\nList of puls\n")

data_list2 = []
for value in zip(value):
    data_list2.append(value[0]['Puls'])
    print(value[0]['Puls'])

print("\nThat seems correct!\n")

with open('./param/aspifile7/data_puls.json', 'a+') as datafile:
    json.dump(data_list2, datafile, indent=4)

try:
    subprocess.run(["scp", "./param/paramdata7.txt",
        "pi@192.168.18.12:~/doc_txt7/paramdata7.txt"])
    subprocess.run(["scp", "./param/aspifile7/puls.json",
        "pi@192.168.18.12:~/doc_txt7/puls.json"])
except (OSError, FileNotFoundError) as e_failed:
    print("+ SCP transfert (upload) failed", e_failed)

print("\nLoading 'plot_prog.py'...")
subprocess.run('./param/aspifile7/plot/plot_puls.py', check=True)
