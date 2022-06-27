import sys
sys.stdin = open("input.txt", "rt")

T = int(input())

for i in range(T):
    n,s,e,k = map(int,input().split())
    num = list(map(int,input().split()))
    result = num[s-1:e]
    result.sort()
    print(f"#{i+1} {result[k-1]}")
    
