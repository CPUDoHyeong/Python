# 백준 알고리즘 - 10773

'''
제로 

'''

import sys

K = int(sys.stdin.readline())
memo = []

for _ in range(K) :
    n = int(sys.stdin.readline())
    if n == 0 :
        memo.pop()
    else :
        memo.append(n)

print(sum(memo))
