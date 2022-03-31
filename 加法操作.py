# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 19:06:37 2022

@author: 21203
"""

a,n = input("请输入两个正整数以逗号分隔:").split(",")
b=a
for i in range(2,eval(n)+1):
    b=b+'+'+a*i
print(eval(b))