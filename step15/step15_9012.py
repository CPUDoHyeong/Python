# 백준 알고리즘 - 9012

'''
괄호
'''

import sys
T = int(sys.stdin.readline())
left = '('
right = ')'

for _ in range(T) :
    inp = input()
    sum = 0
    for i in inp :
        if i == left :
            sum += 1
        elif i == right :
            sum -= 1
        
        if sum < 0 :
            print('NO')
            break
    
    if sum > 0 :
        print('NO')
    elif sum == 0 :
        print('YES')