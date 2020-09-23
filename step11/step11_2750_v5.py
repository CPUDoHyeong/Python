# 병합정렬
# 재귀함수를 이용한 정렬


# 104ms
def merge_sort(a) :
    n = len(a)
    if n <= 1 :
        return a
    mid = n // 2
    g1 = merge_sort(a[:mid])
    g2 = merge_sort(a[mid:])

    result = []
    while g1 and g2 :
        if g1[0] < g2[0] :
            result.append(g1.pop(0))
        else :
            result.append(g2.pop(0))

    while g1 :
        result.append(g1.pop(0))
    while g2 :
        result.append(g2.pop(0))
    return result

# 108ms
def merge_sort_v2(a) :
    n = len(a)
    if n <= 1 :
        return
    mid = n // 2
    g1 = a[:mid]
    g2 = a[mid:]
    merge_sort_v2(g1)
    merge_sort_v2(g2)

    i1 = 0
    i2 = 0
    ia = 0
    while i1 < len(g1) and i2 < len(g2) :
        if g1[i1] < g2[i2] :
            a[ia] = g1[i1]
            i1 += 1
            ia += 1
        else :
            a[ia] = g2[i2]
            i2 += 1
            ia += 1
        
    while i1 < len(g1) :
        a[ia] = g1[i1]
        i1 += 1
        ia += 1
    while i2 < len(g2) :
        a[ia] = g2[i2]
        i2 += 1
        ia += 1

N = int(input())
d = []
for i in range(N) :
    d.append(int(input()))
d = merge_sort(d)

for i in d :
    print(i)