# 백준 알고리즘 - 11050
'''
이항 계수 1
'''

from math import factorial
n, k = map(int, input().split())
b = factorial(n) // (factorial(k) * factorial(n-k))
print(b)