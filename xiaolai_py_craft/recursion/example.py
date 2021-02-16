#!/usr/bin/python
# -*- coding: utf-8 -*-
# Description: 
# Create:  2021/2/16 18:24
# Author: Baihao

def move(n,a,b,c):
    if n==1:
        print(a,"-->",c) #move from a to c
    else:
        move(n-1,a,c,b) #move n-1 from a to b
        move(1,a,b,c) #move 1 from a to c
        move(n-1,b,a,c) #move n-1 from b to c

if __name__ == '__main__':
    move(2,"A","B","C")
    print("=============")
    move(3, "A", "B", "C")