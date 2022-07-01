import sys
sys.stdin = open("input.txt", "r")

card = list(range(21)) # 1 ~ 20까지 초기화

for _ in range(10):
    a, b = map(int,input().split())
    x =(b-a+1)//2
    for i in range(x):
        card[a+i], card[b-i] = card[b-i], card[a+i]

for j in card[1::]:
    print(j, end =" ")
