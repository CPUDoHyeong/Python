# 백준 알고리즘 - 15552
'''
빠른 A + B
'''
import sys
input = sys.stdin.readline

inp = int(input())
for i in range(inp) :
    a, b = map(int, input().split())
    print(a + b)
