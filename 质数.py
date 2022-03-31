# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 18:11:25 2022

@author: 21203
"""
temp=[]
from math import sqrt
for i in range(101,1001,2):
    for j in range(2, int(sqrt(i))):
        if i%j == 0:
            break
    else:
        temp.append(i)
zhishu=list(filter(lambda n:n%10==7,temp))
print('三位整数中，末位为7的素数共有{}个 分别为:\n{} '.format(len(zhishu),zhishu))