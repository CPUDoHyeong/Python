# 파이썬 알고리즘 - 2908
'''
두개의 3자리 숫자가 주어지는데 숫자를 거꾸로 읽어서 어느 숫자가 더 큰지 출력
ex) 734 893 -> 437
'''

# a, b = input().split()
# _a = ''
# _b = ''

# for i in range(2, -1, -1) :
#     _a += a[i]
#     _b += b[i]

# if _a > _b :
#     print(_a)
# else :
#     print(_b)

# 다른방법
# 파이썬 슬리이싱을 이용한다
print(max(input()[::-1].split()))