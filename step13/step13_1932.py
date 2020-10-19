# 백준 알고리즘 - 1932
'''
정수 삼각형
맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 
이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라.
아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 
중에서만 선택할 수 있다.
'''

n = int(input())
save = []

'''
풀이
2번째줄부터 위에거를 더하면서 내려와 본인 자리에 위에 값을 더하여 저장한다.
가장 앞자리와 가장 마지막자리는 계속 위 층의 앞자리, 마지막 자리를 더하면된다.
가운데 자리인 경우는 위의 두 자리에서 큰 값을 골라 본인 자리의 값을 더하여 저장한다.
[7]
[10, 15]
[18, max([10][15] + 1, 15]
...
'''
for _ in range(n) :
    inp_list = list(map(int, input().split()))
    save.append(inp_list)


for i in range(1, n) :
    for j in range(len(save[i])) :
        if j == 0 : # 처음 자리
            save[i][j] += (save[i-1][j])
        elif j == i : # 마지막 자리
            save[i][j] += (save[i-1][j-1])
        else : # 가운데 자리
            save[i][j] += (max(save[i-1][j-1], save[i-1][j]))

print(max(save[n-1]))