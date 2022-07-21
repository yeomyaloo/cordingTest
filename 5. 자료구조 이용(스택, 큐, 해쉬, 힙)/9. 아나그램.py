from collections import defaultdict

s1= input()
s2 = input()

d = defaultdict(int)

for s in s1:
    d[s] += 1

for s in s2:
    if s in d:
        d[s] = d[s] - 1

for dic in d:
    if d[dic] != 0:
        print("NO")
        break
else:
    print("YES")
