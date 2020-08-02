# 백준 알고리즘 문제 2523 - 별찍기9
inp = int(input())

# for i in range(0, inp) :
#     # print(' ' * i, '*' * ((inp*2-1)-(i*2)), ' ' * i)

#     if i == 0 :
#         print('*' * (inp*2-1))
#     else :
#         print(' ' * (i-1), '*' * ((inp*2-1)-(i*2)), ' ' * (i-1))

# for i in range(inp-1, 0, -1) :
#     if i == 0 :
#         print('*' * (inp*2-1))
#     else :
#         print(' ' * (i-1), '*' * ((inp*2-1)-(i)), ' ' * (i-1))

for i in range(inp):
    print(" " * i + "*" * ((inp - i) * 2 - 1))
for i in range(inp - 2, -1, -1):
    print(" " * i + "*" * ((inp - i) * 2 - 1))