n, m = map(int,input().split())

a = list(map(int,input().split()))

a.sort()

num = a.index(m)

print(num+1)
