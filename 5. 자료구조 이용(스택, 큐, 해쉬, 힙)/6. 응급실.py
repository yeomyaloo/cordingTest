from collections import deque

n, m = map(int,input().split())
p = list(map(int,input().split()))
cnt = 0

dq = [(pos,val) for pos, val in enumerate(p)]
dq = deque(dq)

while True:
    now = dq.popleft()
    #any = 반복가능한 자료형 중 단 하나라도 참이라면 참을 반환
    #모든 요소가 거짓인 경우만 거짓 반환!
    if any(now[1] < x[1] for x in dq):
        dq.append(now)
    else:
        cnt += 1
        if now[0] == m:
            print(cnt)
            break
