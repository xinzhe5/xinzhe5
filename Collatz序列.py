# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 18:52:39 2022

@author: 21203
"""

def collatz(number):
    if number%2 == 0:
        return number//2
    else:
        return 3*number+1
    
Num=eval(input("请输入一个正整数："))
while True:
    if Num >= 0 and type(Num) == int:
        print(Num,end=' ')
        Num=collatz(Num)
    else:
        print("输入数据有问题请重新输入")
        Num=eval(input("请输入一个正整数："))
    if Num ==1:
            break
print(Num,end=' ')