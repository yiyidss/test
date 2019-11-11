

def lx(name, age, *args, hobby, **kwargs):
    print("姓名：" + name)
    print("年龄：" + age)
    if not hobby:
        print("没有爱好！")
    else:
        print("我的爱好是{}".format(hobby))

    for i in args:
        print(i)

    for k,v in kwargs.items():
        print(k,v)

name = "HPY"
age = "20"

lx(name,age,"LLL","YYY",hobby="吃饭",hobby2="睡觉",hobby3="打豆豆")