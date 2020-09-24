# 친구 찾기 알고리즘
# 그래프 탐색 알고리즘 이라고 함


def print_all_friends(g, start) :
    qu = []      # 기억장소 : 앞으로 처리해야 할 사람들을 큐에 저장
    done = set() # 기억장소2: 이미 큐에 추가한 사람들을 집합에 기록(중복방지)

    qu.append(start) # 자신을 큐에 넣고 시작
    done.add(start)  # 집합에도 추가

    while qu :
        p = qu.pop(0)
        print(p)
        for x in g[p] :
            if x not in done : # 큐에 추가된 적 없는 사람이라면
                qu.append(x)   # 큐에 추가
                done.add(x)    # 중복방지 집합에도 추가

def print_all_friend2(g, start) :
    qu = [] # 친밀도(촌수) 저장
    done = set()

    qu.append((start, 0)) # 자기 자신은 0촌
    done.add(start)

    while qu :
        (p, d) = qu.pop(0)
        print(p, d)
        for x in g[p] :
            if x not in done :
                qu.append((x, d+1))
                done.add(x)



fr_info = {
    'Summer': ['John', 'Justin', 'Mike'],
    'John': ['Summer', 'Justin'],
    'Justin': ['John', 'Summer', 'Mike', 'May'],
    'Mike': ['Summer', 'Justin'],
    'May': ['Justin', 'Kim'],
    'Kim': ['May'],
    'Tom': ['Jerry'],
    'Jerry': ['Tom']
}

print_all_friend2(fr_info, 'Summer')
print_all_friend2(fr_info, 'Tom')
