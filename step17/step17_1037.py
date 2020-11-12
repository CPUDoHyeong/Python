# 백준 알고리즘
'''
약수
'''

# 가장 작은 값과 가장 큰 값을 곱하여 출력
n = int(input())
a = list(map(int, input().split()))
a_max = max(a)
a_min = min(a)
print(a_max * a_min)