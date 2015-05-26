#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Python对象

身份: 可理解为身份证或内存地址，用id()得到

类型: 可以认为是对象所属的类，用type()得到

值:   对象存储的数值项
"""

__author__ = 'mlyixi'

# 标准类型, 也叫标准内建类型
a = 10  # int
b = False #bool
c = 10L #long
d = 3.4 #float
e = 1+2j #complex
f = 'string' #string
g = (a,) #tuple
h = [a] # list
i = {f:b} # dict

# 其它内建类型, 当然还包括代码组织上的一些类型,如函数,模块,类,包等,这些将在后面具体讲
t = type(type(a)) # type型
n = None # Null
m = file(__file__) # file
s = set('cheeseshoop') # set
fs= frozenset('bookshop') # frozenset

# 工厂函数, 如其它内建类型中的构建函数就是工厂函数,标准类型中的工厂函数是注释名
# 这里注意哪些情况下判断的真值
b = bool(0.0) # 值为0
b = bool(None) # None值
b = bool('') # 空容器


# 标准操作
## 身份比较
b = a is c
b = id(a)==id(c)
nb = a is not c
## 值比较
b = a>c
b = a==c


# 魔术函数,
cmp(a,c)
repr(a)
str(a)
## 可以发现,这些函数可以作用于所有的内建类型,但它明显不是工厂函数. 后面我们可以发现,它其实是通过调用各种类型内定义的
## __funname__来实现的. 魔术方法很多,具体参见http://www.rafekettler.com/magicmethods.html

