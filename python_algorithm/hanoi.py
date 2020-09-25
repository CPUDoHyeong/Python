# 하노이의 탑 알고리즘

# n원판 개수
# a 출발 기둥, b 보조 기둥, c 도착 기둥
def hanoi(n, a, b, c) :
    # 원판이 한개면 출발기둥(a)에서 도착기둥(c)로 옮기면된다.
    if n == 1 :
        print(a, 'to', c)
        return

    # 원반 n-1개를 c를 이용해서 b로 이동
    hanoi(n-1, a, c, b)
    # 남은 가장 큰 원반을 c로 이동
    print(a, 'to', c)
    # 보조 기둥에 있는 n-1개의 원반을 다시 a를 이용해 c로 이동
    hanoi(n-1, b, a, c)

    
hanoi(4, 1, 2, 3)