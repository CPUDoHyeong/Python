# 연습문제


def print_friends(g, start) :
    qu = []
    done = set()

    qu.append(start)
    done.add(start)

    while qu :
        p = qu.pop(0)
        print(p)
        for i in g[p] :
            if i not in done :
                qu.append(i) # 큐에 추가
                done.add(i)  # 집합에 추가

info = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2]
}

print_friends(info, 1)