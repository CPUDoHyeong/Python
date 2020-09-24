# 회문 확인

def palindrome(s) :
    # 큐와 스택을 리스트로 정의
    qu = []
    st = []
    for x in s :
        if x.isalpha() :
            qu.append(x.lower())
            st.append(x.lower())

    while qu :
        if qu.pop(0) != st.pop() :
            return False
    
    return True

def palindrome_v2(s) :
    # 큐와 스택을 사용하지 않고 회문 찾기
    arr = []
    for x in s :
        if x.isalpha() :
            arr.append(x.lower())
    n = len(arr)
    if n % 2 == 0 :
        return False
    else :
        for i in range(n // 2) :
            if arr[i] != arr[n-i-1] :
                return False
    return True

def palindrome_v3(s) :
    # 큐와 스택을 사용하지 않고 회문 찾기2
    i = 0
    j = len(s) - 1
    while i < j :
        if s[i].isalpha() == False :
            i += 1
        elif s[j].isalpha() == False :
            j -= 1
        elif s[i].lower() != s[j].lower() :
            return False
        else :
            i += 1
            j -= 1

    return True

print(palindrome_v3("Wow"))
print(palindrome_v3("Madam, I’m Adam."))
print(palindrome_v3("Madam, I am Adam."))