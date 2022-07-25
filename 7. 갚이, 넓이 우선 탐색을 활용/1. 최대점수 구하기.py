def DFS(L, s,ts):
    global res
    if ts > m:
        return
    if L == n:
        if res < s:
            res = s
    else:
        DFS(L+1, s + a[L][0], ts + a[L][1])
        DFS(L+1, s, ts)


if __name__ =="__main__":
    n, m = map(int,input().split())
    res = -2174000000
    score = []
    for i in range(n):
        a, b = map(int,input().split())
        score.append([a,b])
    a= sorted(score,key=lambda x:x[1])
    a.sort(reverse=True)
    DFS(0,0,0)
    print(res)
    
