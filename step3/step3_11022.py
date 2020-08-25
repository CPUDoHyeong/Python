# 백준 알고리즘 - 11022
'''
A + B - 8

각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다. x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다.
'''

inp = int(input())
for i in range(inp) :
    num1, num2 = map(int, input().split())
    # print('Case #', (i+1), ': ', num1, ' + ', num2, ' = ', num1+num2, sep='')
    print("Case #%s: %s + %s = %s"%(i+1, num1, num2, num1+num2))


# 다른 방법
# print("Case #%s: %s + %s = %s"%(i+1, num1, num2, num1+num2))