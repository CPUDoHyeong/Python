# 백준 알고리즘 - 2588
'''
곱셈
'''

num1 = int(input())
num2 = int(input())

a = num1 * (num2%10)
b = num1 * ((num2//10)%10)
c = num1 * (num2//100)
d = num1 * num2

print(a, b, c, d, sep='\n')