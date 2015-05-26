#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""python2.7以后新增的argparse

用于替代getopt及optparse, 进行命令行应用的构建
ArgumentParser.add_argument(name or flags…[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])
para name/flags: 位置参数不带"-", 开关参数带"-",也可以指定其它符号(一般要遵从Unix标准)
para action: 动作
             store, 默认,即值为字符串.
             store_const, 加载const项中的值
             store_true/false, 加载default中布尔值的相反值
             append: 将值添加到列表
             append_const, 将常数值添加到列表
             version, 打印程序的版本信息
para nargs: 该参数接受多少个变量
            int, 指定具体个数
            "?", 0个或1个, 没有指定name/flag时从default中取值, 指定name/flag但变量为0时从const中取值
            "*", 不定个数,多个. 则保存为列表
            "+", 类似于"*",但对于位置参数,如果不带变量则报错

para default: 参数的默认值
para type: 转化成指定数据类型
para choices: 指定参数值的范围
para required: 指定这个参数是必须提供的
para help: 提供这个参数的帮助信息
para metavar: 也用于帮助信息
para dest:   存储的变量名,如不指定,则默认是参数名
"""
__author__ = 'mlyixi'

import argparse

parser=argparse.ArgumentParser(description='This is a cmd program')
parser.add_argument('-a', action="store_true", default=False)
parser.add_argument('-b', action='store', help="--busy", dest="b")
parser.add_argument('-c', action='store', dest='c', type=int)

dic=parser.parse_args(['-a', '-bval', '-c', '3']) # 生成一个字典
print type(dic)
print dic.c