n = int(input())
p = dict()
for _ in range(n):
    word = input()
    p[word] = 1

for _ in range(n-1):
    word = input()
    p[word] = 0

for k,v in p.items():
    if v == 1:
        print(k)

