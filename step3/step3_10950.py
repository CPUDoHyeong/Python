# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성
# 첫째 줄에 테스트 케이스의 개수 T
# 각 테스트 케이스는 한줄로 이루어져있으며, 각 줄에 A와 B가 주어진다.
count = int(input())
for i in range(count) :
    A, B = map(int, input().split())
    print(A + B)
