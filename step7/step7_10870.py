# 백준 알고리즘 - 10870
'''
파보나치 수
'''
def pabona(n) :
    if n <= 1 :
        return n
    return pabona(n-1) + pabona(n-2)

inp = int(input())
print(pabona(inp))