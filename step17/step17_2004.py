# 백준 알고리즘 - 2004
'''
조합 0의 개수
nCm의 끝자리 0의 개수를 출력하는 프로그램을 작성하시오.
'''

# nCm = n!/((n-m)!*m!)
# 시간초과
# 0이 생기는 경우는 10이 만들어지는 경우
# 10은 2와 5의 곱으로 만들어짐

# 5가 몇번 나누어지는지 구함
def fiveCount(n) :
    result = 0
    while n != 0 :
        n = n // 5
        result += n
    return result

# 2가 몇번 나누어지는지 구함
def twoCount(n) :
    result = 0
    while n != 0 :
        n = n // 2
        result += n
    return result

n, m = map(int, input().split())

if m == 0 :
    print(0)
else :
    # 2와 5의 개수를 nCm을 구할 때처럼 구한 후 더 작은 개수 선택
    print(min(twoCount(n) - twoCount(m) - twoCount(n - m), fiveCount(n) - fiveCount(m) - fiveCount(n - m)))