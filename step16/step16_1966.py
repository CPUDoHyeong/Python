# 백준 알고리즘 - 1966
'''
프린터 큐
현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.
'''

import sys

t = int(sys.stdin.readline())

for _ in range(t) :
    n, m = map(int, sys.stdin.readline().split())
    # 중요도 리스트
    k = list(map(int, sys.stdin.readline().split()))
    # 0으로 된 배열에
    k_ = [0 for i in range(n)]
    # 몇번째 출력인지 알고자 하는 원소를 1로 바꿔준다.
    k_[m] = 1
    # 높은 순위가 출력될때마다 1씩 더할 카운트
    cnt = 0
    while True :
        # 중요도 리스트의 0번 인덱스가 중요도에서 가장 큰 원소라면
        if k[0] == max(k) :
            # 출력해야하므로 1더하고
            cnt += 1
            # 우리가 찾고자 하는 원소인지 확인
            # 맞다면 출력하고 바로 종료
            if k_[0] == 1 :
                print(cnt)
                break
            # 그렇지 않다면 배열에서 삭제
            else :
                del k[0]
                del k_[0]
        # 가장 큰 원소가 아니라면 맨뒤로 보내준다. 중요도도 같이
        else :
            k.append(k[0])
            del k[0]
            k_.append(k_[0])
            del k_[0]
