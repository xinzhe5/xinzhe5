# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 19:57:26 2022

@author: 21203
"""
from functools import reduce
a=list(filter(lambda n:n%2==0,range(1,101)))
Sum=reduce(lambda x,y:x+y,a)
print("1~100内偶数和为：{}".format(Sum))
