# 백준 알고리즘 - 1181
'''
단어 정렬
알파벳 소문자로 이루어진 N개의 단어가 들어오면 조건에 맞추어 정렬
1. 길이가 짧은 것부터
2. 길이가 같다면 사전 순
문자열의 길이는 50을 넘지않는다.
중복 단어는 한 번만 출력한다.
'''

N = int(input())
words = []

for _ in range(N) :
    words.append(input())

words = list(set(words))    # set을 통해 중복제거
sorted_words = []           # 정렬 후 리스트

# 단어 길이와 단어를 묶어서 append
for word in words :
    sorted_words.append((len(word), word))

sorted_words.sort()         # sort는 len으로 정렬 후 word로 정렬한다.

for len_word, word in sorted_words : # 길이와 word를 가져와 word만 출력
    print(word)
