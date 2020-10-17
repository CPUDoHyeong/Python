# 백준 알고리즘 - 9461
'''
파도반 수열
https://www.acmicpc.net/problem/9461
'''

import sys

# 첫번째 규칙
# N이 6부터는 규칙이 나오기 시작한다
# N = (N-1) + (N-5)
T = int(sys.stdin.readline())
padoban_list = [0] * 101

padoban_list[1] = 1
padoban_list[2] = 1
padoban_list[3] = 1
padoban_list[4] = 2
padoban_list[5] = 2

for i in range(6, len(padoban_list)) :
    padoban_list[i] = padoban_list[i-1] + padoban_list[i-5]

for _ in range(T) :
    N = int(sys.stdin.readline())
    print(padoban_list[N])

# 두번째 규칙
# (N+3) = N + N+1
# wh = [0 for i in range(101)]
# wh[1] = 1
# wh[2] = 1
# wh[3] = 1
# for i in range(0, 98):
#     wh[i + 3] = wh[i] + wh[i + 1]
# t = int(input())
# for i in range(t):
#     n = int(input())
#     print(wh[n])