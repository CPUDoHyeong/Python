# 재귀 함수를 이용한 팩토리얼 구하기

def factorial(n) :
    if n <= 1 :
        return 1

    return n * factorial(n-1)


print(factorial(5))