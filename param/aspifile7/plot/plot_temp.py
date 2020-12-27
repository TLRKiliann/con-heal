#!/usr/bin/python3
# -*- coding: utf-8 -*-


import json
import matplotlib.pyplot as plt
import os


print("\nListe1 = dates :")
print("--------------")
fileO = open('./param/aspifile7/data_datetemp.json')
list1 = json.load(fileO)

for letter in list1:
    print("list1: " + letter)

print("\nList2 = temperatures :")
print("--------------------")

fileO = open('./param/aspifile7/data_temp.json')
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
print("\nList of temperatures :")
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
        plt.plot(list1, list2, 'o-', color='purple')
        plt.ylabel('T°C', fontsize=12)
        plt.xlabel('Dates', fontsize=12)
        plt.title('Relevé des températures par date', fontsize=14)
        plt.xticks(rotation=45)
        plt.legend(['Temperatures C°'])
        plt.grid(show_grid)
        plt.show()
except ValueError as shapes_err:
    print("Invalid number", shapes_err)

os.remove('./param/aspifile7/data_datetemp.json')
print("+ File data_datetemp.json removed !")
os.remove('./param/aspifile7/data_temp.json')
print("+ File data_temp.json removed !\n")
