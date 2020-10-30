# 백준 알고리즘 - 2164


# 시간초과
# n = int(input())
# card = []

# for i in range(n, 0, -1) :
#     card.append(i)

# while len(card) != 1 :
#     card.pop()
#     card.insert(0, card.pop())

# print(card[-1])

from collections import deque

N = int(input())
deque = deque([i for i in range(1, N + 1)])

while(not (len(deque) == 1)):
    # 버리고,
    deque.popleft()
    # 맨 앞의 숫자를 뒤로 옮기자.
    move_num = deque.popleft()
    deque.append(move_num)
    
print(deque[0])


    

