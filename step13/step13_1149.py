# 백준 알고리즘 - 1149
'''
RGB 거리
RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 
1번 집부터 N번 집이 순서대로 있다.

집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 
각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 
아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

1번 집의 색은 2번 집의 색과 같지 않아야 한다.
N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
'''

n = int(input())
p = []
for i in range(n):
    p.append(list(map(int, input().split())))

# 결국은 앞뒤로 겹치지만 않으면 된다
# 그래서 두번째집을 시작으로 하여 두번째집의 기준 색을 정하고
# 그 색을 제외한 첫번째 집의 두 색 중 최솟값을 선택해서 
# 두번째 기준 색에 저장한다. 이런식으로 N개의 집까지 계산한 후
# 마지막 배열에 최종 값이 저장 되어있으므로 그 값의 최솟값을 출력한다.
for i in range(1, len(p)):
    p[i][0] = min(p[i - 1][1], p[i - 1][2]) + p[i][0]
    p[i][1] = min(p[i - 1][0], p[i - 1][2]) + p[i][1]
    p[i][2] = min(p[i - 1][0], p[i - 1][1]) + p[i][2]
print(min(p[n - 1][0], p[n - 1][1], p[n - 1][2]))