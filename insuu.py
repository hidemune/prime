#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
argvs = sys.argv
argc = len(argvs)


if (argc != 2):
    print ('Usage: # python %s number' % argvs[0] )
    quit()

try:
    num = int(argvs[1])
except:
    num = 0

ret = ''
flg2 = False

while True:
    f = open('sosuu.txt','r')
    line = f.readline() # 1行読み込む(改行文字も含まれる)
    flg = False
    while line:
        # print line
        i = int(line.strip())
        if num % i == 0:
            ret += '*' + str(i)
            num = num / i
            flg = True
            break
        if i ** 2 > num:
            flg2 = True
            ret += '*' + str(num)
            break
        line = f.readline()
    if num == 1:
        break
    f.close
    if flg == False:
        if flg2 == False:
            ret += '*(' + str(num) + ') 入力された値が大きすぎます'
        break

print (ret[1::])

