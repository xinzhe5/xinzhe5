# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 19:16:57 2022

@author: 21203
"""

def PerferNumber(n):
    temp = 0
    for i in range(1,n):
        if n%i == 0:
            temp += i
        else:
            continue
    if temp == n:
        return True
    else:
        return False
  
print("1000以内所有完数：")
for j in range(6,1001):
    if PerferNumber(j):
        print(j,end=' ')

            