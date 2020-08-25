# 백준 알고리즘 - 2884
'''
알람 시계
'''

hour, minute = map(int, input().split())
set_minute = 45
result_time = minute - set_minute


if result_time >= 0 :
    print(hour, result_time)
else :
    if hour == 0 :
        print(23, result_time+60)
    else :
        print(hour-1, result_time+60)