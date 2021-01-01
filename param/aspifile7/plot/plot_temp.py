#!/usr/bin/python3
# -*- coding: utf-8 -*-


import os
import json
import datetime
import matplotlib.pyplot as plt
#from matplotlib import dates
#from matplotlib.dates import date2num
#from matplotlib.dates import AutoDateLocator


print("\nListe1 = dates :")
print("--------------")

try:
    fileO = open('./param/aspifile7/data_datetemp.json')
    list1 = json.load(fileO)
except ValueError as err_entry:
    print("+ Value Error", err_entry)

try:
    for obj in list1:
        print("list1: " + obj)
except NameError as err_list:
    print("+ Name Error list", err_list)

print("\nList2 = temperatures :")
print("--------------------")

try:
    file1 = open('./param/aspifile7/data_temp.json')
    list2 = json.load(file1)
except ValueError as err_entry2:
    print("+ Value Error", err_entry2)

try:
    for obj in list2:
        print("List2: " + obj)
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

print("\nListe des dates dans l'ordre des entrées :")
print("----------------------------------")
print(list1)
print("\nList of temperatures :")
print("------------------------")
print(list2)

try:
    list1 = list(map(str, list1))
    print(list1)
except ValueError as err_vlist1:
    print("+ False value (no: string or int value)", err_vlist1)

#list3 = [int(list2) for list2 in list2]
try:
    list2 = list(map(float, list2))
except ValueError as err_val:
    print("+ False value (no: string or int value)", err_val)

#converted_dates = list(map(datetime.datetime.strptime,
#    list1, len(list1)*['%d/%m/%Y']))
x_axis = list1
#formatter = dates.DateFormatter('%d/%m/%Y')
y_axis = list2

try:
    show_grid = True
    with plt.style.context('seaborn-darkgrid'):
        figure, axes = plt.subplots()
        plt.plot(x_axis, y_axis, 's--', color='purple')
        for x,y in zip(x_axis, y_axis):
            label = "{:.1f}".format(y)
            plt.annotate(label, (x,y), textcoords="offset points",
                xytext=(0,10), ha='center')
        plt.ylabel('T°C', fontsize=14)
        plt.xlabel('Dates', fontsize=14)
        plt.title('Temperature by Date', fontsize=16)
        plt.xticks(rotation=45)
        plt.legend(['Temperatures C°'])
        #plt.gcf().autofmt_xdate(rotation=45)
        plt.grid(show_grid)
        plt.show()
except ValueError as shapes_err:
    print("Invalid number", shapes_err)

os.remove('./param/aspifile7/data_datetemp.json')
print("+ File data_datetemp.json removed !")
os.remove('./param/aspifile7/data_temp.json')
print("+ File data_temp.json removed !\n")
