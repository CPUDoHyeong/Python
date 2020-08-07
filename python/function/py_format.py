# format 함수
'''
문자열.format() 의 형태
문자열에는 대괄호 {} 가 들어가며
해당 대괄호의 개수에 맞춰 format의 괄호 안에 값을 넣으면 된다.
ex : print('{}{}'.format(1, 2))
문자열의 대괄호의 개수가 부족한 경우는 정상 작동하나,
문자열의 대괄호 개수보다 format 안의 값의 수가 적으면 에러가 발생
print('{}'.format(1, 2)) -> 정상 작동
print('{}{}'.format(1)) -> 에러(IndexError)
'''

a = 1
b = 2
c = 3
base = '{} + {} = {}'

# 결과는 동일
print('{} + {} = {}'.format(a, b, c))
print(base.format(a, b, c))

