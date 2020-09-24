# 딕셔너리 테스트

# 딕셔너리 생성
info = {
    1 : 'Kim',
    2 : 'Lee',
    3 : 'Park'
}

# 빈 딕셔너리 생성
d = dict()
e = {}

# 원소 추가
info[4] = 'Yu'
# 원소 삭제
del info[4]
# 길이 확인
print(len(info))
# 키값이 딕셔너리에 있는지 확인
print(1 in info)
print(4 in info)
# in과 반대
print(4 not in info)
# 모든 자료 삭제
info.clear()
print(info)
