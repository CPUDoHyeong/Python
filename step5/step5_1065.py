# 백준 알고리즘 - 1065
'''
한수 구하기
정수 X의 각 자리수가 등차수열을 이룬다면 그 수는 한수이다.
자연수 N 주어 졌을 때 1부터 N 사이의 한수를 구하는 프로그램
'''

def hansu(num) :
    if num < 100 :
        return num

    hans = 99
    for i in range(100, num+1) :
        nums = list(map(int, str(i)))
        if nums[0] - nums[1] == nums[1] - nums[2] :
            hans += 1
    
    return hans

        