# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 20:50:58 2022

@author: 21203
"""

a,b =map(int,input("请输入通话时间（分:秒）:").split(":"))
if a==00 and b==00: 
    print("通话时间刚接通，被挂断！话费应收0.20元")
elif a<3 or (a==3 and b==00):
    c=0.2
    print("通话时间为{}分{}秒话费应收{:.2f}元".format(a,b,c))
else:
    if b==00:
        c=(a-3)*0.1+0.2
    else:
        c=(a-2)*0.1+0.2
    print("通话时间为{}分{}秒话费应收{:.2f}元".format(a,b,c))
    
              