# 백준 알고리즘 - 2751
'''
수 정렬하기2
파이썬의 sroted 이용-> O(nlog(n))이기 때문에.
그리고 sys를 이용해서 더빠른 입력 출력 가능
'''

import sys
n = int(input())
arr = []
for i in range(n) :
    arr.append(int(sys.stdin.readline()))
for i in sorted(arr) :
    sys.stdout.write(str(i)+'\n')