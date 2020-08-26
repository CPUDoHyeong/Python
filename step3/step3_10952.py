# 백준 알고리즘 - 10952
'''
A+B
while 문 이용
'''
while True :
    num1, num2 = map(int, input().split())
    if num1 == 0 and num2 == 0 :
        break
    print(num1 + num2)