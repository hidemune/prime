#!/usr/bin/python
# -*- coding: utf-8 -*-
def prime():
    counter = 0
    primes = [2, 3]
    with open('./sosuu.txt','w') as f:
        f.write('2\n3\n')
        f.close
    n = 3
    while True:
        #for n in range(5, 1048576, 2):
        n += 2
        isprime = True
        for i in range(1, len(primes)):
            counter += 1
            if primes[i] ** 2 > n:
                break
            counter += 1
            if n % primes[i] == 0:
                isprime = False
                break
        if isprime:
            primes.append(n)
            with open('./sosuu.txt','a') as f:
                f.write(str(n))
                f.write('\n')
                f.close()
    #print primes, len(primes)
    print u'乗除算を行った回数：%d' % counter
if __name__ == '__main__':
    prime()
