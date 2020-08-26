# 백준 알고리즘 별 찍기 - 21
num = int(input())

# if num == 1 :
#     print('*')
# else :
#     for i in range(1, num*2+1) :
#         for j in range(1, num+1) :
#             if i % 2 == 1 :
#                 if j % 2 == 1 :
#                     print('*', end='')
#                 else :
#                     print(' ', end='')
#             else :
#                 if j % 2 == 1 :
#                     print(' ', end='')
#                 else :
#                     print('*', end='')
        
#         print()


a = num//2
b = num - num//2

for i in range(num) :
    print("* " * b)
    print(" *" * a)
        