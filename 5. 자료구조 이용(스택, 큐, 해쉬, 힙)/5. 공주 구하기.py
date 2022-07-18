from collections import deque

n, m = map(int,input().split())
prince = list(range(1, n+1))

dq = deque(prince)

while dq:
    for _ in range(m-1):
        dq.append(dq.popleft())
    dq.popleft()

    if len(dq) == 1:
        print(dq[0])
        break
        
