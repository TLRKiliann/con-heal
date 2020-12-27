#!/usr/bin/python3
# -*- coding: utf-8 -*-


import json
import matplotlib.pyplot as plt
import os


print("\nListe1 = dates :")
print("--------------")

try:
    fileO = open('./param/aspifile7/data_date.json')
    list1 = json.load(fileO)
except ValueError as err_entry:
    print("+ Value Error", err_entry)

try:
    for letter in list1:
        print("list1: " + letter)
except NameError as err_list:
    print("+ Name Error list", err_list)

print("\nList2 = tension :")
print("--------------------")

try:
    fileO = open('./param/aspifile7/data_tension.json')
    list2 = json.load(fileO)
except ValueError as err_entry2:
    print("+ Value Error", err_entry2)

try:
    for letter in list2:
        print("List2: " + letter)
except NameError as err_list2:
    print("+ Name Error list2", err_list2)

dicolist = {}

try:
    for list1, list2 in zip(list1, list2):
        dicolist[list1] = list2
except NameError as not_def:
    print("+ Name Error list", not_def)

print("\nAffichage du dictionnaire :")
print("---------------------------")
print(dicolist)

list1 = []
list2 = []

for key, value in dicolist.items():
    list1.append(key)
    list2.append(value)
    list2 = [item.replace("/", ".") for item in list2]
    
print("\nListe des dates dans l'ordre des entrées :")
print("----------------------------------")
print(list1)
print("\nListe des tensions :")
print("------------------------")
print(list2)

try:
    list2 = list(map(float, list2))
except ValueError as err_val:
    print("+ False value (no: string or int value)", err_val)

try:
    show_grid = True
    with plt.style.context('seaborn-darkgrid'):
        plt.plot(list1, list2, 'o-', color='red')
        plt.ylabel('TA', fontsize=14)
        plt.xlabel('Dates', fontsize=14)
        plt.title('Relevé des tensions (TA) par date', fontsize=16)
        plt.xticks(rotation=45)
        plt.legend(['TA (blood pressure)'])
        plt.grid(show_grid)
        plt.show()
except ValueError as val:
    print("+ False entry value", val)

os.remove('./param/aspifile7/data_date.json')
print("+ File data_date.json removed !")
os.remove('./param/aspifile7/data_tension.json')
print("+ File data_tension.json removed !\n")
