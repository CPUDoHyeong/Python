# 백준 알고리즘 - 1874
'''
'''
n = int(input())
s = []
op = []
count = 1 # count와 입력값을 비교하기 위해
temp = True
for i in range(n):
    num = int(input())
    # 입력값이 카운트와 같아 질때 까지 + 반복
    # 입력값이 append 되어야 그 값을 pop할 수 있기 때문에
    while count <= num:
        s.append(count)
        op.append('+')
        count += 1

    # 마지막 값이 입력값과 같다면 pop을 해주고 -추가
    if s[-1] == num:
        s.pop()
        op.append('-')
    # 마지막값이 입력값과 다르다는 것은 그 앞의 수를 입력 했다는 것임
    # 예를 들어 3을 입력했을 때 마지막 index 값이 4라면 3을 뺄 수가 없음.
    else:
        temp = False
if temp == False:
    print('NO')
else:
    for i in op:
        print(i)