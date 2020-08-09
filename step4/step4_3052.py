# 백준 알고리즘 - 3052
'''
정수 10개를 입력 받은 뒤 42로 나눈 나머지를 구한다.
서로 다른 값이 몇개 있는지 출력하는 프로그램
'''

loop_count = 10
deduplication = 10
input_list = []
remainder_list = []
div_num = 42

for i in range(loop_count) :
    inp = int(input())
    if inp % div_num in remainder_list :
        deduplication -= 1
    else :
        remainder_list.append(inp % div_num)

print(deduplication)
    
# 다른 방법
# num_list = []
# for i in range(loop_count) :
#     inp = int(input())
#     num_list.append(inp % div_num)
# # set은 중복이 없는 것을 이용하여 set으로 변환
# num_list = set(num_list)
# print(len(num_list))

