#!/usr/bin/python3
# -*- coding: utf-8 -*-


import os
import json
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


print("\nListe1 = dates :")
print("--------------")
fileO = open('./param/aspifile21/data_datefr.json')
list1 = json.load(fileO)

for letter in list1:
    print("list1: " + letter)

print("\nList2 = FR :")
print("--------------------")

fileO = open('./param/aspifile21/data_fr.json')
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
print("\nListe des frequences respiratoires :")
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

xdates = [datetime.datetime.strptime('{:10}'.format(str(li)),'%d/%m/%Y : %H:%M:%S') for li in list1]
print(xdates)

x_axis = xdates
y_axis = list2

try:
    show_grid = True
    with plt.style.context('seaborn-darkgrid'):
        #figure, axes = plt.subplots()
        fig = plt.figure()
        fig.set_facecolor("lightsteelblue")
        lab = fig.suptitle('FR/min by Day',
            fontsize=18)
        lab.set_color('navy')
        ax = plt.subplot()
        ax.tick_params(axis='x', colors='navy')
        ax.tick_params(axis='y', colors='navy')
        labelc = plt.ylabel("y-label")
        labelc.set_color('navy')
        labelc2 = plt.xlabel("x-label")
        labelc2.set_color('navy')

        plt.plot(x_axis, y_axis, 's', color='blue')
        plt.plot(x_axis, y_axis, '--', color='cyan')
        for x,y in zip(x_axis, y_axis):
            label = "{}".format(y)
            plt.annotate(label, (x,y), textcoords="offset points",
                xytext=(0,10), ha='center')

        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y : %H:%M:%S'))
        plt.ylabel('FR/min', fontsize=14)
        plt.xlabel('Dates', fontsize=14)
        #plt.title('Relevé des fréquences resp (FR/min) par date', fontsize=16)
        #plt.xticks(rotation=25)
        plt.legend(['Respiratory Frequency'])
        plt.gcf().autofmt_xdate(rotation=25)
        plt.grid(show_grid)
        plt.show()
except ValueError as shapes_err:
    print("Invalid number", shapes_err)

try:
    os.remove('./param/aspifile21/data_datefr.json')
    print("+ File data_datefr.json removed !")
    os.remove('./param/aspifile21/data_fr.json')
    print("+ File data_fr.json removed !\n")
except OSError as os_err:
    print("+ OS error ! ...", os_err)
