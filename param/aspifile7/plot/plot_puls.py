#!/usr/bin/python3
# -*- coding:utf-8 -*-


import json
import matplotlib.pyplot as plt
import os


print("\nListe1 = dates :")
print("--------------")
fileO = open('./param/aspifile7/data_datepuls.json')
list1 = json.load(fileO)

for letter in list1:
    print("list1: " + letter)

print("\nList2 = Puls :")
print("--------------------")

fileO = open('./param/aspifile7/data_puls.json')
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
print("\nListe des pulsations :")
print("------------------------")
print(list2)

#list3 = [int(list2) for list2 in list2]
try:
    list2 = list(map(int, list2))
except ValueError as base_err:
    print("+ Invalid number (no: . or , !)", base_err)
    list2 = []

try:
    show_grid = True
    with plt.style.context('seaborn-darkgrid'):
        plt.plot(list1, list2, 'o--', color='red')
        plt.ylabel('Puls/min', fontsize=12)
        plt.xlabel('Dates', fontsize=12)
        plt.title('Relevé des puls/min par date', fontsize=14)
        plt.xticks(rotation=45)
        plt.legend(['Pulsations/min'])
        plt.grid(show_grid)
        plt.show()
except ValueError as shapes_err:
    print("Invalid number", shapes_err)

os.remove('./param/aspifile7/data_datepuls.json')
print("+ File data_datepuls.json removed !")
os.remove('./param/aspifile7/data_puls.json')
print("+ File data_puls.json removed !\n")
