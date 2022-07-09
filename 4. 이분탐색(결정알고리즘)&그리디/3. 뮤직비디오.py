n, m = map(int,input().split())
music = list(map(int,input().split()))

start = 1
end = sum(music)
res = 0

while start <= end:
    mid = (start+end)//2
    s = 0
    cnt = 1
    for i in music:
        if s + i > mid:
            s = i
            cnt += 1
        else:
            s += i
    if cnt <= m:
        end = mid - 1
        res = mid
    else:
        start = mid + 1
print(res)

    
