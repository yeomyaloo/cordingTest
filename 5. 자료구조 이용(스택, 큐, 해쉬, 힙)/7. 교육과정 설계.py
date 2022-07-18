from collections import deque

need = input()

for i in range(int(input())):
    plan = input()
    dq = deque(need)
    for p in plan:
        if p in dq:
            if p != dq.popleft():
                print(f"#{i+1} NO")
                break
    else:
        if dq:
            print(f"#{i+1} NO")
        else:
            print(f"#{i+1} YES")
