# 백준 알고리즘 - 18258
# 큐2

'''
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''
import sys
from collections import deque

def push(x) :
    deque.append(x)

def pop() :
    if not deque :
        return -1
    else :
        return deque.popleft()

def size() :
    return len(deque)

def empty() :
    return 0 if deque else 1

def front() :
    if not deque :
        return -1
    else :
        return deque[0]

def back() :
    if not deque :
        return -1
    else :
        return deque[-1]

n = int(sys.stdin.readline())
deque = deque([])

for i in range(n) :
    s = sys.stdin.readline().split()
    word = s[0]

    if word == 'push' :
        push(s[1])
    elif word == 'pop' :
        print(pop())
    elif word == 'size' :
        print(size())
    elif word == 'empty' :
        print(empty())
    elif word == 'front' :
        print(front())
    elif word == 'back' :
        print(back())