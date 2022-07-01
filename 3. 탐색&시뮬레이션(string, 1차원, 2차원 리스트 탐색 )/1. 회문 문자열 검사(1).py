import sys
sys.stdin = open("input.txt", "r")

n = int(input())

for i in range(n):
    s = input()
    s = s.lower()
    size = len(s)

    for j in range(size//2):
        if s[j] != s[-j-1]:
            print(f"#{i+1} NO")
            break
    else:
        print(f"#{i+1} YES")
