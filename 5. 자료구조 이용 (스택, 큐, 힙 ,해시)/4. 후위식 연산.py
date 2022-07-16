#해당 연산자 앞에 있는 2개의 숫자를 피연산자로 계산하고 다시 append해준다.
s = input()
stack = []

for i in s:
    if i.isdecimal():
        stack.append(int(i))
    else:
        if i == "+":
            b = stack.pop()
            a = stack.pop()
            stack.append(a+b)
            
        elif i == "-":
            b = stack.pop()
            a = stack.pop()
            stack.append(a-b)
        elif i == "*":
            b = stack.pop()
            a = stack.pop()
            stack.append(a*b)
        elif i == "/":
            b = stack.pop()
            a = stack.pop()
            stack.append(a/b)
print(stack[0])
