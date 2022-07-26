def DFS(L,s):
    global res
    if L == k:
        if s == T:
            res += 1  
    else:
        for i in range(coin[L][1]+1):
            DFS(L+1,s + (coin[L][0]*i))
        
        

if __name__ == "__main__":
    T = int(input()) #지폐의 금액
    k = int(input()) #동전의 가지 수
    res = 0
    coin = []
    for i in range(k):
        #동전 금액, 갯수
        a, b = map(int,input().split())
        coin.append([a,b])
    DFS(0,0)
    print(res)
