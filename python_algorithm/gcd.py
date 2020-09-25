
# 최대 공약수 일반 알고리즘
def gcd(a, b) :
    i = min(a, b) # 최솟값
    while True :
        if a % i == 0 and b % i == 0 :
            return i
        # i 값을 1씩 감소시키면서 a, b둘다 나누어지는지 확인
        i -= 1 

# 유클리드 알고리즘을 이용한 재귀함수
def gcd_recursion(a, b) :
    print(a, b)
    if b == 0 :
        return a

    return gcd_recursion(b, a%b)

print(gcd_recursion(1, 5))
print(gcd_recursion(12, 15))