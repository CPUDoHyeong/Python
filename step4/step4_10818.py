# 백준 알고리즘 - 10818
# 배열 최소, 최대 값 구하기

leng = int(input())

arr = list(map(int, input().split()))
max_num = arr[0]
min_num = arr[0]

for i in range(1, len(arr)) :
    if arr[i] > max_num :
        max_num = arr[i]
    if arr[i] < min_num :
        min_num = arr[i]

print(min_num, max_num)

# 다른 방법
# min, max 함수를 이용
# print('{} {}'.format(min(arr), max(arr)))