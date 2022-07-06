import sys
#sys.stdin = open("input.txt", "r")

n = int(input())
apple = [list(map(int,input().split())) for _ in range(n)]
s = e = n//2
result = 0
for i in range(n):
    #start부분에서 end부분까지만 돌게 j 범위를 설정한다.
    for j in range(s,e+1):
        result += apple[i][j]
    if i < n//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
print(result)
