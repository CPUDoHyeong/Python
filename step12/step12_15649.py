# 백준 알고리즘 - 15649
'''
*****
N과 M
자연수 N과 M이 주어졌을 때,
1~N까지 자연수 중에서 중복 없이 M개를 고른 수열을 구하라
수열은 오름차순으로 출력
ex) 입력 3 1
출력 
1
2
3
'''

'''
1. 1부터 M까지 숫자 선택
2. 
'''
n, m = map(int, input().split())
 
check = [False] * (n + 1)
a = [0] * m
 
 
def go(index, n, m):
    if index == m:
        for i in range(m):
            print(a[i], end=' ')
        print()
 
        return
    for i in range(1, n + 1):
        if check[i]:
           continue
        check[i] = True
        a[index] = i
        go(index + 1, n, m)
        check[i] = False
 
 
go(0, n, m)
