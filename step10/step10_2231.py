# 백준 알고리즘 - 2231
'''
분해합
자연수 N에서 분해합이란 N과 N의 각 자리수의 합을 의미
자연수 M의 분해합이 N인 경우 M을 생성자라고 함.
자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해라
생성자가 없는 경우 0 출력
'''

# 시간 1936ms
# 이중 for문의 영향과 not in, index 찾기 등으로 효율적인 코드는 아닌 듯
N = int(input())
num_list = []
for i in range(1, N+1) :
    for j in str(i) :
        i += int(j)
    num_list.append(i)
if N not in num_list :
    print(0)
else :
    print(num_list.index(N) + 1)

# 수정
# 시간 1572ms
num = int(input())
result = 0
for i in range(1, num+1) :
    arr = list(map(int, str(i)))
    result = i + sum(arr)

    if result == num :
        print(i)
        break
    # 같아지면 값이 없다는 것이므로
    if i == num :
        print(0)

