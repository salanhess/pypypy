#!/usr/bin/python
# -*- coding: utf-8 -*-
# Description: 告别CRUD，拥抱高阶编程
# 列表表达式、lambda匿名函数、反射Reflection、闭包closure
# Create:  2021/2/10 9:56
# Author: Baihao

import inspect


# 闭包closure
def add_closuer():
    a = 10
    def add(b):
        return a+b
    return add


# 列表表达式 List Comprehension
def list_exp(nums):
    print([i * 2 for i in nums if i % 2 == 0])


# lambda arguments : expresssion
a = lambda l: [item * item for item in l]
b = lambda x, y: x + y


# Reflection
# type(obj),dir ,id, inspect
def use_ref():
    a = "123"
    print("a is:%s", type(a))
    print("a func is :%s", dir(a))
    print("a id is:%s", id(a))
    print("inspect module name:%s", inspect.getmodulename(__file__))


if __name__ == '__main__':
    list_exp([1, 2, 3, 4, 8, 10])
    print(a([1, 2, 3]))
    print(b(1, 2))
    use_ref()
    print(add_closuer()(1))
    print(add_closuer()(2))
