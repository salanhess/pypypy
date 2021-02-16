#!/usr/bin/python
# -*- coding: utf-8 -*-
# Description: 
# Create:  2021/2/16 20:47
# Author: Baihao

import this

def trans():
    dic_map=this.d
    orgstr=this.s

    print("this.d is {}".format(this.d))
    print("this.s is {}".format(this.s))

    real=""
    for i in this.s:
        if i in this.d.keys():
            real+=this.d[i]
        else:
            real+=i
    print("="*20)
    print("this.s trans  is {}".format(real))

if __name__ == '__main__':
    trans()