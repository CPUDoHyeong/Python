# 백준 알고리즘 - 1021
'''
회전하는 큐
'''

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
q = deque()

for i in range(n) : 
    q.append(i+1)
want = map(int, sys.stdin.readline().split())

total = 0

for w in want :
    i = 0
    while w != q[i] :
        i += 1
    i = len(q) -i if len(q) - i < i else -i
    q.rotate(i)
    total += abs(i)
    q.popleft()

print(total)