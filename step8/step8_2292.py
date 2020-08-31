# 백준 알고리즘 - 2292
'''
벌집
'''

N = int(input())
cnt = 1
while N > 1 :
    N -= (6 * cnt)
    cnt += 1
print(cnt)

# 재귀 함수 이용
import sys
sys.setrecursionlimit(10**5)
N = int(input())
def bee_house(N, cnt) :
    if N <= 1 :
        print(cnt)
        return
    else :
        bee_house(N-(6*cnt), cnt+1)

bee_house(N, 1)