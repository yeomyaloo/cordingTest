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
    for next in(now-1, now+1, now+5):
        if 0 < next <= MAX and ch[next]==0:
            q.append(next)
            ch[next] = 1
            dis[next] = dis[now] +1
        

print(dis[e])
