# 백준 알고리즘 - 3009
'''
네 번째 점
세 점이 주어졌을 때 축에 평행한 직사각형을 만들기 위해서 필요한 네번째점
구하는 프로그램
세점의 좌표가 한 줄에 하나 씩
1보다 크거나 같고 1000보다 작거나 같은 정수
'''

x_list = []
y_list = []
result_x = 0
result_y = 0
for i in range(3) :
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

# count를 통해서 하나의 값만 있는 것을 저장하고 출력
for i in range(3) :
    if x_list.count(x_list[i]) == 1 :
        result_x = x_list[i]
    if y_list.count(y_list[i]) == 1 :
        result_y = y_list[i]

print(result_x, result_y)
        

