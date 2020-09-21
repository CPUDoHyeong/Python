# 백준 알고리즘
'''
수 정렬하기
N개의 수가 주어졌을 때, 오름차순으로 정렬하시오
'''

N = int(input())
arr = []

for i in range(N) :
    num = int(input())
    arr.append(num)

temp = 0
for i in range(1, N) :
    while (i>0) and (arr[i] < arr[i-1]) :
        arr[i], arr[i-1] = arr[i-1], arr[i]

        i -= 1

for i in arr :
    print(i)
        