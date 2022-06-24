#반복문을 이용한 문제풀이

#1) 1부터 n까지 홀수 출력하기
n = int(input("n을 입력해주세요: "))

print(f"1번 1부터 {n}까지 홀수 출력하기")
for i in range(1, n+1):
    if i%2 != 0:
        print(i)

#2) 1부터 n까지 합 구하기
SUM = 0
for i in range(1, n+1):
    SUM += i 
print(f"2번 1부터 {n}까지 합 구하기: ",SUM)

#3) n의 약수 출력
print(f"{n}의 약수 출력")
for i in range(1, n+1):
    if n%i == 0:
        print(i, end=' ')
