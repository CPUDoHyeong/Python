# 이분 탐색

# a는 리스트, x는 찾는 값
# return은 찾는 값의 위치, 없으면 -1
def binary_search(a, x) : 
    start = 0
    end = len(a) - 1
    while start <= end :
        mid = (start + end) // 2
        if x == a[mid] :
            return mid
        elif x > a[mid] :
            start = mid + 1
        else :
            end = mid - 1

    return -1


# 재귀함수 사용
def binary_search_v2(a, x, start, end) :
    if start > end :
        return -1

    mid = (start + end) // 2
    if x == a[mid] :
        return mid
    elif x > a[mid] :
        return binary_search_v2(a, x, mid + 1, end)
    else :
        return binary_search_v2(a, x, start, mid - 1)

    return -1

d = [1,2,3,4,5,6,7,8,9,10]
result = binary_search_v2(d, 11, 0, len(d)-1)

print('result is', result)