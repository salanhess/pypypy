#!/usr/bin/python
# -*- coding: utf-8 -*-
# Description: 
# Create:  2021/2/17 0:11
# Author: Baihao

import datetime
class golem():
    __age = 10
    def __init__(self,name=None):
        self.name = name
        self.built_year = datetime.date.today()

    def sayhi(self):
        print("[{}] Hi {}! your are {} years old!".format(self.built_year,self.name,self.__age))

    @property
    def age(self):
        return golem.__age

class Newgolem(golem):
    __learn=True
    age = 33
    def new(self):
        print("[{}] Hi {}!your are {} years old, your can learn is {}!".format(self.built_year, self.name, self.age,self.__learn))

if __name__ == '__main__':
    g = Newgolem("baih")
    g.new()
    g.name='niuniubai'
    g.sayhi()
    print("==="*3)
    #print(dir(g))
    print("==="*3)
    print(g.__dict__)
    print("==="*3)
    print(help(g))
    print("==="*3)
    print(hasattr(g,'__name'))
    print(hasattr(g, '__age'))
    g.age=39
    print(hasattr(g, 'age'))
    setattr(g,'age',44)
    g.new()
    g = golem('susan')
    g.age=33
    print(g.age)