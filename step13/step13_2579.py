# 백준 알고리즘 - 2579
'''
계단 오르기
계단 오르는 데는 다음과 같은 규칙이 있다.
계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 
즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
마지막 도착 계단은 반드시 밟아야 한다.
각 계단에 쓰여 있는 점수가 주어질 때 이 게임에서 얻을 수 있는 총 점수의 최댓값
'''

'''
3층까지의 최대값은 구하기 쉽다.
4층부터는 연속된 계산을 생각해서 계산하기 보다는 전에 어떤 계단을 밟았는 가를 생각한다.
첫째. 한칸 전 계단을 밟고 올라 온 경우 -> 이전 계단은 그 전전의(n-3) 계단이 된다.
둘째. 두칸 전 계단을 밟고 올라 온 경우
첫째의 식 -> dp[i] = dp[i-2] + dp[i]
둘째의 식 -> dp[i] = dp[i-3] + dp[i-1] + dp[i]
'''
import sys
input = sys.stdin.readline

N = int(input())
dp = [0 for _ in range(N+3)]
arr = [0 for _ in range(N+3)]
for k in range(1,N+1):
    arr[k] = int(input())

dp [1] = arr[1]
dp [2] = arr[1] + arr[2]
dp [3] = max(arr[1] + arr[3] ,arr[2] + arr[3])

for i in range(4, N+1):
    dp[i] = max( dp[i-3] + arr[i-1] + arr[i] ,  dp[i-2] + arr[i] ) 
print(dp[N])
