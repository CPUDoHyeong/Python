# 백준 알고리즘 - 1003
'''
피보나치 함수
N이 주어졌을 때, fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 
구하는 프로그램을 작성하시오.
'''

import sys

# def fib(n, memo) :
#     if n <= 1 :
#         memo[n] += 1
#         return n
#     return fib(n-1, memo) + fib(n-2, memo)
    
# T = int(sys.stdin.readline())
# memo = {0:0, 1:0}

# for _ in range(T) :
#     N = int(sys.stdin.readline())
#     fib(N, memo)
#     print(memo[0], memo[1])

# 미리 0과 1의 피보나치 수를 구한다 n은 40까지라 했음으로
# 그리고 0과 1도 피보나치의 수에 의해 더해진다.
# ex) 0호출 : 1, 0, 1, 1, 2, 3, 5, 8, 13 ...
# ex) 1호출 : 0, 1, 1, 2, 3, 5, 8, 13, 21 ...
def count_fibonacci(n):
    zero_count = [1,0]
    one_count = [0,1]
    if n <= 1:
        return
 
    for i in range(2, n+1):
        zero_count.append(zero_count[i-1] + zero_count[i-2])
        one_count.append(one_count[i-1] + one_count[i-2])
 
    return zero_count, one_count
 
n = int(input())
zero_count, one_count = count_fibonacci(40)
 
for _ in range(n):
    m = int(input())
    print("%d %d" % (zero_count[m], one_count[m]))