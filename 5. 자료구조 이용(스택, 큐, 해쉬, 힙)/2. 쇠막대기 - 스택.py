#쇠막대기
s= input()
stack = []
cnt = 0

for i in range(len(s)):
    if s[i] == "(":
        stack.append(s[i])
    else:
        #어차피 )인 경우엔 pop해주어야 한다.
        stack.pop()
        if s[i-1] != ')':
            cnt += len(stack)
        else:
            cnt += 1
print(cnt)
