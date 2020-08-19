# 백준 알고리즘 - 1316
'''
그룹 단어 체커
'''

num = int(input())
result = 0
for i in range(num) :
  inp = list(input())
  inp_arr = list()
  for j in range(len(inp)) :
    if inp[j] not in inp_arr :
      inp_arr.append(inp[j])
    else :
      if inp[j-1] != inp[j] :
        break
      else :
        inp_arr.append(inp[j])

  if len(inp) == len(inp_arr) :
    result += 1

print(result)

# cnt = 0
# for i in range(int(input())):
#     word = input()
#     cnt+=list(word) == sorted(word, key=word.find)
# print(cnt)