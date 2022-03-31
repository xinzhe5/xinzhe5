# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 18:55:03 2022

@author: 21203
"""

a = 'python'
for i in range(0,3):
    b = input("请输入六位密码：")
    if len(b)!=6:
        if i == 2:
            print("密码位数不对,请重新登录系统！")
        else:  
            print("密码位数不对，请重新输入！")
    elif a != b:
        if i == 2:
            print("密码不对,请重新登录系统！")
        else:  
            print("密码不对，请重新输入！")
    elif a == b:
        print("密码正确，进入系统")
        break
    
