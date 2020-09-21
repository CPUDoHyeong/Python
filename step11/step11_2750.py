# 백준 알고리즘
'''
수 정렬하기
N개의 수가 주어졌을 때, 오름차순으로 정렬하시오
while문을 이용한 방법
[5,4,3,2,1]의 배열이 있다면
5를 4와 바꾸는게 처음 -> [4, 5, 3, 2, 1]
3을 가지고 5를 비교 한 후 자리 바꾸고 다시 3과 4를 비교하여
자리를 바꾸는 게 두번째 -> [3, 4, 5, 2, 1]
이런식으로 while문의 i를 빼가면서 확인한다.
'''

N = int(input())
arr = []

for i in range(N) :
    num = int(input())
    arr.append(num)

for i in range(1, N) :
    while (i>0) and (arr[i] < arr[i-1]) :
        arr[i], arr[i-1] = arr[i-1], arr[i]
        i -= 1

for i in arr :
    print(i)
        