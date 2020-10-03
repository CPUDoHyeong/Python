# 백준 알고리즘 - 11650
'''
좌표 정렬하기
좌표를 x좌표가 증가하는 순으로,
x좌표가 같으면 y좌표가 증가하는 순으로 정렬 후 출력
'''

N = int(input())
x_y_list = []
for _ in range(N) :
    x, y = map(int, input().split())
    x_y_list.append([x, y])

# 좌표를 정렬 x좌표를 먼저 정렬 후 y좌표 정렬
x_y_list.sort()

# 출력
for i in range(N) :
    print(x_y_list[i][0], x_y_list[i][1])
