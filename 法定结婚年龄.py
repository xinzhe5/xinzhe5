# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 20:31:00 2022

@author: 21203
"""

a,b = input("请输入性别（男或女）和年龄（整数）：").split("，")
if  a in ['男']:
    if eval(b)>=22:
        print("该人达到合法结婚年龄")
    else:
        print("该人未达到合法结婚年龄")
elif  a in ['女']:
    if eval(b)>=20:
        print("该人达到合法结婚年龄")
    else:
        print("该人未达到合法结婚年龄")