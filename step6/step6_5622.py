# 파이썬 문제풀이 - 5622
'''
다이얼
'''

alphabet_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

num = input()
result = 0

for i in num :
    for j in alphabet_list :
        if i in j :
            result += alphabet_list.index(j) + 3

print(result)
    