def func(n):
    if n == 1 or n == 2:
        return 1
    return func(n-1) + func(n-2)

res = func(10)
print(res)

# 汉诺塔方法——————递归函数
a = 'A'
b = 'B'
c = 'C'
def hano(a,b,c,n):
    if n == 1:
        print("{} --> {}".format(a, c))
        return None
    if n == 2:
        print("{} --> {}".format(a, b))
        print("{} --> {}".format(a, c))
        print("{} --> {}".format(b, c))
        return None
    hano(a,c,b,n-1)
    print("{} --> {}".format(a, c))
    hano(b,a,c,n-1)

hano(a,b,c,5)