# 백준 알고리즘 - 4153
'''
직각삼각형
3변이 주어졌을 때 직각삼각형인지 아닌지 출력
'''

while True :
    arr = list(map(int, input().split()))
    if sum(arr) == 0 :
        break
    max_num = max(arr)
    arr.remove(max_num)
    if arr[0] ** 2 + arr[1] ** 2 == max_num ** 2 :
        print('right')
    else :
        print('wrong')

    