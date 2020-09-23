# 백준 알고리즘 - 10989
'''
수 정렬하기 3
0으로 초기화된 배열을 미리 지정해주고
거기에 값을 계속 더한다.
반복문으로 값이 있다면 출력해주면된다.
'''

import sys

N = int(sys.stdin.readline())
d = [0] * 10001
for i in range(N) :
    d[int(sys.stdin.readline())] += 1
for i in range(10001) :
    if d[i] != 0 :
        for j in range(d[i]) :
            print(i)