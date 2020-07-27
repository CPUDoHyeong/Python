# 재귀함수를 이용한 하노이 탑 쌓기
def move(n, a, b, c) :
    if n > 0 :
        move(n-1, a, c, b)
        print("Move a disk from %s to %s" % (a, c))
        move(n-1, b, a, c)

move(3, 'a', 'b', 'c')  