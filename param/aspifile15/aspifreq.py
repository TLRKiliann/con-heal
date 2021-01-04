#!/usr/bin/python3
# -*- coding: utf-8 -*-


import subprocess
import json


file = open('./param/aspifile15/freq.json')
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
        print("FR: " + str(value[0]["FR"]))
        print("\n")
except IndexError as err_read:
    print("+ Error from aspidata.py", err_read)

print("\nList of dates\n")

data_list1 = []
for value in zip(value):
    data_list1.append(value[0]['Date'])
    print(value[0]['Date'])

print("\nThat seems ok!\n")

with open('./param/aspifile15/data_datefr.json', 'a+') as datafile:
    json.dump(data_list1, datafile, indent=4)

for (key, value) in data.items():
    print(key, value)
    print("\n")

print("\nList of freq\n")

data_list2 = []
for value in zip(value):
    data_list2.append(value[0]['FR'])
    print(value[0]['FR'])

print("\nThat seems correct!\n")

with open('./param/aspifile15/data_fr.json', 'a+') as datafile:
    json.dump(data_list2, datafile, indent=4)

print("\nDownloading 'plot_prog.py'...")

subprocess.run('./param/aspifile15/plot/plot_freq.py', check=True)
