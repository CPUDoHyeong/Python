# 백준 알고리즘 - 2869
'''
달팽이는 올라가고 싶다
V미터인 나무 막대를 올라간다
낮에는 A미터 올라가고 밤에는 B미터 미끄러진다
막대를 모두 올라가려면 며칠이 걸리는가?
(단 정상에 올라간 후 미끄러지지 않는다)
'''

a, b, v = map(int, input().split())
# 어제의 기록
# x = 0
# day = 1
# while True :
#     if (x + a) >= v :
#        print(day)
#        break
#     else :
#         x += a - b
#         day += 1

'''
마지막 날 미끄러지는 거는 계산할 필요가 없다
그래서 전체 높이에 미끄러지는 길이를 빼고
마지막 날을 제외한 하루 올라가는 높이인 a - b를 나눠주면된다.
만약 소수점일 경우 올림을 해주어야한다 날짜는 소수가 없기 때문에
'''
x = (v - b) / (a - b)
# 삼항연산자
print(int(x) if x == int(x) else int(x)+1)