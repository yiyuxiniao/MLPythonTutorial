#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Python代码的组织方式

从逻辑结构和文件系统两方面看:
* 包: 其实就是文件夹
* 模块: 其实就是Python文件,在其中可以定义变量,函数和类

名称空间: 由包和模块构成,组成代码的逻辑结构,不致混乱
"""

__author__ = 'mlyixi'

print u'覆盖变量, 方法, 类'
print __doc__
a=50
print a
# from Introduction.PythonObject import * 不好的引入方式
from Introduction.PythonObject import a # 较好的引入方式
# import Introduction.PythonObject as po 最好的方式,不过写起来比较麻烦
print a # 覆盖了

