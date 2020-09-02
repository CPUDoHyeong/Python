# 백준 알고리즘 - 1011
'''
Fly me to the Alpha Centauri
'''
# 처음과 끝의 이동은 항상 1고정
# https://wlstyql.tistory.com/54

import math

T = int(input())
for __ in range(T) :
    # x는 시작점, y는 도착점    
    x, y = map(int, input().split())
    diff = int(y - x)
    if diff <= 3 :
        print(diff)
    else :
        n = int(math.sqrt(diff))
        if diff == n ** 2 :
            print(2*n-1)
        elif n ** 2 < diff <= n ** 2 + n :
            print(2*n)
        else :
            print(2*n+1)
    

