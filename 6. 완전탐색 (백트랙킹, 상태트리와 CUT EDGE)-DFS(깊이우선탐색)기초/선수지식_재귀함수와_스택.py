#재귀함수와 스택

# 3 -> 2 -> 1 출
def DFS(x):
    if x>0:
        print(x)
        DFS(x-1)


# 1 -> 2 -> 3 출력
def DFS2(x):
    if x>0:
        DFS(x-1)
        print(x)
        
if __name__=="__main__":
    n = int(input())
    DFS(n)
