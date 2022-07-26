def DFS(L, s):
    global res
    if L == k:
        if 0<s<=total:
            res.add(s)
    else:
        DFS(L+1, s + a[L]) #추를 왼쪽에 놓는 경우
        DFS(L+1, s - a[L]) #추를 오른쪽에 놓는 경
        DFS(L+1,s)
        



if __name__ =="__main__":
    k = int(input())
    a = list(map(int,input().split()))
    total = sum(a)
    res = set()
    DFS(0,0)
    print(total - len(res))
    
