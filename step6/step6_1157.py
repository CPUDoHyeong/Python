# 백준 알고리즘 - 1157
'''
단어 공부
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된
알파벳이 무엇인지 알아내는 프로그램
대문자와 소문자를 구분하지 않는다.
첫째줄에 단어주어짐 -> 가장 많이 사용된 알파벳 출력
'''

inp_str = str(input()).upper()

al_list = [0] * 26

for i in inp_str :
    al_list[ord(i)-65] += 1

if al_list.count(max(al_list)) >= 2 :
    print('?')
else :
    print(chr(al_list.index(max(al_list)) + 65))


# 다른 방법
words = input().upper()
word_list = list(set(words)) # 먼저 set을 통해 중복 제거 후 리스트로
word_count = list()          # 각 알파벳의 카운트 리스트

for i in word_list :
    count = words.count(i)   # 기존의 단어에서 알파벳이 몇번 들어갔는지 카운트
    word_count.append(count) # 카운트 리스트에 더함

if word_count.count(max(word_count)) >= 2 :
    print('?')
else :
    print(word_list[word_count.index(max(word_count))])

