# 백준 알고리즘 - 2839
'''
설탕 배달
설탕공장에서 만드는 설탕은 3킬로 봉지와 5킬로 봉지가 있다
상근이는 적은 봉지를 들고간다
18 kg -> 5kg 3개 3kg 한개가 최소
설탕의 kg가 주어질 때 최소한으로 가져가는 봉지의 개수를 구하시오
정확하게 나누어 떨어지지 않는 경우 -1 출력
'''

sugar = int(input())
count = 0
x = sugar // 5
# 가장 적은 개수
if sugar % 5 == 0 :
    # 가장 최소
    count = sugar // 5
else :
    # 나누어 떨어지지 않는 경우
    # 5로 나누고 안되면 5를 하나씩 빼가면서 비교하기
    while x > -1 :
        y = sugar - (5 * x)
        if y % 3 == 0 :
            count = x + (y // 3)
            break
        x -= 1

if count != 0 :
    print(count)
else :
    print(-1)

# 다른 방법 가장 좋은 방법인듯
# inp = int(input())
# count = 0
# while True :
#     if inp % 5 == 0 :
#         count += inp // 5
#         break
#     inp = inp - 3
#     count += 1
#     if inp < 0 :
#         print(-1)
#         break