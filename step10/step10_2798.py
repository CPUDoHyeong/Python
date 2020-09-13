# 백준 알고리즘 - 2798
'''
블랙잭
N은 카드 개수, M은 3장의 합
그리고 카드의 숫자가 주어 질 때
3장의 합이 M을 초과하지 않을 때 가장 가까운 카드 3장의 합을 출력
'''

n, m = map(int, input().split())
a = list(map(int, input().split()))
result = 0

# 다중 for문을 사용한다
for i in range(n) :
    for j in range(i+1, n) :
        # 마지막 for문은 위의 숫자보다 뒤차례 순서부터 마지막 순서까지
        # 하나씩 확인해간다.
        for k in range(j+1, n) :
            if a[i] + a[j] + a[k] > m :
                continue
            else :
                result = max(result, a[i] + a[j] + a[k])

print(result)
