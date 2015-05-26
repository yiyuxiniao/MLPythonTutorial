#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""数据类型分类

我们可以从3种模型分类来认识
* 存储模型：原子类型或容器类型
* 更新模型：可变类型或不可变类型
* 访问模型：直接访问、顺序访问或映射访问
"""
__author__ = 'mlyixi'

import PythonObject
print __doc__
print u'原子类型'
print type(PythonObject.a)
print type(PythonObject.b)
print type(PythonObject.c)
print type(PythonObject.d)
print type(PythonObject.e)

print u'容器类型' # 后面我们会说明它们都有迭代器
print type(PythonObject.f)
print type(PythonObject.g)
print type(PythonObject.h)
print type(PythonObject.i)

print u'可变类型'
print type(PythonObject.h)
print type(PythonObject.i)
print type(PythonObject.s)

print u'不可变类型'
print type(PythonObject.a) # int是重指向的
print type(PythonObject.f) # string都是重指向的
print type(PythonObject.g)