def Count(len):
    #해당 길이로 만들 수 있는 랜선 갯수
    cnt = 0
    for x in a:
        cnt += (x//len)
    return cnt

k, n = map(int,input().split())
a = [int(input()) for _ in range(k)]
lt = 1
rt = max(a)
res = 0


while lt <= rt:
    mid = (lt + rt)//2
    if Count(mid)>= n:
        res = mid
        lt = mid + 1
    else:
        rt = mid -1
        
print(res)
