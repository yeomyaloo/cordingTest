n = int(input())
meeting = [tuple(map(int,input().split())) for _ in range(n)]

meeting.sort(key= lambda x: (x[1],x[0]))
cnt = 0
end_time = 0

for s, e in meeting:
    if s >= end_time:
        end_time = e
        cnt += 1
print(cnt)
