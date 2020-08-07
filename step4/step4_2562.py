# 백준 알고리즘 - 2562
'''
9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고
그 최댓값이 몇 번째 수인지를 구하는 프로그램
'''

count = 9
max_num = 0
result = 0
for i in range(count) :
    num = int(input())
    if max_num < num :
        max_num = num
        result = i + 1

print(max_num)
print(result)