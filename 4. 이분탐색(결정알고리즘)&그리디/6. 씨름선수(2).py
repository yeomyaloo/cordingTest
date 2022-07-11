n = int(input())
player = [tuple(map(int,input().split())) for _ in range(n)]
player.sort(reverse = True)
cnt = 0
weight = 0

for h, w in player:
    if w > weight:
        weight = w
        cnt += 1
print(cnt)
