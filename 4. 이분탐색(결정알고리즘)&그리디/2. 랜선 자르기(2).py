#랜선자르기(결정 알고리즘)
k, n = map(int,input().split())
a = [int(input()) for _ in range(k)]
lt = 1
rt = max(a)
res = 0

while lt <= rt:
    mid = (lt+rt)//2
    s = 0
    for i in a:
        s += i//mid
    if s >= n:
        res = mid
        lt = mid + 1
    else:
        rt = mid -1
        
print(res)
