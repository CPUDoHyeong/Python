# 백준 알고리즘 - 2577
'''
자연수 3개가 주어지고 3개를 곱한 값에
0붜 9까지 숫자가 각각 몇개씩 있는지 한줄씩 출력하는 프로그램
'''

multi = 1

for i in range(3) :
    multi = multi * int(input())

multi_arr = list(map(int, str(multi)))
# print(multi_arr)
# 생성 및 0으로 초기화
count_arr = [0] * 10

# i는 1부터 증가하는것이 아니라 리스트의 값이 된다.
for i in multi_arr :
    count_arr[i] += 1

for i in count_arr :
    print(i)