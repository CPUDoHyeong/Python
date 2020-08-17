# 백준 알고리즘 - 2941
'''
크로아티아 알파벳
'''

# apla_list = ['c', 'd', 'l', 'n', 's', 'z']
# croa_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# inp = list(input())
# result = 0

# d 면 3번째까지 
# z 면 앞인덱스도 확인

# check_str = ''
# for i in range(0, len(inp)-1, 1) :
#     # c, d, l, n, s, z 로 시작할 경우만 check
#     check_str = ''
#     if inp[i] in apla_list :
#         check_str += inp[i] + inp[i+1]
#         if check_str in croa_list :
#             if check_str == 'dz' and i == len(inp)-2 :
#                 result += 1
#                 i += 1
#                 continue
#             elif check_str == 'dz' and i != len(inp)-2 :
#                 check_str += inp[i+2]
#                 if check_str in croa_list :
#                     result += 1
#                     i += 2
#                     continue
#         result += 1
#         i += 1
#     else :
#         result += 1

# print(result)

a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
b = input()
for i in a:
    b = b.replace(i, 'a')
print(len(b))