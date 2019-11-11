import random

list = {}
sum = 25
for x in range(1,sum+1):
    list[x] = x
i = 1
y = []                                                          #   随机不重复取出全部单条数据
while i <= sum:
    z = random.randint(1, sum)
    if z not in y:
        y.append(z)
        print(z)

