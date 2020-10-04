# 백준 알고리즘 - 11651
'''
좌표 정렬하기
'''
import sys # 입력 속도 줄이기 위해서 sys 사용
N = int(sys.stdin.readline())
xyList = []

for _ in range(N) :
    x, y = map(int, sys.stdin.readline().split())
    xyList.append([y, x])

xyList.sort()

# 출력 반대로
for i in range(N) :
    print(xyList[i][1], xyList[i][0])