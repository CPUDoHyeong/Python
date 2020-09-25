# 재귀함수로 최대값 찾기

def findmax(a, n) :
    if n == 1 :
        return a[0]
    
    max_n = findmax(a, n-1)
    # max_n이 a[0]부터 시작된다.
    # a[0]이 리턴되면 a[0]과 a[1]을 비교하는식으로
    # 꺼꾸로 올라감
    if max_n > a[n-1] :
        return max_n
    else :
        return a[n-1]


arr = [1, 3, 10, 9, 5]
print(findmax(arr, len(arr)))