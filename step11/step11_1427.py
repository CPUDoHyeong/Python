# 백준 알고리즘 - 1427
'''
소트인사이드
내림차순으로 정렬
'''

def sel_sort(a) :
    n = len(a)
    for i in range(0, n-1) :
        max_idx = i
        for j in range(i+1, n) :
            if a[j] > a[max_idx] :
                max_idx = j
        a[i], a[max_idx] = a[max_idx], a[i]

N = input()
a = []
a = list(map(int, N))
sel_sort(a)
for i in a :
    print(i, end='')


