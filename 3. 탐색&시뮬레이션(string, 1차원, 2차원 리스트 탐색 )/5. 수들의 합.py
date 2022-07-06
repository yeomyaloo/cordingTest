import sys
#sys.stdin = open("input.txt", "r")

#수들의 합
n,m = map(int,input().split())
a = list(map(int,input().split()))
cnt = 0
left = 0
right = 1
total = a[0]

while True:
    if total < m:
        if right < n:
            total += a[right]
            right += 1
        else:
            break
    elif total == m:
        cnt += 1
        total -= a[left]
        left += 1
    else:
        total -= a[left]
        left += 1

print(cnt)
    
