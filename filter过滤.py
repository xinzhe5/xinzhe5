# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 19:50:15 2022

@author: 21203
"""

import math
temp=list(filter(lambda n:math.sqrt(n)==int(math.sqrt(n)),range(1,101)))
print('filter结果：{}'.format(temp))