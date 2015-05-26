#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""继承


"""
__author__ = 'mlyixi'

class RoundFloat(float):
    def __new__(cls, val): # 实例构造器, 一般只有对不可变的标准类型使用
        return super(RoundFloat, cls).__new__(cls,round(val,2))

class SortedKeyDict(dict): # 对于可变对象的继承, 一般只要覆盖特定方法就行了
    def keys(self):
        return sorted(super(SortedKeyDict,self).keys())

from NewClass import Point
class Circle(Point):
    def __init__(self, r=1): # 如果覆盖,则父类同名方法将得不到执行
        self.r =r

class Ellipse(Point):
    def __init__(self, x=1, r=1):
        Point.__init__(self,x) # 调用父类的初始化函数
        self.r =r

if __name__=='__main__':
    print Circle.x

    c=Circle(10)
    print 'x=', c.x, 'y=',c.y, 'r=', c.r
    c.x=5
    print 'x=', c.x, 'y=',c.y, 'r=', c.r
    d=Circle(20)
    print 'x=', d.x, 'y=',d.y,'r=', d.r

    e=Ellipse(10,10)
    print 'x=', e.x, 'y=',e.y, 'r=', e.r