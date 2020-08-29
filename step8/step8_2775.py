# 백준 알고리즘 - 2775
'''
부녀 회장이 될텐야
a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지
사람들의 수의 합만큼 사람들을 데려와 살아야 한다
아파트에 비어있는 집은 없고 모든 주민들이 이 계약 조건을 지키고 왔을 때
주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지 출력하라.
아파트는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.
'''

def floor_sum(k, n) :
    if k == 0 :
        return n
    result = 0
    for i in range(1, n+1) :
        result += floor_sum(k-1, i)
    return result
        

T = int(input())
for i in range(T) :
    k = int(input())
    n = int(input())
    v = [i for i in range(1, n+1)]
    for __ in range(k) :
        for j in range(1, n) :
            v[j] += v[j-1]
    print(v[-1])    



