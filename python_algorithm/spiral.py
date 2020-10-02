# 재귀 함수를 이용한 사각 나선 그리기

import turtle as t
    
def spiral(sp_len) :
    if sp_len <= 5 :
        return
    t.forward(sp_len)
    t.right(90)
    spiral(sp_len-5)

# 선 긋기 속도 지정
t.speed(0)
spiral(200)
t.hideturtle()
t.done()