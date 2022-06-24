# 반복문(for, while)


a = range(10)
print(list(a))

# for
for i in range(10):
    print("hello")

for + range(): for 변수 in range(10) = 0,1,2,3,4,5,6,7,8,9

점점 작아지는 방법
for i in range(10,0,-1):
    print(i)


# while 조건문:
i = 1
while i <= 10:
    print(i)
    i = i + 1
i = 10
while i>=1:
    print(i)
    i -= 1

#break
무한반복문, 특정 조건에서 멈추게 할 때 사용한다.
i = 1
while True:
    print(i)
    if i == 10:
        break
    i += 1

for i in range(1, 11):
    print(i)
    if i == 5:
        break


#continue
홀수만 출력하고 싶을 때
for i in range(1, 11):
    if i %2 ==0:
        continue
    print(i)


    
