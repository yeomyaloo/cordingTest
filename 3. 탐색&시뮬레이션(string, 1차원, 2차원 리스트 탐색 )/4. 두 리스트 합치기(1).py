import sys
#sys.stdin = open("input.txt", "r")

n= int(input())
a = list(map(int,input().split()))
m= int(input())
b = list(map(int,input().split()))

c = a+b
c.sort()

for i in c:
    print(i, end= " ")
