# 백준 알고리즘 - 7568
'''
덩치
자신보다 키와 몸무게가 많은 사람은 덩치가 큰걸로 간주한다.
하지만, 키와 몸무게 중 하나만 크다면 그 둘은 덩치 크기를 정할 수 없다.
전체 사람의 수 N이 주어지고, 그 사람에 대한 키와 몸무게가 주어질 때
덩치 등수를 구해서 그 순서대로 출력해라
'''

N = int(input())
h_list = []
w_list = []
class_list = [1] * N
for __ in range(N) :
    h, w = map(int, input().split())
    h_list.append(h)
    w_list.append(w)

for i in range(N) :
    x = h_list[i]
    y = w_list[i]
    for j in range(N) :
        if i == j : continue
        p = h_list[j]
        q = w_list[j]
        if x < p and y < q :
            class_list[i] += 1

for i in class_list :
    print(i, end=' ')


num_student = int(input())
student_list = []

for _ in range(num_student) :
    h, w = map(int, input().split())
    student_list.append((h, w))

for i in student_list :
    rank = 1
    for j in student_list :
        if i[0] < j[0] and i[1] < j[1] :
            rank += 1
    print(rank, end=' ')