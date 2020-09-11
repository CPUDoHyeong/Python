# 백준 알고리즘 - 3053
'''
택시 기하학
택시 기하학 두점 사이의 거리
D(T1, T2) = |x1-x2| + |y1-y2|
반지름이 주어졌을 때 유클리드 기하학에서 원의 넓이와
택시 기하학에서 원의 넓이를 구하라
첫째 줄에는 유클리드, 둘째 줄에는 택시 기하학의 원의 넓이
'''

import math
R = int(input())
# 원의 넓이
print(math.pi * R**2)
# 마름모 넓이
print(R**2*2)