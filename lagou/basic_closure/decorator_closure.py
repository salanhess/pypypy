#!/usr/bin/python
# -*- coding: utf-8 -*-
# Description: use decorator
# Create:  2021/2/11 17:49
# Author: Baihao

import time


def record_time(func):
    def wrapper(*kwargs):
        print('function start at {}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        time.sleep(2)
        inner_ret = func(*kwargs)
        print('function end at {}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        return inner_ret
    return wrapper

@record_time
def sum_dec(*kwargs):                                                                                                                               
    sum = 0
    for item in kwargs:
        sum += item
    return sum


def sum(*kwargs):
    sum = 0
    for item in kwargs:
        sum += item
    return sum


if __name__ == '__main__':
    print(sum(1, 2, 3))
    print(record_time(sum)(3, 2, 1))
    print(sum_dec(1, 2, 3))
