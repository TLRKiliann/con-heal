#!/usr/bin/python3
# -*- coding: utf-8 -*-


import json
import matplotlib.pyplot as plt
import os


print("\nListe1 = dates :")
print("--------------")
fileO = open('./param/aspifile7/data_datedlr.json')
list1 = json.load(fileO)

for letter in list1:
    print("list1: " + letter)

print("\nList2 = douleurs :")
print("--------------------")

fileO = open('./param/aspifile7/data_dlr.json')
list2 = json.load(fileO)

for letter in list2:
    print("List2: " + letter)

dicolist = {}

for list1, list2 in zip(list1, list2):
    dicolist[list1] = list2

print("\nDictionnary display :")
print("---------------------------")
print(dicolist)

list1 = []
list2 = []

for key, value in dicolist.items():
    list1.append(key)
    list2.append(value)
    
print("\nList of date by entry's order :")
print("----------------------------------")
print(list1)

print("\nList of pain evaluation :")
print("------------------------")
print(list2)

try:
    list1 = list(map(str, list1))
except ValueError as fmt_err:
    print("+ Invalid number (no: . or , !)", fmt_err)

try:
    list2 = list(map(int, list2))
except ValueError as base_err:
    print("+ Invalid number (no: . or , !)", base_err)
    list2 = []

x_axis = list1
y_axis = list2

try:
    show_grid = True
    with plt.style.context('seaborn-darkgrid'):
        figure, axes = plt.subplots()
        plt.plot(x_axis, y_axis, 'o', color='purple')
        plt.plot(x_axis, y_axis, '--', color='purple')
        for x,y in zip(x_axis, y_axis):
            label = "{}".format(y)
            plt.annotate(label, (x,y), textcoords="offset points",
                xytext=(0,10), ha='center')
        plt.ylabel('Dlrs', fontsize=14)
        plt.xlabel('Dates', fontsize=14)
        plt.title('Pain scale (dlr/10) by date', fontsize=16)
        plt.xticks(rotation=45)
        plt.legend(['Douleurs (Pain)'])
        plt.grid(show_grid)
        plt.show()
except ValueError as shapes_err:
    print("Invalid number", shapes_err)

os.remove('./param/aspifile7/data_datedlr.json')
print("+ File data_datedlr.json removed !")
os.remove('./param/aspifile7/data_dlr.json')
print("+ File data_dlr.json removed !\n")
