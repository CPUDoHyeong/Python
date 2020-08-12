# 백준 알고리즘 - 10809
'''
알파벳 소문자로만 이루어진 단어 S 가 주어짐
각각의 알파벳에 대해서 a가 처음 등장하는 위치, b가 처음 등장하는 위치
.... z가 처음 등장하는 위치를 공백으로 구분해서 출력
포함되어 있지 않을 경우 -1 단어의 첫번째를 0번으로 한다.
ex) baekjoon
-> 1 0 -1 -1 2 -1 -1 ....... -1
'''

inp_str = input()
str_list = [-1] * 26    # 첫 자리를 나타낼 list로 -1로 초기화
count = 0

for i in inp_str :
    idx = ord(i)-97
    if str_list[idx] == -1 :
        str_list[ord(i)-97] = count
    count += 1

for i in str_list :
    print(i, end=' ')