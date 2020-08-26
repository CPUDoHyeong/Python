# 백준 알고리즘 - 5543
'''
상근날드
'''
burger = []
side = []
loop = 5
discount = 50

for i in range(loop) :
    inp = int(input())
    if i < 3 :
        burger.append(inp)
    else :
        side.append(inp)

print(min(burger) + min(side) - 50)