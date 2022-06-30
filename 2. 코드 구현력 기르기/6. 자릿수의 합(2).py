
import sys
sys.stdin = open("input.txt", "r")


def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x//10
    return sum

n = int(input())
a = list(map(int,input().split()))
max = -2147000000

for i in a:
    now = digit_sum(i)
    if now > max:
        max = now
        result = i

print(result)

