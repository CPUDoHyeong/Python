# 재귀를 이용한 sum

def sum_recursion(n) :
    if n <= 1 :
        return 1
    
    return n + sum_recursion(n-1)

print(sum_recursion(100))