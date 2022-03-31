# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 17:24:43 2022

@author: 21203
"""
import math
def fact(n):
    if n<=1:
        return 1
    else:
        return n*fact(n-1)
def Cos(angle):
    rad=angle*(math.pi)/180
    num=10;i=2;sym=1;Sum=1
    while num > 1e-10:
        sym = -sym
        num = rad**(i)/fact(i)
        Sum += num*sym
        i = i+2
    return Sum
        
Angle=eval(input("请输入一个角度值："))
print("cos{}°的值为 {:.6f}".format(Angle, Cos(Angle)))