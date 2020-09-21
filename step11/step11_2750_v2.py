'''
선택 정렬 알고리즘 v2
3개중 두번째로 빠른속도 v3와 거의 차이는 없지만
v1보다는 두배 빠름.
최솟값을 찾는 함수를 하나 만들어서 배열의 최솟값 인덱스를 구하고
그 최솟값을 다른 배열에 추가하는 방식
그리고 그 최솟값의 인덱스는 기존의 배열에서 제거해준다.
'''

def find_min_idx(a) :
    n = len(a)
    min_idx = 0
    for i in range(1, n) :
        if a[i] < a[min_idx] :
            min_idx = i
    return min_idx

def sel_sort(a) :
    result = []
    while a :
        min_idx = find_min_idx(a)
        value = a.pop(min_idx)
        result.append(value)
    return result

N = int(input())
d = []
for i in range(N) :
    d.append(int(input()))

d = sel_sort(d)
for i in d :
    print(i)