# 生成列表
# l=[x*x for x in range(1,11)]
# print(l)
# 取列表中最大和最小值
# def find(L):
#     if L == []:
#         print(None,None)
#     else:
#         min=L[0]
#         max=L[0]
#         for i in L:
#             if i > max:
#                 max = i
#             if i < min:
#                 min = i
#     return (min,max)
#
# print(find([1,54,3,2,97,1,321,0]))
#
#  生成器generator
# g=(x*x for x in range(1,11))
# print(next(g))
# print(next(g))

#  求阶乘
# def f(n):
#     if n == 1:
#         return 1
#     return n*f(n-1)
# print(f(5))
#
# def x(i,j):
#     if i == 1:
#         return j
#     return x(i-1,i*j)
# print(x(5,1))

from functools import reduce

a = 60
b = 13
print(a&b)

def add(x,y):
    return (x+y)
x = reduce(add,[1,2,3,4,5,6,7,8,9])
print(x)

def func(name):
    for i in range(len(name)):
        if i == 0 :
            n = name[i].upper()
        else:
            n = n + name[i].lower()
    return n
L=list(map(func,['asdas','ASDA','sfsdASD']))
print(L)

'''
啥意思。。。？
'''
