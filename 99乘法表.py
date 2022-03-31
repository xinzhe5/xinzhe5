# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 14:24:50 2022

@author: 21203
"""

for i in range(1,10):
    for j in range(1,i+1):
        print("{} * {} = {}".format(i,j,i*j),end=("  "))
    print(end=("\n"))