# 백준 알고리즘 - 1978
'''
소수 찾기
주어진 수 N개 중에서 소수가 몇 개인지 출력하시오
'''

N = int(input())
num_list = []
num_list = list(map(int, input().split()))
result = 0

for i in num_list :
    # 먼저 1부터 시작하여 i를 2로나눈 몫까지의 리스트를 만든다.
    # i가 10이라면 list는 [1, 2, 3, 4, 5]가 된다.
    # 어차피 1/2 이 넘어가면 계산할 의미가 없어진다.
    test_list = [i for i in range(1, i//2 + 1)]
    cnt = 0
    # test_list에서 하나씩 꺼내와서 i를 나눴을 때 나머지가 0인게
    # 한개만 있을 때 소수이다.
    for j in test_list :
        if i % j == 0 :
            cnt += 1
    if cnt == 1 :
        result += 1

print(result)

    