import sys
sys.stdin = open("input.txt", "r")

n = int(input())
res = 0
for i in range(n):
    tmp = input().split()
    tmp.sort()

    #정렬한 문자를 숫자화 시켜서 mapping
    a,b,c = map(int,tmp)
    if a == b and b == c:
        money = 10000 + (a*1000)
    elif a==b or a == c:
        money = 1000 + (a*100)
    elif b == c:
        money = 1000 + (b*100)
    else:
        #다 다른 수일 때 c가 오름차순으로 정렬해서 제일 큼.
        money = c * 100
    if money>res:
        res=money

print(res)
