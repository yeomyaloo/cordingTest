n = int(input())
player = [tuple(map(int,input().split())) for _ in range(n)]

cnt = 0
player.sort(reverse = True)

end_weight = 0
fp = 0
#키순으로 정렬하면 그 전에 사람보다 키가 작으니 몸무게를 비교해야 된다.
for h,w in player:
    if fp < h:
        cnt +=1
        end_weight = w
        fp = h
    elif fp > h:
        if end_weight < w:
            cnt += 1
            end_weight = w
print(cnt)
