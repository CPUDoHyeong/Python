# 백준 알고리즘 - 4673
'''
셀프 넘버 : 생성자가 없는 숫자를 셀프 넘버
33 시작 -> 33 + 3 + 3 = 39 -> 51 -> 57 .... 일때
33은 39의 생성자, 39는 51의 생성자가 된다.
그리고 1, 3, 5, 7, 9, 20, 31, 42 ... 와 같이 생성자가
없는 숫자를 셀프 넘버라고 한다.
10000 이하의 숫자 중 셀프 넘버를 출력 하는 프로그램
'''
def self_num(n) :
    nums = list(map(int, str(n)))
    result = n
    for i in nums :
        result += i
    return result

loop_count = 10000
natural_num_set = set(range(1, 10001))
add_num_set = set()
for i in range(1, loop_count+1) :
    result = self_num(i)
    add_num_set.add(result)

self_num_set = natural_num_set - add_num_set

for i in sorted(self_num_set) :
    print(i)

# 함수를 사용하지 않고 하는 방법
# for문 in 뒷부분에 str(i) 를 이용한 것을 알아두기
for i in range(1, loop_count+1) :
    for j in str(i) :
        i += int(j)
    # generated_num_set.add(i)