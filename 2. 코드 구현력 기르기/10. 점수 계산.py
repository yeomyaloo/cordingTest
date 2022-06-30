import sys
#sys.stdin = open("input.txt", "r")

n = int(input())
OX = list(map(int,input().split()))

score = 0
extra_point = 0

for i in OX:
    
    if i == 1:
        extra_point += 1 
        score += extra_point
    else:
        extra_point = 0

print(score)
