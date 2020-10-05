# 파이썬 알고리즘 - 2108
'''
통계학
정수 N개가 주어졌을 때(N은 홀수)
첫쨰줄에 산술평균 - N개의 수들의 합을 N으로 나눈 값(소수 첫째 자리에서 반올림)
둘째줄에 중앙값 - N개의 수들을 증가하는 순서로 나열, 그 중앙에 있는 값
셋째줄에 최빈값 - N개의 수들 중 가장 많이 나타나는 값
넷째줄에 범위 출력 - N개의 수들 중 최댓값과 최솟값의 차이
최빈값의 경우 여러개 있을 때에는 두번째로 작은 값을 출력
'''

import sys

# 중복 값을 찾아 딕셔너리로 반환
def find_same_num(a) :
    num_dict = {}
    for num in a :
        if num in num_dict :
            num_dict[num] += 1
        else :
            num_dict[num] = 1
    
    return num_dict

N = int(sys.stdin.readline())
num_list = []

for _ in range(N) :
    n = int(sys.stdin.readline())
    num_list.append(n)

num_list.sort()
num_dict = find_same_num(num_list)
# 정렬
num_dict = sorted(num_dict.items(), key=lambda x: (-x[1], x[0]))

# 평균 출력
print(round(sum(num_list)/N))
# 중앙값 출력
print(num_list[N//2])
# 최빈값 출력
# 정렬한 딕셔너리의 첫번째 값과 두번째 값이 같다면 최빈값이 여러개 있으므로
# 두번째 것을 출력 최빈값이 하나라면 가장 앞에 것 출력
if len(num_dict) > 1 :
    if num_dict[0][1] == num_dict[1][1] :
        print(num_dict[1][0])
    else :
        print(num_dict[0][0])
else :
    print(num_dict[0][0])

# 범위 출력
print(num_list[-1] - num_list[0])




