# 백준 알고리즘 - 3036
'''
링
첫째 줄에 링의 개수 N이 주어진다. (3 ≤ N ≤ 100)

다음 줄에는 링의 반지름이 상근이가 바닥에 놓은 순서대로 주어진다. 반지름은 1과 1000를 포함하는 사이의 자연수이다.


'''

import sys

def gcd(a, b) :
    while b != 0 :
        a = a % b
        a, b = b, a
    return a

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
for i in range(1, n) :
    g = gcd(a[0], a[i])
    print('{0}/{1}'.format(a[0]//g, a[i]//g))

