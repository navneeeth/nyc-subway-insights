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

time1 = time.time()
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
                entries.append(int(values[-2]))
                exits.append(int(values[-1]))
            #print(values)
        ccfile.close()
        #loaded_text = np.loadtxt(f, skiprows=1)
        #print(loaded_text)

print(len(entries))
count = 1
print(type(entries[0]))
for j in exits:
    if(type(j) == str):
        print(j)
        print(count)
    count = count + 1
print(sum(entries))
print(sum(exits))
print(sum(entries)-sum(exits))

time2 = time.time()
print(time2-time1)