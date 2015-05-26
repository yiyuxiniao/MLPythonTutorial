#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""re库
用于提取较复杂的文本信息

## 元字符
. ^ $ * + ? { } [ ] \ | ( )
## 基本模式
|  符号 | 说明 |
|-----|-----|
|  |  |逻辑或|
|  .  |任意一个字符(除换行符"\n"外)|
|  ^  |字符串开始|
|  $  |字符串结尾|
|  *  |之前出现的模式0到多次|
|  +  |之前出现的模式1到多次|
|  ?  |之前出现的模式0到1次|
|{M,N}|之前出现的模式M到N次|
|[...]|任意一个可能的字符|
|[..x-y..]|缩写|
|[^...]|不匹配所有可能的字符|
|(...)|分组, group方法|
## 字符类别
|字符类别|说明|
|------|-----|
|  \d  |任何数字|
|  \w  |任何数字字母字符|
|  \s  |任何空白符|
|  \b  |单词边界|
|  \nn |子组号|
|  \c  |匹配特殊字符|
|  \A  |字符串起始|
|  \Z  |字符串结束|
|  大写一般表示取反  |

注意点:能找到结构的话尽量用string的方法而不用re,能保证是一行内的就在eachline中匹配,尽量不在大字符串中使用re
"""
__author__ = 'mlyixi'

import re
# 下面从简单的函数说起
# match() 从字符串起点开始比较,不会移动
m1=re.match(r'f.','foo')
m2=re.match(r'f.','gfoo')
if m1 is not None and m2 is None:
    print m1.group()      # 匹配对象SRE_Match的group()方法,参数默认为0,返回整个匹配项,否则子组号对应结果
    print "m2 is None"    # 不会移动

# search() 从字符串起点开始比较,如果不匹配,就向后移动
s1=re.search(r'f.','foo')
s2=re.search(r'f.','gfoo')
if s1 is not None and s2 is not None:
    print s1.group()      # 会移动
    print s2.group()

# findall(), 返回所有"匹配字符串"的列表
f = re.findall(r'f.', 'gfoogf.')
if f is not None:
    print f

# finditer(), 返回所有"匹配对象"的列表的迭代器
i= re.finditer(r'f.', 'gfoogf.')
for matchobject in i:
    print matchobject.group()

# 用了这么多默认参数的group(),我们再来看看子组
g = re.search(r'(a)(b)', 'abgab')
print g.group()  # 匹配字符串
print g.group(1)  # 第一子组
print g.group(2)  # 第二子组
print g.groups()  # 子组的元组
print g.span()   # 只要找到一个就返回了

# split() 将字符串按指定字符串或模式进行分割
sp = re.split(r':s', 'str1:str2:str3')
print sp

# 我们注意到模式前总加了一个'r', 这是因为一些字符类别与asccii码重复了,加r就代表使用字符类别而不是ascci码
sb=re.search('\bblow', 'blow')
if sb is None: print "sb.group() is none"
sr=re.search(r'\bblow', 'blow')
if sr is not None: print sr.group()

# sub()和subn()替换所有,subn返回替换次数
rs=re.sub('X', 'Mr. Smith', 'attn: X\n\nDear X,\n')
print rs
rsn=re.subn('X', 'Mr. Smith', 'attn: X\n\nDear X,\n')
print rsn

# 如果处理大字符串,re会很慢.这时将模式编译出regex对象,再运行上面的方法会快一些
regex=re.compile(r'\bblow')
rm=regex.match('blow')
print rm.group()

# 下面以电子邮箱示例模式的写法, 符合rfc5321标准的模式是很难的,同时也是不合实际的,
# 标准列出允许情况,但是事实上,我们不会使用一些情况,比如区分大小写
email_re = re.compile(r'([\w\-][\w\-\.]+)@([\w\-][\w\-\.]+[a-z]{1,4})',
                      re.IGNORECASE) # 事实标准是不区分大小写
er=email_re.search('yiyef@gmail.com fdafdf') # 必须有非a-z的间隔符
if er is not None:print er.group()