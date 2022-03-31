# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 19:33:48 2022

@author: 21203
"""

from functools import reduce
def fac(n):
    return reduce(lambda x,y:x*y,range(1,n+1))
n=int(input("请输入大于1的整数:"))
print('{}!为{}'.format(n,fac(n)))