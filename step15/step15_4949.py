# 백준 알고리즘 - 4949
'''
균형잡힌 세상
모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.
모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.
모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
모든 괄호들의 짝은 1:1 매칭만 가능하다. 
즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.
'''

while True :
    braket = input()
    if braket == '.' :
        break
    stack = []
    answer = True

    for i in braket :
        if i == '(' or i == '[' :
            stack.append(i)
        elif i == ')' :
            if len(stack) == 0 :
                answer = False
                break
            if stack[-1] == '(' :
                stack.pop()
            else :
                answer = False
                break
        
        elif i == ']' :
            if len(stack) == 0 :
                answer = False
                break
            if stack[-1] == '[' :
                stack.pop()
            else :
                answer : False
                break
    
    # answer이 트루면서 스택이 비어있으면 yes(비어있을 경우 false이므로)
    if answer and not stack :
        print('yes')
    else :
        print('no')
