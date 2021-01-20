#!/usr/bin/python3
# -*- coding : utf-8 -*-


from tkinter import *
import tkinter as tk
from tkinter import ttk
import time
import threading


def task(root):
    root.title("Upload")
    s = ttk.Style()
    s.theme_use('alt')
    s.configure('blue.Horizontal.TProgressbar',
        troughcolor = '#4d4d4d',
        troughrelief = 'flat',
        background = '#2f92ff')

    pb = ttk.Progressbar(root,
        style = 'blue.Horizontal.TProgressbar',
        orient = 'horizontal',
        length = 200,
        mode = 'determinate')
    pb.pack()
    pb.start(20)
    root.mainloop()

def process_of_unknown_duration(root):
    time.sleep(2)
    print('Done')
    root.quit()

def uploadmain():
    root = tk.Tk()
    t1=threading.Thread(target=process_of_unknown_duration, args=(root,))
    t1.start()
    task(root)  # This will block while the mainloop runs
    t1.join()
    root.destroy()
