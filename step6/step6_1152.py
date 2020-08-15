# 백준 알고리즘 - 1152
'''
단어의 개수
영어 대소문자와 띄어쓰기만으로 이루어진 문자열이 주어진다.
이 문자열에 몇 개의 단어가 있는지 구하는 프로그램
중복 단어도 각각 한개로 본다.
'''

# inp = list(input())

# if inp[0] == ' ' :
#     inp.pop(0)
# if inp[len(inp)-1] == ' ' :
#     # remove는 같은게 있으면 앞에거를 먼저지운다 
#     # pop에 인수가 없으면 마지막 항목 제거함
#     # inp.remove(inp[len(inp)-1])
#     inp.pop()

# print(inp.count(' ') + 1)

# split 이용
n = input().split()
print(n)