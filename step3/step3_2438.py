# 별찍기
# 첫째줄 1개 부터 n번째줄에는 n개 별 찍기
# star_count = int(input())
# for i in range(1, star_count+1) :
#     for j in range(1, i+1) :
#         print('*', end='')
#     print()

star_count = int(input())
for i in range(1, star_count+1) :
    print('*' * i)