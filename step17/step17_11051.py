# 백준 알고리즘 - 11051
'''
이항계수 2
'''

from math import factorial

a,b=map(int,input().split())
print((factorial(a)//(factorial(b)*factorial(a-b)))%10007)