# 백준 알고리즘 - 11729
'''
하노이탑
'''

def hanoi(n, a, b, c) :
    if n > 0 :
        hanoi(n-1, a, c, b)
        print(a, c)
        hanoi(n-1, b, a, c)

inp = int(input())
print((2**inp)-1)
hanoi(inp, 1, 2, 3)
