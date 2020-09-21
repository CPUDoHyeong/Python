# v3의 내림차순

def sel_sort(a) :
    n = len(a)
    for i in range(0, n-1) :
        max_idx = i
        for j in range(i+1, n) :
            if a[j] > a[max_idx] :
                max_idx = j
        a[i], a[max_idx] = a[max_idx], a[i]

d = [1,2,3,4,5]
sel_sort(d)
print(d)