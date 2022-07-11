def Count(mid):
    cnt = 1
    #무조건 첫 위치는 인덱스 0번부터 시작!
    end_point = Line[0]
    #0번 자리엔 이미 확인 했기 때문에 1~n까지
    for i in range(1, n):
        if Line[i] - end_point >= mid:
            cnt += 1
            end_point = Line[i]
    return cnt
        
n, c = map(int,input().split())
Line = [int(input()) for _ in range(n)]
Line.sort()

lt = 1
rt = Line[n-1]
res = 0
while lt <= rt:
    mid = (lt+rt) // 2
    #원하는 말 갯수보다 더 많은 말을 놓아도 정답으로 일단 인정
    if Count(mid) >= c:
        res = mid
        lt = mid + 1 
    else:
        rt = mid - 1

print(res)
