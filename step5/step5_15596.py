# 백준 알고리즘 - 15596
'''
정수 n 개가 주어졌을 때, n개의 합을 구하는 함수 작성
'''

def solve(a : list) -> int :
    list_sum = 0
    for i in a :
        list_sum += i
    
    return list_sum

print(solve([1, 2, 3]))