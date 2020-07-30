# 별찍기 거꾸로
inp = int(input())

# for i in range(1, inp+1) :
#     for j in range(1, inp+1-i) :
#         print(' ', end='')
#     for j in range(1, i+1) :
#         print('*', end='')
#     print()

# 더 쉬운 방법
for i in range(1, inp+1) :
    print(' '*(inp-i) + '*'*i)
