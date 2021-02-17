#!/usr/bin/python
# -*- coding: utf-8 -*-
# Description: https://github.com/selfteaching/the-craft-of-selfteaching/blob/master/Part.3.B.3.decorator-iterator-generator.ipynb
# Create:  2021/2/17 19:26
# Author: Baihao

#让 a_func() 将它内部的 b_func() 作为它的返回值
def a_func_ori():
    def b_func():
        print("Hi,I am b_func!")
    print("Hi,I am a_func!")
    return b_func


def a_decorator(func):
    def wrapper():
        print('We can do sth. before a func is called...')
        func()
        print('... and we can do sth. after it is called...')
    return wrapper


# 注意：以上的代码中，a_decorator(func) 返回的是 wrapper 这个函数本身。
# 在我们定义 a_func() 的时候，在它之前，加上了一句 @a_decorator；这么做的结果是：
# 每次 a_func() 在被调用的时候，因为它之前有一句 @a_decorator，
# 所以它会先被当作参数传递到 a_decorator(func) 这个函数中…… 而后，真正的执行，是在 a_decorator() 里被完成的。
# —— 被 @ 调用的函数，叫做 “装饰器”（Decorator），比如，以上代码中的 a_decorator(func)。

@a_decorator
def a_func():
    print("Hi, I'm a_func!")

def test_decor_func():
    # b = a_func_ori()
    # b()
    print(type(a_func_ori()))
    a_func_ori()()
    print("="*10)
    a_func()
    print("=" * 10)
    print(a_decorator(a_func))

def an_output():
    return 'The quick brown fox jumps over the lazy dog.'

#装饰器的用途
#Decorator 最常用的场景是什么呢？最常用的场景就是用来改变其它函数的行为。
def upper_output(func):
    def wrapper():
        s= func()
        return s.upper()
    return wrapper


#还可以给一个函数加上一个以上的装饰器：
def strong(func):
    def wrapper():
        original_result = func()
        modified_restult = '<strong>'+original_result+'</strong>'
        return modified_restult
    return wrapper

@strong
@upper_output
def an_output2():
    return 'The quick brown fox jumps over the lazy dog.'

#装饰器的执行顺序是 “自下而上” —— 其实是 “由里到外” 更为准确。体会一下。
@upper_output
@strong
def an_output3():
    return 'The quick brown fox jumps over the lazy dog.'

def trace(func):
    def wrapper(*args,**kwargs):
        print(f"Trace: You've called a function:{func.__name__}(),",
              f"with args: {args} kwargs:{kwargs}")
        oringinal_result = func(*args,**kwargs)
        print(f"Trace:{func.__name__}() return {oringinal_result}")
        return oringinal_result
    return wrapper

@trace
def say_hi(greeting,name=None):
    return greeting +"! " + name

if __name__ == '__main__':
    test_decor_func()
    print(an_output(),"\n"+"=="*10)
    print(an_output2())
    print("**"*10)
    print(an_output3())
    print("=="*10)
    print(say_hi("hello",name="momo"))
