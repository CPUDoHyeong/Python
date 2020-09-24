# 두 번 이상 나온 이름 찾기

def find_same_name(a) :
    # 이름 등장 횟수의 딕셔너리
    name_dict = {}
    for name in a :
        # 있다면 횟수 + 1
        if name in name_dict :
            name_dict[name] += 1
        # 없다면 딕셔너리에 추가
        else :
            name_dict[name] = 1
    
    # 딕셔너리 중 2 이상 값 추출
    result = set()
    for name in name_dict :
        if name_dict[name] >= 2 :
            result.add(name)

    return result
    
name = ['Tom', 'Jerry', 'Tom', 'Tomas']
print(find_same_name(name))