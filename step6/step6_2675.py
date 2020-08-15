# 백준 알고리즘 - 2675
'''
문자열 반복
문자열 S를 입력 반은 후에 
각 문자를 R 번 박복해 새 문자열 P를 만들어 출력하는 프로그램
ex)
3 ABC -> AAABBBCCC
5 /HTP -> /////HHHHHTTTTTPPPPP
'''
loop = int(input())

for i in range(loop) :
    
    count, word = input().split()
    result = ''
    for j in word :
        result += j * int(count)
    print(result)