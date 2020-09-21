'''
선택 정렬 알고리즘 v3
3개중 가장 빠른 속도.
첫번째 인덱스와 두번째 부터 마지막 인덱스까지를 비교해가며
최솟값을 찾고 첫번째 인덱스 값과 최솟값을 바꾸는 식으로 진행.
'''

def sel_sort(a) :
    n = len(a)
    for i in range(0, n - 1) :
        min_idx = i
        for j in range(i + 1, n) :
            if a[j] < a[min_idx] :
                min_idx = j    
        a[i], a[min_idx] = a[min_idx], a[i]

d = []
N = int(input())
for i in range(N) :
    d.append(int(input()))
sel_sort(d)

for i in d :
    print(i)