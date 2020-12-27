#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
from tkinter import messagebox
import os
import subprocess
import json
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import dates
from matplotlib.dates import date2num
from matplotlib.dates import AutoDateLocator
from matplotlib.dates import AutoDateFormatter
import datetime
import time


print("\nListe1 = dates :")
print("--------------")

try:
    fileO = open('./param/aspifile7/data_datetemp.json')
    list1 = json.load(fileO)
except ValueError as err_entry:
    print("+ Value Error", err_entry)

try:
    for letter in list1:
        print("list1: " + letter)
except NameError as err_list:
    print("+ Name Error list", err_list)

print("\nList2 = temperatures :")
print("--------------------")

try:
    fileO = open('./param/aspifile7/data_temp.json')
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

# Nouvelle partie qui merde totalement dates dans le désordre !!!
# Avec 0 devant (agenda ex. help) + conversion de list1 en float !

data_day = list1[0]
data_month = list1[1]
data_year = list1[2]

try:
    if data_day < 10:
        extraday = '0' +''+ str(data_day)
    elif data_day >= 10:
        extraday = str(data_day)
    else:
        pass
except ValueError as valout:
    print("Value of day is a problem", valout)

try:
    if data_month < 10:
        extramounth = '0' +''+ str(data_month)
    elif data_month >= 10:
        extramounth = str(data_month)
    else:
        pass
except ValueError as valout:
    print("Value of mounth is a problem", valout)

# initword = "Appointment set for :"
# initword +' '+ 
final_data = extraday +'/'+ extramounth +'/'+ str(data_year) +' : '
print(final_data)

#final_data = list(map(str, final_data))
print(final_data)

#list2 = list(map(float, list2))
#print(list2)

converted_dates = list(map(datetime.datetime.strptime, final_data, len(final_data)*['%d/%m/%Y']))
x_axis = converted_dates
formatter = dates.DateFormatter('%d/%m/%Y')
y_axis = list2

try:
    show_grid = True
    with plt.style.context('seaborn-darkgrid'):
        figure, axes = plt.subplots()
        # apply autoformatter for displaying of dates 
        locator = AutoDateLocator()
        axes.xaxis.set_major_locator(locator)
        ax = plt.gcf().axes[0]
        ax.xaxis.set_major_formatter(formatter)
        #axes.xaxis.set_major_formatter(AutoDateFormatter(locator))
        min_date = date2num(datetime.datetime.strptime('01/01/2020', "%d/%m/%Y"))
        max_date = date2num(datetime.datetime.strptime('31/12/2020', "%d/%m/%Y"))
        axes.set_xlim([min_date, max_date])
        #figure.autofmt_xdate()

        plt.plot(x_axis, y_axis, 'o-', color='purple')
        plt.ylabel('T°C', fontsize=14)
        plt.xlabel('Dates', fontsize=14)
        plt.title('Temperature by Date', fontsize=16)
        #plt.xticks(rotation=45)
        plt.legend(['Temperatures C°'])
        plt.grid(show_grid)
        plt.gcf().autofmt_xdate(rotation=45)
        plt.show()
except ValueError as shapes_err:
    print("Invalid number", shapes_err)

os.remove('./param/aspifile7/data_datetemp.json')
print("+ File data_datetemp.json removed !")
os.remove('./param/aspifile7/data_temp.json')
print("+ File data_temp.json removed !\n")

"""
try:
    show_grid = True
    with plt.style.context('seaborn-darkgrid'):
        plt.plot(list1, list2, 'o-', color='purple')
        plt.ylabel('T°C', fontsize=14)
        plt.xlabel('Dates', fontsize=14)
        plt.title('Relevé des températures par date', fontsize=16)

        plt.legend(['Temperatures C°'])
        plt.grid(show_grid)
        plt.show()
except ValueError as shapes_err:
    print("Invalid number", shapes_err)

os.remove('./param/aspifile7/data_datetemp.json')
print("+ File data_datetemp.json removed !")
os.remove('./param/aspifile7/data_temp.json')
print("+ File data_temp.json removed !\n")
"""
