from model import *
import math

for i in reversed(range(1,100,3)):    # reversed 反向遍历序列
    print(i, end='    ')
print('')

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for x in sorted(tuple(basket)):             # tuple 元组返回整个序列
    print(x)
for f in sorted(set(basket)):               # set 集合返回元素序列    ，删除重复数据
    print(f)

fib = fibo(1000)
fib_2 = fibo_2(1000)

print(repr(3).rjust(0))
#  占位符
print('这是一个{}岁的老{}'.format(21,'大叔'))
print('你想{}年里挣够{}这么多钱吗'.format(10,1000000000))
print('梦里都有')
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():
    print('{0:15}=={1:15d}'.format(name,number))
print('我钟意你啊,%s '%'一一')

# #  input使用键盘输入
# a = input('请输入您的年龄：')
# b = input('请输入您的性别：')
# if a >= '20':
#     if b == '男':
#         print('哦哦，是一位'+a+'岁的老大叔了哦')
#     else:
#         print('哦哦，是一位'+a+'岁的老阿姨了哦')
# else:
#     if b == '男':
#         print('怎么是一个才'+a+'岁的小男孩嘛')
#     else:
#         print('怎么是一个才' + a + '岁的小萝莉啊')

# #  打开文件读取文件内容
# f = open('iii.txt', encoding="utf-8")    #  encoding="utf-8"用来解码打开中文内容文档
# str = f.read()
# print(str)
# f.close()
#
# f = open('yyy.txt','w')
# num = f.write('i love you three thousand times')
#
# f = open('yyy.txt','r')              #   文件共能只能选一个，使用先后顺利  W+R
# str = f.read()
# print(str)
# f.close()

f = open('yyy.txt','w')
x = f.write('马新林有点傻逼哦')

f = open('yyy.txt','r')
y  = f.read()
print(y)
f.close()

f = open('iii.txt','r')
z = f.read()
print(z)
f.close()

import re
print(re.match('www', 'www.runoob.com').span())
