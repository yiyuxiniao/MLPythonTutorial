#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""迭代器对象

对于容器类型（文件可认为是字符串,字典默认迭代它的键）,可以通过函数生成迭代器
迭代器就是一个带有next()方法的对象, 可以遍历容器对象

* iter()
* reversed()
* enumerate()

"""
__author__ = 'mlyixi'

myTuple = (123, 'xyz', 45.67)

print u'forin 遍历'
for i in myTuple:
    print i

print u'底层迭代器遍历'
i = iter(myTuple)
while True:
    try:
        print i.next()
    except StopIteration: # 如果超过范围,抛出异常
        break

print u'反向迭代器遍历'
i = reversed(myTuple)
while True:
    try:
        print i.next()
    except StopIteration:
        break

print u'迭代器遍历,enumerate对象'
i = enumerate(myTuple)
while True:
    try:
        print i.next()
    except StopIteration:
        break

# 列表解析 或 列表推断: 我管理叫它列表推断更好些,其实就是根据一个列表生成另一个列表
print "[expr for iter_var in interable if cond_expr]"
l = [x+1 for x in myTuple if isinstance(x, int)]
for i in l:
    print l
