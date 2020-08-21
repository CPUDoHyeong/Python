# 백준 알고리즘 - 10872
'''
팩토리얼 재귀함수
'''
def factorial(n) :
    if n <= 1 :
        return 1
    return n * factorial(n-1)

inp = int(input())
print(factorial(inp))