# 백준 알고리즘 문제 2523 - 별찍기13
inp = int(input())

for i in range(1, inp+1) :
    print('*' * i)

for i in range(inp-1, 0, -1) :
    print('*' * i)