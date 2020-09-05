# 백준 알고리즘 - 1929
'''
소수 구하기
M과 N이 주어졌을 때 한 줄에 하나씩 증가하는 순서대로 소수를 출력하라.
'''

# M, N = map(int, input().split())

# for i in range(M, N+1) :
#     cnt = 0
#     for j in range(1, i//2+1) :
#         if i % j == 0 :
#             cnt += 1
#             if cnt > 1 :
#                 break
#     if cnt == 1 :
#         print(i)
    
import math

def isSosu(num) :
    if num == 1 :
        return False
    
    n = int(math.sqrt(num))
    # 2가 들어오면 range(2, 2)이 된다.
    # 그러므로 True
    for i in range(2, n+1) :
        if num % i == 0 : return False
    return True

M, N = map(int, input().split())
for i in range(M, N+1) :
    if isSosu(i) : print(i)
