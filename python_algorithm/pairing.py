# n명 중 두 명을 뽑아 짝을 지을 때 모든 조합을 출력하시오


def pairing(a) :
    n = len(a)
    for i in range(0, n-1) :
        for j in range(i+1, n) :
            print(a[i], '-', a[j])


arr = ['Tom', 'Jerry', 'Mike', 'Kim']
pairing(arr)