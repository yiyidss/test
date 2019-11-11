# 字符串转换int型
# from functools import reduce
#
# def str2int(s):
#     def func(x,y):
#         return x * 10 + y
#     def char2num(s):
#         return l[s]
#     return reduce(func,map(char2num,s))
# l= {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#
# print(str2int(l))
#
# 排除奇数
# def not_odd_num(s):
#
#     for s in range(1,s):
#         if s % 2 == 0:
#             print(s)
#     return s % 2 == 0
# print(not_odd_num(11))

# filter筛选
# def not_odd(n):
#     return n % 2 == 0
#
# newlist = filter(not_odd, range(10))
# print(list(newlist))
# #
# def func(s):
#     news = str(s)
#     return news == news[::-1]
# print(list(filter(func,range(100))))

# 元组排序
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#
# def by_name(t):
#     return t[0]
# def by_score(t):
#     return t[1]
#
# i=list(sorted(L,key=by_name))                # key函数定义排序方式
# j=list(sorted(L,key=by_score,reverse=True))          # reverse定义倒序
#
# print(i)
# print(j)

# def fab(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#
# for n in fab(10):
#     print(n)

# def odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n
#
# def not_div(n):
#     return lambda x : x % n > 0
#
# def primes():
#     yield 2
#     iter = odd_iter()
#     while True:
#         n = next(iter)
#         yield n
#         iter = filter(not_div(n),iter)
#
# # 打印1000以内的素数:
# for n in primes():
#     if n < 100:
#         print(n)
#     else:
#         break

# def Lsum(*args):
#     def add():
#         x = 0
#         for n in range(1,4):
#             x = x + n
#         return x
#     return add
#
# f = Lsum(1,2,3,4,5,6,6,666,6)
# f
# print(f())
# g = Lsum(1,2,3,4)
# g
# print(g())

# def func():         # 自增整数，每次调用+1
#     def add():
#         n = 1
#         while True:
#
#             yield n
#             n += 1
#     iter = add()
#     def counter():
#         return next(iter)
#     return counter           # 返回函数，调用时返回函数结果
#
# f = func()     #  调用函数
#
# print(f())
# print(f())
# print(f())
# print(f())
# print(f())
# print(f())

# L = [1,3,5,12,7,6,15,4]              # 冒泡排序
# for x in range(len(L)):
#     for y in range(x+1,len(L)):
#         if L[x]>L[y] :
#             L[x],L[y]=L[y],L[x]
# print(L)
#
# L = list(map(lambda x:x*x , [1,2,3,4,5,6,7,8,9]))   # map函数完成一一映射，lambda匿名函数 自己书写功能
# print(L)

# def is_odd(n):
#     return n % 2 == 1
#
# L = list(filter(is_odd, range(1, 20)))

L = list(filter(lambda x: x%2 == 1,range(1,20)))

print(L)

