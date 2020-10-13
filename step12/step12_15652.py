# 백준 알고리즘 - 15652
'''
N과 M(4)
1부터 N까지 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
고른 수열은 비내림차순이어야 한다.
길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.
'''

N, M = map(int, input().split())

num_list = [i + 1 for i in range(N)]
check_list = [False] * N

arr = []

def dfs(cnt):
    if(cnt == M):
        print(*arr)
        return
    
    for i in range(0, N):
        if(check_list[i]):
            continue
            
        arr.append(num_list[i])
        dfs(cnt + 1)
        check_list[i] = True
        arr.pop()
        
        for j in range(i + 1, N):
            check_list[j] = False
        
dfs(0)