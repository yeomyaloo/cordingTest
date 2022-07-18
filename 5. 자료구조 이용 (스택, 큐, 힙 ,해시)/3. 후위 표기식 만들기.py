s = input()
stack = []
res = ""

for i in s:
    if i.isdecimal():
        res+= i
    else: #숫자가 아닌 경우
        if i == "(":
            stack.append(i)
        elif i =="*" or i =="/":
            while stack and (stack[-1] == "*" or stack[-1]=="/"):
                res += stack.pop()
            stack.append(i)
        elif i == "+" or i == "-":
            while stack and stack[-1] != "(":
                res += stack.pop()
            stack.append(i)
        elif i ==")":
            while stack and stack[-1] != "(":
                res += stack.pop()
            stack.pop() #여는 괄호를 빼주어야 다음 작업에 영향 X
while stack:
    res += stack.pop()

print(res)
