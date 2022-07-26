def DFS(L):
    global res
    if L == n:
        Min = max(abc) - min(abc)
        if Min < res:
            tmp = set()
            for x in abc:
                tmp.add(x)
            if len(tmp) == 3:
                res = Min
    else:
        for i in range(3):
            abc[i] += coin[L]
            DFS(L+1)

            #해당 작업이 끝나고 다시 윗 노드로 온 상황이기에 해당 값을 빼주어야 한다.(안 그러면 누적되기 때문)
            abc[i] -= coin[L]


if __name__ == "__main__":
    n = int(input())
    coin = [int(input()) for _ in range(n)]
    abc = [0]*3
    res = 2147000000
    DFS(0)
    print(res)
