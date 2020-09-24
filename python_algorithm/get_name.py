# 14-1 연습문제
# 학생 번호와 이름이 주어졌을 때 학생 번호를 입력하면
# 그 학생 번호에 해당하는 이름을 돌려주고,
# 해당하는 학생 번호가 없으면 물음표를 돌려줌

def get_name(dic, value) :
    if value in dic :
        return dic[value]
    else :
        return '?'

student = {
    39 : 'Justin',
    14 : 'John',
    67 : 'Mike',
    105: 'Summer'
}

print(get_name(student, 1))