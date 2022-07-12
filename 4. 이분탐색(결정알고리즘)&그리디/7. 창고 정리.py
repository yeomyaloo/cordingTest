#높이 조정 = 가장 높은 곳에 있는 상자를 가장 낮은 곳에 있는 곳으로 옮기는 것!

L = int(input())
a = list(map(int,input().split()))
a.sort()
m = int(input())


for i in range(m):
    a[0] += 1
    a[-1] -= 1
    a.sort()
    
print(max(a) - min(a))
