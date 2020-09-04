# 백준 알고리즘 - 2581
'''
자연수 M과 N이 주어지면
M이상 N이하의 자연수 중 소수를 골라 그 합과 최솟값을 출력
소수가 없을 경우 -1출력
'''

M = int(input())
N = int(input())
num_list = []
for i in range(M, N+1) :
    ctn = 0
    for j in range(1, i//2+1) :
        if i % j == 0 :
            ctn += 1
            if ctn > 1 :
                break
    if ctn == 1 :
        num_list.append(i)

if len(num_list) == 0 :
    print(-1)
else :
    print(sum(num_list))
    print(num_list[0])
