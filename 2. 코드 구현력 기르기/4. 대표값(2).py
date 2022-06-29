import sys
#sys.stdin = open("input.txt","rt")

n = int(input())
a = list(map(int,input().split()))

ave = round(sum(a)/n)
min = 2147000000

for i in a:
    tmp = abs(i - ave)
    if tmp < min:
        min = tmp
        score = i
    elif tmp == min:
        if i > score:
           score = i
print(ave, a.index(score)+1)
