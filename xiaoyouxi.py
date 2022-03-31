# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 20:49:08 2022

@author: 21203
"""

n,m=map(eval,input("请输入人数和序号,以逗号分隔:").split(","))
i=0
j=1
people=list(range(1,n+1))
while True:
    if i == len(people):
        i = 0
    if j == m+1:
        j = 1
    if j == m:
        temp = people.pop(0)
    else:
        temp = people.pop(0)
        people.append(temp)
    if len(people) == 1:
        break
    i+=1
    j+=1
print('最后的序号为：{}'.format(people))
