n, m = map(int,input().split())

matrix = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    a, b, c = map(int,input().split())
    if matrix[a][b] == 0:
        matrix[a][b] = c
    else:
        if matrix[a][b] < c:
            matrix[a][b] = c

for i in range(1, n+1):
    for j in range(1, n+1):
        print(matrix[i][j], end =" ")
    print()
