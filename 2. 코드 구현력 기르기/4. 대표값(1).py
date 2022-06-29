import sys
#sys.stdin = open("input.txt","rt")

n = int(input())
a = list(map(int,input().split()))

ave = round(sum(a)/n)
min = 2147000000

for idx, nowScore in enumerate(a):
    tmp = abs(nowScore - ave)
    if tmp < min:
        min = tmp
        score = nowScore
        index = idx + 1
    elif tmp == min:
        if nowScore > score:
            score = nowScore
            index = idx+1
print(ave, index)
