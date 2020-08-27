# 백준 알고리즘 - 1712
'''
손익 분기점
'''

a, b, c = map(int, input().split())

if c <= b :
    print(-1)
else :
    print(a // (c-b) + 1)
