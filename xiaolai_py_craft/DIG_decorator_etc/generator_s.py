#!/usr/bin/python
# -*- coding: utf-8 -*-
# Description: 生成器使用的yield 和 return 最明显的不同在于，在它之后的语句依然会被执行 —— 而 return 之后的语句就被忽略了
# Create:  2021/2/17 12:48
# Author: Baihao

# 生成器函数被 next() 调用后，执行到 yield 生成一个值返回（然后继续执行 next() 外部剩余的语句）；
# 下次再被 next() 调用的时候，从上次生成返回值的 yield 语句处继续执行……
# 如果感觉费解，就多读几遍 —
# 而后再想想若是生成器中有多个 yield 语句会是什么情况？

def counter(start, stop):
    multi_yield=0
    while start <= stop:
        print("Before yield,start is {}".format(start))
        yield start
        start += 1
        print("After yield,start+1 is {}".format(start))
        print("Before multi_yield,start is {}".format(multi_yield))
        yield multi_yield
        multi_yield +=1
        print("After multi_yield,start is {}".format(multi_yield))

def func_counter():
    for i in counter(1, 3):
        print("[next],i is {}".format(i))

def fab(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a, b = b,a+b
        n = n+1

def fab2(n):
    if n==0 or n==1:
        return n
    else:
        return n+fab2(n-1)

def test_fab2():
    for i in range(5):
        print("fab2({})={}".format(i+1,fab2(i+1)))

if __name__ == '__main__':
    #test_fab2()

    #yield + generator version
    f = fab(5)
    print(f.__next__())
    try:
        for i in range(5):
            print("f({})={}".format(i,next(f)))
    except StopIteration:
        pass
