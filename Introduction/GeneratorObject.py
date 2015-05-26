#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""生成器对象

和迭代器类似,可以通过yield语句生成生成器对象,也带有next()方法, 可以遍历.

生成器主要的一个用途就是不必知道完整的容器对象,只需要知道当前的对象就行了.总体上就是节省内存
"""
__author__ = 'mlyixi'

def simpleGen():
    yield 123,
    yield 'xyz'
    yield 45.67

g = simpleGen()
while True:
    try:
        print g.next()
    except StopIteration: # 如果超过范围,抛出异常
        break

# 生成器表达式 或 元组推断
print "(expr for iter_var in interable if cond_expr)"
print "注意, 程序的运行顺序变了"
l = (x+1 for x in g if isinstance(x, int))
for i in l:
    print l