def DFS(x,y):
    global cnt
    if x == mxX and y == mxY:
        cnt += 1
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if board[x][y] < board[nx][ny] and 0<=nx<n and 0<=ny<0 and ch[nx][ny] == 0:
                ch[nx][ny] = 1
                DFS(nx,ny)
                ch[nx][ny] = 0
                
    
if __name__ =="__main__":
    n = int(input())
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    board = [list(map(int,input().split())) for _ in range(n)]
    ch = [[0]*n for _ in range(n)] 
    cnt = 0
    MAX = -2147000000
    MIN = 2147000000

    for i in range(n):
        for j in range(n):
            tmp = board[i][j]

            if tmp < MIN:
                MIN = tmp
                smX = i
                smY = j
            if tmp > MAX:
                MAX = tmp
                mxX = i
                mxY = j    

    ch[smX][smY] = 1
    DFS(smX,smY) 
    print(cnt)
