def DFS(L, s):
    global cnt
    if s > charge:
        return
    if s == charge:
        if L < cnt:
            cnt = L
    else:
        for i in range(n):
            DFS(L+1, s+coins[i])
        


if __name__=="__main__":
    
    n = int(input())
    coins = list(map(int,input().split()))
    charge = int(input())
    cnt = 2147000000
    DFS(0,0)
    print(cnt)
