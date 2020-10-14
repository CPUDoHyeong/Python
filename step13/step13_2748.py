# 백준 알고리즘 - 2748
'''
피보나치 수2
n이 주어졌을 때 n번째 피보나치수를 구하는 프로그램 작성
'''

# 재귀를 이용할 시에는 시간 초과가 발생
def fibonacci(n) :
    if n <= 1 :
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 딕셔너리를 통해 해당 피보나치수를 기록하는 방법을 사용한다.
# 기본 메모에 0과 1을 주고 2일 경우, 3일 경우.... 
# memo에 차례로 더해나가서 기존의 피보나치 재귀함수의 중복을 막아준다.
def fibonacci2(n, memo) :
    if n in memo :
        return memo[n]
    memo[n] = fibonacci2(n-1, memo) + fibonacci2(n-2, memo)
    return memo[n]

N = int(input())
memo = {0:0, 1:1}

print(fibonacci2(N, memo))