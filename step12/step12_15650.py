# 백준 알고리즘 - 15650
'''
N과 M(2)
'''

N, M = map(int, input().split())
visited = [False] * N
out = []

def solve(depth, idx, N, M):
    if depth == M:
        print(' '.join(map(str, out)))
        return
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            out.append(i+1)
            solve(depth+1, i+1, N, M)
            visited[i] = False
            out.pop()
solve(0, 0, N, M)