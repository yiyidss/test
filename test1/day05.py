list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]

print(list[2:3])

a = 12
b = 'aa'
print(hex(a))   #转化16进制
print(oct(a))   #转化8进制

a = ['a', 'b', 'c']
n = [1, 3,2,2]
x = [a, n]
print(x[1][1])
m = n.index(2)
print(m)

x = True
country_counter = {}

def addone(country):
    if country in country_counter:
        country_counter[country] += 1
    else:
        country_counter[country] = 1

addone('China')
addone('Japan')
addone('china')

print(len(country_counter))

confusion = {}
confusion[1] = 1
confusion['1'] = 2
confusion[1] += 1

sum = 0
for k in confusion:
    sum += confusion[k]

print(sum)


a = 1
b = 1
while a < 1000:
    a,b = b, a+b
    print(b)