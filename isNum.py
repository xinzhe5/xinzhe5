# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 16:46:50 2022

@author: 21203
"""

def isNum(str):
    try:
        Type=type(eval(str))
        if Type==int or Type==float or Type==complex:
            return 'Ture'
        else:
            return 'False'
    except :
            return 'False'
Str=input('请输入一个整数、浮点数或复数：')
print(isNum(Str))