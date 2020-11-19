# 백준 알고리즘 - 1676
'''
팩토리얼 0의 개수
N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.
'''

from math import factorial

n = factorial(int(input()))
count = 0
while n%10 == 0 :
    n = n // 10
    count += 1
print(count)