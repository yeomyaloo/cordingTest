from collections import deque

dx = [0,0,-1,1]
dy = [1,-1,0,0]
board = [list(map(int,input().split())) for _ in range(7)]
dist = [[0] * 7 for _ in range(7)]
q = deque()
q.append((0,0))
board[0][0] = 1

while q:
    now = q.popleft()
    for i in range(4):
        nx = now[0] + dx[i]
        ny = now[1] + dy[i]
        if 0<=nx<7 and 0<=ny<7 and board[nx][ny] == 0:
            dist[nx][ny] = dist[now[0]][now[1]] + 1
            board[nx][ny] = 1
            q.append((nx,ny))

if dist[6][6] == 0:
    print(-1)
else:
    print(dist[6][6])
