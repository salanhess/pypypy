#!/usr/bin/python
# -*- coding: utf-8 -*-
# Description:
# In mathematics and computer science,
# an algorithm is an unambiguous specification of how to solve a class of problems.
# Algorithms can perform calculation, data processing, and automated reasoning tasks.
# Create:  2021/2/16 20:59
# Author: Baihao

def is_leap(n):
    flag=False
    if n%4 == 0:
        flag =True
        if n %100 == 0 and n %400 !=0:
            flag=False
    print(flag)
    return flag

if __name__ == '__main__':
    is_leap(4)
    is_leap(200)
    is_leap(220)
    is_leap(400)