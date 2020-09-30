# 백준 알고리즘 - 10814
'''
나이순 정렬
나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에
오도록 정렬.
'''

N = int(input())
age_name_list = []
for _ in range(N) :
    age, name = input().split()
    age_name_list.append([int(age), name])

# 람다 이용
age_name_list.sort(key=lambda x: x[0])

# 2차원 배열이므로 2차원배열 출력
for i in range(N) :
    print(age_name_list[i][0], age_name_list[i][1])


