from collections import deque

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
sum_apple = a[n//2][n//2]
ch = [[0]*n for _ in range(n)]
ch[n//2][n//2] = 1
dx = [0,0,-1,1]
dy = [1,-1,0,0]
q = deque()
q.append((n//2, n//2))
L = 0

while True:
    size = len(q)
    if L == n//2:
        break
    else:
        for i in range(size):
            apple = q.popleft()
            for j in range(4):
                nx = apple[0] + dx[j]
                ny = apple[1] + dy[j]
                if ch[nx][ny] == 0:
                    q.append((nx,ny))
                    ch[nx][ny] = 1
                    sum_apple += a[nx][ny]
    L += 1
    
print(sum_apple)
