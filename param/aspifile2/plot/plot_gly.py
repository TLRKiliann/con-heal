#!/usr/bin/python3
# -*- coding: utf-8 -*-


import json
import matplotlib.pyplot as plt
import os


print("\nListe1 = dates :")
print("--------------")
fileO = open('./param/aspifile2/data_dategly.json')
list1 = json.load(fileO)

for letter in list1:
    print("list1: " + letter)

print("\nList2 = tension :")
print("--------------------")

fileO = open('./param/aspifile2/data_gly.json')
list2 = json.load(fileO)

for letter in list2:
    print("List2: " + letter)

dicolist = {}

for list1, list2 in zip(list1, list2):
    dicolist[list1] = list2

print("\nAffichage du dictionnaire :")
print("---------------------------")
print(dicolist)

list1 = []
list2 = []

for key, value in dicolist.items():
    list1.append(key)
    list2.append(value)
    
print("\nListe des dates dans l'ordre des entrées :")
print("----------------------------------")
print(list1)
print("\nListe des glycemia :")
print("------------------------")
print(list2)

#list3 = [int(list2) for list2 in list2]
try:
    list2 = list(map(float, list2))
except ValueError as err_val:
    print("+ False value (no: string or int value)", err_val)

try:
    show_grid = True
    with plt.style.context('seaborn-darkgrid'):
        plt.plot(list1, list2, 'o-', color='cyan')
        plt.ylabel('Hgt', fontsize=14)
        plt.xlabel('Dates', fontsize=14)
        plt.title('Hgt(mmol/l) by Date', fontsize=16)
        plt.xticks(rotation=45)
        plt.grid(show_grid)
        plt.show()
except ValueError as shapes_err:
    print("Invalid number", shapes_err)

os.remove('./param/aspifile2/data_dategly.json')
print("+ File data_dategly.json removed !")
os.remove('./param/aspifile2/data_gly.json')
print("+ File data_gly.json removed !\n")
