# 백준 알고리즘
'''
최대공약수와 최소공배수
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
'''

import sys

# 유클리드 호제법으로 최대공약수 구하기
def gcd(x, y) :
    while y != 0 :
        x = x % y
        x, y = y, x
    return x

def lcm(x, y) :
    return x * y // gcd(x,y)

a, b = map(int, sys.stdin.readline().split())
print(gcd(a, b))
print(lcm(a, b))

