# 백준 알고리즘 - 10828
'''
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''

import sys

def push(x) :
    stack.append(x)

def pop() :
    if not stack :
        return -1
    else :
        return stack.pop()

def size() :
    return len(stack)

def empty() :
    # if stack -> stack 차있으면 true 비었으면 false
    return 0 if stack else 1

def top() :
    # 스택이 차있을 경우 마지막인덱스 출력 없으면 -1
    return stack[-1] if stack else -1

N = int(sys.stdin.readline())
stack = []

for _ in range(N) :
    cmd = sys.stdin.readline().split()

    word = cmd[0]

    if word == 'push' :
        push(cmd[1])
    elif word == 'pop' :
        print(pop())
    elif word == 'size' :
        print(size())
    elif word == 'empty' :
        print(empty())
    elif word == 'top' :
        print(top())