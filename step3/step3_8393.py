# n이 주어졌을 때 1부터 n까지 합을 구하는 프로그램
input_num = int(input())
result = 0
for i in range(1, input_num+1) :
    result += i
print(result)