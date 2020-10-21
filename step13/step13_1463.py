# 백준 알고리즘 - 1463
'''
1로 만들기
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 
연산을 사용하는 횟수의 최솟값을 출력하시오.
'''

import sys

# x = int(sys.stdin.readline())
# count = 0

# while(x != 1) :
#     if x % 3 == 0 :
#         x = x / 3
#     elif x % 2 == 0 :
#         x = x / 2
#     else :
#         x = x - 1
#     count += 1

# print(count)

a = int(input()) + 1
min_cnt = [-1 for i in range(a)]

for i in range(1, a) :
    min_cnt[i] = min_cnt[i-1] + 1
    if i % 2 == 0 :
        min_cnt[i] = min([min_cnt[i], min_cnt[int(i/2)]+1])

    if i % 3 == 0 :
        min_cnt[i] = min([min_cnt[i], min_cnt[int(i/3)]+1])

print(min_cnt[-1])