import sys
#sys.stdin = open("input.txt","r")


board = [list(map(int,input().split())) for _ in range(7)]
cnt = 0

for i in range(3):
    for j in range(7):
        tmp = board[j][i:i+5]
        if tmp == tmp[::-1]:
            cnt +=1

        #7X7에서 5글자만 비교하면 되기에 앞뒤로 2번만 확인해주면 됨(가운데는 어차피 다 같음)
        #세로의 경우엔 슬라이스 기능 사용 불가!
        for k in range(2):
            if board[i+k][j] != board[i+5-k-1][j]:
                break
        else:
            cnt +=1

print(cnt)
            
