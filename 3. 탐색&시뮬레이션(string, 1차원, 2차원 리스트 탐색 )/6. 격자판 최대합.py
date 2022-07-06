import sys
#sys.stdin = open("input.txt", "r")
#격자판 최대합

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
sum1 = sum2 = sum3 = sum4 = 0
largest = -2147000000

# 행, 렬의 최대합
for i in range(n):
    #0,0 ~ 0,n까지 확인이 끝나면 sum1, sum2 다시 초기화
    sum1 = sum2 = 0

    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]

    #매번 행 확인이 끝날 때 max값을 확인하기 위함
    if largest < sum1:
        largest = sum1
    if largest < sum2:
        largest = sum2

#대각선 확인을 위한 기초
sum1 = sum2 = 0
for i in range(n):

    sum1 += a[i][i]
    sum2 += a[i][n-i-1]

    if largest < sum1:
        largest = sum1
    if largest < sum2:
        largest = sum2

    
print(largest)
