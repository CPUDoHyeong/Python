# 백준 알고리즘 - 11021
'''
A+B - 7
'''

loop = int(input())
for i in range(loop) :
    num1, num2 = map(int, input().split())
    print('Case #', (i+1) , ': ' , (num1+num2), sep='')