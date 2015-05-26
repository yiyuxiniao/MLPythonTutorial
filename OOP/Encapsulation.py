#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""封装

python本身并不是面向对象的,虽然现在要转向面向对象,所以对封装的支持并不好,我们可以随便地访问和修改实例

但是它也提供了一些封装操作
__attr: 类成员属性混淆, 也仅仅是混淆而已
_attr: 属性不可import

封装: 不提供成员变量的访问,只提供函数的访问. 实在不行提供setter, getter函数
"""
__author__ = 'mlyixi'

class WrapMe(object):
    def __init__(self, obj):
        self.__name=obj # 私有实例属性
        self.abc=123
    @property # 只读属性
    def name(self):
        return self.__name
    @name.setter # 写检索
    def name(self,val):
        if not isinstance(val, str):
            raise TypeError('must be a string')
        self.__name=val
    @name.deleter
    def delName(self):
        del self.__name
    __slots__=('__name','abc') # 限制属性数量,防止动态添加

if __name__ == "__main__":
    w=WrapMe('abc')
    print w.name
    w.name='xyz'
    print w.name
    try: # 这是没有的属性
        w.dajiangyou=456
    except AttributeError:
        print "我没有dajiangyou属性"
    try: # __name访问不到了
        w.__name=456
    except AttributeError:
        print "我没有__name属性"
    try: # 只是混淆而已,实际还能访问
        w._WrapMe__name=456
        print "我有_WrapMe__name属性,值",w._WrapMe__name
    except AttributeError:
        print "我没有_WrapMe__name属性"
    print w.name
    print dir(w)
