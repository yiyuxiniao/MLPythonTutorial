#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""新类

正值python2到3的转变时期, 也是python完全对象化的过渡期, 于是有了新类这个词

新类: 从object派生而来的类就是新类

"""
__author__ = 'mlyixi'

class Point(object):
    """
    MyClass docstring
    """
    x=1 # 类属性
    z=2
    def __init__(self, x=0):
        """
        实例初始化函数,只设置实例的属性
        :param val:
        :return:
        """
        self.x = x # 可读写属性

    @classmethod # 类方法, 可以访问类属性,所以必须传入cls
    def hello(cls):
        print cls.x
    @staticmethod # 静态方法, 和类属性,成员属性都无关, 所以类/成员都可以访问
    def world(arg=1):
        print arg
    @property # 只读属性, python的@property设置为只读....
    def y(self):
        return self.x*2

if __name__=='__main__':
    print u"类方法用于访问类属性"
    Point.hello()
    Point.x+=1
    Point.hello()
    print u"静态方法: 和类属性,成员属性都无关, 所以类/成员都可以访问"
    Point.world(50)
    p1=Point(1)
    p1.world(20)
    print u"实例属性"
    p2=Point(10)
    print p2.x, p2.y
    print u"类属性会延伸到实例属性,如果没有定义的话"
    print 'z=',p2.z

    print u"实例属性能随意添加"
    p2.r=20
    print 'r=', p2.r




