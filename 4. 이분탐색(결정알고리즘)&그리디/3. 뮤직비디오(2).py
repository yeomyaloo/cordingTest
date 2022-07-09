def Count(mid):
    s = 0
    cnt = 1
    for i in music:
        if s + i > mid:
             cnt += 1
             s = i
        else:
            s+=i
    return cnt

n, m = map(int,input().split())
music = list(map(int,input().split()))

lt = 1
rt = sum(music)
res = 0

while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid) <= m:
        res = mid
        rt = mid - 1

    else:
        lt = mid +1
print(res)
