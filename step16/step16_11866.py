# 백준 알고리즘 - 11866
'''
1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.
N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오
'''

import sys
from collections import deque

# n, k = map(int, sys.stdin.readline().split())
# result = []
# deque = deque([i for i in range(1, n + 1)])
# index = k-1

# while len(deque) <= 1 :
#     for i in range(k) :
#         if index > len(deque) :
#             index = index % len(deque)

n, k = map(int, input().split())
s = deque([])
for i in range(1, n + 1):
    s.append(i)
print('<', end='')
while s:
    for i in range(k - 1):
        s.append(s[0])
        s.popleft()
    print(s.popleft(), end='')
    if s:
        print(', ', end='')
print('>')

    
    

# result.append(deque[0])

# print('<', deque, '>')
