# 백준 알고리즘 - 9020
'''
골드바흐의 추측
2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다.
그리고, 그 소수 2개를 골드바흐 파티션이라고 한다.
2보다 큰 짝수가 주어졌을 때 골드바흐 파티션을 구하라.
단, 두 수의 차가 최소인 것을 먼저 구하고, 작은 값부터 출력한다.
'''

# 먼저 10000 보다 작은 소수를 구한다.
N = 10000+1
flag_list = [True] * N
for i in range(2, int(N**0.5) + 1) :
    if flag_list[i] :
        for j in range(i*2, N, i) :
            flag_list[j] = False     

T = int(input())
for __ in range(T) :
    n = int(input())
    x = n // 2
    y = n - x
    while True :
        # 2를 나눈 몫이 소수면 바로 통과
        # 2를 나눈 몫이 짝수면 그 몫에 1을 빼고 확인 그리고 계속 반복.
        if flag_list[x] and flag_list[y] :
            print(x, y)
            break
        x -= 1
        y += 1