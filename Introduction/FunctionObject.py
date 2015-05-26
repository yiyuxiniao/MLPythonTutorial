#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""函数对象

函数也是对象!

默认参数, 不定参数, 字典参数

def foo(arg1, arg2='default', *tuple, **dict):
    pass

函数式编程: lambda, filter, map, reduce
* filter(bool_func, seq):将顺序容器按bool_func过滤
* map(func, seq):将func作用到顺序容器的每一个元素上
* reduce(func, seq):将顺序容器的前N个参数调出作为func的参数，再递归下去
"""
__author__ = 'mlyixi'

def foo(arg1, string='default', *z):
    print arg1, string, z
print u'测试函数参数'
foo(50, 'hello')
foo('hello', 50)
foo('hello',string=50)

print u'测试匿名函数: a=lambda args: expr'
b = lambda arg1, string=1, *z : arg1+string+z[0]
print b(23,2, 5,20)
