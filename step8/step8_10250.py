# 백준 알고리즘 - 10250
'''
ACM 호텔
'''

T = int(input())
for __ in range(T) :
    H, W, N = map(int, input().split())

    # 층은 N을 H로 나눈 것과 같다
    # 101호부터 층수대로 배정하는 것이기 때문에
    floor = N % H

    # 호수는 층수로 나눈 나머지 +1과 같은데
    # 만약 나누어떨어질 경우는 00층으로 나오기 때문에
    # 호수를 하나 빼고 층수는 입력된 H층으로 하면된다.
    room = (N // H) + 1
    if floor == 0 :
        room -= 1
        floor = H
    print(floor * 100 + room)