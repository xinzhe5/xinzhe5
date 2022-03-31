# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 20:05:56 2022

@author: 21203
"""

a=list(filter(lambda n:n*n%(10**(len(str(n))))==n,range(5,100001)))
print("1~100000内的自守数为：{}".format(a))