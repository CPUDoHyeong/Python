# 백준 알고리즘 - 1002
'''
터렛
'''
# def distance(x1, y1, x2, y2) :
#     return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))

# for __ in range(T) :
#     arr = list(map(int, input().split()))
#     if arr[0] == arr[3] and arr[1] == arr[4] and arr[2] == arr[5] :
#         print(-1)
#     elif arr[0] == arr[3] and arr[2] == arr[4] :
#         print(0)
#     else :
#         dis = distance(arr[0], arr[1], arr[3], arr[4])
#         r = arr[2] + arr[5]
#         if dis > r :
#             print(0)
#         elif dis == r :
#             print(1)
#         else :
#             print(2)


T = int(input())
for __ in range(T) :
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    # 두 점 사이의 거리
    d = ((x1-x2)**2 + (y1-y2)**2)**0.5
    # 반지름의 합
    rs = r1 + r2
    # 반지름의 차
    rm = abs(r1 - r2)
    # 두 점 사이의 거리가 0일 때
    if d == 0 :
        # 반지름이 같다면 두 원은 일치
        if r1 == r2 :
            print(-1)
        # 그렇지 않으면 만나지 않는다
        else :
            print(0)
    else :
        # 두점 사이의 거리가 각 반지름의 합과 차이가 같다면 접점은 1개
        # 차이를 계산하는 이유는 원안에 원이 존재하는 경우를 생각한 것임
        if d == rs or d == rm :
            print(1)
        # 접점이 두개
        elif d < rs and d > rm :
            print(2)
        # 겹치지 않음(접점이 없음)
        else :
            print(0)




