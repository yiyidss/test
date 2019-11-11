# import datetime
#
#
# def now():
#     time = datetime.datetime.now()
#     print(time)
#
# f = now
# f()
# print(now.__name__)
# print(f.__name__)


# def hi(name="yasoob"):
#     return "hi " + name
# greet = hi
# del hi
#
# print(greet())


def hi(name="yasoob"):
    def greet():
        return "now you are in the greet() function"
    def welcome():
        return "now you are in the welcome() function"
    if name == "yasoob":
        return greet()
    else:
        return welcome()
a = hi
print(a())                                # ()是函数的重要组成部分