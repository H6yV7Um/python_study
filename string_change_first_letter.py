#!/usr/bin/python
#_*_ encoding:utf-8 _*_
import sys
from string import upper
from string import lower
from string import lowercase
from string import capitalize


#功能：首字母转大写
'''
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
'''

#提示输入
#test_str=map(str,raw_input('请输入需转换名字并以空格为区分:').split())

test_str=['adam', 'LISA', 'barT']

#把所有名字的字幕都转化为小写
low_str=map(lower, test_str)

#把每个名字的首字母转化为大写
result=map(capitalize, low_str)

#输出转化后的名字
print "转化结果如下："

for i in result:
    print i

'''
Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积。
'''

def prod(x,y):
        return x*y


list_input=map(int,raw_input('请输入数字:').split(','))


b=reduce(prod, list_input[0:])
print b