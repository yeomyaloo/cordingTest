def DFS(L, money, day):
    global res
    if day > n:
        return
    if day == n:
        if res < money:
            res = money
    else:
        DFS(L+1, money + schedule[day][1], day + schedule[day][0])
        DFS(L+1, money, day+1)



if __name__ =="__main__":
    n = int(input())
    schedule = []
    for _ in range(n):
        a, b = map(int,input().split())
        schedule.append([a,b])
    res = -2147000000
    DFS(0,0,0)
    print(res)
