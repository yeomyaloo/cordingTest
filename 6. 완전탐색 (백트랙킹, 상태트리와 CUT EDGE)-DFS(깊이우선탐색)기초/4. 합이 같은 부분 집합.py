def DFS(level,s):
    global flag
    if flag == 0:
        return
    if level == n:
        if s == (total_sum - s):
            print("YES")
            flag = 0
    else:
        DFS(level + 1, s + a[level])
        DFS(level+1, s)


if __name__ =="__main__":
    n = int(input())
    a =list(map(int,input().split()))
    total_sum = sum(a)
    flag = 1
    DFS(0,0)
    if flag:
        print("NO")
