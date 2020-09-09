# 백준 알고리즘 - 4948
'''
베르트랑 공준
n이 주어졌을 때
n보다 크고 2n보다 작거나 같은 소수의 개수를 구하라
'''
# import math

# def isSosu(num) :
#     if num == 1 :
#         return False
#     # n = int(num**0.5)
#     n = int(math.sqrt(num))
#     for i in range(2, n+1) :
#         if num % i == 0 : return False
#     return True

# N = 123456
# li = list(range(2, N*2))
# sosu_li = []
# for i in li :
#     if isSosu(i) :
#         sosu_li.append(i)

# while True :
#     n = int(input())
#     if n == 0 : break

#     cnt = 0
#     # 여기서 sosu_li만큼 반복이 계속 일어남.. 효율적이지 않음
#     for i in sosu_li :
#         if n < i <= n*2 :
#             cnt += 1
#     print(cnt)

# 다른 방법
N = 123456 * 2 + 1
flag_list = [True] * N
# 2부터 N까지의 소수를 구하는데 제곱근까지만 구해주고
for i in range(2, int(N**0.5) + 1) :
    if flag_list[i] :
        # i값의 배수는 전부 소수가 아니므로 False
        # 시작값이 *2 인 이유는 i는 소수일 수가 잇지만
        # i*2는 소수가 나올리가 없기 때문.
        for j in range(i*2, N, i) :
            flag_list[j] = False

def flag(num) :
    cnt = 0
    # 입력된 값이 flag_list에 True 인지 False인지 판별
    for i in range(num+1 , num*2+1) :
        if flag_list[i] : 
            cnt += 1
    print(cnt)

while True :
    n = int(input())
    if n == 0 : break
    flag(n)




