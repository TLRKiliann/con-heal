#!/usr/bin/python3
# -*- coding: utf-8 -*-


import subprocess
import json


file = open('./param/aspifile2/tensor.json')
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
        print("Tension: " + str(value[0]["Tension"]))
        print("\n")
except IndexError as err_read:
    print("+ Error from aspidata.py", err_read)

print("\nList of dates\n")

data_list1 = []
for value in zip(value):
    data_list1.append(value[0]['Date'])
    
with open('./param/aspifile2/data_date.json', 'a+') as datafile:
    json.dump(data_list1, datafile, indent=4)

for (key, value) in data.items():
    print(key, value)
    print("\n")

print("\nList of tensions\n")

data_list2 = []
for value in zip(value):
    data_list2.append(value[0]['Tension'])

print("\nThat seems correct!\n")

with open('./param/aspifile2/data_tension.json', 'a+') as datafile:
    json.dump(data_list2, datafile, indent=4)

print("\nDownloading 'plot_prog.py'...")

subprocess.run('./param/aspifile2/plot/plot_prog.py', check=True)
