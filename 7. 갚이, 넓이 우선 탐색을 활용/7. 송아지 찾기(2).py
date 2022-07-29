from collections import deque


s, e = map(int,input().split())
MAX = 10000
ch = [0] * (MAX+1)
dis = [0] * (MAX +1)
a = [-1,1,5]
ch[s] = 1 #시작 노드는 체크를 해준 표시를 해야 된다!
dis[s] = 0 #시작 노드의 거리값은 0이다.
q = deque()
q.append(s)

while q:
    now = q.popleft()
    if now == e:
        break
    for next in a:
        if 0 < now + next <= MAX and ch[now + next] == 0:
            ch[now + next] = 1
            dis[now+next] = dis[now]  + 1
            q.append(now+next)
        
    
print(dis[e])
