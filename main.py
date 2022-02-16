#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 18:22:26 2022

@author: navneethkrishna
"""

import os
import numpy as np
import time
dirname = './dataset/'
c_a = []
unit = []
scp = []
station = []
linename = []
division = []
date_data = []
time_data = []
desc = []
entries = []
exits = []
stations_list = []
lines_list = []
lines_cache = ''
stations_cache = ''
time1 = time.time()

def checkStationsList(val):
    if(val not in stations_list):
        stations_list.append(val)

def checkLines(val):
    values = [char for char in val]
    for i in values:
        if i not in lines_list:
            lines_list.append(i)
            lines_cache = val
def readTxtFile(filepath):
    ccfile = open(filepath, "r")
    flag = 1
    flag2 = 1
    for aline in ccfile:
        values = aline.split(',')
    ccfile.close()
for filename in os.listdir(dirname):
    f = os.path.join(dirname, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(filename)
        ccfile = open(f, "r")
        flag = 1
        flag2 = 1
        for aline in ccfile:
            values = aline.split(',')
            if(flag):
                #print(values)
                flag = 0
            else:
                #if(flag2):
                    #print(values[-2])
                    #print(values[-1])
                flag2 = 0
                checkStationsList(values[3])
                
                if(not lines_cache == values[4]):
                    checkLines(values[4])
                
                entries.append(int(values[-2]))
                exits.append(int(values[-1]))
                
            #print(values)
        ccfile.close()
        #loaded_text = np.loadtxt(f, skiprows=1)
        #print(loaded_text)

#print(len(entries))
#count = 1
#print(type(entries[0]))

#print(sum(entries))
#print(sum(exits))
print(sum(entries)-sum(exits))
print(len(stations_list))
print(len(lines_list))
time2 = time.time()
print(time2-time1)