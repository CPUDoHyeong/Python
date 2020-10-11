# 백준 알고리즘 - 15651
'''
N과 M(3)
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 
모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
'''

def f(n,m,k):
    if(n == k):
        print(*res)
        return
    else:
        for i in range(m):
            visited[i] = 1
            res[n] = arr[i]
            f(n+1,m,k)
            visited[i] = 0


n, m = map(int, input().split())
arr = range(1,n+1)
visited = [0 for i in range(n)]
res = [0] * m
f(0,n,m)