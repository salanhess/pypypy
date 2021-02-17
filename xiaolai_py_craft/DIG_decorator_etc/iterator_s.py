#!/usr/bin/python
# -*- coding: utf-8 -*-
# Description: 
# Create:  2021/2/17 12:19
# Author: Baihao


class Counter(object):
    def __init__(self, start, stop):
        self.current = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.stop:
            raise StopIteration
        else:
            c = self.current
            self.current += 1
        return c

def iter_test():
    string = "this is a string."
    for c in string:
        print(c, end=',')
    p = "Python"
    print()
    print('type(p) is {}'.format(type(p)))
    i = iter("Python")
    print(next(i))
    print(next(i))
    print('type(i) is {}'.format(type(i)))
    s = iter((1, 2, 3, 4, 5))
    print('type(s) is {}'.format(type(s)))
    print(next(s))
    print(next(s))

if __name__ == '__main__':
    # iter_test()
    c = Counter(2,5)
    while True:
        try:
            print(next(c),sep=',')
        except StopIteration:
            print("StopIteration")
            break
    # print(next(c))
    # print(next(c))
    # print(next(c))
    # print(next(c))