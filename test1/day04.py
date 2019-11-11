import datetime
z = datetime.datetime.now()
y = datetime.datetime.strptime("2019-7-22-11-50-20","%Y-%m-%d-%H-%M-%S")
print((z-y).days)

import sys
print('================Python import mode==========================');
print ('命令行参数为:' + str(sys.argv) )
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)
