# 백준 알고리즘 - 11720
'''
숫자의 합
N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램
ex)
5
54321
15
'''

count = int(input())
result = 0
inp = input()
for i in inp :
    result += int(i)


print(result)