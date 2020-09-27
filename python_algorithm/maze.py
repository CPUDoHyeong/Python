# 미로 찾기 알고리즘

# 함수
# g : 데이터, start: 시작점, end : 도착점
def solve_maze(g, start, end) :
    qu = []
    done = set()

    qu.append(start)
    done.add(start)

    while qu : # 큐에 처리 가능한 데이터가 없을 때 까지
        p = qu.pop(0) # 큐에서 꺼내어 p에 저장
        v = p[-1]
        if v == end :
            return p
        for x in g[v] :
            if x not in done :
                # 지금까지의 경로 + 새로운 경로
                # abcd와 같이 저장되며, 마지막 길을 찾지 못하면
                # pop으로 인해서 사라진다. 마지막 길 까지 가는 경로만
                # 계속 살아남아서 return됨.
                # 예를 들어 잘못된 길로 들어 abcd에서 막혔다면
                # 새로 추가되는 값이 없기 때문에 pop된 abcd가 append
                # 되지 않으므로 없어짐. 새로운 경로가 계속 갱신되는 것만
                # qu에 계속 추가 된다.
                qu.append(p + x)  
                done.add(x)

    return '?'

# 데이터W
maze = {
    'a': ['e'],
    'b': ['c', 'f'],
    'c': ['b', 'd'],
    'd': ['c'],
    'e': ['a', 'i'],
    'f': ['b', 'g', 'j'],
    'g': ['f', 'h'],
    'h': ['g', 'l'],
    'i': ['e', 'm'],
    'j': ['f', 'k', 'n'],
    'k': ['j', 'o'],
    'l': ['h', 'p'],
    'm': ['i', 'n'],
    'n': ['m', 'j'],
    'o': ['k'],
    'p': ['l']
}

print(solve_maze(maze, 'a', 'p'))