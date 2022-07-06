
import sys
sys.stdin=open("input.txt", "r")
n = int(input())
gotgam = [list(map(int,input().split())) for _ in range(n)]

m = int(input())
for _ in range(m):
    a,b,c = map(int,input().split())

    if b == 0: #왼쪽으로 돌 경우
        #맨 앞의 숫자를 빼서 맨 뒤로 돌려 보내주는 작업을 c번 해야 한다.
        for _ in range(c):
            gotgam[a-1].append(gotgam[a-1].pop(0))
    else:#오른쪽으로 돌 경우
        #맨 뒤의 숫자를 빼서 맨 앞으로 추가해주어야 한다.
        for _ in range(c):
            gotgam[a-1].insert(0, gotgam[a-1].pop())


s = 0
e = n-1
result = 0
for i in range(n):
    for j in range(s, e+1):
        result += gotgam[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(result)
            
